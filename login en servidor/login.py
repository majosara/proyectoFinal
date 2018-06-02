from flask import Flask
from flask import render_template, request, session
import os

app = Flask(__name__)

app.secret_key = os.urandom(32)
#aqui va algo que no entiendo jeje :D

userData = [] #esta lista contendra los datos de los usuarios
#este ciclo va a agregar a la variable userData los datos dentro del archivo
#de texto que contiene los datos de los usuarios
datos = open('datos_estudiantes.txt')
for user in datos:
	user = user.replace('\n','')
	userData.append(user.split(,))
datos.close()

@app.route('/')
def index(rol=None,username=None):
	"""
	Esta funcion lleva al usuario que no ha iniciado sesion a la
	pagina del login y si ha iniciado sesion lo llevara a la funcion
	de usuarios.
	"""
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		return users(rol,username)

@app.route('/admin',methods=['POST'])
def admin(rol=None,username=None):
	"""
	Esta funcion verifica el rol del usuario que inicio sesion, en caso
	que este rol sea administrador, se llama esta funcion.
	"""
	if session.get('logged_in'): #se abren las bases de datos de los usuarios
		perfil = open('perfiles.txt','a') #se usa la opcion a porque el admin podra ingresar usuarios
		#a este archivo.
		file = open('datos_estudiantes.txt','a') #tambien se va a modificar este archivo ya que
		#contiene datos de los usuarios del juego

		datosUsuarios = [] #esta lista tendra los datos de los usuarios
		datosEstudiantes = open('datos_estudiantes.txt','r')

		for dato in datosEstudiantes:
			dato = dato.replace('\n','')
			datosUsuarios.append(dato.split(','))
		datosEstudiantes.close()
		datosUsuarios.pop(0)

		id_usuario = len(datosUsuarios)-1

		for i in range(len(datosUsuarios)):
			if request.form['userRegister'] != datosUsuarios[i][1]:
				agregarUsuarios = request.form['rolRegistrer'] + ',' + request.form['userRegister'] + ',' + request.form['contrasenaRegister'] + ',' + str(id_usuario) + ',' + request.form['correoRegister'] + ',' + request.form['edadRegister'] + ',' + request.form['gradoRegister']
				agregarPerfil = str(id_usuario) + ',' + request.form['userRegister'] + ',' + request.form['gradoRegister'] + ',' + str(0) + ',' + str(5)
				perfil.write(agregarPerfil + '\n')
				file.write(agregarUsuarios + '\n')
				file.close()
				perfil.close()
				return render_template('administrador.html',rol=rol,username=username)
			else:
				file.close()
				perfil.close()
				return index()
		else:
			return index()

@app.route('login', methods=['POST'])
def login(rol=None,username=):
	"""
	Esta funcion hace la validacion del inicio de sesion de los usuarios.
	Ademas el ciclo que se efectua, valida si el usuario y la contrasena que se
	reciben en el input estan en la base de datos.
	"""
	global userData

	for i in range(len(userData)):
		""" si los datos que se ingresaron en el formulario estan en las bases de datos
		entonces el sistema deja que inicie sesion y se toma la informacion(usuario y contrasena)"""
		if request.form['username'] == userData[i][1] and request.form['password'] == userData[i][2]:
			session['logged_in'] = True
			rol = userData[i][0]
			username = request.form['username']
		#en caso de que se encuentre o no un usuario valido va a enviarlo a 'index'
		if rol != None and username != None:
			return index(rol,username)
		else:
			return index(rol,username)

#ruta para los usuarios que tienen estudiante como rol
@app.route('/users')
def users(rol=None,username=None):
	"""
	Esta funcion comprueba el rol del usuario y lo lleva a su respectiva ruta.
	En caso de encontrar que el rol es estudiante, define unas variables con sus 
	datos, que estan almacenados en una variable que abre  archivo de texto que 
	contiene los datos de los usuarios
	"""
	if rol == 'administrador':
		return render_template('administrador.html',rol = rol,username = username)
	else:
		if rol == 'estudiante':
			perfilData = []
			file = open('perfiles.txt')
			for linea in file:
				linea = linea.replace('\n','')
				perfilData.append(linea.split(','))
			file.close()

			for i in range(len(perfilData)):
				if perfilData[i][1] == username:
					grado = perfilData[i][2]
					puntaje = perfilData[i][3]
					vidas = perfilData[i][4]
					infoUser = perfilData[i]
			return render_template('estudiante.html',rol=rol,username=username,grado=grado,puntaje=puntaje,vidas=vidas,infoUser=infoUser)

@app.route('/logout')
def logout():
	"""
	Esta funcion cierra la sesion del usuario que este en ese momento en sesion
	"""
	app.secret_key = os.urandom(32)
	session['logged_in'] = False
	rol = None
	username = None
	return index(rol,username)

if __name__  == '__main__':
	app.run(debug=True)