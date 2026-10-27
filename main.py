# ============================================
# SISTEMA INTEGRADO DE GESTION
# SISTEMA BANCARIO Y SISTEMA MEDICO
# ============================================
print("=========================================")
print("  Sistema Integrado de Gestion  ")
print("  Sistema Bancario y Sistema Medico  ")
print("=========================================")
print(" Nombre de los integrantes del grupo: ")
print(" Junior Alexis Mejía Cheque ")
print(" Luis Antonio Marín López ")
print(" brandon Hercaime Morales Ardon ")
print(" María Isabel Menéndez Fuentes ")
print(" curso: algoritmos ")
print(" Nombre del Catedratico: INGE: Demshin Coutiño ")
print(" Institucion: Universidad Mariano Galvez De Coatepeque")
print(" Facultad: Ingenieria En Sistemas ")
print(" Año: 2026 ")
print("==========================================")
input(" presione ENTER para iniciar el sistema ")
clientes = []
cuentas = []
movimientos = []
creditos = []
pacientes = []
medicos = []
citas = []
consultas = []


# ============================================
# VALIDACIONES
# ============================================
def leer_entero(mensaje):
    while True:
        dato = input(mensaje)
        valido = True
        if len(dato) == 0:
            valido = False
        for caracter in dato:
            if caracter not in "0123456789":
                valido = False
        if valido:
            return int(dato)
        else:
            print("Entrada invalida. Prueba otra vez.")


def leer_decimal(mensaje):
    while True:
        dato = input(mensaje)
        valido = True
        puntos = 0
        digitos = 0
        if len(dato) == 0:
            valido = False
        for caracter in dato:
            if caracter == ".":
                puntos = puntos + 1
            elif caracter in "0123456789":
                digitos = digitos + 1
            else:
                valido = False
        if puntos > 1 or digitos == 0:
            valido = False
        if valido:
            numero = float(dato)
            if numero >= 0:
                return numero
            else:
                print("No se permiten cantidades negativas.")
        else:
            print("Entrada invalida. Prueba otra vez.")


def leer_texto(mensaje):
    while True:
        dato = input(mensaje)
        if len(dato) > 0:
            return dato
        else:
            print("El dato no puede estar vacio. Prueba otra vez.")


def leer_nombre(mensaje):
    while True:
        dato = input(mensaje)
        valido = True
        letras = 0
        letras_palabra = 0
        vocales_palabra = 0
        repeticiones = 1
        anterior = ""


        for caracter in dato + " ":
            if caracter == " ":
                if letras_palabra == 0:
                    valido = False


                if letras_palabra < 3:
                    valido = False


                if letras_palabra > 0 and vocales_palabra == 0:
                    valido = False


                letras_palabra = 0
                vocales_palabra = 0
                repeticiones = 1
                anterior = ""


            elif caracter in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyzÁÉÍÓÚÜáéíóúü":
                if caracter == anterior:
                    repeticiones = repeticiones + 1
                else:
                    repeticiones = 1


                anterior = caracter


                if repeticiones >= 3:
                    valido = False


                letras = letras + 1
                letras_palabra = letras_palabra + 1


                if caracter in "AEIOUaeiouÁÉÍÓÚáéíóú":
                    vocales_palabra = vocales_palabra + 1


            else:
                valido = False


        if letras < 3:
            valido = False


        if valido:
            return dato
        else:
            print("Nombre invalido. Escribe un nombre con letras y vocales.")
            print("No uses numeros ni simbolos. Prueba otra vez.")


def leer_dpi(mensaje):
    while True:
        dato = input(mensaje)
        valido = True
        if len(dato) != 13:
            valido = False
        for caracter in dato:
            if caracter not in "0123456789":
                valido = False
        if valido:
            return dato
        else:
            print("DPI invalido. Debe tener exactamente 13 digitos numericos.")
            print("Prueba otra vez.")


def leer_numero_cuenta(mensaje):
    while True:
        dato = input(mensaje)
        valido = True
        if len(dato) != 10:
            valido = False
        for caracter in dato:
            if caracter not in "0123456789":
                valido = False
        if valido:
            return int(dato)
        else:
            print("Numero de cuenta invalido.")
            print("Debe tener exactamente 10 digitos.")


