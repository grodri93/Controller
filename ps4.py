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
	
	LY = axis.get("LY", 0.0)
	RX = axis.get("RX", 0.0)
	
	if RX >= 0:
		LM_C = 1.0
		RM_C = 1.0 - 0.25 * RX
	else:
		LM_C = 1.0 + 0.25 * RX
		RM_C = 1.0
	
	speed = (1500.0 + 500 * LY)
	LM_speed = speed * LM_C
	RM_speed = speed * RM_C
	
	speedData = "s" + str(LM_speed) + ";" + str(RM_speed) + "e"
	
	ser.write(speedData)
		   
#	for key, val in buttons.items():
#		if buttons[key] == 1:
#			print "%s has been pressed" % key
#			ser.write(key)
			
        	
	
