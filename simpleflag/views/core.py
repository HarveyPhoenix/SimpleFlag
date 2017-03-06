#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
from flask import abort

app = Flask(__name__)

def permission_required(permission):
	def check_token(func):
        # @wraps(func)
		def decorated_function(*args, **kwargs):
			if request.form['token']:
                abort(400)
                req_token = request.form['token']
				if req_token == "123456":
					return func(*args, **kwargs)
			abort(403)
		return decorated_function
	return check_token


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/login', methods=['POST', 'GET'])
@permission_required(None)
def login():
	error = None
	if request.method == 'POST':
		msg = 'OK'
        ret_code = 201
	# the code below is executed if the request method
	# was GET or the credentials were invalid
	return (msg, ret_code)

if __name__ == '__main__':
    app.run()
