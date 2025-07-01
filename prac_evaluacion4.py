estudiantes = {}

def registrar_estudiante(lst_estudiantes: dict, rut: str, nombre: str) -> bool:
    
    if rut in lst_estudiantes:
        print("[ERROR] Este estudiante ya se encuentra registrado, vuelva a intentarlo.")
        return False

    lst_estudiantes[rut] = {
        "nombre": nombre,
        "sesiones": []
    }

    return True

def registrar_participacion(lst_estudiantes: dict, rut: str, puntaje: int) -> bool:
    if rut not in lst_estudiantes:
        print("[ERROR] El RUT del usuario ingresado no es valido, vuelva a intentarlo.")
        return False
    if puntaje <= 0:
        print("No se puede agregar puntaje negativo o igual a cero, vuelva a intentarlo.")
        return False
    
    lst_estudiantes[rut]["sesiones"].append(puntaje)
    print("* Puntaje agregado con exito")
    return True
    
def actualizar_participacion(lst_estudiantes: dict, rut: str, sesion: int, nuevo_puntaje: int) -> bool:
    if rut not in lst_estudiantes:
        print("[ERROR] El RUT del usuario ingresado no es valido, vuelva a intentarlo.")
        return False

    sesiones = lst_estudiantes[rut]["sesiones"]

    if nuevo_puntaje < 0:
        print("[ERROR] El valor minimo admitido es cero, vuelva a intentarlo.")
        return False
        
    try:
        sesiones[sesion - 1] = nuevo_puntaje
    except IndexError:
        print("[ERROR] La sesion ingresada no existe, vuelva a intentarlo.")

    print(f"* El puntaje de la sesion {sesion} de {lst_estudiantes[rut]["nombre"]} ha sido modificado con exito.")
    return True

activo = True
while activo:
    try:
        print("1.- Registrar estudiante")
        print("2.- Registrar puntaje por sesion")
        print("3.- Modificar puntaje de estudiante por sesion")
        print("4.- Ver total acumulado y el promedio de puntajes por estudiante")
        print("5.- Mostrar estudiantes con baja participacion")
        print("6.- Listar todos estudiantes con sus datos y puntajes")
        print("7.- Eliminar estudiante")
        print("0.- Cerrar programa.")
        opcion = int(input("- Seleccione una opcion del 0 al 7: "))

        if opcion == 1:
            rut = input("- Rut: ").lower()
            nombre = input("- Nombre: ")
            registrar_estudiante(estudiantes, rut, nombre)
            

        elif opcion == 0:
            activo = False
            print("* Programa cerrado con exito.")
    except KeyboardInterrupt:
        print("\n[ERROR] Por favor cierre el programa con la opcion indicada.")
    except ValueError:
        print("[ERROR] Asegurese de que el valor escrito sea el indicado, ya sea palabra o numero.")