from flask import Flask
app = Flask(__name__)

@app4.route('/')
def hell_world():
	return 'Hello Sammy!'

