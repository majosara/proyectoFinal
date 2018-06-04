from flask import Flask
from flask import render_template,request,session
import os

app = Flask(__name__)

app.secret_key = os.urandom(32)

userData = [] #lista que contendra las bases de datos de los usuarios y servira para
#validar la informacion de los usuarios
infoUser = []
gradoPreguntas = []

#en el siguiente ciclo se agregara a userData la informacion de los usuarios
#en las bases de datos
lista = open('datos_usuarios.txt')
for user in lista:
	user = user.replace('\n','')
	userData.append(user.split(','))
lista.close()

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
		return users(rol,username) #si inicio sesion se envia a users

#registro de usuarios
@app.route('/admin',methods=['POST'])
def admin(rol=None,username=None):
	"""
	Esta funcion verifica el rol del usuario que inicio sesion, en caso
	que este rol sea administrador, se llama esta funcion.
	"""
	if session.get('logged_in'): #se abren las bases de datos de los usuarios
		perfil = open('perfiles.txt','a') #se usa la opcion a porque el admin 
		#podra ingresar usuarios a este archivo
		file = open('datos_usuarios.txt','a') #tambien se va a modificar este archivo ya que
		#contiene datos de los usuarios del juego

		usersData = [] #esta lista tendra los datos de los usuarios
		datosEstudiante = open('datos_usuarios.txt','r')

		for linea in datosEstudiante:
			linea = linea.replace('\n','')
			usersData.append(linea.split(','))
		datosEstudiante.close()

		id_usuario = len(usersData) - 1

		for i in range(len(usersData)):
			if request.form['userRegister'] != userData[i][1]:
				agregarUsers = request.form['rolRegister'] + ',' + request.form['userRegister'] + ',' + request.form['contraseñaRegister'] + ',' + str(id_usuario) + ',' + request.form['correoRegister'] + ',' + request.form['edadRegister'] + ',' + request.form['gradoRegister']
				agregarPerfil = str(id_usuario) + ',' + request.form['userRegister'] + ',' + request.form['gradoRegister'] + ',' + str(0) + ',' + str(0) + ',' + str(0) + ',' + str(0) + ',' + str(5)
				perfil.write(agregarPerfil + '\n')
				file.write(agregarUsers + '\n')
				file.close()
				perfil.close()
				return render_template('administrador.html',rol=rol,username=username)
			else:
				file.close()
				perfil.close()
				return index()
		else:
			return index()

#inicio de sesion de usuarios
@app.route('/login',methods=['POST'])
def login(rol=None,username=None):
	"""
	Esta funcion hace la validacion del inicio de sesion de los usuarios.
	Ademas el ciclo que se efectua, valida si el usuario y la contrasena que se
	reciben en el input estan en la base de datos.
	"""
	global userData

	for i in range(len(userData)):
		""" si los datos que se ingresaron en el formulario estan en las bases de datos
		entonces el sistema deja que inicie sesion y se toma la informacion(usuario y contrasena)"""
		if request.form['username']==userData[i][1] and request.form['password']==userData[i][2]:
			session['logged_in'] = True
			rol = userData[i][0]
			username = request.form['username']
	#en caso de que se encuentre o no un usuario valido va a enviarlo a 'index'
	if rol != None and username != None:
		return index(rol,username)
	else:
		return index(rol,username)

