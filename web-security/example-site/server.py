from flask import Flask, render_template, request, make_response
import sys
import os

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def index():
	resp = make_response(render_template('index.html'))
	resp.set_cookie("test-cookie", "This is a cookie set by the server", samesite='Lax')
	return resp

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=int(sys.argv[1]))