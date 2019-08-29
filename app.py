# encoding: utf-8

import datetime
import errno
import os
import requests

from flask import Flask, request, abort

app = Flask('Line')

url = 'https://notify-api.line.me/api/notify'
token = 'WtqN6srzyc7SyGNSLDhlTlUJqrAhDiUfUYaUnJQ6CrW'
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}

msg = 'Meraki LINE Notify'
r = requests.post(url, headers=headers, data = {'message':msg})

@app.route("/", methods=['POST'])
def hello():
    msg = 'Meraki LINE Notify'
    r = requests.post(url, headers=headers, data = {'message':msg})
    return 'Hello World'  #ส่วนที่ต้องการแสดงผลออกไป

if __name__ == "__main__":
  app.run(host='0.0.0.0',port=os.environ['PORT'])

