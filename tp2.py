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
            