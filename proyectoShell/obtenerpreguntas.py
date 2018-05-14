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
	pass

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