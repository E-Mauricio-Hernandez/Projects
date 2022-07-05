import paho.mqtt.client as mqtt #import the client1
broker_address="192.168.0.22" 
def hola(client,period=0.25):
 if msgType=="SUBACK":
  if client.on_subscribe:
    while not client.suback_flag:
      logging.info("waiting suback")
      client.loop()  #check for messages
      time.sleep(period)
#broker_address="iot.eclipse.org"
print("creando una nueva instancia")
client = mqtt.Client("P1") #create new instance
print("connectandome al broker")
client.connect(broker_address) #connect to broker
print("Subscribiendome al topico")
client.subscribe("unillanos/laboratorios/windows/win1")
hola(client)
