from flask import Flask, render_template, request, session, redirect, url_for
from data import db
from utils import get_all_messages, get_auth, get_message

app = Flask(__name__)
app.secret_key = b'\xc6g\xa9(\x08$W\xbc\xf2\xc7\x1d\x81\x17\xdf\xc5R'

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('messages_all'))

@app.route('/team/listing')
def team_listing():
    return render_template('team_listing.html', team=db)

@app.route('/messages/all')
def messages_all():
    auth_data = get_auth(session['username'])
    if auth_data['status'] == 'authorized':
        messages = get_all_messages()
        return render_template('messages.html', messages=messages)
    elif auth_data['status'] == 'unauthorized':
        return render_template('error.html')
    else:
        return render_template('error.html')

if __name__ == "__main__":
    app.run(port=5000)