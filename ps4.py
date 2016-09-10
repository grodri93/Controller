import controller
import os
from time import sleep
import serial

ser = serial.Serial('/dev/ttyUSB0', 9600)

ser.isOpen()

c = controller.PS4()
while True:
	buttons, axis, dPad = c.input()
	
	os.system('clear')
	for key, val in buttons.items():
		if buttons[key] == 1:
			print "%s has been pressed" % key
			ser.write(key)
			
        	
	
