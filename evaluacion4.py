tarjetas = {}

def agregar(lst_elementos: dict, codigo: str, datos: list) -> bool:
    if codigo in lst_elementos:
        print("[ERROR] El codigo ingresado ya existe en los registros, vuelva a intentarlo.")
        return False

    lst_elementos[codigo] = {
        "compras": datos[0],
        "saldo": datos[1]
    }

    if datos[1] < 0:
        print("[ERROR] No se puede crear una tarjeta con saldo negativo, vuelva a intentarlo.")
        return False

    print("* Tarjeta prepago registrada con exito")
    return True

def usar(lst_elementos: dict, codigo: str, monto: int) -> bool:
    if codigo not in lst_elementos:
        print("[ERROR] El codigo ingresado no existe en los registros, vuelva a intentarlo.")
        return False

    if lst_elementos[codigo]["saldo"] < monto:
        print("[ERROR] El monto ingresado excede el saldo de la tarjeta, vuelva a intentarlo.")
        return False
    if monto <= 0:
        print("(!) Lo sentimos el monto a usar no puede ser igual o menor a cero, vuelva intentarlo.")
        return False

    descuentoSaldo = lst_elementos[codigo]["saldo"] - monto
    lst_elementos[codigo]["saldo"] = descuentoSaldo
    lst_elementos[codigo]["compras"] += 1
    print("--------------------------")
    print(f"* Se ha hecho uso de la tarjeta [{codigo}]")
    print(f"* Se ha usado un saldo de ${monto} CLP, su saldo actual es de ${descuentoSaldo} CLP")
    print("--------------------------")
    return True

def listar(lst_elementos: dict) -> None:
    for codigo, datos in lst_elementos.items():
        print("--------------------------------------")
        print(f"Codigo: {codigo}")
        print(f"Compras realizadas: {datos['compras']}")
        print(f"Saldo disponible: ${datos['saldo']} CLP")

def ver_saldo_critico(lst_elementos: dict, saldo_minimo: int) -> None:
    if lst_elementos:
        print(f"(TARJETAS CON SALDO CRITICO DE ${saldo_minimo} CLP PARA ABAJO)")
        for codigo, datos in lst_elementos.items():
            if datos["saldo"] <= saldo_minimo:
                print("--------------------------------------")
                print(f"Codigo: {codigo}")
                print(f"Compras realizadas: {datos['compras']}")
                print(f"Saldo disponible: ${datos['saldo']} CLP")
                print("--------------------------------------")

activo = True
try:
    while activo:
        print("1.- Agregar una tarjeta")
        print("2.- Usar tarjeta prepago")
        print("3.- Listar tarjetas")
        print("4.- Ver saldo critico")
        print("0.- Cerrar programa")
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            print("------- CREAR TARJETA -------")
            codigo = input("Codigo unico: ")
            compras = 0
            saldoInicial = int(input("Saldo inicial: "))
            datos = [compras, saldoInicial]
            agregar(tarjetas, codigo, datos)
        elif opcion == "2":
            print("------- USAR SALDO TARJETA -------")
            codigo = input("Codigo:")
            monto = int(input("Monto a usar: "))
            usar(tarjetas, codigo, monto)
        elif opcion == "3":
            if not tarjetas:
                print("[ERROR] No se puede lista debido a que no hay tarjetas registradas, vuelva a intentarlo.")
            else:
                listar(tarjetas)
        elif opcion == "4":
            saldo_minimo = 0

            if not tarjetas:
                print("[ERROR] No se puede ver el saldo critico ya que no hay tarjetas registradas.")

            if tarjetas:
                print("------- VER SALDO CRITICO TARJETAS -------")
                saldo_minimo = int(input("Saldo critico minimo: "))
                ver_saldo_critico(tarjetas, saldo_minimo)
        elif opcion == "0":
            activo = False
            print("* Programa cerrado con exito.")
        else:
            print("- Por favor ingrese una de las opciones indicadas, vuelva a intentarlo.")
except ValueError:
    print("[ERROR] Por favor ingrese los valores indicados, intentelo nuevamente")
except KeyboardInterrupt:
    print("\n[ERROR] Por favor cierre el programa con la opcion indicada.")