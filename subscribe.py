import random

from paho.mqtt import client as mqtt_client


broker = 'wss://vernemq-testops.pwc.dev.cos.pwtestops.com/mqtt'
port = 1883
topic = "python/mqtt"
# generate client ID with pub prefix randomly
topic = "python/mqtt"
client_id = 'test-client-id'
username = 'tsmmqttuser'
password = 'ZFjN39bfg4YgCL9d'



def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client):
    def on_message(client, userdata, msg):
        print("Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        client.loop_stop()

    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()
