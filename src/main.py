import time

import ev3dev.ev3 as ev3
global testlol
heading = 0

globalSpeed = 50
TurnSpeed = 100
a = ev3.LargeMotor("outA")
b = ev3.LargeMotor("outB")
c = ev3.LargeMotor("outC")
d = ev3.LargeMotor("outD")


def turn(value):
    x = int(value)
    if value > 0:  # turn right
        a.duty_cycle_sp = globalSpeed * x / 100
        b.duty_cycle_sp = - globalSpeed * x / 100
        c.duty_cycle_sp = - globalSpeed - globalSpeed * x / 100
        d.duty_cycle_sp = globalSpeed - globalSpeed * x / 100
    elif value < 0:
        a.duty_cycle_sp = globalSpeed
        b.duty_cycle_sp = 0 - globalSpeed * x / 100
        c.duty_cycle_sp = globalSpeed
        d.duty_cycle_sp = 0 - (globalSpeed * x / 100)
    else:
        a.duty_cycle_sp = globalSpeed
        b.duty_cycle_sp = 0 - globalSpeed
        c.duty_cycle_sp = 0 - globalSpeed
        d.duty_cycle_sp = globalSpeed


def set_motor_speed(motor, value):
    if motor == 'a':
        a.run_direct(duty_cycle_sp=value)
    if motor == 'b':
        b.run_direct(duty_cycle_sp=value)
    if motor == 'c':
        c.run_direct(duty_cycle_sp=value)
    if motor == 'd':
        d.run_direct(duty_cycle_sp=value)
    if motor == 'ab':
        a.run_direct(duty_cycle_sp=value)
        b.run_direct(duty_cycle_sp=value)


def stop():
    a.stop()
    b.stop()
    c.stop()


def set_speed(value):
    global globalSpeed
    globalSpeed = int(value)
    a.duty_cycle_sp = globalSpeed
    b.duty_cycle_sp = 0 - globalSpeed
    c.duty_cycle_sp = 0 - globalSpeed
    d.duty_cycle_sp = globalSpeed


def rotacionar(angle):
    c.run_to_abs_pos(position_sp=angle, speed_sp=50, stop_action="hold")


def acceltesting(speed2):
    testlol = speed2
    while testlol != 0:
        a.duty_cycle_sp = testlol
        b.duty_cycle_sp = testlol
        testlol = testlol - 1
        time.sleep(0.1)
