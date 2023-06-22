# https://learning-0mq-with-pyzmq.readthedocs.io/en/latest/pyzmq/patterns/pushpull.html

import zmq
import time
import random

#  socket to join queue
context = zmq.Context()
socket = context.socket(zmq.PUSH)
socket.bind('tcp://*:5557')

# Event
sensor_data = {
    'type': 'Color of Traffic Light',
    'value': '',
    'eventId': 0
}

while True:
    # new sensor data
    time.sleep(3)
    if sensor_data['value'] == '' or sensor_data['value'] == 'YELLOW_UP':
        sensor_data['value'] = 'RED'
    elif sensor_data['value'] == 'RED':
        sensor_data['value'] = 'YELLOW_DOWN'
    elif sensor_data['value'] == 'YELLOW_DOWN':
        sensor_data['value'] = 'GREEN'
    elif sensor_data['value'] == 'GREEN':
        sensor_data['value'] = 'YELLOW_UP'

    # push event
    print('Control Unit pushing event',
          sensor_data['eventId'], ':', sensor_data['type'], '=', sensor_data['value'])
    socket.send_json(sensor_data)

    # upate event id
    sensor_data['eventId'] = sensor_data['eventId'] + 1
