# Week 4 assignment
# by Chris Larson

import RPi.GPIO as GPIO
import time

butPin = 17

pwmPin = 18
ledPin = 23


dc = 95

# we have a wedge, going with BCM, if direct we can go with board
#GPIO.BOARDGPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)                       
GPIO.setup(ledPin, GPIO.OUT)
#GPIO.setup(pwmPin, GPIO.OUT)
#pwm = GPIO.PWM(pwmPin, 1000)
GPIO.setup(butPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#pwm.start(50)
#pwm.ChangeDutyCycle(75)
GPIO.output(ledPin, GPIO.LOW)
#pwm.start(dc)

print("here we go, press CTRL+C to exit")
try:
    while 1:
        if GPIO.input(butPin): #button is released
            #pwm.ChangeDutyCycle(dc)
            GPIO.output(ledPin, GPIO.HIGH)
            time.sleep(0.05)
            GPIO.output(ledPin, GPIO.LOW)
            time.sleep(0.45)
            GPIO.output(ledPin, GPIO.HIGH)
            time.sleep(0.06)
            GPIO.output(ledPin, GPIO.LOW)
            time.sleep(0.15)
           
        else: # if button pushed
            #pwm.ChangeDutyCycle(100-dc)
            GPIO.output(ledPin, GPIO.HIGH)
except KeyboardInterrupt:
    #pwm.stop()
    GPIO.cleanup()
#if GPIO.input(17):
#    print("pin 11 is high")
#else:
#    print("pin 11 is low")
    
