# TAREA 2: Dosificacion de presion en red de gas natural
# Sensor: XMLP010BC71F

presion = 3.0

for numero_lectura in range(1, 11):

    print(f"Lectura {numero_lectura}: {presion:.1f} bar")

    if presion >= 6.0:
        print("CRITICO: Ruptura inminente. Abortar operacion.")
        break

    if presion < 2.0:
        print("Accion: Inyectando presion a la red")
        presion += 0.5

    elif presion <= 4.5:
        print("Accion: Flujo nominal estabilizado")
        presion += 0.1

    else:
        print("Accion: Purga de emergencia abierta")
        presion -= 0.8

print("Ciclo de monitoreo finalizado.")
