from machine import Pin
import time

in1 = Pin(23, Pin.OUT)
in2 = Pin(22, Pin.OUT)
in3 = Pin(19, Pin.OUT)
in4 = Pin(18, Pin.OUT)

btn = Pin(26, Pin.IN, Pin.PULL_UP)

cw  = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
acw = [[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]]

a = 0

while True:

    if btn.value() == 0:
        a = 1 - a
        time.sleep(0.2)

    if a == 0:
        for s in cw:
            in1.value(s[0])
            in2.value(s[1])
            in3.value(s[2])
            in4.value(s[3])
            time.sleep(0.01)

    if a == 1:
        for s in acw:
            in1.value(s[0])
            in2.value(s[1])
            in3.value(s[2])
            in4.value(s[3])
            time.sleep(0.01)
