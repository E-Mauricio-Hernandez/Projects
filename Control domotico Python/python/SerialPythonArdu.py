import serial
import time

arduino = serial.Serial('COM5', baudrate=9600, timeout = 1.0)

arduino.setDTR(False)
time.sleep(1)
arduino.flushInput()
arduino.setDTR(True)

time.sleep(2) #importantisimo esto

arduino.write(b'9')

line = arduino.readline()
line2 = line.decode('ascii', 'strict')
print(line2)

arduino.close()