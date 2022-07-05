

from sys import byteorder
from array import array
from struct import pack
from features import mfcc
from features import logfbank

import serial
import string
import scipy.io.wavfile as wav
import numpy as np
import dataset
import pyaudio
import wave
import os
import time
import kaboom, tornado

##h = bytes('d',"utf-8")


#comando = serial.Serial("/dev/rfcomm0", baudrate=9600, timeout=0.5)

THRESHOLD = 2000
CHUNK_SIZE = 512
FORMAT = pyaudio.paInt16
RATE = 44100
exit_flag = 0

def si_esta_en_silencio(snd_data):
    "Returns 'True' if below THRESHOLD"
    return max(snd_data) < THRESHOLD

def normalize(snd_data):
    "Average the volume out"
    MAXIMUM = 16384
    times = float(MAXIMUM)/max(abs(i) for i in snd_data)

    r = array('h')
    for i in snd_data:
        r.append(int(i*times))
    return r

def trim(snd_data):  
    "Trim the blank spots at the start and end"
    def _trim(snd_data):
        snd_started = False
        r = array('h')

        for i in snd_data:
            if not snd_started and abs(i)>THRESHOLD:
                snd_started = True
                r.append(i)

            elif snd_started:
                r.append(i)
        return r

    # Trim to the left
    snd_data = _trim(snd_data)

    # Trim to the right
    snd_data.reverse()

    snd_data = _trim(snd_data)
    snd_data.reverse()
    return snd_data

def record():
    """
    Record a word or words from the microphone and 
    return the data as an array of signed shorts.
    """
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=1, rate=RATE,
        input=True, output=True,
        frames_per_buffer=CHUNK_SIZE)

    num_silent = 0
    snd_started = False

    r = array('h')

    while 1:
        # little endian, signed short
        snd_data = array('h', stream.read(CHUNK_SIZE))
        if byteorder == 'big':
            snd_data.byteswap()
        r.extend(snd_data)

        silent = si_esta_en_silencio(snd_data)

        if silent and snd_started:
            num_silent += 1
        elif not silent and not snd_started:
            snd_started = True

        if snd_started and num_silent > 30:
            break

    sample_width = p.get_sample_size(FORMAT)
    stream.stop_stream()
    stream.close()
    p.terminate()

    r = normalize(r)
    r = trim(r)
    return sample_width, r

def record_to_file(path):  
    "Records from the microphone and outputs the resulting data to 'path'"
    sample_width, data = record()
    data = pack('<' + ('h'*len(data)), *data)

    wf = wave.open(path, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(sample_width)
    wf.setframerate(RATE)
    wf.writeframes(data)
    wf.close()

#programa main
def check_for_match(input):  
    "Takes input and searches dataset for a hit" 
    flag = 0
    
    global exit_flag
    for i in np.array((tornado.tornado)):
        no_match = i
        if (np.allclose(input,no_match,0.00000000,2.70000000)==True) and (flag == 0):
            print ("ATACANDO CON TORNADO")
            flag = 1
            #comando.write('t')
            return "tornado"


    for i in np.array((kaboom.kaboom)):
        no_match = i
        if (np.allclose(input,no_match,0.00000000,3.00000000)==True) and (flag == 0):
            print ("KAAAAABOOOOM!")
            flag = 1
            #comando.write('w')
            return "kaboom"
    

    if flag == 0:
        print ("DESCONOCIDA PALABRA")



while True:
    "Passively listen for user input"
  
    if __name__ == '__main__':
        print("ejecute comando de PANCHO.PRIME")
        record_to_file('testing1.wav')
        print("done - result written to testing1.wav")
        
        (rate,sig) = wav.read("testing1.wav")

        mfcc_feat = mfcc(sig,rate)
        fbank_feat = logfbank(sig,rate)

        input = fbank_feat[1:3,:] 
        print (input)
        check_for_match(input)

        print (exit_flag)
        if exit_flag == 1:
            break

#turn off LEDs and clean GPIO


print ("program has exited")
