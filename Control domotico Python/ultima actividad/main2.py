import board
import busio
import math
import numpy as np
import adafruit_mcp4725
import matplotlib.pyplot as  plt
from time import sleep
i2c = busio.I2C(board.SCL, board.SDA)
dac = adafruit_mcp4725.MCP4725(i2c)
dac.raw_value = 4095
i=0
f=100
t=1/f
n=50
while True: 
    f = open ('datos.txt','r')
    mensaje = f.read()
    f.close()
    formadeonda=int(mensaje)
    ts=t/n
    dac.raw_value = 2047
    sleep(0.1)
    for i in range(n):
        coseno=np.cos((2*math.pi*f*i*ts)+(2*math.pi*formadeonda/8))*2047
        señal=coseno+2047
        out=int(señal)
        dac.raw_value = out
