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
        ##Abre el archivo que contiene los usuarios y los lee, a medida que los lee
        ##añade cada linea del texto en la lista "datos"
        valFile = open("datos_estudiantes.txt","r")
        for linea in valFile:
            linea = linea.replace('\n','')
            datos.append(linea.split(','))
        ##Cierra el documento para dejar de leer sus lineas para posteriormente modificarlas
        valFile.close()
        ##Establece que aún no se encuentra el usuario en la base de datos
        ##es decir que el usuario que se ingreso es único y se puede escribir en ella (base de datos)
        finded = False
        ##En los siguientes inputs se pide la información del usuario
        rol = input("Ingrese el rol del usuario: ")
        usuario = input("Nombre de usuario: ")
        contraseña = input("Contraseña del usuario: ")
        correo = input("Correo del usuario: ")
        edad = int(input("Ingrese la edad del usuario: "))
        grado = int(input("Ingrese el grado en el que se encuentra el estudiante: "))
        id_estudiante = int(input("ingrese un numero que se le asignara al estudiante: "))

        ##En el siguiente ciclo se va a validar los datos que se ingresaron (el usuario)
        ##Entra en la primera sublista de datos
        for i in range(len(datos)):
            ##Entra en la primera lista de la sublista
            for j in range(len(datos[i])):
                ##Este ciclo hace lo siguiente: Si el nombre del usuario que se ingreso
                ##corresponde a un valor que está contenido en la lista de datos.
                ##Entonces le va a decir que ese usuario ya se encuentra y le va a pedir
                ##que ingrese un nuevo usuario hasta que no sea igual a uno que este en la lista "datos"
                while usuario == datos[i][j]:
                    print("Ya se encuentra el usuario, intente nuevamente")
                    usuario = input("Nombre de usuario: ")
                    if usuario == datos[i][j]:
                        finded = True
                        print('Ya se encuentra el usuario, intente nuevamente')
        ##En caso de que no se encuentre el nombre de usuario, se amacenaran los datos
        ##en una variable llamada "add" y esta se añadira al documento de texto finalizando con un enter.
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