# encoding: utf-8

import datetime
import errno
import os
import requests
import json

from flask import Flask, request, abort

app = Flask('Line')

url = 'https://notify-api.line.me/api/notify'
token = 'FdsZX6K2Kg6tinYVtgG872eLAs3vSPW5ZH7klySWWx7'
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}


@app.route("/")
def Notify():
    msg = 'Meraki LINE Notify No Post'
    r = requests.post(url, headers=headers, data = {'message':msg})
    return ("Complete")

@app.route("/", methods=['POST'])
def NotifyPost():
    msg = 'Meraki LINE Notify with POST\n'   
    msg = msg + str(request.form)
    
    print('P Start =====')
    print(msg)
    print('P Stop =====')
    
    r = requests.post(url, headers=headers, data = {'message':msg})
    return('')
    
if __name__ == "__main__":
  app.run(host='0.0.0.0',port=os.environ['PORT'])

