import sys

sys.path.append('/home/oshara/Documents/fyp_streaming')

from flask import Flask, request
import json
from fyp_flask_server.dto import access_layer as acl

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/info', methods=['POST', 'GET'])
def func():
    if request.method == 'POST':
        json_data = json.loads(request.data)
        return acl.get_ransomware_info(json_data)
