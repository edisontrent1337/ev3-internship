import paho.mqtt.client as mqtt
import ev3dev.ev3 as ev3
from main import start

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("/valtech/internship/#")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    decoded = msg.payload.decode('utf-8')
    print(msg.topic + " " + decoded)
    if decoded == 'start':
        start()



client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipseprojects.io", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface


client.loop_forever()
