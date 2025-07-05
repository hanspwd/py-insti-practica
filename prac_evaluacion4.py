estudiantes = {}

def registrar_estudiante(lst_estudiantes: dict, rut: str, nombre: str) -> bool:
    
    if rut in lst_estudiantes:
        print("[ERROR] Este estudiante ya se encuentra registrado, vuelva a intentarlo.")
        return False

    lst_estudiantes[rut] = {
        "nombre": nombre,
        "sesiones": []
    }
    print(f"* Nuevo estudiante agregado con exito")
    return True

def registrar_participacion(lst_estudiantes: dict, rut: str, puntaje: int) -> bool:
    if rut not in lst_estudiantes:
        print("[ERROR] El RUT del usuario ingresado no existe, vuelva a intentarlo.")
        return False
    if puntaje <= 0:
        print("No se puede agregar puntaje negativo o igual a cero, vuelva a intentarlo.")
        return False
    
    lst_estudiantes[rut]["sesiones"].append(puntaje)
    print("* Puntaje agregado con exito")
    return True
    
def actualizar_participacion(lst_estudiantes: dict, rut: str, sesion: int, nuevo_puntaje: int) -> bool:
    if rut not in lst_estudiantes:
        print("[ERROR] El RUT del usuario ingresado no existe, vuelva a intentarlo.")
        return False

    sesiones = lst_estudiantes[rut]["sesiones"]

    if nuevo_puntaje < 0:
        print("[ERROR] El valor minimo admitido es cero, vuelva a intentarlo.")
        return False
        
    try:
        sesiones[sesion - 1] = nuevo_puntaje
    except IndexError:
        print("[ERROR] La sesion ingresada no existe, vuelva a intentarlo.")
        return False

    print(f"* El puntaje de la sesion {sesion} de {lst_estudiantes[rut]["nombre"]} ha sido modificado con exito.")
    return True

def calcular_total_y_promedio(lst_estudiantes: dict, rut: str) -> tuple[int, float]:
    if rut not in lst_estudiantes:
        print("[ERROR] El RUT del usuario ingresado no existe, vuelva a intentarlo.")
        return 0, 0.0

    if not lst_estudiantes[rut]["sesiones"]:
        print("[ERROR] No hay sesiones existentes registradas en este estudiante, vuelva a intentarlo luego de haberle agregado al menos una sesion.")
        return 0, 0.0
    
    sesiones = lst_estudiantes[rut]["sesiones"]
    total: int = sum(sesiones)
    promedio: float = total / len(sesiones)
    
    return total, promedio


def mostrar_estudiantes(lst_estudiantes: dict) -> None:
    
    aviso = ""
    
    for estudiante, datos in lst_estudiantes.items():

        sesiones = datos["sesiones"]

        if not sesiones:
            aviso += f"[Aviso] Estudiante {estudiante} no tiene puntajes aún, por lo tanto no tiene promedio ni total.\n".strip()
            continue

        total = sum(sesiones)
        promedio = total / len(sesiones)

        print("-------------------------------------------")
        print("Rut:", estudiante)
        print("Nombre:", datos["nombre"])
        print("Total puntos:", total)
        print("Promedio:", promedio)

        if aviso:
            print("-------------------------------------------")
            print(aviso)

    print("-------------------------------------------")
    return None
#Muestra para cada estudiante su RUT, nombre, total acumulado y promedio de puntos

def participacion_baja(lst_estudiantes: dict, umbral: float) -> None:
#Muestra estudiantes con promedio de puntaje por debajo del umbral entregado.
    return None

activo = True
while activo:
    try:
        print("1.- Registrar estudiante")
        print("2.- Registrar puntaje por sesion")
        print("3.- Modificar puntaje de estudiante por sesion")
        print("4.- Ver total acumulado y el promedio de puntajes por estudiante")
        # LOS DE ABAJO AUN NO HAN SIDO IMPLEMENTADOS
        print("5.- Mostrar estudiantes con baja participacion")
        print("6.- Listar todos estudiantes con sus datos y puntajes")
        print("7.- Eliminar estudiante")
        print("0.- Cerrar programa.")
        opcion = int(input("- Seleccione una opcion del 0 al 7: "))

        if opcion == 1:
            rut = input("+ Rut: ").lower()
            nombre = input("+ Nombre: ")
            registrar_estudiante(estudiantes, rut, nombre)
        
        elif opcion == 2:
            rut = input("+ Rut: ").lower()
            puntaje = int(input("+ Puntaje: "))
            registrar_participacion(estudiantes, rut, puntaje)
        elif opcion == 3:
            rut = input("+ Rut: ").lower()
            sesion = int(input("+ Sesion a cambiar: "))
            nuevo_puntaje = int(input("+ Nuevo puntaje: "))
            actualizar_participacion(estudiantes, rut, sesion, nuevo_puntaje)
        elif opcion == 4:
            rut = input("+ Rut: ").lower()
            
            total, promedio = calcular_total_y_promedio(estudiantes, rut)
            
            if total > 0 or promedio > 0:
                print("-------------------------------------------")
                print(f"Nombre: {estudiantes[rut]["nombre"]}")
                print(f"Total: {total}")
                print(f"Promedio: {promedio:.2f}")
                print("-------------------------------------------")

        elif opcion == 5:
            mostrar_estudiantes(estudiantes)
        elif opcion == 0:
            activo = False
            print("* Programa cerrado con exito.")
    except KeyboardInterrupt:
        print("\n[ERROR] Por favor cierre el programa con la opcion indicada.")
    except ValueError:
        print("[ERROR] Asegurese de que el valor escrito sea el indicado, ya sea palabra o numero.")