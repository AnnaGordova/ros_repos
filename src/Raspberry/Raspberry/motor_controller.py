import RPi.GPIO as GPIO
from time import sleep

in1 = 24
in2 = 23
en = 25
temp1 = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(en, GPIO.OUT)
GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)
p = GPIO.PWM(en, 1000)
p.start(25)
print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n") 
'''

    r – run (to run or start the motor)
  na  s – stop (to stop the motor)
    f – forward (to run the motor in forward direction) – default direction
    b – backward (to reverse the direction of rotation)
    l – low (to decrease the speed to 25%) – default speed
    m – medium (to run the motor at medium speed 50%)
    h – high (to increase the speed to 75% level)
    e – exit (to stop the motor and exit Python)

'''
while(1):
    GPIO.output(in1,GPIO.HIGH)

    GPIO.output(in2,GPIO.LOW)


