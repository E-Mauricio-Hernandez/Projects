import serial
import time

arduino = serial.Serial('COM5', baudrate=9600, timeout = 1.0)
arduino.setDTR(False)
time.sleep(1)
arduino.flushInput()
arduino.setDTR(True)

while True:
	line = arduino.readline()
	line2 = line.decode('ascii', 'strict')
	print(line2)
	#print(line)
	#print(type(line2))
