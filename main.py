#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
#import pyb, sdcard
# Write your program here


motorLeft = Motor(Port.A)
motorRight = Motor(Port.D)
sensor = UltrasonicSensor(Port.S1)
wheelDiam = 56
wheelSpace = 150
robot = DriveBase(motorLeft, motorRight, wheelDiam, wheelSpace)
f = open('distance_data.dat','w')
t = 0
while t < 10000:
    sensorValue = sensor.distance()
    f.write(sensorValue)
    print(sensorValue)
    kp = .9
    if sensorValue <  100:
        kp = 1.5
    t = t + 1
    motorSpeed = kp*(sensorValue - 100)
    robot.drive(motorSpeed, 0)
f.close()
