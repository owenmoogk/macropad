import serial, time

def main():
	# make serial connection
	global arduino
	arduino = serial.Serial('COM3', 9600)
	arduino.reset_input_buffer()

	while True:

		data = arduino.readline().decode("utf-8")

		print(data, end="")

if __name__ == '__main__':
	main()