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
                       ["","",""],
                       ["","",""],
                       ["","",""],
                       ["1","1","ACTIVO"]
                       ]
moderadorIngreso   = [["moderador1@gmail.com","123","ACTIVO"],
                       ["","",""],
                       ["","",""],
                       ["2","2","ACTIVO"]
                       ]
cantEstudiantesActivos = 8
cantModeradoresActivos = 1

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
    
def Inicializacion(cEA,cMA,inicio):
    while(inicio != "LOGIN" and inicio != "REGISTRARSE"):
        clearConsole()
        print("Opcion no valida\nporfavor ingrese una de las siguientes opciones")
        inicio = input("-LOGIN\n-REGISTRARSE\nIngrese su opcion:")
        inicio = inicio.upper() 
        
    if(cEA < 4 or cMA < 1 and inicio == "LOGIN"):
        return False
    elif(cEA >= 4 or cMA >= 1):
        return True

inicio = input("-LOGIN\n-REGISTRARSE\nIngrese su opcion:")
inicio = inicio.upper()

while(not(Inicializacion(cantEstudiantesActivos,cantModeradoresActivos,inicio))):
    clearConsole()
    print("Necesita ingresar mas estudiantes[",cantEstudiantesActivos,"/4] o modereadores[",cantModeradoresActivos,"/1]")
    inicio = input("-LOGIN\n-REGISTRARSE\nIngrese su opcion:")
    inicio = inicio.upper()
    #HACER UNA FUNCION PARA REGISTRAR ESTUDIANTES'''

while(inicio == "REGISTRARSE"):
    clearConsole()
    if(cantEstudiantesActivos < 8 or cantModeradoresActivos < 4 ):
        #HACER UNA FUNCION PARA REGISTRAR ESTUDIANTES'''
        inicio = input("-LOGIN\n-REGISTRARSE\nIngrese su opcion:")
        inicio = inicio.upper()
         

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

