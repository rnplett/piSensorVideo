import datetime, re, os
from pandas import Series, DataFrame
from flask import Flask
from flask import send_file
from inputs.settings import *
import requests
#from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/cam')
def cam():
    return send_file('data/image.jpg', mimetype='image/gif')

@app.route('/who')
def who():
    return "This is a message to display who."
