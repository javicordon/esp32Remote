import time
from machine import Pin
from machine import Timer
from ir_rx import NEC_16

def ir_callback(data,addr,ctrl):
    global ir_data
    global ir_addr
    if data > 0:
        ir_data = data
        ir_addr = addr
        print('Data {:02x} Addr {:04}'.format(data,addr))

def timer_callback(timer):
    led.value( not led.value() )

ir = NEC_16(Pin(5, Pin.IN), ir_callback)
ir = NEC_16(Pin(35, Pin.IN), ir_callback)

led = Pin(2, Pin.OUT)
tim0 = Timer(0)
isLedBlinking = False