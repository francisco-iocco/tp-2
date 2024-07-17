'''Lucas Michelini, Francisco Iocco, Sebastian Gonzales, Joaquin Benitez'''
import random

matriz = [[random.randint(0,1) for _ in range(7)] for _ in range(7)]
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
    
def Logueo(cEA,cMA,inicio):
    while(inicio != "LOGIN" and inicio != "REGISTRARSE"):
        print("Opcion no valida\nporfavor ingrese una de las siguientes opciones")
        inicio = input("-LOGIN\n-REGISTRARSE\nIngrese su opcion:")
        inicio = inicio.upper() 
        
    if(cEA < 4 or cMA < 1 and inicio == "LOGIN"):
        return False
    elif(cEA >= 4 or cMA >= 1):
        return True

inicio = input("-LOGIN\n-REGISTRARSE\nIngrese su opcion:")
inicio = inicio.upper()

while(not(Logueo(cantEstudiantesActivos,cantModeradoresActivos,inicio))):
    print("Necesita ingresar mas estudiantes[",cantEstudiantesActivos,"/4] o modereadores[",cantModeradoresActivos,"/1]")
    inicio = input("-LOGIN\n-REGISTRARSE\nIngrese su opcion:")
    inicio = inicio.upper()
    #HACER UNA FUNCION PARA REGISTRAR ESTUDIANTES'''

while(inicio == "REGISTRARSE" and cantEstudiantesActivos < 8 or cantModeradoresActivos < 4):
    if(cantEstudiantesActivos < 8 or cantModeradoresActivos < 4 ):
        #HACER UNA FUNCION PARA REGISTRAR ESTUDIANTES'''
        inicio = input("-LOGIN\n-REGISTRARSE\nIngrese su opcion:")
        inicio = inicio.upper()
         
        
email = input("Ingrese su email: ")
contrasena = input("ingrese su contraseña: ")

estudianteActual = -1
moderadorActual = -1

contIntentos = 0
while(contIntentos < 3):            
    for i in range(len(estudiantesIngreso)):
        if(email == estudiantesIngreso[i][0] and
        contrasena == estudiantesIngreso[i][1] and
        estudiantesIngreso[i][2] == "ACTIVO"):
            estudianteActual = i
            moderadorActual = -1
        elif(email == moderadorIngreso[i][0] and        #PROBLEMA AL TRATAR DE LEER MODERADOR EN POSICION
            contrasena == moderadorIngreso[i][1] and    #MAYOR Q 4(SIN SOLUCIONAR)
            moderadorIngreso[i][2] == "ACTIVO"):
            moderadorActual = i
            estudianteActual = -1
        else:
            contIntentos+=1
print(estudianteActual, moderadorActual)            
