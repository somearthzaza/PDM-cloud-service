
import json
import config as cfg
import time
import datetime
con = cfg.connectDB()

def on_sensor_connect(client, userdata, flags, rc , topic = cfg.TOPIC ):
    print("Connected with result code "+str(rc) + " to topic " + topic)
    client.subscribe(topic)

def on_sensor_message(client, userdata, msg ):
    import json
    print(msg.topic+" "+str(msg.payload))
    tag = json.loads(msg.payload)['tag']
    g = json.loads(msg.payload)['g']
    description = json.loads(msg.payload)['description']
    sensor_name = json.loads(msg.payload)['sensor_name']
    timestamp = json.loads(msg.payload)['timestamp']
    m_id = json.loads(msg.payload)['m_id']
    tag = json.loads(msg.payload)['tag']
    data = {
        'x': json.loads(msg.payload)['x'],
        'y': json.loads(msg.payload)['y'],
        'z': json.loads(msg.payload)['z'],
    }


    valdata = json.dumps(data)
    cur = con.cursor()
 
    cur.execute('SELECT * FROM public."Slave_boards" WHERE s_id = %s', (tag,))
    data = cur.fetchone()
    if data is None:
        cur.execute('INSERT INTO public."Slave_boards" (s_id,m_id, s_name, last_update) VALUES (%s, %s, %s, %s)', (tag,m_id, sensor_name, datetime.datetime.now()))
        con.commit()
    
    cur.execute('INSERT INTO public."Slave_sensor_vals" (vals, last_update , s_id) VALUES ( %s, %s, %s)', (valdata, timestamp,tag))
    # cur.execute('INSERT INTO public."sensor_data" (val, sensor_name, g, timestamp, motor_describe) VALUES ( %s, %s, %s ,%s,%s)', ( data, sensor_name,g, timestamp,description))
    con.commit()
    cur.close()


def on_pi_data_connect(client, userdata, flags, rc , topic = cfg.MQTT_TOPIC_PI):
    print("Connected with result code "+str(rc) + " to topic " + topic)
    client.subscribe(topic)



def on_pi_data_handler(client, userdata, msg):
    global con
    global json
    global transection_id
    print(msg.topic+" "+str(msg.payload))
    pi_id = json.loads(msg.payload)['pi_id']
    pi_name = json.loads(msg.payload)['pi_name']
    factory = json.loads(msg.payload)['factory']
    transection_id = json.loads(msg.payload)['transection_id']
    
    cur = con.cursor()
    cur.execute('SELECT * FROM public."Master_boards" WHERE m_id = %s AND m_name = %s AND fac_id = %s ', (pi_id,pi_name,factory))
    data = cur.fetchone()

    if data is None:
        cur.execute('INSERT INTO public."Master_boards" (m_id, m_name, fac_id , last_update) VALUES ( %s, %s, %s)', (pi_id,pi_name,factory , datetime.datetime.now()))
        conn.commit()
        jsondata = {
            'status': 'success',
            'transection_id': transection_id,
            'message': f'Pi with id {pi_id} and name {pi_name} and factory {factory} added successfully',
            'allowed': 'true'
        }
    else:
        jsondata = {
            'status': 'success',
            'transection_id': transection_id,
            'message': f'Pi with id {pi_id} and name {pi_name} and factory {factory} already exists',
            'allowed': 'true'
        }

    jsondata = json.dumps(jsondata)
    client.publish(cfg.PI_TOPIC_RESPONSE, jsondata)
    cur.close()



def on_predict_connect(client, userdata, flags, rc , topic = cfg.MQTT_TOPIC_PREDICT):
    print("Connected with result code "+str(rc) + " to topic " + topic)
    client.subscribe(topic)

def on_predict_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    tag = json.loads(msg.payload)['tag']
    predictValue = json.loads(msg.payload)['predictValue']
    timestamp = json.loads(msg.payload)['timestamp']
    
    cur = con.cursor()
    cur.execute('SELECT * FROM public."Slave_boards" WHERE s_id = %s', (tag,))
    data = cur.fetchone()
    if data is None:
        cur.execute('INSERT INTO public."Slave_boards" (s_id,m_id, s_name, last_update) VALUES (%s, %s, %s, %s)', (tag,m_id, sensor_name, timestamp))
        con.commit()
    
    cur.execute('INSERT INTO public."Slave_predict" (s_id, predict_value,timestamp) VALUES ( %s, %s, %s)', (tag, predictValue,timestamp))
    con.commit()

    cur.close()
    



        
