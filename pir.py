#!/usr/bin/python

import Adafruit_DHT
import time
import requests, json
import RPi.GPIO as GPIO
from influxdb import InfluxDBClient as influxdb
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)

def interrupt_fired(channel):
    a = 5
    data = [{
        'measurement':'pir',
        'tags':{
            'visionUV':'2410', 
        },
        'fields':{
            'pir':a,
        }
    }]
    client=None
    try:
        client = influxdb('localhost',8086,'root','root','pir')
    except Exception as e:
        print "Exception" + str(e)
    if client is not None:
        try:
            client.write_points(data)
        except Exception as e:
            print "Exception write " + str(e)
        finally:
            client.close()
    print("interrupt Fired") 
    print(a)


GPIO.add_event_detect(4, GPIO.FALLING, callback=interrupt_fired)

while True:
    time.sleep(1)
    a = 1
    data = [{
        'measurement':'pir',
        'tags':{
            'visionUV':'2410',
         },
        'fields':{
            'pir':a,
         }
    }]
    client=None
    try:
        client = influxdb('localhost',8086,'root','root','pir')
    except Exception as e:
        print "Exception" + str(e)
    if client is not None:
        try:
            client.write_points(data)
        except Exception as e:
            print "Exception write "+str(e)
        finally:
            client.close()
    print("runnig influxdb OK")
