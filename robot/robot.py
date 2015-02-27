import RPI.GPIO as GPIO
import time

#use BOARD pin numbering
GPIO.setmode(GPIO.BOARD)

engineLeft1 = 3
engineLeft2 = 5
engineRight1 = 8
engineRight2 = 10
dc = 50.0

GPIO.setup(engineLeft1, GPIO.OUT)
GPIO.setup(engineLeft2, GPIO.OUT)
GPIO.setup(engineRight1, GPIO.OUT)
GPIO.setup(engineRight2, GPIO.OUT)

pwmleft1 = GPIO.PWM(engineLeft1,10000) 
pwmleft2 = GPIO.PWM(engineLeft2,10000) 
pwmright1 = GPIO.PWM(engineRight1,10000)
pwmright2 = GPIO.PWM(engineRight2,10000)

pwmleft1.start(dc)
pwmleft2.start(dc)


GPIO.cleanup