'''Lucas Michelini, Francisco Iocco, Sebastian Gonzales, Joaquin Benitez'''
import random
import os
import datetime

matriz = [[random.randint(0,1) for _ in range(7)] for _ in range(7)]
def clearConsole(email = ""):
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
datosPersonales = [["Nombre: Lucas Michelini","Edad: ",(datetime.now() - datetime.fromisoformat("2005-06-04")).days // 365,"Sexo: M","Biografia: Rellenar","Hobbies: Progamacion competitiva,gimanasio,leer"],
                   ["Nombre: Francisco Iocco","Edad: ",(datetime.now() - datetime.fromisoformat("2006-01-02")).days // 365,"Sexo: M","Biografia: Rellenar","Hobbies: Rellenar Hobbies"],
                   ["Nombre: Francisco Iocco","Edad: ",(datetime.now() - datetime.fromisoformat("2006-01-02")).days // 365,"Sexo: M","Biografia: Rellenar","Hobbies: Rellenar Hobbies"],
                   ["Nombre: Francisco Iocco","Edad: ",(datetime.now() - datetime.fromisoformat("2006-01-02")).days // 365,"Sexo: M","Biografia: Rellenar","Hobbies: Rellenar Hobbies"],
                   ["","","","",""],
                   ["","","","",""],
                   ["","","","",""],
                   ["","","","",""]
                   ]

def editarDatos():
    '''por hacer'''
    
def menuPrincipal(estudiante):
    print("\t",estudiante)
    print("MENU PRINCIPAL\n")
    print("1-Gestionar Perfil")
    print("2-Gestionar Canditos")
    print("3-Matcheos")
    print("4-Reportes estadisticos")
    print("0-Salir")
    

def menu1(estudiante):
    print("\t",estudiante)
    print("1-Gestionar Perfil")
    print("\ta.Editar mis datos personales")
    print("\tb.Eliminar mi perfil")
    print("\tc.volver")
    

def menu2(estudiante):
    print("\t",estudiante)
    print("2-Gestionar candidatos")
    print("\ta. Ver candidatos")
    print("\tb. Reportar un candidato")
    print("\tc. Volver")
    

def menu3(estudiante):
    print("\t",estudiante)
    print("3-Matcheos")
    print("\ta. Ver matcheos")
    print("\tb. Eliminar un matcheo")
    print("\tc. Volver")
    

def menu4(estudiante):
    print("\t",estudiante)
    print("4-Reportes estadisticos")
    print("")
    
 
def cartel():
    print("En construccion\n")

def subMenu1(estudiante):
    clearConsole(estudiante)
    opc1 = ""
    while(opc1 != "c"):
        menu3()
        opc1 = input("\nIngrese su opción: ")
        if(opc1 != "a" and opc1 != "b" and opc1 !="c"):
            clearConsole()
            print("Opción invalida - Ingrese su opcion nuevamente\n")
        clearConsole()
        match opc1:
            case "a": 
                datosPersonales = editarDatos(estudiante, datosPersonales)
            case "b": cartel()
            
def subMenu2(estudiante):
    clearConsole()
    opc2 = ""
    while(opc2 != "c"):
        menu3()
        opc2 = input("\nIngrese su opción: ")
        if(opc2 != "a" and opc2 != "b" and opc2 !="c"):
            clearConsole()
            print("Opción invalida - Ingrese su opcion nuevamente\n")
        clearConsole()
        match opc2:
            case "a": cartel()
            case "b": cartel()
def subMenu3(estudiante):
    clearConsole()
    opc3 = ""
    while(opc3 != "c"):
        menu3(estudiante)
        opc3 = input("\nIngrese su opción: ")
        if(opc3 != "a" and opc3 != "b" and opc3 !="c"):
            clearConsole()
            print("Opción invalida - Ingrese su opcion nuevamente\n")
        clearConsole()
        match opc3:
            case "a": cartel()
            case "b": cartel()
            
def subMenu4(estudiante):
    clearConsole()
    cartel()
                
def menuIterativo(estudiante):
    opc = ""
    clearConsole()
    while(opc != '0'):
        menuPrincipal(estudiante)
        opc = input("\nIngrese su opción: ")
        esDigito = opc.isdigit()
        if(not(esDigito) or not(int(opc) >= 0 and int(opc) <= 4)):
            clearConsole()
            print("\nPor favor, ingrese un opción valida.\n")
        else:
            match int(opc):
                case 1:
                    subMenu1(estudiante)
                case 2:
                    subMenu2(estudiante)
                case 3:
                    subMenu3(estudiante)
                case 4:
                    subMenu4(estudiante)
                case 0:
                    clearConsole()
                    print("Gracias por usar nuestro programa!")
    
def registrar(baseDePerfiles,nuevoUsuario,tipoUsuario):
    if(tipoUsuario == 1):
        if(nuevoUsuario <= 7):
            clearConsole()
            print("MENU DE REGISTRO")
            email = input("Ingrese su email: ")
            
            contrasena = input("ingrese su contraseña: ")
            baseDePerfiles[nuevoUsuario][0] = email
            baseDePerfiles[nuevoUsuario][1] = contrasena
            baseDePerfiles[nuevoUsuario][2] = "ACTIVO"
            return baseDePerfiles
    elif(tipoUsuario == 2):
        if(nuevoUsuario <= 3):
            clearConsole()
            print("MENU DE REGISTRO")
            email = input("Ingrese su email: ")
            contrasena = input("ingrese su contraseña: ")
            baseDePerfiles[nuevoUsuario][0] = email
            baseDePerfiles[nuevoUsuario][1] = contrasena
            baseDePerfiles[nuevoUsuario][2] = "ACTIVO"
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
                if(cantEstudiantesActivos < 8):
                    estudiantesIngreso == registrar(estudiantesIngreso,cantEstudiantesActivos,tipoDeUsuarioARegistrar)
                    cantEstudiantesActivos += 1
                    clearConsole()
                    print("Usuario ingresado correctamente")
                else:
                    print("Cantidad maxima de alumnos alcanzada")
            elif(tipoDeUsuarioARegistrar == 2):
                if(cantModeradoresActivos < 4):
                    moderadorIngreso = registrar(moderadorIngreso,cantModeradoresActivos,tipoDeUsuarioARegistrar)
                    cantModeradoresActivos += 1
                    clearConsole()
                    print("Usuario ingresado correctamente")
                else:
                    clearConsole()
                    print("Cantidad maxima de moderadores alcanzada")
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
    menuIterativo(estudianteActual)


        
elif(moderadorActual != -1):
    print(moderadorActual)
else:
    print("n")
