from registrar_usuario import *
from obtenerpreguntas import *
def comprobar_usuario():
    rol = None
    logged = False
    lista = open('login.txt')
    l = []
    datos = []
    usuario = input('ingrese el usuario: ')
    contrasena = input('ingrese la contrasena: ')
    for user in lista:
        user = user.replace('\n', '')
        l.append(user.split(','))

    ##Verifica si el usuario se encuentra en la base de datos
    for n in range(len(l)):
        if usuario == l[n][0] and contrasena == l[n][1]:
            logged = True
            rol = l[n][0]
        else:
            logged = False
            
        if logged:
            if rol == 'admin':
                registrar_usuario(datos)
            else:
                print('Bienvenido a Check you!,',usuario)
                return showQuestions(usuario)

    
comprobar_usuario()
