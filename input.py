#Inputs to serial arduino Ports
#pip intstall pyserial, requests

import serial 
import time
import requests

def get_posts():

    #API endpoint 
    url = 'http://127.0.0.1:8000/state/'

    try:
        #Make a get request to the API endpoint
        response = requests.get(url)

        #Check if the request was succesful 
        if response.status_code == 200:
            posts = response.json()
            return posts
        else:
            print('Error:', response.status_code)
            return None
        
    except requests.exceptions.RequestException as e:

        # For handling any network related errors or exceptions
        print('Error:', e)
        return None

def main():

    posts = get_posts()
    if posts:
        print('Value:', posts['switchState'])

    else:
        print('Failed to fetch posts from API.')

if __name__ == '__main__':
    main()


#Serial Object
arduino = serial.Serial(port = '/dev/cu.usbmodem146401', baudrate=115200, timeout=.1) #Port should be whichever com port

def write_read(x):
    arduino.write(bytes(x,'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return   data

while True:
    main()
    time.sleep(0.5)




   