def leer_fecha(mensaje):
 
    while True:
        fecha = input(mensaje)
        valido = True
        if len(fecha) != 10:
            valido = False
        if len(fecha) == 10:
            if fecha[2] != fecha[5]:
                valido = False
            if fecha[2] != "-" and fecha[2] != "/":
                valido = False
            for i in range(10):
                if i != 2 and i != 5:
                    if fecha[i] not in "0123456789":
                        valido = False
            if valido:
                dia = int(fecha[0:2])
                mes = int(fecha[3:5])
                anio = int(fecha[6:10])
                if mes < 1 or mes > 12 or anio < 1:
                    valido = False
                else:
                    if mes in (4, 6, 9, 11):
                        dias_mes = 30
                    elif mes == 2:
                        dias_mes = 28
                        if anio % 400 == 0:
                            dias_mes = 29
                        elif anio % 100 == 0:
                            dias_mes = 28
                        elif anio % 4 == 0:
                            dias_mes = 29
                    else:
                        dias_mes = 31
                    if dia < 1 or dia > dias_mes:
                        valido = False
        if valido:
          return fecha
        else:
            print("Fecha invalida.")
            print("Usa DD-MM-AAAA o DD/MM/AAAA.")
def leer_especialidad(mensaje):
    while True:
        print("1. Medicina general")
        print("2. Pediatria")
        print("3. Cardiologia")
        print("4. Dermatologia")
        print("5. Ginecologia")
        print("6. Traumatologia")


        opcion = leer_entero(mensaje)


        if opcion == 1:
            return "Medicina general"
        elif opcion == 2:
            return "Pediatria"
        elif opcion == 3:
            return "Cardiologia"
        elif opcion == 4:
            return "Dermatologia"
        elif opcion == 5:
            return "Ginecologia"
        elif opcion == 6:
            return "Traumatologia"
        else:
            print("Especialidad invalida. Prueba otra vez.")


def leer_hora(mensaje):
    while True:
        hora = input(mensaje)
        valido = True
        if len(hora) != 5:
            valido = False
        elif hora[2] != ":":
            valido = False
        else:
            for i in (0, 1, 3, 4):
                if hora[i] not in "0123456789":
                    valido = False
            if valido:
                horas = int(hora[0:2])
                minutos = int(hora[3:5])
                if horas > 23 or minutos > 59:
                    valido = False
        if valido:
            return hora
        else:
            print("Hora invalida. Usa HH:MM (00:00 a 23:59).")


# ============================================
# FUNCIONES DE BUSQUEDA
# ============================================
def buscar_cliente(codigo):
    for cliente in clientes:
        if cliente[0] == codigo:
            return cliente
    return None


def buscar_cuenta(numero):
    for cuenta in cuentas:
        if cuenta[0] == numero:
            return cuenta
    return None


def buscar_paciente(codigo):
    for paciente in pacientes:
        if paciente[0] == codigo:
            return paciente
    return None


def buscar_medico(codigo):
    for medico in medicos:
        if medico[0] == codigo:
            return medico
    return None


def buscar_cita(codigo):
    for cita in citas:
        if cita[0] == codigo:
            return cita
    return None


def buscar_credito(numero):
    for credito in creditos:
        if credito[0] == numero:
            return credito
    return None


# ============================================
# SISTEMA BANCARIO
# ============================================
def registrar_cliente():
    print("--- REGISTRO DE CLIENTE ---")
    codigo = leer_entero("Codigo del cliente: ")
    if buscar_cliente(codigo) is not None:
        print("Ese codigo ya existe.")
        return
    nombre = leer_nombre("Nombre completo: ")
    identificacion = leer_dpi("Numero de identificacion (DPI): ")
    for cliente in clientes:
        if cliente[2] == identificacion:
            print("Esa identificacion ya esta registrada.")
            return
    clientes.append([codigo, nombre, identificacion])
    print("Cliente registrado correctamente.")


def consultar_clientes():
    print("--- LISTA DE CLIENTES ---")
    if len(clientes) == 0:
        print("No hay clientes registrados.")
    else:
        for cliente in clientes:
            print("Codigo:", cliente[0])
            print("Nombre:", cliente[1])
            print("Identificacion:", cliente[2])
            print("------------------------")


