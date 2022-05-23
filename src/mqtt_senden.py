import paho.mqtt.publish as publish

while True:
    cmd = (str(input("Command:")))
    publish.single("/valtech/internship", cmd, hostname="mqtt.eclipseprojects.io")
