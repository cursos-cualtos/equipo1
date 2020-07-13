from flask import Flask
from markupsafe import escape
import json

validUsers = ('Diego', 'Migue', 'Antonio', 'Alan', 'Ricardo')

app = Flask(__name__)

@app.route('/auth/<string:userName>')
def auth(userName):
  if userName in validUsers:
    return json.dumps({'status': 'authorized'})
  else:
    return json.dumps({'status': 'unauthorized'})

if __name__ == "__main__":
    app.run(port=5001)