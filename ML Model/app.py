from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pickle as p
import json
from fastai.imports import *
from fastai import *
from fastai.vision import *
from fastai.metrics import error_rate


app = Flask(__name__)
# app = Flask(__name__) = pickle.load(open('model.pkl','rb'))


@app.route('/', methods = ['POST'])
def make_predict():
    #return jsonify(request.get_json())
    data = request.get_json(force=True)
    #return '123'
    #predict_request = [data['dept_date_time'],data['origin'],data['destination']]
    #predict_request = np.array(predict_request)
    #delay_predicted = model.predict(predict_request)
    output = predict_dr(data['url'])
    #return '123'
    return jsonify(output)

def predict_dr(url):
    img = open_image(url)
    pred_class, pred_idx, outputs = model.predict(img)
    return str(pred_class).capitalize()

if __name__ == '__main__':
    modelfile = 'DiabeticRetinopathy.pth'
    modelfile = 'model.pkl'
    model = p.load(open(modelfile, 'rb'))
    app.run(debug=True, port=3000)
