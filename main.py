import serial, os
from pycaw.pycaw import AudioUtilities
import win32api
from win32con import *

def main():
	# configure arduino
	global arduino
	arduino = serial.Serial('COM3', 9600)
	arduino.reset_input_buffer()

	while True:

		data = arduino.readline().decode("utf-8")
		print(data, end='')

		# discord volume
		if 'discord' in data:
			sessions = AudioUtilities.GetAllSessions()
			for session in sessions:
				volume = session.SimpleAudioVolume
				if session.Process and session.Process.name() == 'Discord.exe':
					volume.SetMasterVolume(max(round(volume.GetMasterVolume() - 0.01, 2), 0), None)

		if 'pause' in data:
			win32api.keybd_event(VK_MEDIA_PLAY_PAUSE, 0, KEYEVENTF_EXTENDEDKEY, 0)

		if 'skip' in data:
			win32api.keybd_event(VK_MEDIA_NEXT_TRACK, 0, KEYEVENTF_EXTENDEDKEY, 0)

		if "prev" in data:
			win32api.keybd_event(VK_MEDIA_PREV_TRACK, 0, KEYEVENTF_EXTENDEDKEY, 0)


if __name__ == '__main__':
	main()