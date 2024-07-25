def desactivarUsuario(email, baseDePerfiles):
    for i in range(len(baseDePerfiles)):
        if email == baseDePerfiles[i][0]:
            baseDePerfiles[i][2] = "INACTIVO"
            return True
    return False

def subMenu1Mod(usuario, moderadorIngreso):
    clearConsole()
    opc1 = ""
    while opc1 != "b":
        menu1mod(usuario, moderadorIngreso)
        opc1 = input("\nIngrese su opción: ")
        clearConsole()
        if opc1 != "a" and opc1 != "b":
            clearConsole()
            print("Opción inválida - Ingrese su opción nuevamente\n")
        elif opc1 == "a":
            email = input("Ingrese el email del usuario a desactivar: ")
            if desactivarUsuario(email, estudiantesIngreso) or desactivarUsuario(email, moderadorIngreso):
                clearConsole()
                print("Usuario desactivado correctamente")
            else:
                clearConsole()
                print("Usuario no encontrado")
# Datos iniciales para los reportes
reportes = [
    {"reportante": "estudiante1@gmail.com", "reportado": "estudiante2@gmail.com", "estado": 0},
    {"reportante": "estudiante3@gmail.com", "reportado": "estudiante4@gmail.com", "estado": 0},
    {"reportante": "estudiante5@gmail.com", "reportado": "estudiante6@gmail.com", "estado": 1},
]


def verReportes():
    for reporte in reportes:
        if reporte["estado"] == 0:
            if (reporte["reportante"] in [perfil[0] for perfil in estudiantesIngreso] and 
                reporte["reportado"] in [perfil[0] for perfil in estudiantesIngreso]):
                
                print(f"Reporte de {reporte['reportante']} contra {reporte['reportado']}")
                print("1. Ignorar reporte")
                print("2. Bloquear al reportante")
                opcion = input("Ingrese su opción: ")
                
                if opcion == "1":
                    reporte["estado"] = 2
                elif opcion == "2":
                    reporte["estado"] = 1
                    desactivarUsuario(reporte["reportado"])
                
def subMenu2Mod(usuario, moderadorIngreso):
    clearConsole()
    opc2 = ""
    while opc2 != "b":
        menu2mod(usuario, moderadorIngreso)
        opc2 = input("\nIngrese su opción: ")
        clearConsole()
        if opc2 != "a" and opc2 != "b":
            clearConsole()
            print("Opción inválida - Ingrese su opción nuevamente\n")
        elif opc2 == "a":
            verReportes()
