from rtttl import RTTTL
import songs
import time
from machine import Pin, PWM

def play_tone(freq, msec, tone):
    print('freq = {:6.1f} msec = {:6.1f}'.format(freq, msec))
    if freq > 0:
        tone.duty(10)
        tone.freq(int(freq))
	time.sleep(msec*0.001)  # Play for a number of msec
    tone.duty(0)            # Stop playing
    time.sleep(0.01)        # Delay 50 ms between notes

#tune = RTTTL(songs.find('Super Mario - Main Theme'))
#tune = RTTTL(songs.find('MissionImp'))
#tune = RTTTL(songs.find('StarWars'))
#tune = RTTTL(songs.find('Bond'))

def play_song(name='SMBtheme'):
    tune = RTTTL(songs.find(name))
    # Initialize input/output pins
    speaker_pin   = 13  # Speaker is connected to this DIGITAL pin
    tone = PWM(Pin(speaker_pin, Pin.OUT), freq=1000, duty=8)

    for freq, msec in tune.notes():
        play_tone(freq, msec, tone)

    tone.deinit() 