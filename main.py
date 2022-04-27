from time import sleep
import serial, win32api, pyautogui, requests
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume, ISimpleAudioVolume
from win32con import *

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
from time import sleep
import os

os.environ["SPOTIPY_CLIENT_ID"] = '76c57350098e47e19eab6a4f50782348'
os.environ["SPOTIPY_CLIENT_SECRET"] = 'c98eed161a6c434ca3e4b0d080de5c8a'
os.environ["SPOTIPY_REDIRECT_URI"] = 'http://localhost'

scope = "user-read-playback-state,user-modify-playback-state"

sp = spotipy.Spotify(client_credentials_manager=SpotifyOAuth(scope=scope))

def getSpotifyVolume():
	res = sp.devices()
	for device in res['devices']:
		if device['is_active']:
			return(device['volume_percent'])

def main():
	# configure arduino
	global arduino
	arduino = serial.Serial('COM3', 9600)
	arduino.reset_input_buffer()

	print('running')

	while True:

		data = arduino.readline().decode("utf-8")
		print("Incoming Data: " + data, end='')

		# discord volume
		if 'discordDown' in data:
			sessions = AudioUtilities.GetAllSessions()
			for session in sessions:
				volume = session.SimpleAudioVolume
				if session.Process and session.Process.name() == 'Discord.exe':
					volume.SetMasterVolume(max(round(volume.GetMasterVolume() - 0.02, 2), 0), None)
		
		if 'discordUp' in data:
			sessions = AudioUtilities.GetAllSessions()
			for session in sessions:
				volume = session.SimpleAudioVolume
				if session.Process and session.Process.name() == 'Discord.exe':
					volume.SetMasterVolume(max(round(volume.GetMasterVolume() + 0.02, 2), 0), None)

		if 'pause' in data:
			win32api.keybd_event(VK_MEDIA_PLAY_PAUSE, 0, KEYEVENTF_EXTENDEDKEY, 0)

		if 'skip' in data:
			win32api.keybd_event(VK_MEDIA_NEXT_TRACK, 0, KEYEVENTF_EXTENDEDKEY, 0)

		if "prev" in data:
			win32api.keybd_event(VK_MEDIA_PREV_TRACK, 0, KEYEVENTF_EXTENDEDKEY, 0)

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
			newVolume = volume.GetMasterVolumeLevelScalar() + 0.02
			volume.SetMasterVolumeLevelScalar(newVolume, None)

		if "volumeDown" in data:
			devices = AudioUtilities.GetSpeakers()
			interface = devices.Activate(
				IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
			volume = cast(interface, POINTER(IAudioEndpointVolume))
			newVolume = volume.GetMasterVolumeLevelScalar() - 0.02
			volume.SetMasterVolumeLevelScalar(newVolume, None)

		if 'spotifyDown' in data:
			newVolume = getSpotifyVolume() - 10
			sp.volume(newVolume)

		if 'spotifyUp' in data:
			newVolume = getSpotifyVolume() + 10
			sp.volume(newVolume)

		if "stickyCaps" in data:
			with open('sticky.txt', "r") as f:
				lines = f.readlines()
			with open('sticky.txt', "w") as f:

				# if off turn on
				if lines[0] == 'false':
					f.write('true')

				# if on turn off, and fix caps state
				else:
					f.write('false')

if __name__ == '__main__':
	main()