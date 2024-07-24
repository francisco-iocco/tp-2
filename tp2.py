'''Lucas Michelini, Francisco Iocco, Sebastian Gonzales, Joaquin Benitez'''
import random
import os
from datetime import datetime

matriz = [[random.randint(0,1) for _ in range(7)] for _ in range(7)]
def clearConsole(email = ""):
    if os.name in ('nt', 'dos'):  
        command = 'cls'
    os.system(command)
    

estudiantesIngreso = [["lucas","123","ACTIVO"],
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
datosPersonales = [["Lucas Michelini","2005-06-04","M","Rellenar","Progamacion competitiva,gimanasio,leer"],
                   ["Francisco Iocco","15","M","Rellenar","Rellenar"],
                   ["Sebastian Gonzales","14","M","Rellenar","Rellenar"],
                   ["Joaquin Benitez","29","M","Rellenar","Rellenar"],
                   ["","","","",""],
                   ["","","","",""],
                   ["","","","",""],
                   ["","","","",""]
                   ]
def verCandidatos(datos,cant):
    for i in range(cant):
        print("-----Estudiante",i,"------")
        for j in range(5):
            print(datos[i][j])
    matcheo = ""
    while matcheo != "NO":
        matcheo = input("¿Quieres dar matcheo? (SI/NO): ")
        if(matcheo != "SI" and matcheo != "NO"):
            clearConsole()
            for i in range(cant):
                print("-----Estudiante",i,"------")
                for j in range(5):
                    print(datos[i][j])
            print("Opcion inválida.")
        else:
            clearConsole()
            meGusta = input("¿Quien te gusta? (nombre y apellido): ")
            for i in range(cant):
                if(datos[i][0] == meGusta):
                    '''POR HACER'''
            
            
def editarDatos(x,datos):
    for i in range(5):
        print(datos[x][i])
    datoCambiar = -1         
    while(int(datoCambiar) != 0):
        print("\nQue dato quiere cambiar?\n\t1-Nombre\n\t2-Edad\n\t3-Sexo\n\t4-Biografia\n\t5-Hobbies\n\t(0)-salir")
        datoCambiar = input("Ingrese una opción: ")
        clearConsole()
        match int(datoCambiar):
            case 1:
                nuevoNombre = input("\nIngrese su nuevo nombre: ")
                datos[x][0] = nuevoNombre
            case 2:
                nuevaEdad = input("ingrese su nueva edad: ")
                datos[x][1] = nuevaEdad
            case 3:
                nuevoSexo = input("ingrese su nuevo sexo: ")
                datos[x][1] = nuevoSexo
            case 4:
                nuevaBiografia = input("ingrese su nueva biografia: ")
                datos[x][1] = nuevaBiografia
            case 5:
                nuevosHobbies = input("ingrese sus nuevo hobbies: ")
                datos[x][1] = nuevosHobbies
        clearConsole()
    clearConsole()
    return datos
def eliminarDatos(x,datos):
    for i in range(3):
        print(datos[x][i])
    confirm =input("\nSeguro que quiere eliminar este perfir[SI/NO]")
    confirm = confirm.upper()
    while(confirm != "SI" and confirm != "NO"):
        print("Porfavor ingrese SI o no")
        confirm =input("Seguro que quiere eliminar este perfir[SI/NO]")     
        confirm = confirm.upper()
    if(confirm == "SI"):
        datos[x][2] = "INACTIVO"
        return datos
                
    
def menuPrincipal(x,estudiante):
    print("\t",estudiante[x][0])
    print("MENU PRINCIPAL\n")
    print("1-Gestionar Perfil")
    print("2-Gestionar Canditos")
    print("3-Matcheos")
    print("4-Reportes estadisticos")
    print("0-Salir")
    

def menu1(x,estudiante):
    print("\t",estudiante[x][0])
    print("1-Gestionar Perfil")
    print("\ta.Editar mis datos personales")
    print("\tb.Eliminar mi perfil")
    print("\tc.volver")
    

def menu2(x,estudiante):
    print("\t",estudiante[x][0])
    print("2-Gestionar candidatos")
    print("\ta. Ver candidatos")
    print("\tb. Reportar un candidato")
    print("\tc. Volver")
    

def menu3(x,estudiante):
    print("\t",estudiante[x][0])
    print("3-Matcheos")
    print("\ta. Ver matcheos")
    print("\tb. Eliminar un matcheo")
    print("\tc. Volver")
    

def menu4(x,estudiante):
    print("\t",estudiante[x][0])
    print("4-Reportes estadisticos")
    print("")

def menuPrincipalMod(x,moderador):
    print("\t",moderador[x][0])
    print("1-Gestionar Usuario")
    print("2-Ver reportes")
    
def menu1mod(x,moderador):
    print("\t",moderador[x][0])
    print("1-Gestionar Usuario")
    print("\ta.Desactivar Usuario")
    print("\tb.Volver")
    
def menu2mod(x,moderador):
    print("\t",moderador[x][0])
    print("1-Gestionar Usuario")
    print("\ta.Ver reportes")
    print("\tb.Volver")
    
def cartel():
    print("En construccion\n")

def subMenu1(usuario,datosPersonales,estudiantesIngreso):
    clearConsole()
    opc1 = ""
    while(opc1 != "c"):
        menu1(usuario,datosPersonales)
        opc1 = input("\nIngrese su opción: ")
        clearConsole()
        if(opc1 != "a" and opc1 != "b" and opc1 !="c"):
            clearConsole()
            print("Opción invalida - Ingrese su opcion nuevamente\n")
        match opc1:
            case "a": 
                datosPersonales = editarDatos(usuario,datosPersonales)
            case "b": 
                estudianteIngreso = eliminarDatos(usuario,estudiantesIngreso)
                clearConsole()
                inicializacion(cantEstudiantesActivos,cantModeradoresActivos,moderadorIngreso,estudiantesIngreso)
            
def subMenu2(usuario,datosPersonales,cantEstudiantesActivos):
    clearConsole()
    opc2 = ""
    while(opc2 != "c"):
        menu2(usuario,datosPersonales)
        opc2 = input("\nIngrese su opción: ")
        clearConsole()
        if(opc2 != "a" and opc2 != "b" and opc2 !="c"):
            clearConsole()
            print("Opción invalida - Ingrese su opcion nuevamente\n")
        match opc2:
            case "a": 
                verCandidatos(datosPersonales,cantEstudiantesActivos)
            case "b": 
                cartel()
def subMenu3(usuario,datosPersonales):
    clearConsole()
    opc3 = ""
    while(opc3 != "c"):
        menu3(usuario,datosPersonales)
        opc3 = input("\nIngrese su opción: ")
        clearConsole()
        if(opc3 != "a" and opc3 != "b" and opc3 !="c"):
            clearConsole()
            print("Opción invalida - Ingrese su opcion nuevamente\n")
        match opc3:
            case "a": 
                cartel()
            case "b": 
                cartel()
            
def subMenu4(usuario,datosPersonales):
    clearConsole()
    cartel()
    
def subMenu1Mod(usuario,moderadorIngreso):
    clearConsole()
    opc1 = ""
    while(opc1 != "b"):
        menu1mod(usuario,moderadorIngreso)
        opc1 = input("\nIngrese su opción: ")
        clearConsole()
        if(opc1 != "a" and opc1 != "b" ):
            clearConsole()
            print("Opción invalida - Ingrese su opcion nuevamente\n")
        match opc1:
            case "a": 
                cartel()
                
def subMenu2Mod(usuario,moderadorIngreso):
    clearConsole()
    opc2 = ""
    while(opc2 != "b"):
        menu2mod(usuario,moderadorIngreso)
        opc2 = input("\nIngrese su opción: ")
        clearConsole()
        if(opc2 != "a" and opc2 != "b" ):
            clearConsole()
            print("Opción invalida - Ingrese su opcion nuevamente\n")
        match opc2:
            case "a": 
                cartel()
                
def menuIterativo(usuario,datosPersonales,moderadorIngreso,estudiantesIngreso,modo,cantEstudiantesActivos):
    if(modo == "estudiante"):
        opc = ""
        clearConsole()
        while(opc != '0'):
            menuPrincipal(usuario,datosPersonales)
            opc = input("\nIngrese su opción: ")
            clearConsole()
            esDigito = opc.isdigit()
            if(not(esDigito) or not(int(opc) >= 0 and int(opc) <= 4)):
                clearConsole()
                print("\nPor favor, ingrese un opción valida.\n")
            else:
                match int(opc):
                    case 1:
                        subMenu1(usuario,datosPersonales,estudiantesIngreso)
                    case 2:
                        subMenu2(usuario,datosPersonales,cantEstudiantesActivos)
                    case 3:
                        subMenu3(usuario,datosPersonales)
                    case 4:
                        subMenu4(usuario,datosPersonales)
                    case 0:
    
                        print("Gracias por usar nuestro programa!")
    if(modo == "moderador"):
        opc = ""
        clearConsole()
        while(opc != '0'):
            menuPrincipalMod(usuario,moderadorIngreso)
            opc = input("\nIngrese su opción: ")
            esDigito = opc.isdigit()
            if(not(esDigito) or not(int(opc) >= 0 and int(opc) <= 4)):
                clearConsole()
                print("\nPor favor, ingrese un opción valida.\n")
            else:
                match int(opc):
                    case 1:
                        subMenu1Mod(usuario,moderadorIngreso)
                    case 2:
                        subMenu2Mod(usuario,moderadorIngreso)
                    

    
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

def ingreso(cantEstudiantesActivos):
    estudianteActual = -1
    moderadorActual = -1
    clearConsole()        
    email = input("Ingrese su email: ")
    contrasena = input("ingrese su contraseña: ")
    contIntentos = 1
    while(contIntentos < 3 and estudianteActual == -1 and moderadorActual == -1):            
        estudianteActual = login(email,contrasena,estudiantesIngreso)
        moderadorActual = login(email,contrasena,moderadorIngreso) 
        if(estudianteActual == -1 and moderadorActual == -1):
            contIntentos += 1
            clearConsole()
            print("Email o contraseña no encontrados")
            email = input("Ingrese su email: ")
            contrasena = input("ingrese su contraseña: ")
    
    if(estudianteActual != -1):
        modo = "estudiante"
        menuIterativo(estudianteActual,datosPersonales,moderadorIngreso,estudiantesIngreso,modo,cantEstudiantesActivos)        
    elif(moderadorActual != -1):
        modo = "moderador"
        menuIterativo(moderadorActual, datosPersonales,moderadorIngreso,estudiantesIngreso,modo)
    else:
        clearConsole()
        print("Intentalo mas tarde nuevamente")
        
def inicializacion(cantEstudiantesActivos,cantModeradoresActivos,moderadorIngreso,estudiantesIngreso):
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
    ingreso(cantEstudiantesActivos)

        
inicializacion(cantEstudiantesActivos,cantModeradoresActivos,moderadorIngreso,estudiantesIngreso)
