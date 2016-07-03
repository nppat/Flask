from flask import Flask, render_template
app = Flask(__name__)

# set up root route
@app.route('/')
def index():
	return render_template("index.html")

# /ninja route and function
@app.route('/ninja/')
def ninja():
	return render_template("ninja.html", show='all')

#set /ninja/<color> route and function
@app.route('/ninja/<color>/') #<color> sets the specific route to the color chosen
def color(color): #passes color argument to the funciton
	return render_template('ninja.html', show=color) #which ever color is chosen will be passed up to the route

app.run(debug=True) #run server