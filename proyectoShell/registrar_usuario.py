##Crea la base de datos de los usuarios pero en un diccionario

##Lista que va a contener los datos de los usuarios para luego validarlo
datos = []

def registrar_usuario(datos):
    ##Cantidad de usuarios que se van a crear
    loop = int(input("¿Cuantos estudiantes va a agregar?: "))

    ##Apertura del archivo de los usuarios, información: rol, usuario, contraseña y correo electronico
    file = open("datos_estudiantes.txt","a")


    ##Inicia un ciclo para el registro de los usuarios
    for n in range(loop):
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
        ##
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
            ##Data['{}'.format(usuario)]= ['{},{},{}'.format(rol,contraseña,correo)]
            add = rol + "," + usuario + "," + contraseña  + "," + correo + "," + str(edad) + "," + str(grado) + "," + str(id_estudiante)
            file.write(add + "\n")
            input("¡Usuario agregado! presiona ENTER para salir.")
    ##Se cierra el documento.
    file.close()
