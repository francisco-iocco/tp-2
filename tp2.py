'''Lucas Michelini, Francisco Iocco, Sebastian Gonzales, Joaquin Benitez'''
import random
import os
from datetime import datetime
from math import factorial

matriz = [[random.randint(0,1)for _ in range(8)] for _ in range(8)]
likes = [[0]*7 for _ in range(7)]
def clearConsole():
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)
clearConsole()
estudiantesIngreso = [["lucas","123","ACTIVO"],
                      ["pepe","123","ACTIVO"],
                      ["sebastiangonzales@gmail.com","123","ACTIVO"],
                      ["","","INACTIVO"],
                      ["","","INACTIVO"],
                      ["","","INACTIVO"],
                      ["","","INACTIVO"],
                      ["","","INACTIVO"]]

moderadoresIngreso = [["moderador1@gmail.com","123","ACTIVO"],
                    ["2","2","ACTIVO"],
                    ["","",""],
                    ["","",""]]

datosPersonales = [["Lucas Michelini","2005-06-04","M","Rellenar","Progamacion competitiva,gimanasio,leer"],
                   ["pepe","Vacio","Vacio","Vacio","Vacio"],
                   ["Sebastian Gonzales","Vacio","Vacio","Vacio","Vacio"],
                   ["Joaquin Benitez","Vacio","Vacio","Vacio","Vacio"],
                   ["1","Vacio","Vacio","Vacio","Vacio"],
                   ["Vacio","Vacio","Vacio","Vacio","Vacio"],
                   ["Vacio","Vacio","Vacio","Vacio","Vacio"],
                   ["Vacio","Vacio","Vacio","Vacio","Vacio"]]
def registrar(nuevoUsuario,tipoUsuario):
    if(tipoUsuario == 1):
        if(nuevoUsuario <= 7):
            clearConsole()
            print("MENU DE REGISTRO")
            email = input("Ingrese su email: ")
            contrasena = input("ingrese su contraseña: ")
            estudiantesIngreso[nuevoUsuario][0] = email
            estudiantesIngreso[nuevoUsuario][1] = contrasena
            estudiantesIngreso[nuevoUsuario][2] = "ACTIVO"
            for i in range(5):
                datosPersonales[nuevoUsuario][i] = "Vacio"
    elif(tipoUsuario == 2):
        if(nuevoUsuario <= 3):
            clearConsole()
            print("MENU DE REGISTRO")
            email = input("Ingrese su email: ")
            contrasena = input("ingrese su contraseña: ")
            estudiantesIngreso[nuevoUsuario][0] = email
            estudiantesIngreso[nuevoUsuario][1] = contrasena
            estudiantesIngreso[nuevoUsuario][2] = "ACTIVO"
            

def login(email, contrasena):
    perfilID = -1
    modo = -1
    salirDelMenu = False 
    for i in range(8):
        if(email == estudiantesIngreso[i][0] and 
           contrasena == estudiantesIngreso[i][1] and 
           estudiantesIngreso[i][2] == "ACTIVO"):
            perfilID = i
            modo = 0
            salirDelMenu = menuIterativo(perfilID,modo)
        if(i < 4 and (email == moderadoresIngreso[i][0] and
                      contrasena == moderadoresIngreso[i][1])):
            perfilID = i
            modo = 1
            menuIterativo(perfilID,modo)
    if(salirDelMenu):
        return salirDelMenu
    return perfilID


def correcion(inicio):
    while(inicio != "LOGIN" and inicio != "REGISTRARSE" and inicio != "SALIR" and inicio != '1' and inicio != '2'):
        clearConsole()
        print("Opcion no valida\nporfavor ingrese una de las siguientes opciones")
        inicio = input("-LOGIN\n-REGISTRARSE\n-SALIR\n-1)Bonus Track 1\n-2)Bonus Track 2\nIngrese su opcion: ").upper()
    return inicio

