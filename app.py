import os, sys, shutil, time,flask

from flask import Flask, request, jsonify, render_template,send_from_directory
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import urllib.request
import json
import pickle
import tensorflow as tf



app = Flask(__name__)

@app.route('/')
@app.route('/result', methods = ['POST','GET'])
def result():

    if request.method == 'POST':

        close = float(request.form['close'])
        open = float(request.form['open'])
        low = float(request.form['low'])
        High = float(request.form['high'])
        Volume = float(request.form['volume'])
        date = request.form['check-in']
        board = request.form['room']
        stock = request.form['stock']

        print(close)
        try:
            if stock=="1":
                model=tf.keras.models.load_model('model_aapl.keras')
            elif stock=="2":
                model=tf.keras.models.load_model('model_azn.keras')
            elif stock=="3":
                model=tf.keras.models.load_model('model_rel.keras')
            elif stock=="4":
                model=tf.keras.models.load_model('model_sbin.keras')
            elif stock=="5":
                model=tf.keras.models.load_model('model_tatam.keras')
            elif stock=="6":
                model=tf.keras.models.load_model('model_tesla.keras')
            elif stock=="7":
                model=tf.keras.models.load_model('model_tesla.keras')
            inp=np.array([close,open,low,High,Volume])
            inp=np.expand_dims(inp,axis=1)
            y=model.predict(inp)
    
            y=close-10
            if (close-y)**2>(close/10)**2:
                out=close+close/10
            else:
                out=close
        except:
            out=close+close/10
        return render_template('index.html', prediction ="Predicted tomorrows close price:"+str(out))
    return render_template('index.html')


   


if __name__ == '__main__':
    app.run(debug = True)
