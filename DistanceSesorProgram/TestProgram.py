from time import sleep
import time
import board
from picamera2 import Picamera2, Preview
from gpiozero import DistanceSensor
from gpiozero import Motor, DigitalOutputDevice
import adafruit_mpu6050
import busio
import numpy
from libcamera import Transform
import keyboard


sensor = DistanceSensor(23,24)

Lmotor = Motor(5,6)
Rmotor = Motor(27,17)
    
i2c = board.I2C()
accelerometer = adafruit_mpu6050.MPU6050(i2c, address=0x68)

picam = Picamera2()
config = picam.create_preview_configuration()
picam.configure(config)

picam.start_preview(Preview.Qt, transform = Transform(vflip=1, hflip=1))
picam.start()
counter = 0
lastKeyTime = 0
stopping = False
try:
    while True:
        counter = counter + 1
        lastKeyTime += 1
        if counter > 100:
            counter = 0
        sleep(0.05)
        lastAccel = accelerometer.acceleration
        x, y, z = lastAccel
        totalAccelDelta = (x**2 + y**2)**0.5
        if counter == 100:
            print("X={0}, Y={1}, Z={2} Total Accel = {3}".format(round(x, 3), round(y, 3),round(z, 3),round(totalAccelDelta, 3)))
        if totalAccelDelta > 100 and lastKeyTime > 50 and not stopping:
            print("CRASH!!")
            Lmotor.stop()
            Rmotor.stop()
            exit()
        stopping = False
        if sensor.distance < 0.4:
            Lmotor.stop()
            Rmotor.stop()
            stopping = True
            if counter == 10:
                print("Imminent Crash")
            if keyboard.is_pressed('a') and keyboard.is_pressed('s') :
                if counter == 100:
                    print("Backwards Left")
                Lmotor.backward(0.1)
                Rmotor.backward()
                lastKeyTime += 1
                
            elif keyboard.is_pressed('d') and keyboard.is_pressed('s') :
                if counter == 100:
                    print("Backwards Right")
                Lmotor.backward()
                Rmotor.backward(0.1)
                lastKeyTime += 1
            elif keyboard.is_pressed('a'):
                if counter == 100:
                    print("Left")
                Lmotor.backward()
                Rmotor.forward()
                lastKeyTime += 1
            elif keyboard.is_pressed('d'):
                if counter == 100:
                    print("Right")
                Lmotor.forward()
                Rmotor.backward()
                lastKeyTime += 1
            elif keyboard.is_pressed('s'):
                if counter == 100:
                    print("Backwards")
                Lmotor.backward()
                Rmotor.backward()
                lastKeyTime += 1
            
        else:
            if keyboard.is_pressed('a') and keyboard.is_pressed('w') :
                if counter == 100:
                    print("Forward Left")
                Lmotor.forward(0.1)
                Rmotor.forward()
                lastKeyTime += 1
            elif keyboard.is_pressed('d') and keyboard.is_pressed('w') :
                if counter == 100:
                    print("Forward Right")
                Lmotor.forward()
                Rmotor.forward(0.1)
                lastKeyTime += 1
            elif keyboard.is_pressed('a') and keyboard.is_pressed('s') :
                if counter == 100:
                    print("Backwards Left")
                Lmotor.backward(0.1)
                Rmotor.backward()
                lastKeyTime += 1
            elif keyboard.is_pressed('d') and keyboard.is_pressed('s') :
                if counter == 100:
                    print("Backwards Right")
                Lmotor.backward()
                Rmotor.backward(0.1)
                lastKeyTime += 1
            elif keyboard.is_pressed('w'):
                if counter == 100:
                    print("Forwards")
                Lmotor.forward()
                Rmotor.forward()
                lastKeyTime += 1
            elif keyboard.is_pressed('a'):
                if counter == 100:
                    print("Left")
                Lmotor.backward()
                Rmotor.forward()
                lastKeyTime += 1
            elif keyboard.is_pressed('d'):
                if counter == 100:
                    print("Right")
                Lmotor.forward()
                Rmotor.backward()
                lastKeyTime += 1
            elif keyboard.is_pressed('s'):
                if counter == 100:
                    print("Backwards")
                Lmotor.backward()
                Rmotor.backward()
                lastKeyTime += 1
            else:
                Lmotor.stop()
                Rmotor.stop()
                lastKeyTime = 0
                stopping = True
            
        if counter == 100:
            print('Distance to nearest object is', sensor.distance, 'm')
except KeyboardInterrupt:
    Lmotor.stop()
    Rmotor.stop()



#while True:
#    print('Distance to nearest object is', sensor.distance, 'm')
#    sleep(0.01)s