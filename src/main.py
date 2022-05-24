import ev3dev.ev3 as ev3

heading = 0

globalSpeed = 50
TurnSpeed = 100
a = ev3.LargeMotor("outA")
b = ev3.LargeMotor("outB")
c = ev3.LargeMotor("outC")
d = ev3.LargeMotor("outD")


def turn(value):
    x = int(value)
    if value > 0:
        a.duty_cycle_sp = 0 - (globalSpeed*x/100)
        b.duty_cycle_sp = globalSpeed
        c.duty_cycle_sp = 0 - globalSpeed*x/100
        d.duty_cycle_sp = globalSpeed
    elif value < 0:
        a.duty_cycle_sp = globalSpeed
        b.duty_cycle_sp = 0 - globalSpeed*x/100
        c.duty_cycle_sp = globalSpeed
        d.duty_cycle_sp = 0 - (globalSpeed*x/100)
    else:
        a.duty_cycle_sp = globalSpeed
        b.duty_cycle_sp = 0 - globalSpeed
        c.duty_cycle_sp = 0 - globalSpeed
        d.duty_cycle_sp = globalSpeed


def stop():
    a.stop()
    b.stop()
    c.stop()
    d.stop()


def forward():
    print("Moving forward")
    print()
    a.run_direct(duty_cycle_sp=0 - globalSpeed)
    b.run_direct(duty_cycle_sp=0 - globalSpeed)
    c.run_direct(duty_cycle_sp=0 - globalSpeed)
    d.run_direct(duty_cycle_sp=globalSpeed)
    # while True:
    #    if g.distance_centimeters <= 10:
    #        stop()
    #        break


def right():
    print("Turning right")
    print()
    a.run_direct(duty_cycle_sp=0 - TurnSpeed)
    b.run_direct(duty_cycle_sp=TurnSpeed)
    c.run_direct(duty_cycle_sp=0 - TurnSpeed)
    d.run_direct(duty_cycle_sp=TurnSpeed)
    # while True:
    # if g.distance_centimeters <= 20:
    # stop()
    # break


def left():
    print("Turning left")
    print()
    a.run_direct(duty_cycle_sp=TurnSpeed)
    b.run_direct(duty_cycle_sp=0 - TurnSpeed)
    c.run_direct(duty_cycle_sp=TurnSpeed)
    d.run_direct(duty_cycle_sp=0 - TurnSpeed)
    # while True:
    # if g.distance_centimeters <= 20:
    # stop()
    # break


def set_speed(value):
    global globalSpeed
    globalSpeed = int(value)
    a.duty_cycle_sp = globalSpeed
    b.duty_cycle_sp = 0 - globalSpeed
    c.duty_cycle_sp = 0 - globalSpeed
    d.duty_cycle_sp = globalSpeed


def set_motor_speed(motor, value):

    if motor == 'a':
        a.duty_cycle_sp = value
    if motor == 'b':
        b.duty_cycle_sp = value
    if motor == 'c':
        c.duty_cycle_sp = value
    if motor == 'd':
        d.duty_cycle_sp = value

    if motor == 'ab':
        a.run_direct(duty_cycle_sp=value)
        b.run_direct(duty_cycle_sp=value)


def drive(base_speed=50):
    a.position = 0
    b.position = 0
    while True:
        if a.position < b.position:
            a.run_direct(duty_cycle_sp=base_speed + 3)
            b.run_direct(duty_cycle_sp=base_speed)
        if b.position < a.position:
            a.run_direct(duty_cycle_sp=base_speed)
            b.run_direct(duty_cycle_sp=base_speed + 3)
        else:
            a.run_direct(duty_cycle_sp=base_speed)
            b.run_direct(duty_cycle_sp=base_speed)




def turn_test(value):
    if float(value) < 0:
        c.run_timed(speed_sp=-250, time_sp=50)
    else:
        c.run_timed(speed_sp=250, time_sp=50)

