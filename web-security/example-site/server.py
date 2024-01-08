from flask import Flask, render_template
import sys
import os

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=int(sys.argv[1]))