from flask import Flask
from flas import render_template,request,session

app = Flask(__name__)


userData = [] #lista que va a almacenar
rol = None


@app.route('/')
def index():
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		return render_template('users.html')

@app.route('/login', methods= ['POST'])
def login():
	global userData
	for n in range(len(userData)):
		if request.form['username'] == userData[n][1] and request.form['password'] == userData[n][2]:
			session['logged_in'] = True
			username = request.form['username']
			rol = userData[n][0]
	return index()

##@app.route('/users')


@app.route('/logout')
def logout():
	"""
	Funcion para cerrar sesion
	"""
	session['logged_in'] = False
	rol = None
	return index()