# ESCENARIO 3: Sistema de Bombeo Hidroeléctrico
nivel = float(input("Ingrese valor de nivel del tanque (0-100%): "))
monitoreo = True
contador = 0
max_muestras = 10  # Límite de seguridad par la simulacion

while monitoreo and contador < max_muestras:
    print(f"\n--- Ciclo de muestreo #{contador + 1} ---")
    
    if nivel == 0 or nivel == 100:
        print("ERROR: Falla de lectura del sensor")
        monitoreo = False  # finaliza el ciclo ante la falla del sensor
        
    elif nivel < 15:
        print("Control: Bomba encendida - Nivel bajo")
        nivel += 5  
        
    elif 15 <= nivel <= 85:
        print("Control: Operación hidráulica normal")
        nivel += 2 
        
    else:
        print("Control: Bomba apagada - Tanque lleno")
        nivel -= 4  
        
    print("Nivel actual:", round(nivel, 2))
    contador += 1

print("\n--- Simulación finalizada ---")


