import json, requests, datetime
from flask import Flask, request, abort, jsonify
import requests
url = 'http://127.0.0.1:5000/'
# date_time = datetime.datetime.strptime('1/10/2018 21:45:00', '%d/%m/%Y %H:%M:%S').timestamp()
j_data = json.dumps({"url":r'C:\Users\rohit\Documents\Hackathon\Diabetic Retinopathy\Tlevel0\41_left.jpeg'})
r = requests.post(url, data=j_data)

print(r, r.text)
