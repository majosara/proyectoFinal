def comprobar_usuario():
    lista = open('login.txt')
    l = []
    usuario = input('ingrese el usuario: ')
    contrasena = input('ingrese la contrasena: ')
    for user in lista:
        user = user.replace('\n', '')
        l.append(user.split(','))
        if usuario == l[0][0] and contrasena == l[0][1]:
            print('bienvenido',usuario)
            break
    
comprobar_usuario()
