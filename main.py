import handler
import paho.mqtt.client as mqtt
import config as cfg
import threading
import json

#global variables





print("Starting MQTT client...")


def on_pi_data_connect():
    print("listening to pi data")
    checkclient = mqtt.Client()
    checkclient.on_connect = handler.on_pi_data_connect
    checkclient.on_message = handler.on_pi_data_handler
    checkclient.connect(cfg.MQTT_IP, cfg.MQTT_PORT, 60)
    checkclient.loop_forever()



def sensor_data_connect():
    sensorClient = mqtt.Client()
    print("listening to sensor data")
    sensorClient.on_connect = handler.on_sensor_connect
    sensorClient.on_message = handler.on_sensor_message
    sensorClient.connect(cfg.MQTT_IP, cfg.MQTT_PORT, 60)
    sensorClient.loop_forever()

def predict_data_connect():
    predictClient = mqtt.Client()
    print("listening to predict data")
    predictClient.on_connect = handler.on_predict_connect
    predictClient.on_message = handler.on_predict_message
    predictClient.connect(cfg.MQTT_IP, cfg.MQTT_PORT, 60)
    predictClient.loop_forever()

th1 = threading.Thread(target=on_pi_data_connect)
th1.start()

th2 = threading.Thread(target=sensor_data_connect)
th2.start()

th3 = threading.Thread(target=predict_data_connect)
th3.start()