def cantidadMinimaNoCompletada(cEA,cMA):
    print("Necesita haber un minimo de [",cEA,"/4] estudiantes y [",cMA,"/1] modereadores")
    inicio = input("-LOGIN\n-REGISTRARSE\n-SALIR\n-1)Bonus Track 1\n-2)Bonus Track 2\nIngrese su opcion: ").upper()
    inicio = inicio.upper()
    inicio = correcion(inicio)
    return inicio        

def ingreso():
    clearConsole()
    email = input("Ingrese su email: ")
    contrasena = input("ingrese su contraseña: ")
    contIntentos = 1
    perfilID = login(email, contrasena)
    while(contIntentos < 3 and perfilID == -1):
        contIntentos += 1
        clearConsole()
        print("Email o contraseña no encontrados")
        email = input("Ingrese su email: ")
        contrasena = input("ingrese su contraseña: ")
        perfilID = login(email, contrasena)
    return perfilID

cantEstudiantesActivos = 0
cantModeradoresActivos = 0

def contarEstudiantes():
    global cantEstudiantesActivos
    i = 0
    
    while(i < 8 and estudiantesIngreso[i][2] == "ACTIVO"):
        i +=1
    cantEstudiantesActivos = i

def ordenarEstudiantes():
    for i in range(8):
        if(estudiantesIngreso[i][2] == "INACTIVO"):
            cambio = False
            j=i
            listaTEmail = ["","",""]
            listaTDatos = ["","",""]
            listaTEmail = estudiantesIngreso[i]
            listaTDatos = datosPersonales[i]
            while(j <= 7 and estudiantesIngreso[j][2]!="ACTIVO"):
                j+=1
            if(j<8):
                estudiantesIngreso[i] = estudiantesIngreso[j]
                datosPersonales[i] = datosPersonales[j]
                estudiantesIngreso[j] = listaTEmail
                datosPersonales[j] = listaTDatos
    contarEstudiantes()

def edades():
    clearConsole()
    edades = [21, 18, 20, 19, 23, 24]
    for i in range(6):
        for j in range(i+1, 5):
            if(edades[i] > edades[j]):
                temp = edades[i]
                edades[i] = edades[j]
                edades[j] = temp
    clearConsole()
    for i in range(5):
        if(edades[i]+1 != edades[i+1]):
            print("El elemento (edad) faltante es:", edades[i]+1,"\n")
def bonus2():
    ordenarEstudiantes()
    posiciones = (cantEstudiantesActivos*cantEstudiantesActivos)-cantEstudiantesActivos
    numerador = factorial(posiciones)
    denominador = factorial(2) * factorial((posiciones-2))
    posibleMatcheo = numerador // denominador
    clearConsole()
    print(f"La posibles matcheos son: {posibleMatcheo}\n")
               
def incializacion(inicio):
    global cantEstudiantesActivos
    global cantModeradoresActivos
    ordenarEstudiantes()
    while((inicio != "LOGIN" and inicio != "SALIR" and inicio != '1' and inicio != '2')or (cantEstudiantesActivos <4 and cantModeradoresActivos < 1)):
        if(inicio == "LOGIN"):
            clearConsole()
            inicio = cantidadMinimaNoCompletada(cantEstudiantesActivos,cantModeradoresActivos)
        elif(inicio == "REGISTRARSE"):
            ordenarEstudiantes()
            tipoDeUsuarioARegistrar = 0
            while(tipoDeUsuarioARegistrar == 0):
                clearConsole()
                tipoDeUsuarioARegistrar = int(input("1-Estudiante\n2-Moderador\nOpcion: "))
                if(tipoDeUsuarioARegistrar == 1):
                    if(cantEstudiantesActivos < 8):
                        registrar(cantEstudiantesActivos,tipoDeUsuarioARegistrar)
                        cantEstudiantesActivos += 1
                        clearConsole()
                        print("Usuario ingresado correctamente")
                    else:
                        clearConsole()
                        print("Cantidad maxima de alumnos alcanzada")
                elif(tipoDeUsuarioARegistrar == 2):
                    if(cantModeradoresActivos < 4):
                        moderadoresIngreso = registrar(moderadoresIngreso,cantModeradoresActivos,tipoDeUsuarioARegistrar)
                        cantModeradoresActivos += 1
                        clearConsole()
                        print("Usuario ingresado correctamente")
                    else:
                        clearConsole()
                        print("Cantidad maxima de moderadores alcanzada")
                elif(tipoDeUsuarioARegistrar != 1 and tipoDeUsuarioARegistrar != 2):
                    tipoDeUsuarioARegistrar = 0
                    print("opcion no valida\n")

            inicio = input("-LOGIN\n-REGISTRARSE\n-SALIR\n-1)Bonus Track 1\n-2)Bonus Track 2\nIngrese su opcion: ").upper()
            inicio = inicio.upper()
            inicio = correcion(inicio)
            
    if(inicio == '1'):
        edades()
        return True
    elif(inicio == '2'):
        bonus2()
        return True
    elif(inicio == "SALIR"):
        clearConsole()
        print("Gracias por usar nuestro progama")
        return False
    if(inicio ==  "LOGIN"):
        perfilID = ingreso()
        
    if(perfilID == -1): 
        clearConsole()
        print("\nLimite de intetos superado")
        return False
    elif(perfilID == True):
        return True
    if(inicio == "SALIR"):
        clearConsole()
        print("Gracias por usar nuestro progama")
        return False
    
