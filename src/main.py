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


def stop():
    a.stop()
    b.stop()
    c.stop()
    d.stop()


def forward():
    print("Moving forward")
    print()
    a.run_direct(duty_cycle_sp=globalSpeed)
    b.run_direct(duty_cycle_sp=-globalSpeed)
    c.run_direct(duty_cycle_sp=-globalSpeed)
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
            a.run_direct(duty_cycle_sp=base_speed + 1)
            b.run_direct(duty_cycle_sp=base_speed)
        if b.position < a.position:
            a.run_direct(duty_cycle_sp=base_speed)
            b.run_direct(duty_cycle_sp=base_speed + 1)
        else:
            a.run_direct(duty_cycle_sp=base_speed)
            b.run_direct(duty_cycle_sp=base_speed)


def turn_test(value):
    c.run_to_abs_pos(position_sp=value, speed_sp=120, stop_action="hold")


def rotacionar(angle):
    c.run_to_abs_pos(position_sp=angle, speed_sp=50, stop_action="hold")
