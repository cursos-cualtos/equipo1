from flask import Flask
from markupsafe import escape
import json

mensajes = [
    {
        'message': 'hello',
        'status': 'OK',
        'user': 'admin'
    },
    {
        'message': 'Who is it?',
        'status': 'NOT OK',
        'user': 'user1'
    },
    {
        'message': 'Hi!',
        'status': 'OK',
        'user': 'user2'
    },
    {
        'message': 'Ein Fremder',
        'status': 'NOT OK',
        'user': 'user3'
    }
]

app = Flask(__name__)

@app.route('/messages')
def messages():
    return json.dumps(mensajes)

@app.route('/messages/<int:id>')
def messages_id(id):
    return json.dumps(mensajes[id])


if __name__ == "__main__":
    app.run(port=5001)