reportes = [[-1]*8 for _ in range(8)]
motivos = [[""]*8 for _ in range(8)]

def mostrarEstudiantes():
    for i in range(cantEstudiantesActivos):
        print("-----Estudiante",i,"------")
        for j in range(5):
            print(datosPersonales[i][j])
            
def verCandidatos(usuario):
    mostrarEstudiantes()
    matcheo = ""
    while matcheo != "NO":
        matcheo = input("\n¿Quieres dar matcheo? (SI/NO): ")
        matcheo = matcheo.upper()
        clearConsole()
        
        if(matcheo != "SI" and matcheo != "NO"):
            clearConsole()
            for i in range(cantEstudiantesActivos):
                print("-----Estudiante",i,"------")
                for j in range(5):
                    print(datosPersonales[i][j])
            print("\nOpcion inválida.")
        elif(matcheo == "SI"):
            clearConsole()
            mostrarEstudiantes()
            meGusta = input("\n¿Quien te gusta? (nombre y apellido): ")
            existe = False
            for i in range(cantEstudiantesActivos):
                if(meGusta == datosPersonales[i][0]):
                    existe = True
            if(existe):
                for i in range(cantEstudiantesActivos):
                    if(datosPersonales[i][0] == meGusta and i != usuario):
                        if(matriz[usuario][i] == 1):
                            clearConsole()
                            print("\nYa has dado like a este usuario\n")
                        else:
                            matriz[usuario][i] = 1
                            clearConsole()
                            print("Usuario likeado correctamente\n")
                    elif(datosPersonales[i][0] == meGusta and i == usuario):
                        clearConsole()
                        print("No te puedes dar like a ti mismo\n")
            else:
                clearConsole()
                print("Usuario Inexistente\n")

def editarDatos(x):
    datoCambiar=-1
    while(int(datoCambiar) != 0):
        for i in range(5):
            if(datosPersonales[x][i]): print("-", datosPersonales[x][i])
        datoCambiar = -1         
        print("Que dato quiere cambiar?\n\t1-Nombre\n\t2-Edad\n\t3-Sexo\n\t4-Biografia\n\t5-Hobbies\n\t(0)-salir")
        datoCambiar = input("Ingrese una opción: ")
        clearConsole()
        if(datoCambiar.isdigit() and int(datoCambiar) >= 0 and int(datoCambiar) <= 5):
            match int(datoCambiar):
                case 1:
                    nuevoNombre = input("Ingrese su nuevo nombre: ")
                    datosPersonales[x][0] = nuevoNombre
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
                    datosPersonales[x][1] = fechaN
                case 3:
                    nuevoSexo = input("ingrese su nuevo sexo: ")
                    datosPersonales[x][2] = nuevoSexo
                case 4:
                    nuevaBiografia = input("ingrese su nueva biografia: ")
                    datosPersonales[x][3] = nuevaBiografia
                case 5:
                    nuevosHobbies = input("ingrese sus nuevo hobbies: ")
                    datosPersonales[x][4] = nuevosHobbies
            clearConsole()
            if(datoCambiar != '0'):
                print("La información se ha guardado correctamente!")
        else:
            clearConsole()
            print("Por favor, elija una opción del menu")


