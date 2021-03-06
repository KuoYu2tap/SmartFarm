# import paho.mqtt.client as mqtt
# import time
#
# HOST = "127.0.0.1"
# PORT = 1883
#
# def client_loop():
#     client_id = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
#     client = mqtt.Client(client_id)    # ClientId不能重复，所以使用当前时间
#     client.username_pw_set("admin", "123456")  # 必须设置，否则会返回「Connected with result code 4」
#     client.on_connect = on_connect
#     client.on_message = on_message
#     client.connect(HOST, PORT, 60)
#     client.loop_forever()
#
# def on_connect(client, userdata, flags, rc):
#     print("Connected with result code "+str(rc))
#     client.subscribe("test")
#
# def on_message(client, userdata, msg):
#     print(msg.topic+" "+msg.payload.decode("utf-8"))
#
# if __name__ == '__main__':
#     client_loop()

import json

import paho.mqtt.client as MQTT


#
def on_connect(client, rc):
    print('Connected with result code ' + str(rc))
    client.subscribe([("index/field", 0), ("index/record", 2), ("detail/field", 3)])


def on_message(client, msg):
    print(msg.topic + ' ' + str(msg.payload))
    print(json.loads(msg.payload))


if __name__ == '__main__':
    client = MQTT.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    try:
        client.connect_async('127.0.0.1', port=1883)
        client.loop_forever()
    except KeyboardInterrupt:
        client.disconnect()
