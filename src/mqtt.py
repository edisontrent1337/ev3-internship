import paho.mqtt.client as mqtt
from ev3dev.core import Sound

from main import stop
from main import left
from main import right
from main import forward
from main import setSpeed
from main import turn


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    client.subscribe("/valtech/internship/#")


def on_message(client, userdata, msg):
    decoded = msg.payload.decode('utf-8')
    print(msg.topic + " " + decoded)
    if decoded == "forward":
        forward()
    elif decoded == "left":
        left()
    elif decoded == "right":
        right()
    elif decoded == "stop":
        stop()
    elif "speed" in decoded:
        speed = decoded.split(":")[1]
        setSpeed(speed)
    elif "chat" in decoded:
        text = decoded.split(":")[1]
        Sound.speak(text).wait()
    elif "turn" in decoded:
        ha = decoded.split(":")[1]
        turn(int(ha))
    else:
        print("Unknown message:" + decoded)


print("can start robot now")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipseprojects.io", 1883, 60)

client.loop_forever()