def reportesEstadisticos(usuario):
    cont=0
    cont2=0
    cont3=0
    for i in range(cantEstudiantesActivos):
        if(matriz[usuario][i] == matriz[i][usuario]):
            cont+=1
        if(matriz[usuario][i] == 1 and matriz[i][usuario] == 0 ):
            cont2+=1
        if(matriz[usuario][i] == 0 and matriz[i][usuario] == 1 ):
            cont3+=1
    print("-Haz hecho match con el",(cont*100)//cantEstudiantesActivos,"%")
    print("-Likes dados y no recibidos",cont2)
    print("-Likes recibidos y no dados",cont3,"\n")
    
def crearReporte(denunciante, reportado):
    clearConsole()
    motivo = input("Ingrese el motivo de su reporte: ")
    reportes[denunciante][reportado] = 0
    motivos[denunciante][reportado] = motivo
     
def reportarEstudiante(usuario):
    for i in range(cantEstudiantesActivos):
        print(f"{i}-{datosPersonales[i][0]}")
    reportado = input("\nID o nombre del usuario reportado: ")
    digito = reportado.isdigit()
    if(not(digito)):
        i = 0
        while(datosPersonales[i][0] != reportado and i <= 7):
            i+=1
        reportado = i
    if(int(reportado)<=7 and int(reportado) != usuario):
        crearReporte(usuario,int(reportado))
        clearConsole()
        print(f"ID del reportante: {usuario} -ID del reportado: {reportado} - {motivos[usuario][int(reportado)]} -Estado 0.")
    elif(int(reportado) == usuario):
        clearConsole()
        print("No te podes reportar a vos mismo\n")
    else:
        clearConsole()
        print("Usuario a reportar no encontrado\n")
    
def menuPrincipalE(x):
    print("MENU PRINCIPAL\n")
    print("1-Gestionar Perfil")
    print("2-Gestionar Canditos")
    print("3-Matcheos")
    print("4-Reportes estadisticos")
    print("0-Salir")

def menuPrincipalM(usuario):
    print("1-Gestionar Usuario")
    print("2-Ver reportes")
    
def menu1mod(x):
    print("1-Gestionar Usuario")
    print("\ta.Desactivar Usuario")
    print("\tb.Volver")
    
def menu2mod(x):
    print("1-Gestionar Reportes")
    print("\ta.Ver reportes")
    print("\tb.Volver")
    
def cartel():
    print("en construccion")
    
def idEstudiante(nombre):
    i = 0
    while(estudiantesIngreso[i][0] != nombre): i+=1
    if(estudiantesIngreso[i][0] == nombre): return i
    return -1            

def verReportes():
    for i in range(8):
        for j in range(7):
            if(reportes[i][j] == 0 and estudiantesIngreso[i][2] == "ACTIVO" and estudiantesIngreso[j][2] == "ACTIVO"):
                clearConsole()
                print(f"ID del reportante: {i}\nID del reportado: {j}\nMotivo: {motivos[i][j]}.\n")
                opc2 = input("1- Ignorar reporte | 2- Bloquear al reportante: ")
                if(not(opc2.isdigit()) and int(opc2) != 1 and int(opc2) != 2):
                    print("Por favor, ingrese una opción válida.")
                elif(int(opc2) == 1):
                    reportes[i][j] = 2
                else:
                    reportes[i][j] = 1
                    estudiantesIngreso[j][2] == "INACTIVO"

def desactivarUsuario():
    encontrado = False
    while(not(encontrado)):
        clearConsole()
        for i in range(8):
            if(estudiantesIngreso[i][0]):       
                print("ID:", i)
                print("Nombre:", estudiantesIngreso[i][0])
                print("Estado:", estudiantesIngreso[i][2], "\n")
        opc2 = input("Ingrese el ID o el nombre del usuario a eliminar: ")
        if(not(opc2.isdigit()) and idEstudiante(int(opc2)) != -1):
            eliminarDatos(idEstudiante(int(opc2)))
            encontrado = True
        elif(opc2.isdigit() and int(opc2) >= 0 and int(opc2) <= 7):
            eliminarDatos(int(opc2))  
            encontrado = True
        else:
            print("Por favor, ingrese un ID o nombre válido.")
def eliminarDatos(x):
    for i in range(3):
        print(estudiantesIngreso[x][i])
    confirm =input("\nSeguro que quiere eliminar este perfir[SI/NO]")
    confirm = confirm.upper()
    clearConsole()
    while(confirm != "SI" and confirm != "NO"):
        print("Porfavor ingrese SI o no")
        confirm =input("Seguro que quiere eliminar este perfir[SI/NO]")    
        confirm = confirm.upper()
        clearConsole()
    if(confirm == "SI"):
        estudiantesIngreso[x][2] = "INACTIVO"
        clearConsole()
        print("Perfil eliminiado\n")
        ordenarEstudiantes
        return True
            
def subMenuE(opc, usuario,salirDelMenu):
    opc2 = ""
    while(opc2 != "c" and not(salirDelMenu)):
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
                if(opc2 == "a"): editarDatos(usuario)
                elif(opc2 == "b"): salirDelMenu = eliminarDatos(usuario)
            case 2:
                clearConsole()
                if(opc2 == "a"): verCandidatos(usuario)
                elif(opc2 == "b"): reportarEstudiante(usuario)
            case 3:
                if(opc2 == "a"): cartel()
                elif(opc2 == "b"): cartel()
    if(salirDelMenu):
        return salirDelMenu
                
def subMenuM(opc, usuario):
    opc2 = ""
    while(opc2 != "b"):
        match int(opc):
            case 1:
                print("1-Gestionar Usuario")
                print("\ta.Desactivar Usuario")
                print("\tb.Volver")
            case 2:
                print("1-Gestionar Usuario")
                print("\ta.Ver reportes")
                print("\tb.Volver")
        opc2 = input("\nIngrese su opción: ")
        clearConsole()
        if(opc2 != "a" and opc2 != "b" and opc2 !="c"): print("Opción invalida - Ingrese su opcion nuevamente\n")
        match int(opc):
            case 1:
                if(opc2 == "a"): desactivarUsuario()
            case 2:
                clearConsole()
                if(opc2 == "a"): verReportes()
                
def menuIterativo(usuario, modo):
    clearConsole()
    opc = ""
    salirDelMenu = False
    if(modo == 0):
        while(opc != '0' and not(salirDelMenu)):
            menuPrincipalE(usuario)
            opc = input("\nIngrese su opción: ")
            clearConsole()
            if(not(opc.isdigit()) or not(int(opc) >= 0 and int(opc) <= 4)): print("\nPor favor, ingrese un opción valida.\n")
            elif(opc == "4"): reportesEstadisticos(usuario)
            elif(opc == "0"): salirDelMenu = True
            else: salirDelMenu = subMenuE(opc, usuario, salirDelMenu)
    if(modo == 1):
        while(opc != '0'):
            menuPrincipalM(usuario)
            opc = input("\nIngrese su opción: ")
            clearConsole()
            if(not(opc.isdigit()) or not(int(opc) >= 0 and int(opc) <= 2)): print("\nPor favor, ingrese un opción valida.\n")
            elif(opc == "0"): salirDelMenu = True
            else: subMenuM(opc, usuario)
    if(salirDelMenu):
        return salirDelMenu
    
prendido = True
while(prendido):
    inicio = input("-LOGIN\n-REGISTRARSE\n-SALIR\n-1)Bonus Track 1\n-2)Bonus Track 2\nIngrese su opcion: ").upper()
    inicio = correcion(inicio)
    prendido = incializacion(inicio)