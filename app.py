from flask import Flask
import json

app = Flask(__name__)

@app.route('/')
def index():
    message = {'message': 'Bienvenido'}
    return json.dumps(message)

@app.route('/greeting')
def greeting():
    message = {'message': 'Hola usuario'}
    return json.dumps(message)

@app.route('/greeting/<name>')
def greeting_by_name(name):
    message = {'message': 'Hola '+name}
    return json.dumps(message)

if __name__ == "__main__":
    app.run(port=5002)