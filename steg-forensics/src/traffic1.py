from scapy.all import *
from flask import Flask, render_template, request, make_response
import time
import os
import requests

def client():
	names = ['Bob', 'Will', 'Matt', 'Bearshell', 'Hacker']
	for i in range(4):
		time.sleep(0.1)
		if i % 2 == 0:
			requests.get('http://localhost:8000/')
		else:
			requests.get('http://localhost:8000/index.html')

	for i in range(10):
		time.sleep(0.1)
		if i % 2 == 0:
			requests.get('http://localhost:8000/fake')
		else:
			name = names[i % len(names)]
			requests.get('http://localhost:8000/hello/' + name)

	requests.get('http://localhost:8000/flag')

	for i in range(5):
		requests.get('http://localhost:8000/')
		time.sleep(0.1)

def server():
	app = Flask(__name__)

	@app.route('/')
	@app.route('/index.html')
	def index():
		resp = make_response("<h1>This is the home page</h1>")
		resp.set_cookie("cookie", "value", samesite='Lax')
		return resp

	@app.route('/hello/<name>')
	def hello(name):
		page = f'Hello, {name}. Would you like the flag?'
		return page

	@app.route('/fake')
	def fake_flag():
		return "This is a fake flag"

	@app.route('/flag')
	def flag():
		return "flag: bearshell{wireshark-do-do-dodo-dodo}"

	app.run(host='0.0.0.0', port=8000)


if os.fork() == 0:
	if os.fork() == 0:
		wrpcap("traffic1.pcap", sniff(iface='lo', count=500))
	else:
		server()
else:
	time.sleep(1)
	client()
