import psycopg2
from dotenv import load_dotenv
import os


dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)
# MQTT


DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DB_PORT = os.getenv("DB_PORT")

MQTT_IP = os.getenv("MQTT_IP")
MQTT_PORT = int(os.getenv("MQTT_PORT"))
TOPIC = os.getenv("TOPIC")
MQTT_TOPIC_PI = os.getenv("MQTT_TOPIC_PI")
PI_TOPIC_RESPONSE = os.getenv("PI_TOPIC_RESPONSE")

MQTT_TOPIC_PREDICT = os.getenv("MQTT_TOPIC_PREDICT")


def connectDB():
    return psycopg2.connect(host=DB_HOST ,port = DB_PORT,database=DB_NAME, user=DB_USER, password=DB_PASSWORD)


# DB_USER = "postgres"
# DB_PASSWORD = "postgres"
# DB_NAME = "postgres"
# DB_PORT = 5433


# MQTT_IP = "localhost"
# MQTT_PORT =1883
# TOPIC ="sensor"
# MQTT_TOPIC_PI = "pi_data"
# PI_TOPIC_RESPONSE = "pi_data_response"
# MQTT_TOPIC_PREDICT = "predict"



# topic ="sensor"
# ip = "localhost"
# ip_mqtt = "localhost"
# port =1883
# pi_topic = "pi_data"
# pi_topic_response = "pi_data_response"
# predict_topic = "predict"