import ev3dev.ev3 as ev3

globalSpeed = 50
TurnSpeed = 100
a = ev3.LargeMotor("outA")
b = ev3.LargeMotor("outB")
c = ev3.LargeMotor("outC")
d = ev3.LargeMotor("outD")
f = ev3.TouchSensor("in1")
g = ev3.UltrasonicSensor("in3")
h = ev3.TouchSensor("in4")
i = ev3.TouchSensor("in2")
dist = g.MODE_US_DIST_CM


def stop():
    print("Object located at a distance of " + str(g.distance_centimeters) + " Centimeters. Turning off...")
    a.stop()
    b.stop()
    c.stop()
    d.stop()
    print("Stopped action. Object at a distance of " + str(g.distance_centimeters) + " Centimeters.")
    print("Waiting for new command")
    print()
    while True:
        if 1 == h.is_pressed:
            right()
        if 1 == f.is_pressed:
            left()
        if 1 == i.is_pressed:
            forward()


def forward():
    print("Moving forward")
    print()
    a.run_direct(duty_cycle_sp=globalSpeed)
    b.run_direct(duty_cycle_sp=0 - globalSpeed)
    c.run_direct(duty_cycle_sp=0 - globalSpeed)
    d.run_direct(duty_cycle_sp=globalSpeed)
    while True:
        if 1 == h.is_pressed:
            right()
        if 1 == f.is_pressed:
            left()
        if g.distance_centimeters <= 20:
            stop()


def right():
    print("Turning right")
    print()
    a.run_direct(duty_cycle_sp=0 - TurnSpeed)
    b.run_direct(duty_cycle_sp=TurnSpeed)
    c.run_direct(duty_cycle_sp=0 - TurnSpeed)
    d.run_direct(duty_cycle_sp=TurnSpeed)
    while True:
        if 1 == f.is_pressed:
            left()
        if 1 == i.is_pressed:
            forward()
        if g.distance_centimeters <= 10:
            stop()


def left():
    print("Turning left")
    print()
    a.run_direct(duty_cycle_sp=TurnSpeed)
    b.run_direct(duty_cycle_sp=0 - TurnSpeed)
    c.run_direct(duty_cycle_sp=TurnSpeed)
    d.run_direct(duty_cycle_sp=0 - TurnSpeed)
    while True:
        if 1 == h.is_pressed:
            right()
        if 1 == i.is_pressed:
            forward()
        if g.distance_centimeters <= 10:
            stop()


def start():
    print("Started Robot")
    print()
    print()
    while True:
        if 1 == h.is_pressed:
            right()
        if 1 == f.is_pressed:
            left()
        if 1 == i.is_pressed:
            forward()
