from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


class AudioHandler:
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    def __init__(self):
        self.isMuted = self.volume.GetMute()
        self.currentVolume = self.get_master_volume()

    def get_master_volume(self):
        return (round(self.volume.GetMasterVolumeLevelScalar() * 100))

    def set_master_volume(self, var):
        self.volume.SetMasterVolumeLevelScalar((var / 100), None)

    def change_master_volume(self, percentage):
        if self.isMuted:
            return
        if (self.currentVolume + percentage) <= 100 and (self.currentVolume+percentage) >= 0:
            self.currentVolume += percentage
            self.set_master_volume(self.currentVolume)

    def toggle_master_mute(self):
        self.isMuted = not self.isMuted
        # print('Muted' if self.isMuted else 'Unmuted')
        # print(f'Is muted? {self.isMuted}\n Current volume: {self.currentVolume}')
        self.set_master_volume(0 if self.isMuted else self.currentVolume)