def modificar_cliente():
    codigo = leer_entero("Codigo del cliente que deseas modificar: ")
    cliente = buscar_cliente(codigo)
    if cliente is None:
        print("Cliente no encontrado.")
    else:
        print("1. Modificar nombre")
        print("2. Modificar identificacion")
        opcion = leer_entero("Elige una opcion: ")
        if opcion == 1:
            cliente[1] = leer_nombre("Nuevo nombre: ")
            print("Nombre actualizado.")
        elif opcion == 2:
            identificacion = leer_dpi("Nueva identificacion (DPI): ")
            repetida = False
            for otro in clientes:
                if otro[2] == identificacion and otro[0] != codigo:
                    repetida = True
            if repetida:
                print("Esa identificacion ya pertenece a otro cliente.")
            else:
                cliente[2] = identificacion
                print("Identificacion actualizada.")
        else:
            print("Opcion invalida. Prueba otra vez.")


def crear_cuenta():
    print("--- CREAR CUENTA ---")
    numero = leer_numero_cuenta("Numero de cuenta: ")
    if buscar_cuenta(numero) is not None:
        print("Ese numero de cuenta ya existe.")
        return
    codigo = leer_entero("Codigo del cliente propietario: ")
    cliente = buscar_cliente(codigo)
    if cliente is None:
        print("El cliente no existe.")
        return
    print("1. Cuenta de ahorro")
    print("2. Cuenta corriente")
    tipo = leer_entero("Tipo de cuenta: ")
    if tipo == 1:
        nombre_tipo = "Ahorro"
    elif tipo == 2:
        nombre_tipo = "Corriente"
    else:
        print("Opcion invalida. Prueba otra vez.")
        return
    saldo = leer_decimal("Saldo inicial: ")
    cuentas.append([numero, codigo, nombre_tipo, saldo])
    print("Cuenta creada correctamente.")


def consultar_cuentas():
    print("--- CUENTAS BANCARIAS ---")
    if len(cuentas) == 0:
        print("No hay cuentas registradas.")
    else:
        for cuenta in cuentas:
            print("Cuenta:", cuenta[0])
            print("Cliente:", cuenta[1])
            print("Tipo:", cuenta[2])
            print("Saldo: Q", round(cuenta[3], 2))
            print("------------------------")


def depositar():
    numero = leer_numero_cuenta("Numero de cuenta: ")
    cuenta = buscar_cuenta(numero)
    if cuenta is None:
        print("La cuenta no existe.")
        return
    cantidad = leer_decimal("Cantidad a depositar: ")
    if cantidad <= 0:
        print("El deposito debe ser mayor que cero.")
    else:
        cuenta[3] = round(cuenta[3] + cantidad, 2)
        fecha = leer_fecha("Fecha del movimiento: ")
        movimientos.append([numero, "Deposito", cantidad, fecha])
        print("Deposito realizado.")
        print("Nuevo saldo: Q", round(cuenta[3], 2))


def retirar():
    numero = leer_numero_cuenta("Numero de cuenta: ")
    cuenta = buscar_cuenta(numero)
    if cuenta is None:
        print("La cuenta no existe.")
        return
    cantidad = leer_decimal("Cantidad a retirar: ")
    if cantidad <= 0:
        print("El retiro debe ser mayor que cero.")
    elif cantidad > cuenta[3]:
        print("Saldo insuficiente. No se realizo el retiro.")
    else:
        cuenta[3] = round(cuenta[3] - cantidad, 2)
        fecha = leer_fecha("Fecha del movimiento: ")
        movimientos.append([numero, "Retiro", cantidad, fecha])
        print("Retiro realizado.")
        print("Nuevo saldo: Q", round(cuenta[3], 2))


