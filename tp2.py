'''Lucas Michelini, Francisco Iocco, Sebastian Gonzales, Joaquin Benitez'''
import random
import os
from datetime import datetime

matriz = [[random.randint(0,1)] * 7 for _ in range(7)]
def clearConsole():
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)
clearConsole()
estudiantesIngreso = [["lucas","123","ACTIVO"],
                      ["franciscoiocco@gmail.com","123","ACTIVO"],
                      ["sebastiangonzales@gmail.com","123","ACTIVO"],
                      ["joaquinbenitez@gmail.com","123","ACTIVO"],
                      ["1","1","ACTIVO"],
                      ["","",""],
                      ["","",""],
                      ["","",""]]
moderadoresIngreso = [["moderador1@gmail.com","123","ACTIVO"],
                    ["2","2","ACTIVO"],
                    ["","",""],
                    ["","",""]]
cantEstudiantesActivos = 5
cantModeradoresActivos = 2
datosPersonales = [["Lucas Michelini","2005-06-04","M","Rellenar","Progamacion competitiva,gimanasio,leer"],
                   ["Francisco Iocco","15","M","Rellenar","Rellenar"],
                   ["Sebastian Gonzales","14","M","Rellenar","Rellenar"],
                   ["Joaquin Benitez","29","M","Rellenar","Rellenar"],
                   ["","","","",""],
                   ["","","","",""],
                   ["","","","",""],
                   ["","","","",""]]

def editarDatos(x,datos):
    for i in range(5):
        if(datos[x][i]): print("-", datos[x][i])
    datoCambiar = -1         
    while(int(datoCambiar) != 0):
        #imprime el submenu de a-editar datos personales
        print("Que dato quiere cambiar?\n\t1-Nombre\n\t2-Edad\n\t3-Sexo\n\t4-Biografia\n\t5-Hobbies\n\t(0)-salir")
        datoCambiar = input("Ingrese una opción: ")
        clearConsole()
        if(datoCambiar.isdigit() and int(datoCambiar) >= 1 and int(datoCambiar) <= 5):
            match int(datoCambiar):
                case 1:
                    nuevoNombre = input("Ingrese su nuevo nombre: ")
                    datos[x][0] = nuevoNombre
                case 2:
                    fechaN = input("ingrese su fecha de nacimiento (YYYY-MM-DD): ")
                    partes = fechaN.split("-")
                    while(len(fechaN) != 10 or fechaN[4] != "-" or fechaN[4] != "-" or len(partes) != 3 or
                          not(partes[0].isdigit() and partes[1].isdigit() and partes[2].isdigit()) or
                          not(1 <= int(partes[1]) <= 12) or not(1 <= int(partes[2]) <= 31) or 
                          (int(partes[1]) in [4, 6, 9, 11] and int(partes[2]) > 30) or
                          (int(partes[1]) == 2 and int(partes[0])%4!=0 and int(partes[2]) > 28) or 
                          (int(partes[1]) == 2 and int(partes[0])%4==0 and int(partes[2]) > 29)):
                        print("El formato de la fecha es inválido.")
                        fechaN = input("ingrese su fecha de nacimiento (YYYY-MM-DD): ")
                        partes = fechaN.split("-")
                    datos[x][1] = fechaN
                case 3:
                    nuevoSexo = input("ingrese su nuevo sexo: ")
                    datos[x][2] = nuevoSexo
                case 4:
                    nuevaBiografia = input("ingrese su nueva biografia: ")
                    datos[x][3] = nuevaBiografia
                case 5:
                    nuevosHobbies = input("ingrese sus nuevo hobbies: ")
                    datos[x][4] = nuevosHobbies
            clearConsole()
            print("La información se ha guardado correctamente!")
        else:
            clearConsole()
            print("Por favor, elija una opción del menu")
    return datos

def menuPrincipalE(x, estudiante):
    print("MENU PRINCIPAL\n")
    print("1-Gestionar Perfil")
    print("2-Gestionar Canditos")
    print("3-Matcheos")
    print("4-Reportes estadisticos")
    print("0-Salir")

def menuPrincipalM():
    print("1-Gestionar Usuario")
    print("2-Ver reportes")
    
def menu1mod(x,moderador):
    print("1-Gestionar Usuario")
    print("\ta.Desactivar Usuario")
    print("\tb.Volver")
    
