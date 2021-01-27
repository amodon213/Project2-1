import os
import signal
from flask import Flask
from db_connector import *
app = Flask(__name__)


# supported methods
@app.route('/users/get_user_data/<user_id>')
def user(user_id):
    try:
        name = get_user_id(user_id)
        return "<H1 id='user'>" + name + "</H1>", 200
    except:
        return "<H1 id='error'>""no such user: " + user_id + "</H1>", 500

@app.route('/stop_server')
def stop_server():
    try:
        os.kill(os.getpid(), signal.SIGINT)
        return 'Server stopped', 200

    except:
        return {'status': 'error', 'reason': "didn't manage to close rest app'"}, 500


app.run(host='127.0.0.1', debug=True, port=5001)
