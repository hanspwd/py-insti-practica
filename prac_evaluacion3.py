aventureros = {}

def registrar_aventurero(lst_aventureros: dict, codigo: str, datos: list) -> bool:
    if codigo in lst_aventureros:
        print(f"[ERROR] El codigo {codigo} ya existe, intentelo nuevamente.")
        return False
    if datos[1] < 0:
        print("[ERROR] Edad ingresada no valida, tiene que ser mayor a cero.")
        return False
    
    lst_aventureros[codigo] = {
        "nombre": datos[0],
        "edad": datos[1],
        "puntajes": []
    } 
    
    print("* El aventurero ha sido registrado exitosamente!")
    return True
    
def registrar_puntaje(lst_aventureros: dict, codigo: str, puntaje: int) -> bool:
        if codigo not in lst_aventureros:
            print("[ERROR] El codigo ingresado no existe, vuelva a intentarlo.")
            return False
        if puntaje < 0:
            print("[ERROR] El puntaje no puede ser negativo, vuelva a intentarlo.")
            return False

        lst_aventureros[codigo]["puntajes"].append(puntaje)
        print("* Puntaje agregado con exito")
        return True

def modificar_puntaje(lst_aventureros: dict, codigo: str, sesion: int, nuevo_puntaje: int) -> bool:
            if codigo not in lst_aventureros:
                print("[ERROR] El codigo ingresado no existe, vuelva a intentarlo.")
                return False
            
            puntajes = lst_aventureros[codigo]["puntajes"]
            
            if sesion < 0:
                print("[ERROR] El numero de sesion no puede ser negativo, vuelva a intentarlo.")
                return False
            if nuevo_puntaje < 0:
                print("[ERROR] Solo se puede ingresar puntaje mayor o igual a cero, no negativos, vuelva a intentarlo.")
                return False

            try:
                # SI NO HAY VALOR AL QUE CAMBIAR (SI NO EXISTE LA SESION)
                puntajes[sesion - 1] = nuevo_puntaje
            
            except IndexError:
                print("[ERROR] No se puede modificar la sesion ya que no existe.")
                return False
            
            print("* Puntaje modificado con exito")
            return True

def mostrar_participacion(lst_aventureros: dict):
    if not lst_aventureros:
        print("[ERROR] Asegúrese de que haya al menos un aventurero registrado para listar.")
        return False

    advertencias = ""

    for codigo, datos in lst_aventureros.items():
        puntajes = datos["puntajes"]

        if not puntajes:
            advertencias += f"[Advertencia] Aventurero {codigo} no tiene puntajes aún, por lo tanto no tiene promedio.\n".strip()
            continue

        total = sum(puntajes)
        promedio = total / len(puntajes)

        print(f"------------------------------------------")
        print(f"Código: {codigo}")
        print(f"Nombre: {datos['nombre']}")
        print(f"Puntaje Total: {total}")
        print(f"Promedio: {promedio:.2f}")

    if advertencias:
        print(f"------------------------------------------")
        print(advertencias)

    print(f"------------------------------------------")
    return True

def participantes_con_bajo_promedio(lst_aventureros: dict, umbral: float):
    advertencias = ""
    if not lst_aventureros:
        print("[ERROR] No hay aventureros para listar por umbral.")
        return False

    for codigo, datos in lst_aventureros.items():
        puntajes = datos["puntajes"]

        if not puntajes:
            advertencias += f"[Advertencia] Aventurero {codigo} no tiene puntajes aún, por lo tanto no tiene promedio.\n".strip()
            continue

        promedio = sum(puntajes) / len(puntajes)

        if promedio <= umbral:
            print(f"------------------------------------------")
            print(f"Codigo: {codigo}")
            print(f"Nombre: {datos["nombre"]}")
            print(f"Edad: {datos["edad"]}")
            print(f"Promedio: {promedio:.2f}")

    if advertencias:
        print("------------------------------------------")
        print(advertencias)

    print(f"------------------------------------------")
    return True
    

