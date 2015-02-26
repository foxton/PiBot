import RPI.GPIO as GPIO
import time

#use BOARD pin numbering
GPIO.setmode(GPIO.BOARD)

engineLeft1 = 3
engineLeft2 = 5
engineRight1 = 8
engineRight2 = 10
GPIO.setup(engineLeft1, GPIO.OUT)
GPIO.setup(engineLeft2, GPIO.OUT)
GPIO.setup(engineRight1, GPIO.OUT)
GPIO.setup(engineRight1, GPIO.OUT)

GPIO.output(engineLeft1, 0) #Turn off Left engine
GPIO.output(engineLeft2, 0) #Turn off Left engine
GPIO.output(engineRight1, 0) #Turn off Right engine
GPIO.output(engineRight2, 0) #Turn off Right engine
GPIO.cleanup