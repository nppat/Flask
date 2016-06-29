from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/ninja')
def ninjas():
	return render_template('ninja.html', phrase="ninjas", times= 5)

@app.route('/dojos/new')
def new():
	return render_template('dojos.html')

app.run(debug=True)