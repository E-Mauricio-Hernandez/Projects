import paho.mqtt.client as mqtt

broker_address = "10.1.128.1"
client = mqtt.Client('Publicador_ejem1') # Creación del cliente
client.connect(broker_address)
topic = "casa/habitaciones/hab1/luz"

client.publish(topic, "Ejemplo desde Python")