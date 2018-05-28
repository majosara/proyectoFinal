from registrar_usuario import *
from obtenerpreguntas2 import *

def comprobar_usuario():
    rol = None
    loggin = False
    login = open('login.txt')
    newlogin = [] #lista que contendra los datos de login.txt
    datos = []
    usuario = input('ingrese el usuario: ')
    contrasena = input('ingrese la contrasena: ')
    for user in login:
        user = user.replace('\n', '')
        newlogin.append(user.split(','))

    ##Verifica si el usuario se encuentra en la base de datos
    for i in range(len(newlogin)):
        if usuario == newlogin[i][0] and contrasena == newlogin[i][1]:
            loggin = True
            rol = newlogin[i][0]
        else:
            loggin = False

        if usuario not in newlogin[i][0]:
            loggin = False
            print('Usuario incorrecto o no registrado')
            break
        if contrasena not in newlogin[i][1]:
            loggin=False
            print('Contrasena incorrecta')
            break

            #if usuario != newlogin[i][0]:
             #   loggin = False
              #  print('Usuario incorrecto o no registrado')
               # break
            #if contrasena != newlogin[i][1]:
             #   loggin = False
              #  print('Contrasena incorrecta!')
               # break

        if loggin:
            if rol == 'admin':
                registrar_usuario(datos)
            else:
                print('Bienvenido a Check you!,',rol,usuario)
                #return showQuestions(usuario)



comprobar_usuario()