def transferir():
    origen_numero = leer_numero_cuenta("Cuenta de origen: ")
    origen = buscar_cuenta(origen_numero)
    if origen is None:
        print("La cuenta de origen no existe.")
        return
    destino_numero = leer_numero_cuenta("Cuenta de destino: ")
    destino = buscar_cuenta(destino_numero)
    if destino is None:
        print("La cuenta de destino no existe.")
        return
    if origen_numero == destino_numero:
        print("No puedes transferir a la misma cuenta.")
        return
    cantidad = leer_decimal("Cantidad a transferir: ")
    if cantidad <= 0:
        print("La cantidad debe ser mayor que cero.")
    elif cantidad > origen[3]:
        print("Saldo insuficiente.")
    else:
        origen[3] = round(origen[3] - cantidad, 2)
        destino[3] = round(destino[3] + cantidad, 2)
        fecha = leer_fecha("Fecha de la transferencia: ")
        movimientos.append([
        origen_numero, "Transferencia enviada", cantidad, fecha])
        movimientos.append([destino_numero, "Transferencia recibida", cantidad, fecha])
        print("Transferencia realizada correctamente.")


def historial_movimientos():
    numero = leer_numero_cuenta("Numero de cuenta: ")
    cuenta = buscar_cuenta(numero)
    if cuenta is None:
        print("La cuenta no existe.")
        return
    encontrado = False
    print("--- HISTORIAL DE MOVIMIENTOS ---")
    for movimiento in movimientos:
        if movimiento[0] == numero:
            print("Tipo:", movimiento[1])
            print("Cantidad: Q", round(movimiento[2], 2))
            print("Fecha:", movimiento[3])
            print("------------------------")
            encontrado = True
    if not encontrado:
        print("Esta cuenta no tiene movimientos.")


# ============================================
# CREDITOS BANCARIOS
# ============================================
def registrar_credito():
    print("--- REGISTRO DE CREDITO ---")
    codigo = leer_entero("Codigo del cliente: ")
    cliente = buscar_cliente(codigo)
    if cliente is None:
        print("El cliente no existe.")
        return
    numero = leer_entero("Numero de credito: ")
    if buscar_credito(numero) is not None:
        print("Ese numero de credito ya existe.")
        return
    monto = leer_decimal("Monto del credito: ")
    if monto <= 0:
        print("El monto debe ser mayor que cero.")
        return
    interes = leer_decimal("Interes porcentual total del credito: ")
    cuotas = leer_entero("Numero de cuotas: ")
    if cuotas <= 0:
        print("El numero de cuotas debe ser mayor que cero.")
        return
    total = round(monto + monto * interes / 100, 2)
    creditos.append([
        numero, codigo, monto, interes, cuotas, total, 0, "Activo"
    ])
    print("Credito registrado.")
    print("Monto total con interes: Q", total)
    print("Valor aproximado por cuota: Q", round(total / cuotas, 2))


def consultar_creditos():
    print("--- CREDITOS REGISTRADOS ---")
    if len(creditos) == 0:
        print("No hay creditos registrados.")
    else:
        for credito in creditos:
            pendiente = round(credito[5] - credito[6], 2)
            print("Credito:", credito[0])
            print("Cliente:", credito[1])
            print("Monto inicial: Q", credito[2])
            print("Interes porcentual:", credito[3], "%")
            print("Cuotas:", credito[4])
            print("Total con interes: Q", credito[5])
            print("Pagado: Q", credito[6])
            print("Pendiente: Q", pendiente)
            print("Estado:", credito[7])
            print("------------------------")


def pagar_credito():
    numero = leer_entero("Numero de credito: ")
    credito_encontrado = buscar_credito(numero)
    if credito_encontrado is None:
        print("Credito no encontrado.")
        return
    pendiente = round(
        credito_encontrado[5] - credito_encontrado[6], 2)
    if pendiente <= 0:
        print("Este credito ya esta cancelado.")
        return
    pago = leer_decimal("Cantidad del pago: ")
    if pago <= 0:
        print("El pago debe ser mayor que cero.")
    elif pago > pendiente:
        print("El pago supera la deuda pendiente.")
    else:
        credito_encontrado[6] = round(
            credito_encontrado[6] + pago, 2
        )
        if credito_encontrado[6] >= credito_encontrado[5]:
            credito_encontrado[7] = "Cancelado"
        print("Pago registrado.")
        print("Saldo pendiente: Q", round(
            credito_encontrado[5] - credito_encontrado[6], 2
        ))


