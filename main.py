import sys
from PyQt6.QtWidgets import QApplication
import PyQt
from fuzzywuzzy import fuzz
import config
import warnings


def settings_handler():
    if config.LANGUAGE not in config.SupportedLanguages:
        for lang in config.SupportedLanguages:
            if fuzz.WRatio(lang, config.LANGUAGE) >= 85:
                print('Error! Language is not supported! Perhaps you wanted to enter: "{}"'.format(lang))
                return 1
        print('Error! Language is not supported!')
        return 1
    if config.ACTIVATION_WORD not in config.SupportedActivationWords:
        for word in config.SupportedActivationWords:
            if fuzz.WRatio(word, config.ACTIVATION_WORD) >= 85:
                print('Error! Activation word is not supported! Perhaps you wanted to enter "{}"'.format(word))
                return 1
        print('Error! Activation word is not supported!')
        return 1
    if len(config.GPT_TOKEN) <= 5:
        print('Error! ChatGPT api key is invalid!')
        return 1
    if len(config.PICOVOICE_ACCESS_KEY) <= 5:
        print('Error! Picovoice api key is invalid!')
        return 1
    if len(config.ELEVENLABS_API_KEY) <= 5:
        print('Error! Elevenlabs api key is invalid!')
        return 1
    return 0

#

#

if __name__ == '__main__':
    # warnings.filterwarnings('ignore')
    # for device in PvRecorder.get_audio_devices():
    #     print('{} --> {}'.format(PvRecorder.get_audio_devices().index(device), device))
    # input_device = int(input('Please type index of preferred device: '))
    # recorder = PvRecorder(device_index=input_device, frame_length=
    if settings_handler():
        sys.exit('Error! Bad settings!')

    app = QApplication([])
    window = PyQt.UI()
    window.show()
    app.exec()

