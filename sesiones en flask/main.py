from flask import Flask
from flask import render_template,request,session
import os

app = Flask(__name__)
app.secret_key = os.urandom(32) # no me acuerdo para que es esto

userData = [] #lista que va a almacenar todos los datos de los estudiantes
#que hay en las tablas
rol = None #variable para el rol de la persona que ingrese al juego

user = open('datos_estudiantes.txt')
for data in user: #este ciclo toma todos los datos de los estudiantes y 
#los guarda en la variable userData
	data = data.replace('/n','')
	userData.append(data.split(','))
user.close()

@app.route('/')
def index():
	"""
	Es el inicio del login, si no ha iniciado sesion, lo envia al formulario
	"""
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		return render_template('users.html')

@app.route('/login', methods= ['POST'])
def login(rol=None,username=None):
	"""
	Inicio de sesion de los usuarios, la funcion recibe el rol y el username
	que en este caso son parametros vacios y comprueba ambos datos
	para saber a donde direccionarlos dentro del juego
	"""
	global userData
	for n in range(len(userData)): #
		if request.form['username'] == userData[n][1] and request.form['password'] == userData[n][2]:
			session['logged_in'] = True
			username = request.form['username']
			rol = userData[n][0]
			username = request.form['username']
	if rol != None and username != None:
		return index(rol,username)
	else:
		return index(rol,username)

@app.route('/users')
def users(rol,username):
	"""
	Esta funcion identifica el rol del usuario, si es administrador o estudiante y dirige a cada uno a donde le corresponda
	"""
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


@app.route('/admin')
def admin(rol=None,username=None):
	"""
	Esta funcion define lo que el administrador puede realizar
	"""
	if session.get('logged_in') and rol == admin:
		users = open('datos_estudiantes.txt','a')

		usersData = [] #no se para que se usa
		datosEstudiantes = open('datos_estudiantes.txt','r')

		for linea in datosEstudiantes:
			linea = lina.replace('\n','')
			usersData.append(linea.split(','))
		datosEstudiantes.close()

		id_estudiante = len(usersData) - 1
		for n in range(len(usersData)):
			if request.form['userRegister'] != usersData[n][1]:
				agregar = request.form['rolRegister'] + ',' + request.form['userRegister']  + ',' + request.form['passwordRegister'] + ',' + str(id_estudiante) + ',' + request.form['correoRegister'] + ',' + request.form['ageRegister'] + ',' + request.form['gradeRegister']
				file.write(agregar + '\n')
				file.close
				return render_template('admin.html',rol=rol,username=username)
			else:
				return render_template('admin.html',rol=rol,username=username)
		else:
			index()

@app.route('/logout')
def logout():
	"""
	Funcion para cerrar sesion
	"""
	session['logged_in'] = False
	rol = None
	return index()