# encoding: utf-8

import datetime
import errno
import os
import requests
import json

from flask import Flask, request, abort

app = Flask('Line')

url = 'https://notify-api.line.me/api/notify'
token = 'WtqN6srzyc7SyGNSLDhlTlUJqrAhDiUfUYaUnJQ6CrW'
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}


@app.route("/")
def Notify():
    msg = 'Meraki LINE Notify No Post'
    r = requests.post(url, headers=headers, data = {'message':msg})
    return ("Complete")

@app.route("/", methods=['POST'])
def NotifyPost():
    msg = 'Meraki LINE Notify with POST\n'   
    print('P Start =====')
    print(request.form)
    print('P Stop =====')
    r = requests.post(url, headers=headers, data = {'message':msg})
    return(msg)
    
if __name__ == "__main__":
  app.run(host='0.0.0.0',port=os.environ['PORT'])

