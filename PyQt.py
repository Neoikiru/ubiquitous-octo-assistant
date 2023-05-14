from threading import Thread
import time
import re
import cv2
import numpy as np
from PyQt6.QtCore import QCoreApplication, pyqtSlot, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit
from PyQt6 import uic, QtGui
from PyQt6.QtGui import QPixmap
from voiceModule import VoiceModule
from CameraModule import HandGestureDetector
from audioControllerFull import AudioHandler
import SchoolModule
import config


class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        # loading the ui file with uic module
        uic.loadUi("./GUI/layout.ui", self)

        self.disply_width = 279
        self.display_height = 158

        self.WaitTimeSpinBox.setValue(7)
        self.LanguageComboBox.setCurrentText('English')
        self.setWindowIcon(QtGui.QIcon('./GUI/Icons/logo.png'))

        for word in config.STOP_WORDS:
            self.StopWordsText.appendPlainText(word)

        self.RecognizedInputText.setPlainText(config.Recognized_input)
        self.CurrentStatusText.setPlainText(config.Current_status)
        self.GeneratedOutputText.setPlainText(config.Text_output)

        self.isPassVisible = False
        self.EduPasswordLineEdit.textEdited.connect(self.change_edu_password)
        self.ShowPassButton.clicked.connect(self.change_pass_button_icon)
        self.ShowPassButton.setIcon(QtGui.QIcon("./GUI/Icons/hide.png"))

        self.isLoginVisible = False
        self.EduLoginLineEdit.textEdited.connect(self.change_edu_login)
        self.ShowLoginButton.clicked.connect(self.change_login_button_icon)
        self.ShowLoginButton.setIcon(QtGui.QIcon("./GUI/Icons/hide.png"))

        self.LanguageComboBox.setCurrentText(config.LANGUAGE)
        self.change_language()
        self.WaitTimeSpinBox.setValue(config.Time_to_listen_after_request)

        self.StopWordsText.textChanged.connect(self.change_stop_word)
        self.LanguageComboBox.currentTextChanged.connect(self.change_language)
        self.WaitTimeSpinBox.valueChanged.connect(self.change_wait_time)

        self.audio_controller = AudioHandler()
        self.volumeChangeTime = 0
        self.muteCount = 0
        self.logicTime = 0

        self.edu_controller = SchoolModule.SchoolAutomationSystem()
        self.edu_controller.StatusUI.connect(self.change_current_status_text)
        self.edu_controller.SchoolOutputText.connect(self.display_edu_data)

        self.thread_Camera = HandGestureDetector()
        self.thread_Camera.change_pixmap_signal.connect(self.update_image)
        self.thread_Camera.current_gesture_signal.connect(self.change_hand_status)
        self.thread_Camera.start()

        self.thread_Voice = VoiceModule()
        self.thread_Voice.logicSignal.connect(self.start_edu_data_fetch)
        self.thread_Voice.recognizedText.connect(self.change_recognized_text)
        self.thread_Voice.currentStatus.connect(self.change_current_status_text)
        self.thread_Voice.outputText.connect(self.change_output_text)
        self.thread_Voice.start()

    def change_config(self, id, input_text):
        with open('config.py', 'r') as f: 
            text = f.read().split('\n')
            text[id] = input_text
        with open('config.py', 'w') as f:
            # print('\n'.join(text))
            f.write('\n'.join(text))

    def change_edu_login(self):
        config.EDU_LOGIN = self.EduLoginLineEdit.text()
        self.change_config(8, f"EDU_LOGIN = '{self.EduLoginLineEdit.text()}'")

    def change_edu_password(self):
        config.EDU_PASSWORD = self.EduPasswordLineEdit.text()
        self.change_config(7, f"EDU_PASSWORD = '{self.EduPasswordLineEdit.text()}'")

    def change_login_button_icon(self):
        self.isLoginVisible = not self.isLoginVisible
        if self.isLoginVisible:
            self.EduLoginLineEdit.setEchoMode(QLineEdit.EchoMode.Normal)
            self.ShowLoginButton.setIcon(QtGui.QIcon("./GUI/Icons/view.png"))
        else:
            self.EduLoginLineEdit.setEchoMode(QLineEdit.EchoMode.Password)
            self.ShowLoginButton.setIcon(QtGui.QIcon("./GUI/Icons/hide.png"))

    def change_pass_button_icon(self):
        self.isPassVisible = not self.isPassVisible
        if self.isPassVisible:
            self.EduPasswordLineEdit.setEchoMode(QLineEdit.EchoMode.Normal)
            self.ShowPassButton.setIcon(QtGui.QIcon("./GUI/Icons/view.png"))
        else:
            self.EduPasswordLineEdit.setEchoMode(QLineEdit.EchoMode.Password)
            self.ShowPassButton.setIcon(QtGui.QIcon("./GUI/Icons/hide.png"))

    def display_edu_data(self, command, data):
        if command == 'tasks':
            output = ''
            for task in data:
                output += f'{task.course_name} ↓\n'
                for module in task.modules:
                    output += f'    {module.module_name}\n'
                    output += '     —Тестування\n'
                    for test in module.tests:
                        output += f'      ↪ {str(test)}\n'
                    output += '     —Творчі завдання\n'
                    for creative in module.creative:
                        output += f'      ↪ {str(creative)}\n'
            self.change_output_text(output)
        if command == 'schedule':
            output = ''
            for lesson in data:
                output += f'{lesson.date}, {lesson.name}\n-----------------\n'
            self.change_output_text(output)

    def start_edu_data_fetch(self, command):
        if command == 'schoolTasks':
            Thread(target=self.edu_controller.display_tasks).start()
        elif command == 'schoolSchedule':
            Thread(target=self.edu_controller.display_tomorrow_schedule).start()


    def change_hand_status(self, status):
        self.logicTime = time.time()

        # if status[0] != 'Close':
        #     self.muteTime = self.logicTime

        # if self.logicTime - self.muteTime >= 2:
        #     self.muteTime = self.logicTime
        #     self.audio_controller.toggle_master_mute()

        if time.time() - self.volumeChangeTime >= 0.3:
            self.volumeChangeTime = time.time()
            hand_sign = status[0]
            point_status = status[1]
            if self.muteCount == 8:
                self.audio_controller.toggle_master_mute()
                self.muteCount = 0
            if hand_sign == 'Close':
                self.muteCount += 1
            else:
                self.muteCount = 0

            if point_status == 'Clockwise':
                self.audio_controller.change_master_volume(1)
            elif point_status == 'Counter Clockwise':
                self.audio_controller.change_master_volume(-1)
            print(self.audio_controller.get_master_volume())
            print(hand_sign, point_status)
            print('-------------------------------------------')

    def closeEvent(self, event):
        self.thread_Camera.stop()
        # self.thread_Voice.stop()
        event.accept()

    @pyqtSlot(np.ndarray)
    def update_image(self, cv_img):
        """Updates the image_label with a new opencv image"""
        qt_img = self.convert_cv_qt(cv_img)
        self.CameraFeed.setPixmap(qt_img)

    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format.Format_RGB888)
        p = convert_to_Qt_format.scaled(self.disply_width, self.display_height, Qt.AspectRatioMode.KeepAspectRatioByExpanding)
        return QPixmap.fromImage(p)

    def change_output_text(self, val):
        self.GeneratedOutputText.setPlainText(val)

    def change_current_status_text(self, val):
        self.CurrentStatusText.setPlainText(val)
        if val == 'Stop word!':
            QCoreApplication.quit()

    def change_recognized_text(self, val):
        self.RecognizedInputText.setPlainText(val)

    def change_stop_word(self):
        config.STOP_WORDS = self.StopWordsText.toPlainText().split('\n')
        print(config.STOP_WORDS)

    def change_wait_time(self):
        self.change_config(13, f"Time_to_listen_after_request = {self.WaitTimeSpinBox.value()}")
        config.Time_to_listen_after_request = self.WaitTimeSpinBox.value()

    def change_language(self):
        language = self.LanguageComboBox.currentText()
        self.change_config(12, f"LANGUAGE = '{language}'")
        config.LANGUAGE = language
        match language:
            case 'Ukrainian':
                self.RecognizedInputLabel.setText('Розпізнаний ввід')
                self.CurrentStatusLabel.setText('Поточний статус')
                self.TextOutputLabel.setText('Вихідний текст')
                self.LanguageLabel.setText('Мова')
                self.WaitTimeLabel.setText('Час очікування')
                self.StopWordsLabel.setText('Стоп слова')
                self.EduLoginLabel.setText('Edu.edu Логін')
                self.EduPasswordLabel.setText('Edu.edu Пароль')
                self.CameraFeedLabel.setText('Камера')
            case 'English':
                self.RecognizedInputLabel.setText('Recognized Input')
                self.CurrentStatusLabel.setText('Current Status')
                self.TextOutputLabel.setText('Text Output')
                self.LanguageLabel.setText('Language')
                self.WaitTimeLabel.setText('Wait time')
                self.StopWordsLabel.setText('Stop Words')
                self.EduLoginLabel.setText('Edu.edu Login')
                self.EduPasswordLabel.setText('Edu.edu Password')
                self.CameraFeedLabel.setText('Camera Feed')
            case _:
                self.CurrentStatusText.setPlainText('Language set ERROR! Language does not exist or not supported!')


