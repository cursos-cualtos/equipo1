import requests

base_url = 'http://localhost:'
auth_url = base_url + '5001/auth'
messages_url = base_url + '5002/messages'

def get_all_messages():
    r = requests.get(messages_url)
    return r.json()

def get_message(id):
    r = requests.get(messages_url + '/' + id)
    return r.json()

def get_auth(username):
    r = requests.get(auth_url + '/' + username)
    return r.json()