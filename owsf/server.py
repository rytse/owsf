from flask import Flask, flash, redirect, render_template, request, session, abort
 
app = Flask(__name__)
 
@app.route("/")
def home():
	return render_template('home.html')

@app.route("/map")
def map():
	return render_template('webmap-basic.html')
 
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80)

