# RCCar
RC Car with Auto Stop
Caleb Incarnato
RC Car with Auto-Stop using Wi-Fi and Bluetooth
	This project aims to create an RC car with an auto-stop feature. A Raspberry Pi is used to control all parts of the car, with one python program running to interface with all connected devices. Wi-Fi and Bluetooth technologies are utilized to remotely control the car. The car communicates wirelessly with a remote PC, streaming live camera footage via VNC while using a Bluetooth keyboard for remote control. An ultrasonic distance sensor is used to automatically stop the car when it gets too close to an obstacle, and an accelerometer is used to detect crashes. Four DC motors are connected to two motor controllers and separate batteries which provide adequate movement control.

	•Physical Components Used
	  oRaspberry Pi 5
	    It is the controller for the entire car with everything connected to it, except the separate batteries for the motors.
	    Python program that has all control logic is loaded manually.
	    
	  o2x L298N Motor Controllers
	    Connected to four TT Motors with separate left-right control via the Raspberry Pi.
	  o4x TT Motors
	    Connected to the L298N Controllers in a configuration that allows for separate left-right side control
	    Powered via two 3.7V 18650 batteries in series
	  o1x MPU-6050 Accelerometer
	    Provides live updates of the acceleration in the X, Y, Z axes for detection of crashes, connected to Raspberry Pi
	  o1x 10000mAh Anker “PowerCore Slim”
	    Provides multiple hours of power to the Raspberry Pi
	    Could be swapped for any power source that can provide at least 15W via USB-C
	  o1x 222° FOV Wide Angle RPi Camera
	    Allows for live feed from the RC Car via VNC
	    Mounted to laser cut front piece
	  o1x HC-SR04 Ultrasonic Distance Sensor
	    Provides precise distance data from the front of the car and is used to implement auto-stop functionality.
	    Mounted to laser cut front piece 
	  o1x COKOINO 4WD Car Chassis Kit
	    A frame that has enough room to mount all components to and has slots for additional laser-cut pieces to be added.
	•Libraries Used
	  oAll code is written in Python and uses libraries to control all connected components
	  otime
	      sleep
	        •Used to add delays in the program
	  opicamera2
	      Picamera2
	        •Used to receive input from the camera
	  	  Preview
	        •Used to display camera input to the user
	  ogpiozero
	    	DistanceSensor
	       	 •Reads distance data from the HC-SR04
	      Motor
	        •	Allows for easy control of the motor controllers
	  oadafruit_mpu6050
	    	Reads data from the accelerometer and turns it into an array of x,y,z acceleration
	  onumpy
	      Allows for math to find total acceleration in the xy-plane
	  olibcamera
	      Transform
	        •Used to flip the camera preview vertically and horizontally so it displays properly
	  okeyboard
	    	Reads input from the keyboard which is used to control the direction of the car
	•Pseudocode
	  oInitialize distance sensor, camera preview, accelerometer, motors
	  oCalculate total acceleration in xy-plane
	  oIf crash then exit program
	  oIf closer than 0.4m to object
	  	Only allow turning and backwards movement
	  oElse allow free movement
	  	W – Forward
	  	A – Left
	  	S – Backward
	  	D - Right
