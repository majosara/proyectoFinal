from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os

app = Flask(__name__)

@app.route('/')
def home():
	if not session.get('logged_in'):
		return render_template('examplelogin.html')
	else:
		return admin()

@app.route('/login', methods=['POST'])
def do_admin_login():
	if request.form['password']=='admin1234' and request.form['username']=='admin':
		session['logged_in'] = True
	else:
		flash('wrong password or username')
	return home()

@app.route('/admin')
def admin():
	return render_template('menuadmin.html')

if __name__=="__main__":
	app.secret_key = os.urandom(12)
	app.run(debug=True)