def menu_bancario():
    while True:
        print("========== SISTEMA BANCARIO ==========")
        print("1. Registrar cliente")
        print("2. Consultar clientes")
        print("3. Modificar cliente")
        print("4. Crear cuenta")
        print("5. Consultar cuentas y saldos")
        print("6. Depositar")
        print("7. Retirar")
        print("8. Transferir")
        print("9. Historial de movimientos")
        print("10. Registrar credito")
        print("11. Consultar creditos")
        print("12. Pagar credito")
        print("13. Volver al menu principal")
        opcion = leer_entero("Elige una opcion: ")
        if opcion == 1:
            registrar_cliente()
        elif opcion == 2:
            consultar_clientes()
        elif opcion == 3:
            modificar_cliente()
        elif opcion == 4:
            crear_cuenta()
        elif opcion == 5:
            consultar_cuentas()
        elif opcion == 6:
            depositar()
        elif opcion == 7:
            retirar()
        elif opcion == 8:
            transferir()
        elif opcion == 9:
            historial_movimientos()
        elif opcion == 10:
            registrar_credito()
        elif opcion == 11:
            consultar_creditos()
        elif opcion == 12:
            pagar_credito()
        elif opcion == 13:
            break
        else:
            print("Opcion invalida. Prueba otra vez.")


# ============================================
# SISTEMA MEDICO
# ============================================
def registrar_paciente():
    print("--- REGISTRAR PACIENTE ---")
    codigo = leer_entero("Codigo del paciente: ")
    if buscar_paciente(codigo) is not None:
        print("Ese codigo ya existe.")
        return
    nombre = leer_nombre("Nombre del paciente: ")
    edad = leer_entero("Edad: ")
    if edad < 1 or edad > 120:
        print("Edad invalida.")
        return
    identificacion = leer_dpi("Identificacion del paciente (DPI): ")
    for paciente in pacientes:
        if paciente[3] == identificacion:
            print("La identificacion ya esta registrada.")
            return
    pacientes.append([codigo, nombre, edad, identificacion])
    print("Paciente registrado correctamente.")


def consultar_pacientes():
    print("--- PACIENTES ---")
    if len(pacientes) == 0:
        print("No hay pacientes registrados.")
    else:
        for paciente in pacientes:
            print("Codigo:", paciente[0])
            print("Nombre:", paciente[1])
            print("Edad:", paciente[2])
            print("Identificacion:", paciente[3])
            print("------------------------")


def registrar_medico():
    print("--- REGISTRAR MEDICO ---")
    codigo = leer_entero("Codigo del medico: ")
    if buscar_medico(codigo) is not None:
        print("Ese codigo ya existe.")
        return
    nombre = leer_nombre("Nombre del medico: ")
    especialidad = leer_especialidad("Elige una especialidad: ")
    medicos.append([codigo, nombre, especialidad])
    print("Medico registrado correctamente.")


def consultar_medicos():
    print("--- MEDICOS ---")
    if len(medicos) == 0:
        print("No hay medicos registrados.")
    else:
        for medico in medicos:
            print("Codigo:", medico[0])
            print("Nombre:", medico[1])
            print("Especialidad:", medico[2])
            print("------------------------")


def programar_cita():
    print("--- PROGRAMAR CITA ---")
    codigo = leer_entero("Codigo de la cita: ")
    if buscar_cita(codigo) is not None:
        print("Ese codigo de cita ya existe.")
        return
    codigo_paciente = leer_entero("Codigo del paciente: ")
    paciente = buscar_paciente(codigo_paciente)
    if paciente is None:
        print("El paciente no existe.")
        return
    codigo_medico = leer_entero("Codigo del medico: ")
    medico = buscar_medico(codigo_medico)
    if medico is None:
        print("El medico no existe.")
        return
    fecha = leer_fecha("Fecha de la cita (DD-MM-AAAA o DD/MM/AAAA): ")
    hora = leer_hora("Hora de la cita (HH:MM): ")
    for cita in citas:
        if cita[2] == codigo_medico and cita[4] == fecha and cita[5] == hora:
            if cita[6] == "Programada":
                print("El medico ya tiene una cita a esa hora.")
                return
    citas.append([
        codigo, codigo_paciente, codigo_medico,
        paciente[1], fecha, hora, "Programada" ])
    print("Cita programada correctamente.")


