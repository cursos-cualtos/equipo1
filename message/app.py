from flask import Flask, request
from markupsafe import escape
from db_utils import add_message, get_message, get_all_messages, edit_message
from bson.objectid import ObjectId
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

@app.route('/messages/add',methods=['POST','GET'])
def messages_add():
    id_document = add_message(request.json)
    retorna = {"ID":str(id_document)}
    return retorna


if __name__ == "__main__":
    app.run(port=5002)