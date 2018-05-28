f = open('datos.txt')
l = []
d = {}
for linea in f:
    linea = linea.replace('\n', ' ')
    l.append(linea.split(','))
f.close()
d['p1@p.com']
print(l)
