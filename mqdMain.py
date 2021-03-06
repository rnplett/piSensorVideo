from flask import Flask
from flask import send_file
import os

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/cam')
def cam():
    os.system("fswebcam image.jpg")
    return send_file('data/image.jpg', mimetype='image/gif')

@app.route('/campi')
def campi():
    os.system("python camera.py")
    return send_file('data/image.jpg', mimetype='image/gif')

@app.route('/qr')
def qr():
    #cam()
    campi()
    return send_file('data/image.jpg', mimetype='image/gif')

@app.route('/who')
def who():
    return "This is a message to display who."
