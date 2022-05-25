import paho.mqtt.client as mqtt
from ev3dev.core import Sound

from main import stop
from main import turn
from main import turn_test
from main import set_motor_speed
from main import acceltesting
from main import speedup


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("/valtech/internship/#")


def on_message(client, userdata, msg):
    decoded = msg.payload.decode('utf-8')
    if decoded == "stop":
        stop()
    elif "chat" in decoded:
        text = decoded.split(":")[1]
        Sound.speak(text).wait()
    elif "turn" in decoded:
        ha = decoded.split(":")[1]
        turn(int(ha))
    elif "steer" in decoded:
        angle = float(decoded.split(":")[1])
        angle_squared = angle * angle * (-1 if angle < 0 else 1)
        turn_test(angle_squared*30)
    elif decoded == "accel":
        speedup(2)
    elif decoded == "brake":
        speedup(-2)


print("can start robot now")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipseprojects.io", 1883, 60)

client.loop_forever()
