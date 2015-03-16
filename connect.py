#!/usr/bin/python
import urllib2
import datetime
import json
import time
import threading
from threading import Thread
from pymongo import MongoClient
client = MongoClient()
db = client.opengraph
historic = db.historic
while True:
  response = urllib2.urlopen('https://graph.facebook.com/NoticiasMVS')
  response_json = json.loads(response.read())
  response_json['ts'] = int(time.time())
  historic.insert(response_json)
  time.sleep(1)

