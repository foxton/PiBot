import RPI.GPIO as GPIO
import time

def driveForward(seconds):
GPIO.output(MOTOR_A_DIR, GPIO.LOW)
GPIO.output(MOTOR_B_DIR, GPIO.HIGH)
MOTOR_A_PWM.start(dc_A)
MOTOR_B_PWM.start(dc_B)
time.sleep(seconds) 
return

#use BOARD pin numbering
GPIO.setmode(GPIO.BOARD)


#Motor pins
MOTOR_A_PWM = 3
MOTOR_A_DIR = 5
MOTOR_B_PWM = 8
MOTOR_B_DIR = 10
dc_a = 50
dc_b = 50

GPIO.setup(engineLeft1, GPIO.OUT)
GPIO.setup(engineLeft2, GPIO.OUT)
GPIO.setup(engineRight1, GPIO.OUT)
GPIO.setup(engineRight2, GPIO.OUT)

MOTOR_A_PWM = GPIO.PWM(MOTOR_A_PWM,500) 
MOTOR_B_PWM = GPIO.PWM(MOTOR_B_PWM,500)
pwmright1 = GPIO.PWM(engineRight1,10000)
pwmright2 = GPIO.PWM(engineRight2,10000)

driveForward(5)
GPIO.cleanup