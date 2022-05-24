import paho.mqtt.client as mqtt
from ev3dev.core import Sound

from main import stop
from main import turn
from main import rotacionar
from main import set_motor_speed
from main import acceltesting
from main import speedup


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("/valtech/internship/#")


def on_message(client, userdata, msg):
    decoded = msg.payload.decode('utf-8')
    print(msg.topic + " " + decoded)
    if decoded == "stop":
        stop()
    elif "chat" in decoded:
        text = decoded.split(":")[1]
        Sound.speak(text).wait()
    elif "turn" in decoded:
        ha = decoded.split(":")[1]
        turn(int(ha))
    elif "rotarlasmotoresenelgrado" in decoded:
        rotaciones = decoded.split(":")[1]
        rotacionar(float(rotaciones))
    elif "acceleration" in decoded:
        speed = decoded.split(":")[1]
        set_motor_speed("ab", float(speed) * 75)
    elif "acceltesting" in decoded:
        testspeed = decoded.split(":")[1]
        acceltesting(int(testspeed))
    elif "speedup" in decoded:
        speedaddition = decoded.split(":") [1]
        speedup(int(speedaddition))

    else:
        print("Unknown message:" + decoded)


print("can start robot now")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipseprojects.io", 1883, 60)

client.loop_forever()
