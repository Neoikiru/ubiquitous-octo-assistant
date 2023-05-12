import random
import sys
import time

from PyQt6.QtCore import QCoreApplication, QThread, pyqtSignal

import openai
from fuzzywuzzy import fuzz
from pvrecorder import PvRecorder
from ukrainian_tts.tts import TTS, Voices, Stress
import simpleaudio as sa
import speech_recognition as sr
from elevenlabslib import *
import pvporcupine
import os
import yaml
# test
# import torch
# import sounddevice as sd
# test
import config


class VoiceModule(QThread):
    recognizedText = pyqtSignal(str)
    currentStatus = pyqtSignal(str)
    outputText = pyqtSignal(str)
    logicSignal = pyqtSignal(str)

    openai.api_key = config.GPT_TOKEN

    user = ElevenLabsUser(config.ElevenLabsUserApiKey)
    voice = user.get_voices_by_name('Elli')[0]

    data = yaml.safe_load(open('customCommands.yaml', 'rt', encoding='utf8'))

    porcupine = pvporcupine.create(
        access_key=config.PICOVOICE_ACCESS_KEY,
        keyword_paths=['./wake-words/Start_en_windows_v2_1_0.ppn',
                       './wake-words/Hey-elli_en_windows_v2_1_0.ppn'],
        sensitivities=[1] * 2
    )

    tts = TTS(device='cpu')

    # language = 'ua'
    # model_id = 'v3_ua'
    # sample_rate = 48000
    # speaker = 'mykyta'
    # device = torch.device('cpu')
    #
    # model, example_text = torch.hub.load(repo_or_dir='snakers4/silero-models',
    #                                      model='silero_tts',
    #                                      language=language,
    #                                      speaker=model_id)
    # model.to(device)

    recorder = PvRecorder(device_index=-1, frame_length=porcupine.frame_length)
    print('Using device: %s' % recorder.selected_device)

    def run(self):
        self.SpeachModule()

    def speech_to_text(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
        try:
            if config.LANGUAGE == 'English':
                out = r.recognize_google(audio, language='en-US')
            elif config.LANGUAGE == 'Ukrainian':
                out = r.recognize_google(audio, language='uk-UA')
            else:
                print(f'ERR! Whisper AI is DEAD {config.LANGUAGE}')
            # out = r.recognize_whisper(audio, language=LANGUAGE)
            return out
        except sr.UnknownValueError:
            self.currentStatus.emit('Could not understand!')
            print('could not understand')
        except sr.RequestError as e:
            self.currentStatus.emit('Could not request results!')
            print('Could not request results')

    def play_audio(self, file):
        wave_obj = sa.WaveObject.from_wave_file(file)
        play_obj = wave_obj.play()
        play_obj.wait_done()

    def text_to_speech_ukrainian(self, text):
        # audio = self.model.apply_tts(text=text,
        #                              speaker=self.speaker,
        #                              sample_rate=self.sample_rate)
        # sd.play(audio, self.sample_rate)
        with open('audio.wav', mode='wb') as file:
            _, output_text = self.tts.tts(text, Voices.Tetiana.value, Stress.Dictionary.value, file)
        # print('Accented text:', output_text)
        self.play_audio('audio.wav')

    def text_to_speech_english(self, text):
        self.voice.generate_and_play_audio(text, playInBackground=False)

    def GPT_response(self, text):
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[
                {'role': 'system', 'content': f'You are a virtual assistant. You must reply in {config.LANGUAGE}.'},
                {'role': 'user', 'content': text}
            ],
            max_tokens=200,
            temperature=0.6,
        )
        return response['choices'][0]['message']['content']

    def executeCustomCommands(self, text):
        path = os.getcwd() + '\scripts'
        method, command = self.customCommands(text)
        match method:
            case 'bat':
                # f'cmd /c "{path}/{command}.bat"'
                os.system(f'{path}/{command}.bat')
                # os.spawnl(os.P_NOWAIT, f'{path}/{command}.bat')
                self.currentStatus.emit(f'Successfully executed {command}')
            case 'cmd':
                # executeCommand = f'{command}'
                os.system(command)
                # os.spawnl(os.P_NOWAIT, command)
                self.currentStatus.emit(f'Successfully executed {command}')
            case 'EduModule':
                self.currentStatus.emit(f'Fetching data about: {command}')
                self.logicSignal.emit(command)
            case _:
                return None
        if config.LANGUAGE == 'Ukrainian':
            return ['Виконано', 'Добре', 'Один момент', 'Секунду'][random.randint(0, 3)]
        else:
            return ['Yes, sir!', 'Done', 'Success', 'Easy peasy'][random.randint(0, 3)]

    def customCommands(self, text):
        executeMethod = None
        executeCommand = None
        maxConfidence = 0
        for command, phrases in self.data.items():
            for phrase in phrases:
                if fuzz.WRatio(text, phrase) >= maxConfidence:
                    maxConfidence = fuzz.WRatio(text, phrase)
                    try:
                        executeCommand = command.split('_')[0]
                        executeMethod = command.split('_')[1]
                    except:
                        print('Invalid custom command!')
        if maxConfidence <= 87: return None, executeCommand
        print(executeMethod, executeCommand, maxConfidence)
        return executeMethod, executeCommand

    def SpeachModule(self):
        print('Successfully started Speach Module!')
        recorder = self.recorder
        while True:
            recorder.start()
            pcm = recorder.read()
            keyword_index = self.porcupine.process(pcm)
            if keyword_index == config.SupportedActivationWords.index(config.ACTIVATION_WORD):
                recorder.stop()
                print('Listening to your commands: ')
                self.currentStatus.emit('Listening to your commands: ')
                startTime = time.time()
                while time.time() - startTime <= config.Time_to_listen_after_request:
                    text = self.speech_to_text()
                    if text:
                        print(text)
                        self.currentStatus.emit('Success!')
                        self.recognizedText.emit(text)
                        if any(ele in text for ele in config.STOP_WORDS):  # Stop condition
                            recorder.stop()
                            self.currentStatus.emit('Stop word!')

                        # implement custom commands, like set timer, google something or anything else
                        response = self.executeCustomCommands(text)
                        if response is None:
                            response = self.GPT_response(text)

                        # Synthesize answer
                        self.currentStatus.emit('Synthesizing answer!')
                        self.outputText.emit(response)
                        print(config.LANGUAGE)
                        if config.LANGUAGE == 'Ukrainian':
                            self.text_to_speech_ukrainian(response)
                        elif config.LANGUAGE == 'English':
                            self.text_to_speech_english(response)
                        startTime = time.time()
                    self.currentStatus.emit('Listening...')
                self.currentStatus.emit('Waiting for key word...')
                print('Waiting for key word...')
            recorder.stop()
