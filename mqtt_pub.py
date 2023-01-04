import paho.mqtt.client as paho
from paho import mqtt

import random
import time

brokerUrl = "821032442a5c4b30982ba8c1b2085d07.s2.eu.hivemq.cloud"
brokerPort = 8883
brokerUsername = "morgana"
brokerPassword = "morgana01"

client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
client.username_pw_set(brokerUsername, brokerPassword)
client.connect(brokerUrl, brokerPort)

def mock_number(min, max): 
  return random.randrange(min,max)

def mock_presence(): 
  list = [1, 0]
  return random.choice(list)

def mock_topic(): 
  list = ['temperature', 'presence']
  return random.choice(list)

def mock_msgs(max):
  i=0
  payload = []
  while (i<max):
      topic = mock_topic()
      if topic == 'temperature':
        temp = mock_number(17,25)  
        msg = {'topic':'lab/temperature', 'payload': temp}
      if topic == 'presence':
        pres = mock_presence()  
        msg = {'topic':'lab/presence', 'payload': pres}
      payload.append(msg)
      i=i+1
  return payload

qnt = mock_number(5, 15)
msgs = mock_msgs(qnt)
for el in msgs:
  time.sleep(5)
  #client.publish("lab/temperature", payload="21", qos=1, retain=True)
  client.publish(el["topic"], payload=el["payload"], qos=1, retain=True)
  print(el)