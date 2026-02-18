from machine import Pin
import time

in1 = Pin(23, Pin.OUT)
in2 = Pin(22, Pin.OUT)
in3 = Pin(19, Pin.OUT)
in4 = Pin(18, Pin.OUT)

cw = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
ancw = [[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]]


while True:
    for i in range(500):
        for s in cw:
            in1.value(s[0])
            in2.value(s[1])
            in3.value(s[2])
            in4.value(s[3])
            time.sleep(0.005)

    for x in range(500):
        for s in ancw:
            in1.value(s[0])
            in2.value(s[1])
            in3.value(s[2])
            in4.value(s[3])
            time.sleep(0.005)
