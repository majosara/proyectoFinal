def getQuestions(grado):
	"""

	"""
	preguntas = [] #lista que contiene las preguntas del juego
	preguntas_grado = []
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

def showQuestions(preguntas):
	""" 
	Esta funcion mostrara en pantalla las preguntas que se anadieron a la lista preguntas
	"""
	pass

def getAnswers():
	pass

def getOptions(id_pregunta):
	"""
	Esta funcion Lista que contiene las opciones segun el id 
	de cada pregunta
	"""
	options = []
	id_options = []
	opt = open('opciones.txt')

	for opt in p:
		opt = opt.replace('\n','')
		options.append(opt.split(','))
	opt.close()
	options.pop(0)

	for n in range(len(options)):
		if options[n][0] == str(id_pregunta):
			id_options.append(options[n])
getOptions('00')