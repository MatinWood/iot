# orangepi zero2
# UL2003 driver
# 28BYJ-48 stepping motor
from wiringpi import GPIO
import wiringpi
import time
import sys

wiringpi.wiringPiSetup()

pin1 = 10
pin2 = 13
pin3 = 15
pin4 = 16

pin_list = [pin1, pin2, pin3, pin4]


def init():
    for pin in pin_list:
        wiringpi.pinMode(pin, GPIO.OUTPUT)
    for pin in pin_list:
        wiringpi.digitalWrite(pin, GPIO.LOW)


def setStep(a, b, c, d):
    wiringpi.digitalWrite(pin1, a)
    wiringpi.digitalWrite(pin2, b)
    wiringpi.digitalWrite(pin3, c)
    wiringpi.digitalWrite(pin4, d)


def clockwize(delay_ms):
    setStep(GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.HIGH)
    wiringpi.delay(delay_ms)
    setStep(GPIO.LOW, GPIO.LOW, GPIO.HIGH, GPIO.HIGH)
    wiringpi.delay(delay_ms)
    setStep(GPIO.LOW, GPIO.HIGH, GPIO.HIGH, GPIO.LOW)
    wiringpi.delay(delay_ms)
    setStep(GPIO.HIGH, GPIO.HIGH, GPIO.LOW, GPIO.LOW)
    wiringpi.delay(delay_ms)


def rclockwize(delay_ms):
    setStep(GPIO.HIGH, GPIO.HIGH, GPIO.LOW, GPIO.LOW)
    wiringpi.delay(delay_ms)
    setStep(GPIO.LOW, GPIO.HIGH, GPIO.HIGH, GPIO.LOW)
    wiringpi.delay(delay_ms)
    setStep(GPIO.LOW, GPIO.LOW, GPIO.HIGH, GPIO.HIGH)
    wiringpi.delay(delay_ms)
    setStep(GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.HIGH)
    wiringpi.delay(delay_ms)


def stop():
    setStep(GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.LOW)


if __name__ == '__main__':
    init()
    for i in range(500):
        clockwize(10)
    stop()
