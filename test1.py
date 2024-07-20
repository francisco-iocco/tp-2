def registrar(baseDePerfiles,nuevoUsuario):
    email = input("Ingrese su email: ")
    contrasena = input("ingrese su contraseña: ")
    baseDePerfiles[nuevoUsuario][0] = email
    baseDePerfiles[nuevoUsuario][1] = contrasena
    baseDePerfiles[nuevoUsuario][2] = "ACTIVO"
    return baseDePerfiles
    
    
inicio = input("-LOGIN\n-REGISTRARSE\nIngrese su opcion:")
inicio = inicio.upper()

if(not(inicializacion(cantEstudiantesActivos,cantModeradoresActivos,inicio))):
    clearConsole()
    print("Necesita haber minimo estudiantes[",cantEstudiantesActivos,"/4] y modereadores[",cantModeradoresActivos,"/1]")
    inicio = input("-LOGIN\n-REGISTRARSE\nIngrese su opcion:")
    inicio = inicio.upper()
    #HACER UNA FUNCION PARA REGISTRAR ESTUDIANTES'''


while(inicializacion(cantEstudiantesActivos,cantModeradoresActivos,inicio)):
    tipoDeUsuarioARegistrar = 0
    while(tipoDeUsuarioARegistrar == 0):
        clearConsole()
        tipoDeUsuarioARegistrar = int(input("1-Estudiante\n2-Moderador\nOpcion: "))
        
        if(tipoDeUsuarioARegistrar == 1 and cantEstudiantesActivos < 8):
            estudiantesIngreso = registrar(estudiantesIngreso,cantEstudiantesActivos)
            cantEstudiantesActivos += 1
            clearConsole()
            print("Usuario ingresado correctamente")
        elif(tipoDeUsuarioARegistrar == 2 and cantModeradoresActivos < 4):
            moderadorIngreso = registrar(moderadorIngreso,cantModeradoresActivos)
            cantModeradoresActivos += 1
            clearConsole()
            print("Usuario ingresado correctamente")
        elif(tipoDeUsuarioARegistrar != 1 and tipoDeUsuarioARegistrar != 2):
            tipoDeUsuarioARegistrar = 0
            clearConsole()
            print("opcion incorrecta, ingrese nuevamente\n")        
        elif(cantEstudiantesActivos == 8):
            clearConsole()
            print("Cantidad maxima de alumnos")
        elif(cantModeradoresActivos == 4):
            clearConsole()
            print("Cantidad maxima de moderadores\n")
