import RPi.GPIO as gpio
import time



gpio.setmode(gpio.BOARD)

gpio.setup(12,gpio.OUT)
gpio.setup(11,gpio.OUT)
gpio.setup(13,gpio.OUT)
gpio.setup(15,gpio.OUT)
gpio.setup(19,gpio.OUT)
gpio.setup(21,gpio.OUT)
gpio.setup(23,gpio.OUT)

gpio.output(12,True)
gpio.output(11,True)
gpio.output(13,True)
gpio.output(15,True)
gpio.output(19,True)
gpio.output(21,True)
gpio.output(23,True)


print("Laboratorio Felipe Coral and Brayan Saldarriaga")
for x in range(0,200):
	#NUmero 0
	gpio.output(12,False)
	gpio.output(11,False)
	gpio.output(13,False)
	gpio.output(15,False)
	gpio.output(19,False)
	gpio.output(21,False)
	gpio.output(23,True)
	time.sleep(0.5)

	#NUmero 1
	gpio.output(12,True)	#a
	gpio.output(11,False)	#b
	gpio.output(13,False)	#c
	gpio.output(15,True)	#d
	gpio.output(19,True)	#e
	gpio.output(21,True)	#f
	gpio.output(23,True)	#g	
	time.sleep(0.5)
	#NUmero 2
	gpio.output(12,False)
	gpio.output(11,False)
	gpio.output(13,True)
	gpio.output(15,False)
	gpio.output(19,False)
	gpio.output(21,True)
	gpio.output(23,False)
	time.sleep(0.5)

	#NUmero 3
	gpio.output(12,False)
	gpio.output(11,False)
	gpio.output(13,False)
	gpio.output(15,False)
	gpio.output(19,True)
	gpio.output(21,True)
	gpio.output(23,False)
	time.sleep(0.5)
	#NUmero 4
	gpio.output(12,True)
	gpio.output(11,False)
	gpio.output(13,False)
	gpio.output(15,True)
	gpio.output(19,True)
	gpio.output(21,False)
	gpio.output(23,False)
	time.sleep(0.5)
	#Numero 5
	gpio.output(12,False)
	gpio.output(11,True)
	gpio.output(13,False)
	gpio.output(15,False)
	gpio.output(19,True)
	gpio.output(21,False)
	gpio.output(23,False)
	time.sleep(0.5)
	#NUmero 6
	gpio.output(12,False)
	gpio.output(11,True)
	gpio.output(13,False)
	gpio.output(15,False)
	gpio.output(19,False)
	gpio.output(21,False)
	gpio.output(23,False)
	time.sleep(0.5)

	#NUmero 7
	gpio.output(12,False)
	gpio.output(11,False)
	gpio.output(13,False)
	gpio.output(15,True)
	gpio.output(19,True)
	gpio.output(21,True)
	gpio.output(23,True)
	time.sleep(0.5)
	#NUmero 8
	gpio.output(12,False)
	gpio.output(11,False)
	gpio.output(13,False)
	gpio.output(15,False)
	gpio.output(19,False)
	gpio.output(21,False)
	gpio.output(23,False)
	time.sleep(0.5)
	#NUmero 9
	gpio.output(12,False)
	gpio.output(11,False)
	gpio.output(13,False)
	gpio.output(15,False)
	gpio.output(19,True)
	gpio.output(21,False)
	gpio.output(23,False)
	time.sleep(0.5)