def listar_aventureros(lst_aventureros: dict):
    if not lst_aventureros:
        print("[ERROR] Asegurese de que haya al menos un aventurero registrado para listar.")
        return False
    
    for codigo, datos in lst_aventureros.items():
        print(f"------------------------------------------")
        print(f"Codigo: {codigo}")
        print(f"Nombre: {datos["nombre"]}")
        print(f"Edad: {datos["edad"]}")
        print(f"Puntajes: {datos["puntajes"]}")

    print(f"------------------------------------------")
    return True

def obtener_aventureros_por_edad(lst_aventureros: dict, edad: int):
    for codigo, datos in lst_aventureros.items():

        if edad == datos["edad"]:
            print(f"------------------------------------------")
            print(f"Código: {codigo}")
            print(f"Nombre: {datos['nombre']}")
            print(f"Edad: {datos['edad']}")
            print(f"Puntajes: {datos['puntajes']}")

        if edad != datos["edad"]:
            print("[ERROR] La edad ingresada no es valida o no existe en nuestros registros.")
            continue
        
    print(f"------------------------------------------")
    return True
        
def eliminar_aventurero(lst_aventureros: dict, codigo: str, confirmacion: bool):
        
        if codigo not in lst_aventureros and confirmacion:
            print("[ERROR] Se a cancelado la eliminacion del aventurero debido a que el codigo no existe, vuelva a intentarlo.")
            return False
        elif confirmacion:
            lst_aventureros.pop(codigo)
            print("* Aventurero eliminado con exito.")
        else:
            print("* Se a cancelado la eliminacion del aventurero.")
        return True

activo = True
while activo:
    try:
        print("1.- Registrar aventureros.")
        print("2.- Registrar puntajes obtenidos por sesión.")
        print("3.- Modificar puntaje.")
        print("4.- Visualizar el total acumulado y el promedio de puntajes por aventurero.")
        print("5.- Mostrar los aventureros con promedio por bajo del umbral.")
        print("6.- Listar todos los aventureros con sus datos y puntajes.")
        print("7.- Filtrar los aventureros por edad específica.")
        print("8.- Eliminar un aventurero.")
        print("0.- Cerrar programa.")
        opcion = int(input("- Seleccione una opcion del 0 al 8: "))

        if opcion == 1:
            codigo = input("- Codigo: ").lower()
            nombre = input("- Nombre: ")
            edad = int(input("- Edad: "))
            datos = [nombre, edad]
            registrar_aventurero(aventureros, codigo, datos)
        elif opcion == 2:
            codigo = input("- Codigo: ").lower()
            puntajeAgregar = int(input("- Puntaje a agregar: "))
            registrar_puntaje(aventureros, codigo, puntajeAgregar)
        elif opcion == 3:
            codigo = input("- Codigo: ").lower()
            sesion = int(input("- Sesion a cambiar: "))
            nuevoPuntaje = int(input("- Ingrese el nuevo puntaje: "))
            modificar_puntaje(aventureros, codigo, sesion, nuevoPuntaje)
        elif opcion == 4:
            mostrar_participacion(aventureros)
        elif opcion == 5:
            umbral = float(input("- Ingrese el umbral de promedio: "))
            participantes_con_bajo_promedio(aventureros, umbral)
        elif opcion == 6:
            listar_aventureros(aventureros)
        elif opcion == 7:
            edad = int(input("- Filtrar por edad: "))
            obtener_aventureros_por_edad(aventureros, edad)
        elif opcion == 8:
            aprobado = False
            codigo = input("- Código del aventurero a eliminar: ").lower()
            while True:
                confirmacion = input("- ¿Confirma esta operación? Escriba 'si' o 'no': ").lower()
                if confirmacion == "si":
                    aprobado = True
                    break
                elif confirmacion == "no":
                    aprobado = False
                    break
                else:
                    print("[ERROR] Valor inválido. Por favor, escriba exactamente 'si' o 'no'.")
                    
            eliminar_aventurero(aventureros, codigo, aprobado)
        elif opcion == 0:
            activo = False
            print("* Programa cerrado con exito.")
    except KeyboardInterrupt:
        print("\n[ERROR] Por favor cierre el programa con la opcion indicada.")
    except ValueError:
        print("[ERROR] Asegurese de que el valor escrito sea el indicado, ya sea palabra o numero.")