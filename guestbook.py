from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return '<h1>Hello there!<h1>'

# Adding in variables into the route name
@app.route('/home/<place>')
def home(place):
	return '<h1> You are on the home' + place + ' page<h1>'

if __name__ == '__main__':
	app.run(host='127.0.0.1',debug=True, port = 5001)