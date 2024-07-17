while(inicio == "LOGIN" and not(Logueo(cantEstudiantesActivos,cantModeradoresActivos))):
        print("Necesita ingresar mas estudiantes[",cantEstudiantesActivos,"/4] o modereadores[",cantModeradoresActivos,"/1]")
        inicio = input("LOGIN/REGISTRARSE")
        inicio = inicio.upper   
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
            elif(email == moderadorIngreso[i][0] and
                contrasena == moderadorIngreso[i][1] and
                moderadorIngreso[i][2] == "ACTIVO"):
                moderadorActual = i
                estudianteActual = -1
            else:
                contIntentos+=1

    print(estudianteActual, moderadorActual)
