from flask import Flask
app = Flask(__name__)
a = 'sina'
@app.route('/')
def hello_world():
    return 'Hello, World!'
