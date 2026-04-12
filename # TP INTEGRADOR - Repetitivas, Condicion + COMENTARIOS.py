# TP INTEGRADOR - Repetitivas, Condicionales y Secuenciales

print("TP INTEGRADOR")

#EJERCICIO 1: CAJA DEL KIOSCO

print("\n Ejercicio 1: Caja del Kiosco")

#Validación del nombre del cliente
while True:
    nombre = input("Nombre del cliente: ").strip()
    if nombre and nombre.isalpha():
        break
    print("Error: Solo letras y no puede estar vacío.")

#Validación de la cantidad de productos
while True:
    cant = input("Cantidad de productos: ")
    if cant.isdigit() and int(cant) > 0:
        cantidad = int(cant)
        break
    print("Error: número entero mayor a 0.")

print(f"Cliente: {nombre}")
print(f"Cantidad de productos: {cantidad}")

total_sin = 0.0
total_con = 0.0

# Procesamiento de cada producto
for i in range(1, cantidad + 1):
    #Ingreso y validación del precio
    while True:
        precio_str = input(f"Producto {i} - Precio: ")
        if precio_str.isdigit():
            precio = float(precio_str)
            break
        print("Error: número entero.")
    
    #Ingreso y validación del descuento
    while True:
        desc = input(f"Producto {i} - Descuento (S/N): ").strip().lower()
        if desc in ["s", "n"]:
            break
        print("Error: solo S o N.")
    
    print(f"Producto {i} - Precio: {int(precio)} Descuento (S/N): {desc.upper()}")
    
    #Cálculo de totales
    total_sin += precio
    if desc == "s":
        precio = precio * 0.9   # aplico descuento del 10%
    total_con += precio

ahorro = total_sin - total_con
promedio = total_con / cantidad

print(f"Total sin descuentos: ${total_sin:.2f}")
print(f"Total con descuentos: ${total_con:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")


#EJERCICIO 2: ACCESO AL CAMPUS

print("\n Ejercicio 2: Acceso al Campus")

intentos = 0
acceso = False

#Sistema de login con máximo de 3 intentos
while intentos < 3:
    usuario = input("Usuario: ").strip()
    clave = input("Clave: ").strip()
    
    if usuario == "alumno" and clave == "python123":
        acceso = True
        break
    
    intentos += 1
    print("Error: credenciales inválidas.")

if not acceso:
    print("Cuenta bloqueada.")
else:
    #Menú principal una vez logueado
    while True:
        print("\n1) Estado  2) Cambiar clave  3) Mensaje  4) Salir")
        opcion = input("Opción: ").strip()
        
        if not opcion.isdigit():
            print("Error: ingrese un número.")
            continue
            
        op = int(opcion)
        if op < 1 or op > 4:
            print("Error: opción fuera de rango.")
            continue
        
        if op == 1:
            print("Inscripto")
        elif op == 2:
            #Cambio de contraseña con validaciones
            while True:
                nueva = input("Nueva clave: ")
                if len(nueva) >= 6:
                    if nueva == input("Confirmar clave: "):
                        print("Clave cambiada.")
                        break
                    else:
                        print("Las claves no coinciden.")
                else:
                    print("Error: mínimo 6 caracteres.")
        elif op == 3:
            print("Cada día sabemos más y entendemos menos.")  # frase de intento motivacional
        elif op == 4:
            print("Saliendo...")
            break


#EJERCICIO 3: AGENDA DE TURNOS

print("\n Ejercicio 3: Agenda de Turnos")

# Inicialización de turnos (vacíos)
lun1 = lun2 = lun3 = lun4 = ""
mar1 = mar2 = mar3 = ""

# Registro del operador
while True:
    operador = input("Nombre del operador: ").strip()
    if operador and operador.isalpha():
        break
    print("Error: solo letras.")

