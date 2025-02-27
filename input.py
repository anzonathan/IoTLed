#CMD input to Arduino Using Serial communication
#pip intstall pyserial

import serial 
import time



#Serial Object
arduino = serial.Serial(port = '/dev/cu.usbmodem144401', baudrate=115200, timeout=.1) #Port should be whichever com port

def write_read(x):
    arduino.write(bytes(x,'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return   data

while True:
    num = input("Press 1 for 'on' and 2 for 'off'\nEnter: ")
    value = write_read(num)
    print(value)



   