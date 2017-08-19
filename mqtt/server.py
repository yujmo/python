import paho.mqtt.client as mqtt
import json
mqttc = mqtt.Client()
mqttc.connect(host='127.0.0.1',port=1883,keepalive=60)
while True:
    test = "test"
    mqttc.publish('mqtt', test)
mqttc.loop_forever()
