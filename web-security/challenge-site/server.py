from flask import Flask, render_template, request
import sys
import os

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def index(): #has flag1, flag2
	return render_template('index.html')


@app.route('/robots.txt')
def robots(): #flag3
	return render_template('flag3.txt') 

@app.route('/flag4.txt')
def flag4(): #flag4
	return render_template('flag4.txt')

@app.route("/login", methods=['GET'])
def login(): #flag 5
	user = request.args.get('user')
	passw = request.args.get('pass')
	if user == "admin" and passw == "supersecretpassword":
		return render_template('flag5.txt')
	return "Failed Login"

@app.route('/flag6.txt')
def flag6(): #flag6
	if 'secure' in request.cookies:
		if request.cookies.get('secure') == 'not a robot':
			return render_template('flag6.txt')
		return "Incorrect cookie value"
	return "Cookie not found"	


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=int(sys.argv[1]))