#ruta para los estudiantes que tiene estudiante como rol
@app.route('/users/<rol>/<username>/<infoUsuario>')
def users(rol=None,username=None,infoUsuario=None):
	"""
	Esta funcion comprueba el rol del usuario y lo lleva a su respectiva ruta.
	En caso de encontrar que el rol es estudiante, define unas variables con sus 
	datos, que estan almacenados en una variable que abre  archivo de texto que 
	contiene los datos de los usuarios
	"""
	global infoUser,gradoPreguntas
	if rol == 'Administrador':
		return render_template('administrador.html',rol=rol,username=username)
	else:
		if rol == 'Estudiante':
			gradoPreguntas = []
			perfilData = []
			archivo = open('perfiles.txt')
			for linea in archivo:
				linea = linea.replace('\n','')
				perfilData.append(linea.split(','))
			archivo.close()
			perfilData.pop(0)

			if infoUsuario != None:
				infoUsuario = " ".join(infoUsuario)
				infoUsuario = str(infoUsuario)
				infoUsuario = infoUsuario.replace(" ","")
				infoUsuario = infoUsuario.replace(",","")
				#infoUsuario = infoUsuario.replace(",",'","')
				#infoUsuario = infoUsuario.replace('"',"'")
				infoUsuario = list(infoUsuario)
				for n in range(len(infoUsuario)):
					idUser = infoUsuario[0]
					grado = infoUsuario[-6]
					puntajeMatematicas = infoUsuario[-5]
					puntajeEspañol = infoUsuario[-4]
					puntajeNaturales = infoUsuario[-3]
					puntajeSociales = infoUsuario[-2]
					vidas = infoUsuario[-1]
					infoUser = [idUser,username,grado,puntajeMatematicas,puntajeEspañol,puntajeNaturales,puntajeSociales,vidas]
					newInfo = str(idUser) + "," + username + "," + grado + "," + puntajeMatematicas + "," + puntajeEspañol + "," + puntajeNaturales + "," + puntajeSociales + "," + vidas
					database = open("perfiles.txt","a")
					database.write(newInfo + "\n")
					database.close()
			else:
				for i in range(len(perfilData)):
					if perfilData[i][1] == username:
						grado = perfilData[i][2]
						puntajeMatematicas = perfilData[i][3]
						puntajeEspañol = perfilData[i][4]
						puntajeNaturales = perfilData[i][5]
						puntajeSociales = perfilData[i][6]
						vidas = perfilData[i][7]
						infoUser = perfilData[i]
			obtenerPreguntasGrado(grado)
			return render_template('estudianteMenu.html',rol=rol,username=username,grado=grado,puntajeMatematicas=puntajeMatematicas,puntajeEspañol=puntajeEspañol,puntajeNaturales=puntajeNaturales,puntajeSociales=puntajeSociales,vidas=vidas,infoUser=infoUser,gradoPreguntas=gradoPreguntas,infoUsuario=infoUsuario)

def obtenerPreguntasGrado(grado):
	"""
	Esta funcion mete las preguntas que estan en las bases de datos en una lista,
	luego va a ponerlas en una lista que contendra las preguntas segun el grado
	del usuario.
	"""
	global gradoPreguntas

	preguntas = []

	todasPreguntas = open('preguntas.txt',encoding='utf8')
	for linea in todasPreguntas:
		linea = linea.replace('\n','')
		preguntas.append(linea.split(','))
	todasPreguntas.close()
	preguntas.pop(0)

	for i in range(len(preguntas)):
		if str(preguntas[i][2]) == str(grado) and preguntas[i] not in gradoPreguntas:
			gradoPreguntas.append(preguntas[i])

	for n in range(len(gradoPreguntas)):
		gradoPreguntas[n].pop(0)
		gradoPreguntas[n].pop(0)
		gradoPreguntas[n].pop(0)

@app.route('/estudiante/<rol>/<username>/<grado>/<infoUsuario>', methods=['POST'])
def estudiante(rol=None,username=None,materias=None,grado=None,infoUsuario=None):
	"""
	Esta funcion verifica si el usuario que ha iniciado sesion es estudiante y lo lleva
	a el menu donde respondera las preguntas.
	"""
	global infoUser,gradoPreguntass

	if session.get('logged_in'):
		##El código va a verificar que el usuario ya selecciono una materia del menú que 
		#se mostrará en pantalla, después, va a retornar el script con las preguntas.
		session['logged_in'] = True

		materia = request.form['materias']

		grado = infoUser[2]
		puntajeMatematicas = infoUser[3]
		puntajeEspañol = infoUser[4]
		puntajeNaturales = infoUser[5]
		puntajeSociales = infoUser[6]
		vidas = infoUser[7]

		if materia == 'Matematicas' or materia == 'Español' or materia == 'Naturales' or materia == 'Sociales':
			return render_template('estudiantePreguntas.html',rol=rol,username=username,grado=grado,puntajeMatematicas=puntajeMatematicas,puntajeEspañol=puntajeEspañol,puntajeNaturales=puntajeNaturales,puntajeSociales=puntajeSociales,vidas=vidas,infoUser=infoUser,gradoPreguntas=gradoPreguntas,materia=materia,infoUsuario=infoUsuario)
		elif materia == "0":
			return render_template('estudianteMenu.html',rol=rol,username=username,grado=grado,puntajeMatematicas=puntajeMatematicas,puntajeEspañol=puntajeEspañol,puntajeNaturales=puntajeNaturales,puntajeSociales=puntajeSociales,vidas=vidas,infoUser=infoUser,gradoPreguntas=gradoPreguntas,infoUsuario=infoUsuario)
	else:
		return index()

@app.route('/logout')
def logout():
	"""
	Esta funcion cierra la sesion del usuario que este en ese momento en sesion
	"""
	app.secret_key = os.urandom(32)
	session['logged_in'] = False
	rol = None
	username = None
	gradoPreguntas = []
	return index(rol,username)

if __name__ == '__main__':
	app.run(debug=True)
