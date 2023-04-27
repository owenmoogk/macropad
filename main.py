import pyautogui
import os

from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL

import serial
from ctypes import cast, POINTER

# api sim skipping keypresses
from win32con import *
import win32api

def main():
    # configure arduino
    global arduino
    arduino = serial.Serial('COM3', 9600)
    arduino.reset_input_buffer()

    print('running main')

    while True:

        data = arduino.readline().decode("utf-8")
        print("Incoming Data: " + data, end='')

        # spotify volume
        if 'spotifyDown' in data:
            sessions = AudioUtilities.GetAllSessions()
            for session in sessions:
                volume = session.SimpleAudioVolume
                if session.Process and session.Process.name() == 'Spotify.exe':
                    volume.SetMasterVolume(
                        max(round(volume.GetMasterVolume() - 0.10, 2), 0), None)

        if 'spotifyUp' in data:
            sessions = AudioUtilities.GetAllSessions()
            for session in sessions:
                volume = session.SimpleAudioVolume
                if session.Process and session.Process.name() == 'Spotify.exe':
                    volume.SetMasterVolume(
                        min(round(volume.GetMasterVolume() + 0.10, 2), 1), None)
                    
        # discord volume
        if 'discordDown' in data:
            sessions = AudioUtilities.GetAllSessions()
            for session in sessions:
                volume = session.SimpleAudioVolume
                if session.Process and session.Process.name() == 'Discord.exe':
                    volume.SetMasterVolume(
                        max(round(volume.GetMasterVolume() - 0.1, 2), 0), None)

        if 'discordUp' in data:
            sessions = AudioUtilities.GetAllSessions()
            for session in sessions:
                volume = session.SimpleAudioVolume
                if session.Process and session.Process.name() == 'Discord.exe':
                    volume.SetMasterVolume(
                        min(round(volume.GetMasterVolume() + 0.1, 2), 1), None)

        if 'pause' in data:
            win32api.keybd_event(VK_MEDIA_PLAY_PAUSE, 0,
                                 KEYEVENTF_EXTENDEDKEY, 0)

        if 'skip' in data:
            win32api.keybd_event(VK_MEDIA_NEXT_TRACK, 0,
                                 KEYEVENTF_EXTENDEDKEY, 0)

        if "prev" in data:
            win32api.keybd_event(VK_MEDIA_PREV_TRACK, 0,
                                 KEYEVENTF_EXTENDEDKEY, 0)

        if 'copy' in data:
            pyautogui.keyDown('ctrl')
            pyautogui.press('c')
            pyautogui.keyUp('ctrl')

        if 'paste' in data:
            pyautogui.keyDown('ctrl')
            pyautogui.press('v')
            pyautogui.keyUp('ctrl')

        if "volumeUp" in data:
            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(
                IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            volume = cast(interface, POINTER(IAudioEndpointVolume))
            newVolume = min(volume.GetMasterVolumeLevelScalar() + 0.02, 1)
            volume.SetMasterVolumeLevelScalar(newVolume, None)

        if "volumeDown" in data:
            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(
                IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            volume = cast(interface, POINTER(IAudioEndpointVolume))
            newVolume = max(volume.GetMasterVolumeLevelScalar() - 0.02, 0)
            volume.SetMasterVolumeLevelScalar(newVolume, None)


if __name__ == '__main__':
    main()
