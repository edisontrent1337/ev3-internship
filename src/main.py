import ev3dev.ev3 as ev3

a = ev3.LargeMotor("outA")
b = ev3.LargeMotor("outB")
c = ev3.LargeMotor("outC")
d = ev3.LargeMotor("outD")
f = ev3.TouchSensor("in1")
g = ev3.UltrasonicSensor("in3")
h = ev3.TouchSensor("in4")
dist = g.MODE_US_DIST_CM


def forward():
    a.run_direct(duty_cycle_sp=50)
    b.run_direct(duty_cycle_sp=-50)
    c.run_direct(duty_cycle_sp=-50)
    d.run_direct(duty_cycle_sp=50)
    while True:
        if g.distance_centimeters <= 20 or 1 == f.is_pressed:
            a.stop()
            b.stop()
            c.stop()
            d.stop()
            start()


def start():
    while True:
        if 1 == h.is_pressed:
            forward()


start()
