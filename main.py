import serial
from pycaw.pycaw import AudioUtilities

def main():
	# make serial connection
	global arduino
	arduino = serial.Serial('COM3', 9600)
	arduino.reset_input_buffer()

	while True:

		data = arduino.readline().decode("utf-8")

		# loop thru sessions
		sessions = AudioUtilities.GetAllSessions()
		for session in sessions:
			volume = session.SimpleAudioVolume
			if session.Process and session.Process.name() == "Discord.exe":
				volume.SetMasterVolume(0.6, None)

		print(data, end="")

if __name__ == '__main__':
	main()