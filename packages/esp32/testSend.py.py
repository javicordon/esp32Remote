from ir_tx import Player
from sys import platform
from machine import Pin
import ujson

# TX
if platform == 'esp32':
    pintx = Pin(32, Pin.OUT)
ir = Player(pintx)

def sendIRcmd(cmdName = None):
    try:
        with open(cmdName, 'r') as f:
            cmdTX = ujson.load(f)
        ir.play(cmdTX)
    except:
        print('Command not found')