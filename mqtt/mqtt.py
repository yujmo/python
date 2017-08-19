

##server 
from paho.mqtt.publish import mqtt
import json
mqttc = mqtt.Client()
mqttc.connect(host='10.16.89.91',port=1883,keepalive=60)

while True:
	if __name__ == '__main__':
		dis=Get_Distance() #接收距离的函数
		mqttc.publish('mqtt', dis)
mqttc.loop_forever()




##client
import paho.mqtt.client as mqtt
import json
def on_connect(client, userdata, flags, rc):
    print('Connected with result code ' + str(rc))
    client.subscribe('mqtt')


def on_message(client, userdata, msg):
#    print  str(msg.payload)
    print (100+json.loads(msg.payload))

if __name__ == '__main__':
	client = mqtt.Client()
	client.on_connect = on_connect
	client.on_message = on_message
	a = on_message
	print a



	try:
		client.connect(host='10.16.89.91',port=1883,keepalive=60)
		client.loop_forever()
	except KeyboardInterrupt:
		client.disconnect()
'''

