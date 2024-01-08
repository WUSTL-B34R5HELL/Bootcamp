from flask import Flask, render_template, request
import sys
import os

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def index():
	return render_template('index.html')


@app.route('/robots.txt')
def robots():
	return render_template('flag3.txt') 

@app.route('/flag4.txt')
def flag4():
	return render_template('flag4.txt')

@app.route("/login", methods=['GET'])
def login():
	user = request.args.get('user')
	passw = request.args.get('pass')
	if user == "admin" and passw == "supersecretpassword":
		return render_template('flag5.txt')
	return "Failed Login"

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=int(sys.argv[1]))