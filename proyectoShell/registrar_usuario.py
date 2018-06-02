##Crea la base de datos de los usuarios pero en un diccionario

##Lista que va a contener los datos de los usuarios para luego validarlo
datos = []

def registrar_usuario(datos):
    """
    La funcion recibe la lista vacia datos y la llena con los
    datos de los estudiantes, ademas hace un input con la cantidad de
    usuarios que se van a agregar y un ciclo para ello
    """

    #opcion = int(input('¿Que desea relizar?','\n'
        #'1.Registrar usuario','\n'
        #'2.Modificar usuario'))

    #if opcion == 1:
    cant = int(input("Numero de estudiantes que va a agregar:"))

    #Apertura del archivo de los datos de los usuarios
    file = open("datos_estudiantes.txt","a")

    #Inicia un ciclo para el registro de los usuarios
    for n in range(cant):
        valFile = open("datos_estudiantes.txt","r")
        for linea in valFile:
            linea = linea.replace('\n','')
            datos.append(linea.split(','))
        valFile.close()
        finded = False #variable que se usa para retificar que no se encuentre el usuario ya registrado
        #se pide la informacion del usuario
        while finded == False
            rol = input("Ingrese el rol del usuario: ")
            usuario = input("Nombre de usuario: ")
            contraseña = input("Contraseña del usuario: ")
            try:
                correo = input("Correo del usuario(terminado en '@mail.com': ")
                p = re.compile(r'\w\{@}\w\{.com}')
                salida = p.search(correo)
            except Exception:
                print('Ingrese un correo valido')
            try:
                edad = int(input("Ingrese la edad del usuario: "))
            except ValueError:
                print('Por favor ingrese un numero')
            try:
                grado = int(input("Ingrese el grado en el que se encuentra el estudiante: "))
            except ValueError:
                print('Por favor ingrese un numero')
            try:
                id_estudiante = int(input("ingrese un numero que se le asignara al estudiante: "))
            except ValueError:
                print('Por favor ingrese un numero')

        for i in range(len(datos)):
            for j in range(len(datos[i])):
                while usuario == datos[i][j]:
                    print("Ya se encuentra el usuario, intente nuevamente")
                    usuario = input("Nombre de usuario: ")
                    if usuario == datos[i][j]:
                        finded = True
                        print('Ya se encuentra el usuario, intente nuevamente')
        ##En caso de que no se encuentre el nombre de usuario, se amacenaran los datos
        if finded == False:
            add = rol + "," + usuario + "," + contraseña  + "," + correo + "," + str(edad) + "," + str(grado) + "," + str(id_estudiante)
            file.write(add + "\n")
            print("¡Usuario agregado!")
    file.close()

    #if opcion == 2:

        #user = input('Ingrese el usuario al que desea modificarle datos:')
        ##Esta variable tendra el usuario que se quiere modificar

        #datos2 = []

        #file = open('datos_estudiantes.txt','a')

        #for user in file:
            #user = user.replace('\n','')
            #datos2.append(user.split(','))
        

        #if user == datos2[1]:
            #print('Actualice los datos del usuario!')

        #else:
            #print('Usuario no registrado, vaya al formulario de registrar usuario')