while True:
    print("\n1. Reservar  2. Cancelar  3. Ver agenda  4. Resumen  5. Salir")
    opcion = input("Opción: ").strip()
    
    if not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 5:
        print("Opción inválida.")
        continue
        
    op = int(opcion)
    
    if op == 1:  #Reservar turno
        #Selección de día
        while True:
            dia_str = input("Día (1=Lunes, 2=Martes): ").strip()
            if dia_str.isdigit() and dia_str in ["1", "2"]:
                dia = int(dia_str)
                break
            print("Error: ingrese 1 o 2.")
        
        #Nombre del paciente
        while True:
            paciente = input("Nombre paciente: ").strip()
            if paciente and paciente.isalpha():
                break
            print("Error: solo letras.")
        
        #Asignación de turno según el día
        if dia == 1:
            if paciente in [lun1, lun2, lun3, lun4]:
                print("Error: El paciente ya tiene turno ese día.")
                continue
            if lun1 == "": lun1 = paciente
            elif lun2 == "": lun2 = paciente
            elif lun3 == "": lun3 = paciente
            elif lun4 == "": lun4 = paciente
            else: 
                print("Lunes lleno.")
        else:  # Martes
            if paciente in [mar1, mar2, mar3]:
                print("Error: El paciente ya tiene turno ese día.")
                continue
            if mar1 == "": mar1 = paciente
            elif mar2 == "": mar2 = paciente
            elif mar3 == "": mar3 = paciente
            else: 
                print("Martes lleno.")
    
    elif op == 2:  # Cancelar
        while True:
            dia_str = input("Día (1=Lunes, 2=Martes): ").strip()
            if dia_str.isdigit() and dia_str in ["1", "2"]:
                dia = int(dia_str)
                break
            print("Error: ingrese 1 o 2.")
        
        while True:
            paciente = input("Nombre a cancelar: ").strip()
            if paciente and paciente.isalpha():
                break
            print("Error: solo letras.")
        
        if dia == 1:
            if lun1 == paciente: lun1 = ""
            elif lun2 == paciente: lun2 = ""
            elif lun3 == paciente: lun3 = ""
            elif lun4 == paciente: lun4 = ""
        else:
            if mar1 == paciente: mar1 = ""
            elif mar2 == paciente: mar2 = ""
            elif mar3 == paciente: mar3 = ""
    
    elif op == 3:  #Ver agenda
        while True:
            dia_str = input("Día (1=Lunes, 2=Martes): ").strip()
            if dia_str.isdigit() and dia_str in ["1", "2"]:
                dia = int(dia_str)
                break
            print("Error: ingrese 1 o 2.")
        
        print("Agenda:")
        if dia == 1:
            print("1:", lun1 or "(libre)")
            print("2:", lun2 or "(libre)")
            print("3:", lun3 or "(libre)")
            print("4:", lun4 or "(libre)")
        else:
            print("1:", mar1 or "(libre)")
            print("2:", mar2 or "(libre)")
            print("3:", mar3 or "(libre)")
    
    elif op == 4:  #Resumen de ocupación
        ol = sum(1 for x in [lun1, lun2, lun3, lun4] if x != "")
        om = sum(1 for x in [mar1, mar2, mar3] if x != "")
        
        print(f"Lunes: {ol} ocupados, {4-ol} libres")
        print(f"Martes: {om} ocupados, {3-om} libres")
        
        if ol > om:
            print("Más turnos: Lunes")
        elif om > ol:
            print("Más turnos: Martes")
        else:
            print("Empate")
    
    elif op == 5:
        print("Sistema cerrado.")
        break


#EJERCICIO 4: LA BÓVEDA

print("\n--- Ejercicio 4: Escape Room - La Bóveda ---")

energia = 100
tiempo = 12
cerradas = 0
alarma = False
codigo = ""
racha = 0

#Nombre del agente
while True:
    nombre = input("Nombre del agente: ").strip()
    if nombre and nombre.isalpha():
        break
    print("Error: Solo letras.")