def consultar_citas():
    print("--- CITAS MEDICAS ---")
    if len(citas) == 0:
        print("No hay citas registradas.")
    else:
        for cita in citas:
            print("Codigo de cita:", cita[0])
            print("Codigo de paciente:", cita[1])
            print("Paciente:", cita[3])
            print("Codigo de medico:", cita[2])
            print("Fecha:", cita[4])
            print("Hora:", cita[5])
            print("Estado:", cita[6])
            print("------------------------")


def cancelar_cita():
    codigo = leer_entero("Codigo de la cita que deseas cancelar: ")
    cita = buscar_cita(codigo)
    if cita is None:
        print("Cita no encontrada.")
    elif cita[6] != "Programada":
        print("La cita no esta programada.")
    else:
        cita[6] = "Cancelada"
        print("Cita cancelada correctamente.")
def leer_consulta(mensaje):
    while True:
        dato = input(mensaje)
        valido = True
        letras = 0
        vocales = 0


        for caracter in dato:
            if caracter in "0123456789":
                valido = False


            if caracter in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzÁÉÍÓÚáéíóúÜüÑñ":
                letras = letras + 1


            if caracter in "AEIOUaeiouÁÉÍÓÚáéíóú":
                vocales = vocales + 1


        if letras == 0 or vocales == 0:
            valido = False


        if valido:
            return dato
        else:
            print("Texto invalido. No uses numeros ni palabras sin vocales.")
            print("Prueba otra vez.")


def registrar_consulta():
    print("--- REGISTRAR CONSULTA MEDICA ---")
    codigo_cita = leer_entero("Codigo de la cita: ")
    cita = buscar_cita(codigo_cita)
    if cita is None:
        print("La cita no existe.")
        return
    if cita[6] != "Programada":
        print("La cita no esta disponible para consulta.")
        return
    diagnostico = leer_consulta("Diagnostico: ")
    tratamiento = leer_consulta("Tratamiento indicado: ")
    consultas.append([codigo_cita, cita[1], cita[2],diagnostico, tratamiento])
    cita[6] = "Atendida"
    print("Consulta registrada correctamente.")


def consultar_historial_medico():
    codigo = leer_entero("Codigo del paciente: ")
    paciente = buscar_paciente(codigo)
    if paciente is None:
        print("El paciente no existe.")
        return
    encontrado = False
    print("--- HISTORIAL MEDICO ---")
    for consulta in consultas:
        if consulta[1] == codigo:
            print("Cita:", consulta[0])
            print("Medico:", consulta[2])
            print("Diagnostico:", consulta[3])
            print("Tratamiento:", consulta[4])
            print("------------------------")
            encontrado = True
        if not encontrado:
            print("El paciente no tiene consultas registradas.")


def menu_medico():
    while True:
        print("========== SISTEMA MEDICO ==========")
        print("1. Registrar paciente")
        print("2. Consultar pacientes")
        print("3. Registrar medico")
        print("4. Consultar medicos")
        print("5. Programar cita")
        print("6. Consultar citas")
        print("7. Cancelar cita")
        print("8. Registrar consulta")
        print("9. Historial medico del paciente")
        print("10. Volver al menu principal")
        opcion = leer_entero("Elige una opcion: ")
        if opcion == 1:
            registrar_paciente()
        elif opcion == 2:
            consultar_pacientes()
        elif opcion == 3:
            registrar_medico()
        elif opcion == 4:
            consultar_medicos()
        elif opcion == 5:
            programar_cita()
        elif opcion == 6:
            consultar_citas()
        elif opcion == 7:
            cancelar_cita()
        elif opcion == 8:
            registrar_consulta()
        elif opcion == 9:
            consultar_historial_medico()
        elif opcion == 10:
            break
        else:
            print("Opcion invalida. Prueba otra vez.")


# ============================================
# MENU PRINCIPAL
# ============================================
while True:
    print("====================================")
    print("     SISTEMA INTEGRADO DE GESTION")
    print("====================================")
    print("1. Sistema bancario")
    print("2. Sistema medico")
    print("3. Salir")
    opcion = leer_entero("Que opcion eliges?: ")
    if opcion == 1:
        menu_bancario()
    elif opcion == 2:
        menu_medico()
    elif opcion == 3:
        print("Gracias por utilizar el sistema.")
        break
    else:
        print("Opcion invalida. Prueba otra vez.")
