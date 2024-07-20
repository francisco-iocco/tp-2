'''Lucas Michelini, Francisco Iocco, Sebastian Gonzales, Joaquin Benitez'''
import random
import os
matriz = [[random.randint(0,1) for _ in range(7)] for _ in range(7)]
def clearConsole():
    if os.name in ('nt', 'dos'):  
        command = 'cls'
    os.system(command)
estudiantesIngreso = [["Lucasmichelini@gmail.com","123","ACTIVO"],
                       ["franciscoiocco@gmail.com","123","ACTIVO"],
                       ["sebastiangonzales@gmail.com","123","ACTIVO"],
                       ["joaquinbenitez@gmail.com","123","ACTIVO"],
                       ["1","1","ACTIVO"],
                       ["","",""],
                       ["","",""],
                       ["","",""]
                       ]
moderadorIngreso   = [["moderador1@gmail.com","123","ACTIVO"],
                       ["2","2","ACTIVO"],
                       ["","",""],
                       ["","",""]
                       ]
cantEstudiantesActivos = 5
cantModeradoresActivos = 2

def menuEstudiantes(opcion, subOpcion):
    match(opcion):
        case 0:
            print("1. Gestionar mi perfil")
            print("2. Gestionar candidatos")
            print("4. Reportes Estadísticos")
        case 1:
            print("1. Gestionar mi perfil")
            print("\t a. Editar mis datos personales")
            print("\t b. Eliminar mi perfil")
            print("\t c. Volver")
        case 2:
            print("2. Gestionar candidatos")
            print("\t a. Ver candidatos")
            print("\t b. Reportar un candidato")
            print("\t c. Volver")
        case 4:
            print("4. Reportes Estadísticos")
            print("\t En Construcción")
        case _:
            print("Por favor, elija una opcion válida.")
    
    
def registrar(baseDePerfiles,nuevoUsuario,tipoUsuario):
    if(tipoUsuario == 1):
        if(nuevoUsuario <= 7):
            email = input("Ingrese su email: ")
            contrasena = input("ingrese su contraseña: ")
            baseDePerfiles[nuevoUsuario][0] = email
            baseDePerfiles[nuevoUsuario][1] = contrasena
            baseDePerfiles[nuevoUsuario][2] = "ACTIVO"
            return baseDePerfiles
        else:
            return baseDePerfiles
    elif(tipoUsuario == 2):
        if(nuevoUsuario <= 3):
            email = input("Ingrese su email: ")
            contrasena = input("ingrese su contraseña: ")
            baseDePerfiles[nuevoUsuario][0] = email
            baseDePerfiles[nuevoUsuario][1] = contrasena
            baseDePerfiles[nuevoUsuario][2] = "ACTIVO"
            return baseDePerfiles
        else:
            return baseDePerfiles
    
def login(email,contrasena,baseDePerfiles):
    perfilEncontrado = 0
    encontrado = False 
    for i in range(len(baseDePerfiles)):
        if(email == baseDePerfiles[i][0] and
        contrasena == baseDePerfiles[i][1] and
        baseDePerfiles[i][2] == "ACTIVO"):
            encontrado = True
            perfilEncontrado = i
    if(encontrado):
        return perfilEncontrado
    else:
        return -1
    
def correcion(inicio):
    while(inicio != "LOGIN" and inicio != "REGISTRARSE"):
        clearConsole()
        print("Opcion no valida\nporfavor ingrese una de las siguientes opciones")
        inicio = input("-LOGIN\n-REGISTRARSE\nIngrese su opcion:")
        inicio = inicio.upper()
    return inicio

def cantidadMinimaNoCompletada(cEA,cMA):
    print("Necesita haber un minimo de [",cEA,"/4] estudiantes y [",cMA,"/1] modereadores")
    inicio = input("-LOGIN\n-REGISTRARSE\nIngrese su opcion:")
    inicio = inicio.upper()
    inicio = correcion(inicio)
    return inicio        


inicio = input("-LOGIN\n-REGISTRARSE\nIngrese su opcion:")
inicio = inicio.upper()
inicio = correcion(inicio)
          
while(inicio != "LOGIN" or (cantEstudiantesActivos <4 and cantModeradoresActivos < 1)):
    if(inicio == "LOGIN"):
        clearConsole()
        inicio = cantidadMinimaNoCompletada(cantEstudiantesActivos,cantModeradoresActivos)
    else:
        tipoDeUsuarioARegistrar = 0
        while(tipoDeUsuarioARegistrar == 0):
            clearConsole()
            tipoDeUsuarioARegistrar = int(input("1-Estudiante\n2-Moderador\nOpcion: "))
            if(tipoDeUsuarioARegistrar == 1):
                baseDePerfiles = registrar(estudiantesIngreso,cantEstudiantesActivos,tipoDeUsuarioARegistrar)
                if(estudiantesIngreso != baseDePerfiles):
                    estudiantesIngreso == registrar(estudiantesIngreso,cantEstudiantesActivos,tipoDeUsuarioARegistrar)
                    cantEstudiantesActivos += 1
                    clearConsole()
                    print("Usuario ingresado correctamente")
                else:
                    print("Cantidad Maxima de Alumnos")
            elif(tipoDeUsuarioARegistrar == 2):
                moderadorIngreso = registrar(moderadorIngreso,cantModeradoresActivos,tipoDeUsuarioARegistrar)
                cantModeradoresActivos += 1
                clearConsole()
                print("Usuario ingresado correctamente")
            elif(tipoDeUsuarioARegistrar != 1 and tipoDeUsuarioARegistrar != 2):
                tipoDeUsuarioARegistrar = 0
                print("opcion no valida\n")
                
        inicio = input("-LOGIN\n-REGISTRARSE\nIngrese su opcion:")
        inicio = inicio.upper()
        inicio = correcion(inicio)
        

estudianteActual = -1
moderadorActual = -1
clearConsole()        
email = input("Ingrese su email: ")
contrasena = input("ingrese su contraseña: ")
contIntentos = 0
while(contIntentos < 3 and estudianteActual == -1 and moderadorActual == -1):            
    estudianteActual = login(email,contrasena,estudiantesIngreso)
    moderadorActual = login(email,contrasena,moderadorIngreso) 
    if(estudianteActual == -1 and moderadorActual == -1):
        contIntentos += 1
        clearConsole()
        email = input("Ingrese su email: ")
        contrasena = input("ingrese su contraseña: ")
if(estudianteActual != -1):
    print(estudianteActual)
elif(moderadorActual != -1):
    print(moderadorActual)
else:
    print("n")