#Bucle principal del juego
while energia > 0 and tiempo > 0 and cerradas < 3 and not (alarma and tiempo <= 3):
    print(f"\nEnergía:{energia} Tiempo:{tiempo} Cerraduras:{cerradas}/3 Alarma:{'ON' if alarma else 'OFF'}")
    print("1.Forzar  2.Hackear  3.Descansar")
    
    op_str = input("Acción: ").strip()
    if not op_str.isdigit() or int(op_str) < 1 or int(op_str) > 3:
        continue
    op = int(op_str)
    
    if op == 1:  #Forzar cerradura
        racha += 1
        energia -= 20
        tiempo -= 2
        
        if racha == 3:
            alarma = True
            print("¡La cerradura se trabó!")
        else:
            if energia < 40:
                #Riesgo de activar alarma cuando hay poca energía
                while True:
                    riesgo_str = input("Riesgo de alarma. Elige 1-3: ").strip()
                    if riesgo_str.isdigit() and 1 <= int(riesgo_str) <= 3:
                        break
                    print("Error: ingrese 1-3.")
                if int(riesgo_str) == 3:
                    alarma = True
                else:
                    cerradas += 1
                    print("¡Cerradura abierta!")
            else:
                cerradas += 1
                print("¡Cerradura abierta!")
    
    elif op == 2:  #Hackear
        energia -= 10
        tiempo -= 3
        print("Hackeando panel...")
        for paso in range(1, 5):
            print(f"  Paso {paso}/4")
            codigo += "A"
        
        if len(codigo) >= 8 and cerradas < 3:
            cerradas += 1
            print("¡Cerradura abierta por hackeo!")
    
    elif op == 3:  #Descansar
        energia = min(100, energia + 15)
        tiempo -= 1
        if alarma:
            energia -= 10
            print("Alarma activa: -10 energía extra")
    
    #Resetear racha si no se usó forzar
    if op != 1:
        racha = 0

#Resultado final del juego
if cerradas == 3:
    print(f"¡VICTORIA! {nombre} abrió la bóveda.")
else:
    print(f"DERROTA. {nombre} no lo logró.")


#EJERCICIO 5: ARENA DEL GLADIADOR

print("\n--- Ejercicio 5: La Arena del Gladiador ---")

# Nombre del gladiador
while True:
    nombre = input("Nombre del Gladiador: ").strip()
    if nombre and nombre.isalpha():
        break
    print("Error: Solo se permiten letras.")

hp_j = 100
hp_e = 100
pociones = 3

#Combate por turnos
while hp_j > 0 and hp_e > 0:
    print(f"\n{nombre} (HP:{hp_j}) vs Enemigo (HP:{hp_e}) | Pociones:{pociones}")
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")
    
    #Validación de opción
    while True:
        op_str = input("Opción: ").strip()
        if op_str.isdigit() and 1 <= int(op_str) <= 3:
            op = int(op_str)
            break
        print("Error: Ingrese un número válido.")
    
    if op == 1:  #Ataque pesado
        dano = 15 * 1.5 if hp_e < 20 else 15
        hp_e -= dano
        print(f"¡Atacaste al enemigo por {dano} puntos de daño!")
    
    elif op == 2:  #Ráfaga rapida
        print(">> ¡Inicias una ráfaga de golpes!")
        for _ in range(3):
            hp_e -= 5
            print("> Golpe conectado por 5 de daño")
    
    else:  # Curar
        if pociones > 0:
            hp_j += 30
            pociones -= 1
            print("¡Te curaste +30 HP!")
        else:
            print("¡No quedan pociones!")
    
    #Ataque del enemigo (si está vivo)
    if hp_e > 0:
        hp_j -= 12
        print("¡El enemigo te atacó por 12 puntos de daño!")

#Resultado de la batalla
if hp_j > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")

print("\n FIN DEL TP INTEGRADOR")