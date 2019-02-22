from flask import Flask
from flask import request
app = Flask(__name__)

app.run(
    host="0.0.0.0",
    port=5000
)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'
