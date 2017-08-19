import paho.mqtt.client as mqtt
def on_connect(client, userdata, flags, rc):
    print('Connected with result code ' + str(rc))
    client.subscribe('mqtt')
def on_message(client, userdata, msg):
    print (msg.payload)
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
try:
client.connect(host='127.0.0.1',port=1883,keepalive=60)
    client.loop_forever(2)
except KeyboardInterrupt:
    client.disconnect()
