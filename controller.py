import pygame

class Controller(object):

	def __init__(self):
		pygame.init()
		pygame.joystick.init()
		self.controller = pygame.joystick.Joystick(0)
		self.controller.init()
		self.numButtons = self.controller.get_numbuttons()
		self.buttons = {}
		for buttonNum in range(self.numButtons):
			self.buttons[buttonNum] = 0
		self.axis = {0:0}
		self.dPad = {0:(0,0)}

	def read(self):

		for event in pygame.event.get():
			# Button pressing
			if event.type == pygame.JOYBUTTONDOWN:
				self.buttons[event.button] = 1
			if event.type == pygame.JOYBUTTONUP:
				self.buttons[event.button] = 0
			# Joystick movement
			if event.type == pygame.JOYAXISMOTION:
				self.axis[event.axis] = round(event.value, 3)
			# D-Pad pressing
			if event.type == pygame.JOYHATMOTION:
				self.dPad[event.hat] = event.value

		return self.buttons, self.axis, self.dPad

class PS4(Controller):

	def __init__(self):
		super(PS4, self).__init__()
		self.buttons, self.axis, self.dPad = self.read()
		self.BLayout = ['Square', 'X', 'Circle', 'Triangle', 'L1',
						'R1', 'L2', 'R2', 'Share', 'Options', 
						'Left', 'Right', 'PS', 'Trackpad']
		self.ALayout = ['LX', 'LY', 'RX', 'LTrigger', 'RTrigger', 'RY'
						'nothing1', 'TX', 'TY', 'nothing2']
		self.PS4Buttons = {}
		self.PS4Axis = {}
	
	def input(self):
		self.buttons, self.axis, self.dPad = self.read()

		self.PS4Buttons =  dict(zip(self.BLayout, self.buttons.values()))
		self.PS4Axis = dict(zip(self.ALayout, self.axis.values()))

		return self.PS4Buttons, self.PS4Axis, self.dPad




	