def menu2mod(x,moderador):
    print("1-Gestionar Usuario")
    print("\ta.Ver reportes")
    print("\tb.Volver")
        
def subMenuE(opc, usuario, datosPersonales):
    opc2 = ""
    while(opc2 != "c"):
        match int(opc):
            case 1: 
                print("1-Gestionar Perfil")
                print("\ta.Editar mis datos personales")
                print("\tb.Eliminar mi perfil")
                print("\tc.volver")
            case 2:
                print("2-Gestionar candidatos")
                print("\ta. Ver candidatos")
                print("\tb. Reportar un candidato")
                print("\tc. Volver")
            case 3:
                print("3-Matcheos")
                print("\ta. Ver matcheos")
                print("\tb. Eliminar un matcheo")
                print("\tc. Volver")
        opc2 = input("\nIngrese su opción: ")
        clearConsole()
        if(opc2 != "a" and opc2 != "b" and opc2 !="c"): print("Opción invalida - Ingrese su opcion nuevamente\n")
        match int(opc):
            case 1: 
                if(opc2 == "a"): editarDatos(usuario, datosPersonales)
                else: ""
            case 2:
                if(opc == "a"): ""
                else: ""
            case 3:
                if(opc2 == "a"): ""
                else: ""
        clearConsole()
    
def subMenu1Mod(usuario,moderadorIngreso):
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
                
def menuIterativo(usuario, datosPersonales, modo):
    opc = ""
    if(modo == 0):
        while(opc != '0'):
            menuPrincipalE(usuario,datosPersonales)
            opc = input("\nIngrese su opción: ")
            clearConsole()
            if(not(opc.isdigit()) or not(int(opc) >= 0 and int(opc) <= 4)): print("\nPor favor, ingrese un opción valida.\n")
            elif(opc == "4"): print("4-Reportes estadisticos\n\tEn construcción...")
            elif(opc == "0"): print("Gracias por usar nuestro programa!")
            else: subMenuE(opc, usuario, datosPersonales)
    if(modo == 1):
        while(opc != '0'):
            menuPrincipalM(usuario,moderadorIngreso)
            opc = input("\nIngrese su opción: ")
            clearConsole()
            if(not(opc.isdigit()) or not(int(opc) >= 0 and int(opc) <= 4)): print("\nPor favor, ingrese un opción valida.\n")
            else:
                match int(opc):
                    case 1: subMenu1Mod(usuario,moderadorIngreso)
                    case 2: subMenu2Mod(usuario,moderadorIngreso)
    
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
    
def login(email, contrasena):
    perfilID = -1
    modo = -1
    for i in range(8):
        if(email == estudiantesIngreso[i][0] and contrasena == estudiantesIngreso[i][1] and estudiantesIngreso[i][2] == "ACTIVO"):
            perfilID = i
            modo = 0
        if(i < 4 and (email == moderadoresIngreso[i][0] and contrasena == moderadoresIngreso[i][1])):
            perfilID = i
            modo = 1
    return [perfilID, modo]
    
def correcion(inicio):
    while(inicio != "LOGIN" and inicio != "REGISTRARSE"):
        clearConsole()
        print("Opcion no valida\nporfavor ingrese una de las siguientes opciones")
        inicio = input("-LOGIN\n-REGISTRARSE\nIngrese su opcion:").upper()
    return inicio

def cantidadMinimaNoCompletada(cEA,cMA):
    print("Necesita haber un minimo de [",cEA,"/4] estudiantes y [",cMA,"/1] modereadores")
    inicio = input("-LOGIN\n-REGISTRARSE\nIngrese su opcion:")
    inicio = inicio.upper()
    inicio = correcion(inicio)
    return inicio        

inicio = input("-LOGIN\n-REGISTRARSE\nIngrese su opcion:").upper()
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
        
clearConsole()
email = input("Ingrese su email: ")
contrasena = input("ingrese su contraseña: ")
contIntentos = 1
datosOperador = login(email, contrasena)
while(contIntentos < 3 and datosOperador[0]  == -1):
    if(datosOperador[0] == -1):
        contIntentos += 1
        clearConsole()
        print("Email o contraseña no encontrados")
        email = input("Ingrese su email: ")
        contrasena = input("ingrese su contraseña: ")
        datosOperador = login(email, contrasena)

clearConsole()
if(datosOperador[0] != -1): menuIterativo(datosOperador[0], datosPersonales, datosOperador[1])
else: print("Intentalo mas tarde nuevamente")
