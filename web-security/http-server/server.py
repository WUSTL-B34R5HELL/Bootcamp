from flask import Flask, request
import sys

app = Flask(__name__)

@app.route('/flag1', methods=['GET'])
def get():
	return "bearshell-flag-1{first-flag}\n"

@app.route('/flag2', methods=['POST'])
def post():
	return "bearshell-flag-2{second-flag}\n"

@app.route('/flag3', methods=['GET'])
def query():
	passw = request.args.get('password')
	extra = request.args.get('extra')

	if passw is None or extra is None:
		return "Missing query parameter\n", 400
	
	if passw == "12345" and extra == "bearshell":
		return "bearshell-flag-3{third-flag}\n"
	return "Incorrect value in query parameter\n"

@app.route('/flag4', methods=['POST'])
def json():

	data = request.get_json()
	if not data:
		return "No Data in the request body\n", 400

	try:
		passw = data['password']
	except KeyError as err:
		return "Must provide password\n", 400

	if passw == "json-data":
		return "bearshell-flag-4{fourth-flag}\n"
	return "Incorrect Password\n"
	
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=int(sys.argv[1]))