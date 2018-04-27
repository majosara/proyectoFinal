f = open('datos_estudiantes.txt')
l = []
for linea in f:
    linea = linea.replace('\n', ' ')
    l.append(linea.split(','))
f.close()
print(l)

#mostrar correos
for dato_estudiante in l:
    print(dato_estudiante[2])

f = open('nuevo_archivo.txt', 'w')
f.write('1,2,3,4\n')
f.write('1,2,3,4\n')
f.close()
