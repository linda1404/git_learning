from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def homepage():
	return render_template('homepage.html')


@app.route('/add_question')
def add_question():
	return render_template('add_question.html')

@app.route('/process', methods = ['POST'])
def process():
	question= request.form['question'] 

	return render_template('homepage.html', question = question)



if __name__ == '__main__':
	app.run(host='127.0.0.1',debug=True, port = 5001)