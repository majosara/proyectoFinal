preguntas_grado = [] #Lista que guarda las preguntas segun el grado

id_answers = [] #esta lista contiene las respuestas de acuerdo al id de opciones

id_options= []  #esta variable contiene la lista de las opciones de cada pregunta segun su id

def getQuestions(grado,preguntas_grado):
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
	#print(preguntas)
	for preg in range(len(preguntas)):
		if preguntas[preg][2] == str(grado):
			preguntas_grado.append(preguntas[preg])
	
	##print(preguntas_grado)


def getAnswers(id_pregunta,id_answers):
	"""
	Esta funcion obtiene la respuesta correcta en base al id de pregunta
	"""
	answers = [] #esta lista contiene todas las respuestas

	ans = open('respuesta_correcta.txt')

	for an in ans:
		an = an.replace('\n','')
		answers.append(an.split(','))
	ans.close()
	answers.pop(0)

	for i in range (len(answers)):
		if answers[i][0] == str(id_pregunta):
			id_answers.append(answers[i])
		##print (id_answers)
	##getAnswers('00')


def getOptions(id_pregunta,id_options):
	"""
	Esta funcion Lista que contiene las opciones segun el id 
	de cada pregunta
	"""
	options = [] #esta lista contiene las opciones segun el id de pregunta
	opt = open('opciones.txt')

	for op in opt:
		op = op.replace('\n','')
		options.append(op.split(','))
	opt.close()
	options.pop(0)

	for i in range(len(options)):
		if options[i][0] == str(id_pregunta):
			id_options.append(options[i])

def menu(preguntas_grado,id_options,id_answers):
	"""
	Esta funcion recibe la lista donde estan las preguntas por el grado,
	los id de las opciones y los id de las respuestas, lo pone en un menu
	y solo basta que el usuario ingrese la letra que tiene la opcion correcta.
	"""
	for i in range(len(preguntas_grado)):
		#print(id_answers[i][2])
		if preguntas_grado[i][0] == id_options[i][0]:
			respuesta = input("""{}
				a.{}	b.{}
				c.{}	d.{} 
				Respuesta: """.format(preguntas_grado[i][3], id_options[i][2],id_options[i][3],id_options[i][4],id_options[i][5]))
			if respuesta == id_answers[i][2]:
				print('Correcto!')
			else:
				print('Incorrecto!')

def showQuestions(usuario):
	""" 
	Esta funcion mostrara en pantalla las preguntas que se anadieron a la lista preguntas
	"""
	dataUser = [] #esta lista tiene la base de datos de los usuarios del juego
	info_user = []#esta lista contiene la informacion del usuario que se recibe en el parametro de entrada
	lista = open('datos_estudiantes.txt') 
	
	for user in lista:
		user = user.replace('\n','')
		dataUser.append(user.split(','))
	lista.close()
	dataUser.pop(0)

	for i in range(len(dataUser)):
		if dataUser[i][1] == usuario:
			info_user=dataUser[i]
			print(info_user)

	getQuestions(preguntas,info_user[6], preguntas_grado)

	for i in range(len(preguntas_grado)):
		getOptions(preguntas_grado[i][0],id_options)
	
	for i in range(len(preguntas_grado)):
		getAnswers(preguntas_grado[i][0],id_answers)

	menu(preguntas_grado,id_options,id_answers)

##showQuestions('robinquintero')
##if __name__ == '__main__':
##	getQuestions(1,preguntas_grado)
