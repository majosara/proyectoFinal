##archivos
f = open('preguntas.txt','r')
for linea in f:
    print(linea, type(linea))
f.close()
print(f.readline())

f = open('preguntas.txt','r')
for linea in f:
    print(linea, type(linea))
f.close()
print('nuevo for')

