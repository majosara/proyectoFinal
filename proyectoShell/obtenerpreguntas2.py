id_answers = [] #esta variable contiene la respuesta correcta a una pregunta segun las opciones
preguntas_grado = [] #esta variable contiene las preguntas segun el grado del usuario
id_options = [] #esta variable contiene las opciones segun el id de la pregunta

def getQuestions(grado,preguntas_grado):
	"""Esta funcion se utilizara para obtener las preguntas del
	archivo plano y ponerlas en una lista"""
	preguntas = []
	p = open('preguntas.txt')

	for pregunta in p:
		pregunta = pregunta.replace('\n','')
		preguntas.append(pregunta.split(','))

	p.close()
	preguntas.pop(0)
	##print(preguntas)

	for i in range(len(preguntas)):
		if preguntas[i][2] == str(grado):
			preguntas_grado.append(preguntas[i])

def getOptions(preguntas,id_options):
	"""Esta funcion se utilizara para obtener las opciones de las
	preguntas que estan en un archivo plano y las pondra en una
	lista"""
	options = []
	o = open('opciones.txt')

	for opcion in o:
		opcion = opcion.replace('\n','')
		options.append(opcion.split(','))
	o.close()

	options.pop(0)

	for i in range(len(options)):
		if options[i][0] == str(preguntas[0]):
			id_options.append(options[i])

def rightAnswers(preguntas_grado,id_answers):
	"""Esta funcion se utilizara para obtener la respuesta correcta
	de cada pregunta y las  pondra en una lista"""

	right_answers = [] #lista que contendra las respuestas correctas
	ans = open('respuesta_correcta.txt')

	for a in ans:
		a = a.replace('\n','')
		right_answers.append(a.split(','))
	ans.close()
	right_answers.pop(0)

	for i in range(len(right_answers)):
		if right_answers[i][1] == str(preguntas_grado[0]):
			id_answers.append(right_answers[i])
	#print(id_answers)


#def questions4grade(preguntas,grado,preguntas_grado):
	"""Esta funcion pone en una lista las preguntas segun el usuario,
	es decir, por el grado de dicho usuario"""
	#for preg in range(len(preguntas)):
		#if preguntas[preg][2] == str(grado):
			#preguntas_grado.append(preguntas[preg])
			#print(preguntas_grado)

def menuPreguntasOpciones(preguntas_grado,id_options,id_answers):
	"""Esta funcion recibe las listas donde se encuentran las preguntas
	segun el grado del usuario, las opciones y las respuestas e estas mismas"""
	
	for i in range(len(preguntas_grado)):
		if preguntas_grado[i][0] == id_options[i][0]:
			userAnswer = input("""{}
				a.{}	b.{}
				c.{}	d.{}
				Respuesta: """.format(preguntas_grado[i][3], id_options[i][2], id_options[i][3],id_options[i][4],id_options[i][5]))
			if userAnswer == id_answers[i][2]:
				print('Correcto!')
			else:
				print('Incorrecto!')

def showQuestions(usuario):
	""" """
	dataUser = [] #esta lista contiene la base de datos de los usuarios
	infoUser = [] #esta lista contiene la informacion del usuario que se recibe como parametro

	datos = open('datos_estudiantes.txt')

	for user in datos:
		user = user.replace('\n','')
		dataUser.append(user.split(','))
	datos.close()
	dataUser.pop(0)

	for i in range(len(dataUser)):
		if dataUser[i][1] == usuario:
			infoUser = dataUser[i]
			print(infoUser)

	getQuestions(infoUser[6],preguntas_grado)

	for i in range(len(preguntas_grado)):
		getOptions(preguntas_grado[i][0],id_options)

	for i in range(len(preguntas_grado)):
		rightAnswers(preguntas_grado[i][0],id_answers)

	menuPreguntasOpciones(preguntas_grado,id_options,id_answers)