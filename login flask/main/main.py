from flask import Flask
from flask import render_template,request,session
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

userData = [] #lista que va a almacenar
rol = None

user = open('datos_estudiantes.txt')
for data in user: #este ciclo toma todos los datos de los estudiantes y los guarda en la variable userData
	data = data.replace('/n','')
	userData.append(data.split(','))
user.close()

@app.route('/')
def index():
	"""
	"""
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		return render_template('users.html')

@app.route('/login', methods= ['POST'])
def login():
	"""
	"""
	global userData
	for n in range(len(userData)):
		if request.form['username'] == userData[n][1] and request.form['password'] == userData[n][2]:
			session['logged_in'] = True
			username = request.form['username']
			rol = userData[n][0]
	return index()

@app.route('/users')
def users(rol,username):
	if rol == 'admin':
		return render_template('admin.html')
	else:
		if rol == 'estudiante':
			profileData = []
			prof = open('perfildelestudiante.txt')
			for linea in prof:
				linea = linea.replace('/n', '')
				profileData.append(linea.split(','))
			prof.close()

			for n in range(len(profileData)):
				if profileData[n][1] == username:
					grado = profileData[n][2]
					puntos = profileData[n][3]
					vidas = profileData[n][4]
			return render_template('estudiantes.html', rol=rol,username=username,grado=grado,puntaje=puntaje,vidas=vidas)
	pass


@app.route('/admin')
def admin():
	"""
	Esta funcion define lo que el administrador puede 
	"""


@app.route('/logout')
def logout():
	"""
	Funcion para cerrar sesion
	"""
	session['logged_in'] = False
	rol = None
	return index()