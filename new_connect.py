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

def getNoticiasMVS():
  response = urllib2.urlopen('https://graph.facebook.com/NoticiasMVS')
  return json.loads(response.read())

def getAristeguiOnline():
  response = urllib2.urlopen('https://graph.facebook.com/AristeguiOnline')
  return json.loads(response.read())
if __name__ == '__main__':

while True:

  response_json['ts'] = int(time.time())
  historic.insert(response_json)
  time.sleep(1)

