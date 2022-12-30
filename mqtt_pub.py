import ssl
from paho import mqtt
import paho.mqtt.client as paho
import paho.mqtt.publish as publish
import random
import json

brokerUrl = "821032442a5c4b30982ba8c1b2085d07.s2.eu.hivemq.cloud"
brokerPort = 8883
brokerUsername = "morgana"
brokerPassword = "morgana01"
temp = random.randint(17,25)
pres = bool(random.choice([True, False]))

# create a set of 2 test messages that will be published at the same time
msgs = [
  {'topic': "lab/temperature", 'payload': (temp)}, ("lab/presence", (pres), 0, False)
]

# use TLS for secure connection with HiveMQ Cloud
sslSettings = ssl.SSLContext(mqtt.client.ssl.PROTOCOL_TLS)

# put in your cluster credentials and hostname
auth = {'username': brokerUsername, 'password': brokerPassword}
publish.multiple(msgs, hostname=brokerUrl, port=brokerPort, auth=auth,
                 tls=sslSettings, protocol=paho.MQTTv31)