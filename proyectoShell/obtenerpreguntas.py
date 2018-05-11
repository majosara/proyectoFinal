def getQuestions(grado):
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
	print(preguntas_grado)

if __name__ == '__main__':
	getQuestions(1)

