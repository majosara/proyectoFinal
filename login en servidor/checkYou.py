from flask import flask
from flask import render_template,request,session
import os

app = Flask(__name__)

app.secret-key = os.random(32)

userData = []
infoUser = []
gradoPreguntas = []

lista = open('datos_usuarios.txt')
for user in lista:
	user = user.replace('\n','')
	userData.append(user.split(','))
lista.close()

@app.route('/')
def index(rol = None, username = None):
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		return users(rol,username)

@app.route('/admin',methods=['POST'])
def admin(rol=None,username=None):
	if session.get('logged_in'):
		perfil = open('perfiles.txt','a')
		file = open('datos_usuarios.txt','a')

		usersData = []
		datosEstudiante = open('datos_usuarios.txt','r')

		for linea in datosEstudiante:
			linea = linea.replace('\n','')
			usersData.append(linea.split(','))
		datosEstudiante.close()

		id_usuario = len(usersData) - 1
		for i in range(len(usersData)):
			if request.form['userRegister'] != userData[n][1]:
				agregarUsers = request.form['rolRegister'] + ',' + request.form['userRegister'] + ',' + request.form['contraseñaRegister'] + ',' + ´str(id_usuario) + ',' + request.form['correoRegister'] + ',' + request.form['edadRegister'] + ',' + request.form['gradoRegister']
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

@app.route('/login',methods=['POST'])
def login(rol=None,username=None):
	global userData
	for i in range(len(userData)):
		if request.form['username']==userData[i][1] and request.form['password']==userData[i][2]:
			session['logged_in'] = True
			rol = userData[i][0]
			username = request.form['username']
	if rol != None and username != None:
		return index(rol,username)
	else:
		return index(rol,username)

@app.route('/users/<rol>/<username>/<infoUsuario>')
def users(rol=None,username=None,infoUsuario=None):
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
				infoUsuario = list(infoUsuario)
				for i in range(len(infoUsuario)):
					idUser = infoUsuario[0]
					grado = infoUsuario[-6]
					puntajeMatematicas = [-5]
					puntajeEspañol = [-4]
					puntajeNaturales = [-3]
					puntajeSociales = [-2]
					vidas = infoUsuario[-1]
					infoUser = [idUser,username,grado,puntajeMatematicas,puntajeEspañol,puntajeNaturales,puntajeSociales,vidas]
					newInfo = str(idUser) + ',' + username + ',' + grado + ',' + puntajeMatematicas + ',' + puntajeEspañol + ',' + puntajeNaturales + ',' + puntajeSociales + ',' + vidas
					database = open('perfiles.txt','a')
					database.write(newInfo + '\n')
					database.close()
			else:
				for i in range(len(perfilData)):
					if perfilData[i][1]==username:
						grado = perfilData[i][2]
						puntajeMatematicas = perfilData[i][3]
						puntajeEspañol = perfilData[i][4]
						puntajeNaturales = perfilData[i][5]
						puntajeSociales = perfilData[i][6]
						vidas = perfilData[i][7]
						infoUser = perfilData[i]
			obtenerPreguntasGrado(grado)
			return render_template('estudianteMenu.html',rol=rol,username=username,grado=grado,puntajeMatematicas=puntajeMatematicas,puntajeEspañol=puntajeEspañol,puntajeNaturales=puntajeNaturales,puntajeSociales=puntajeSociales,vidas=vidas,infoUser=infoUser)

def obtenerPreguntasGrado(grado):
	global gradoPreguntas

	preguntas = []

	todasPreguntas = open('preguntas.txt')
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

def estudiante(rol=None,username=None,materias=None,grado=None,infoUsuario=None):
	global infoUser,gradoPreguntas

	if session.get('logged_in'):
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
	else:
		return index()


@app.route('/logout')
def logout():
	app.secret_key = os.urandom(32)
	session['logged_in'] = False
	rol = None
	username = None
	gradoPreguntas = []
	return index(rol,username)

if __name__ == '__main__':
	app.run(debug=True)