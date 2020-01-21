#!/usr/bin/env python
# coding: Latin-1

# Load library functions we want
import time
import pygame
import RPi.GPIO as GPIO


axisUpDown = 1                          # Joystick axis to read for up / down position
axisUpDownInverted = False            # Set this to True if up and down appear to be swapped

axisLeftRight = 0                       # Joystick axis to read for left / right position
axisLeftRightInverted = False       #Set this to True if left and right appear to be swapped
interval = 0.1                          # Time between keyboard updates in seconds, smaller responds faster but uses more processor time

# Setup pygame and key states
global hadEvent
global moveUp
global moveDown
global moveLeft
global moveRight
global moveQuit
hadEvent = True
moveUp = False
moveDown = False
moveLeft = False
moveRight = False
moveQuit = False
pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()
#screen = pygame.display.set_mode([300,300])
#pygame.display.set_caption("JoyBorg - Press [ESC] to quit")

# Function to handle pygame events
def PygameHandler(events):
    # Variables accessible outside this function
    global hadEvent
    global moveUp
    global moveDown
    global moveLeft
    global moveRight
    #global moveQuit
    # Handle each event individually
    for event in events:

        if event.type == pygame.JOYAXISMOTION:
            # A joystick has been moved, read axis positions (-1 to +1)
            hadEvent = True
            
            upDown = joystick.get_axis(axisUpDown)
            leftRight = joystick.get_axis(axisLeftRight)
            
                
            # Determine Up / Down values
            if upDown < -0.1:
                moveUp = True
                moveDown = False
                
            elif upDown > 0.1:
                moveUp = False
                moveDown = True
                
            else:
                moveUp = False
                moveDown = False
                
            # Determine Left / Right values
            if leftRight < -0.1:
                moveLeft = True
                moveRight = False
                
            elif leftRight > 0.1:
                moveLeft = False
                moveRight = True
                
            else:
                moveLeft = False
                moveRight = False
                
#import RPi.GPIO as GPIO
import time

class MotorDriver(object):

    def __init__(self):

        self.PIN = 18
        
        self.PWMA1 = 8
        self.PWMA2 = 10
        self.PWMB1 = 12
        self.PWMB2 = 13
        self.D1 = 7
        self.D2 = 11

        self.PWM = 50

        #GPIO.setmode(GPIO.BCM)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(self.PIN, GPIO.IN, GPIO.PUD_UP)
        GPIO.setup(self.PWMA1, GPIO.OUT)
        GPIO.setup(self.PWMA2, GPIO.OUT)
        GPIO.setup(self.PWMB1, GPIO.OUT)
        GPIO.setup(self.PWMB2, GPIO.OUT)
        GPIO.setup(self.D1, GPIO.OUT)
        GPIO.setup(self.D2, GPIO.OUT)
        self.p1 = GPIO.PWM(self.D1, 500)
        self.p2 = GPIO.PWM(self.D2, 500)
        self.p1.start(50)
        self.p2.start(50)

    def set_motor(self, A1, A2, B1, B2):
        GPIO.output(self.PWMA1, A1)
        GPIO.output(self.PWMA2, A2)
        GPIO.output(self.PWMB1, B1)
        GPIO.output(self.PWMB2, B2)

    def forward(self):
        self.set_motor(1, 0, 1, 0)

    def stop(self):
        self.set_motor(0, 0, 0, 0)

    def reverse(self):
        self.set_motor(0, 1, 0, 1)

    def left(self):
        self.set_motor(0, 1, 1, 0)

    def right(self):
        self.set_motor(1, 0, 0, 1)
        
        
                
if __name__ == '__main__':     # Program start from here
    motor = MotorDriver()
    try:
        print('Press [ESC] to quit')
        # Loop indefinitely
        while True:
            # Get the currently pressed keys on the keyboard
            PygameHandler(pygame.event.get())
            
            if hadEvent:
                # Keys have changed, generate the command list based on keys
                hadEvent = False

                if moveLeft:
                    print("LEFT")
                    motor.left()
                    #time.sleep(0.2)
  
                elif moveRight:
                    print("RIGTH")
                    motor.right()
                    #ime.sleep(0.2)
                    
                elif moveUp:
                    print("UP")
                    motor.forward()
                    #time.sleep(0.2)
                    
                    
                elif moveDown:
                    print("DOWN")
                    motor.reverse()
                    #time.sleep(0.2)
                   
                else:
                    print(" ")
                    motor.stop()
                    #time.sleep(0.2)
                    
            # Wait for the interval period
            time.sleep(interval)
        # Disable all drives
        MotorOff()
        
    except KeyboardInterrupt:
        # CTRL+C exit, disable all drives
        MotorOff()       
        GPIO.cleanup()
        print("Starting Motor DRiver Test...END")

