'''
Jacob George (jg965)
Kevin J. Wang (kjw99)

ECE 5990 Final Project: traning.py
December 11, 2015

'''

from sys import byteorder
from array import array
from struct import pack
from features import mfcc
from features import logfbank

import scipy.io.wavfile as wav
import numpy as np
import dataset
import pyaudio
import wave
import lumos, close, nox, yes1, no

THRESHOLD = 500
CHUNK_SIZE = 2048
FORMAT = pyaudio.paInt16
RATE = 48000
exit_flag = 0

def is_silent(snd_data):
    "Returns 'True' if below THRESHOLD"
    return max(snd_data) < THRESHOLD

def normalize(snd_data):
    "Average volume out"
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

        silent = is_silent(snd_data)

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

def check_for_match(input):
    "Takes input and searches dataset for a hit"
    
    flag = 0
    global exit_flag
    
    for i in np.array(close.close):
        no_match = i
        if (np.allclose(input,no_match,0.00000000,3.00000000)==True) and (flag == 0):
            print "CLOSE"
            flag = 1
            exit_flag = 1
            return "close"

    for i in np.array((lumos.lumos)):
        no_match = i
        if (np.allclose(input,no_match,0.00000000,2.30000000)==True) and (flag == 0): #2.2
            print "LUMOS"
            flag = 1
            return "lumos"
    
    for i in np.array(nox.nox):
        no_match = i
        if (np.allclose(input,no_match,0.00000000,2.50000000)==True) and (flag == 0):
            print "NOX"
            flag = 1
            return "nox"
            
    for i in np.array((no.no)):
        no_match = i
        if (np.allclose(input,no_match,0.00000000,3.00000000)==True) and (flag == 0):
            print "NO"
            flag = 1
            return "no"

    for i in np.array(yes1.yes1):
        yes_match = i
        if (np.allclose(input,yes_match,0.00000000,3.00000000)==True) and (flag == 0):
            print "YES1"
            flag = 1
            return "yes1"

    if flag == 0:
        print "desconocida"
        return "desconocida"

def parse_array(recording,word):
    "Write calculated coefficients into database"

    if word is 'lumos':
        testing = recording.tolist()
        testfile = open('lumos.py','a')
        testfile.write(",")
        testfile.write(str(testing))
        print "adding"
    
    if word is 'close':
        testing = recording.tolist()
        testfile = open('close.py','a')
        testfile.write(",")
        testfile.write(str(testing))
        print "adding"

    if word is 'nox':
        testing = recording.tolist()
        testfile = open('nox.py','a')
        testfile.write(",")
        testfile.write(str(testing))
        print "adding"

    if word is 'yes1':
        testing = recording.tolist()
        testfile = open('yes1.py','a')
        testfile.write(",")
        testfile.write(str(testing))
        print "adding"    

    if word is 'no':
        testing = recording.tolist()
        testfile = open('no.py','a')
        testfile.write(",")
        testfile.write(str(testing))
        print "adding"


def training():
    '''
    Takes input signal and searches current dataset for hit.
    If hit, then add to correct dataset.
    If miss, asks user for currect input and adds to dataset.
    '''
    
    print("please speak a word into the microphone")
    record_to_file('training.wav')
    print("done - result written to training.wav")

    (rate,sig) = wav.read("training.wav")

    mfcc_feat = mfcc(sig,rate)
    fbank_feat = logfbank(sig,rate)
    
    recording = fbank_feat[1:3,:] 


    testing = check_for_match(recording)

    verify = raw_input("did you say " + testing + " ")

    if verify is 'y':
        parse_array(recording,testing)

    if verify is 'n':
        correct_word = input("what word did you mean? ")
        print correct_word
        parse_array(recording,correct_word)

while True:
    "Continously run program until user finishes training"
    
    if __name__ == '__main__':
        user_input = raw_input("what would you like to do? ")

        if user_input in 'train':
            training()
        
        if user_input in 'exit':
            break        

print "program has exited"
