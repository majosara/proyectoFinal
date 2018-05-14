preguntas_grado = [] #Lista que guarda las preguntas segun el grado

id_answers = [] #esta lista contiene las respuestas de acuerdo al id de opciones

id_options= []

def getQuestions(grado, preguntas_grado):
	"""
	Esta funcion recibe el grado que esta contenido en las tablas relacionado
	con las preguntas y mete en una lista las preguntas y en otra las preguntas
	segun el grado que le entra de parametro
	"""
	preguntas = [] #lista que contiene las preguntas del juego
	p = open('preguntas.txt','r')

	for line in p:
		line = line.replace('\n','')
		preguntas.append(line.split(','))
	p.close()
	preguntas.pop(0)
	print(preguntas)
	for preg in range(len(preguntas)):
		if preguntas[preg][2] == str(grado):
			preguntas_grado.append(preguntas[preg])
	
	##print(preguntas_grado)

if __name__ == '__main__':
	getQuestions(1)

def showQuestions(usuario):
	""" 
	Esta funcion mostrara en pantalla las preguntas que se anadieron a la lista preguntas
	"""
	dataUser = [] #esta lista tiene la base de datos de los usuarios del juego
	info_user = #esta lista contiene la informacion del usuario que se recibe en el parametro de entrada
	
	lista = open('datos_estudiantes.txt') 
	
	for user in lista:
		user = user.replace('\n','')
		dataUser.append(user.split(','))
	lista.close()
	dataUser.pop(0)

	for i in range(len(dataUser)):
		if dataUser[i][1] == usuario:
			info_user.append(dataUser[i])
	getQuestions(info_user[6], preguntas_grado)

def getAnswers(id_pregunta):
	"""
	Esta funcion obtiene la respuesta correcta en base al id de pregunta
	"""
	answers = [] #esta lista contiene todas las respuestas

	ans = open('opciones.txt')

	for an in ans:
		an = an.replace('\n','')
		answers.append(an.split(','))
	ans.close()
	answers.pop(0)

	for n in range (len(answers)):
		if answers[n][0] == str(id_pregunta):
			id_answers.append(answers[n])
		print (id_answers)
	getAnswers('00')


def getOptions(id_pregunta):
	"""
	Esta funcion Lista que contiene las opciones segun el id 
	de cada pregunta
	"""
	options = []
	opt = open('opciones.txt')

	for op in opt:
		op = op.replace('\n','')
		options.append(opt.split(','))
	op.close()
	options.pop(0)

	for n in range(len(options)):
		if options[n][0] == str(id_pregunta):
			id_options.append(options[n])
getOptions('00')

def menu(preguntas_grado,id_options,id_answers):
	for n in range(len(preguntas_grado)):
		if preguntas_grado[n][0] == id_options[n][0]:
			respuesta = input("""{}
				a.{}b.{}
			c.{} d.{} """.format(preguntas_grado[n][3], id_options[n][1],id_options[n][2],id_options[n][3],id_options[n][4]))
