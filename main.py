from PyQt6.QtWidgets import QApplication
import PyQt
import warnings


if __name__ == '__main__':
    warnings.filterwarnings('ignore')
    # for device in PvRecorder.get_audio_devices():
    #     print('{} --> {}'.format(PvRecorder.get_audio_devices().index(device), device))
    # input_device = int(input('Please type index of preferred device: '))
    # recorder = PvRecorder(device_index=input_device, frame_length=

    app = QApplication([])
    window = PyQt.UI()
    window.show()
    app.exec()

