# Diccionario anidado corregido y estructurado (Escenario 5)
mppt_phocos = {
    "0x10": {"hardware_source": "PV_ARRAY", "max_safe_value": 150.0, "system_flag": True},
    "0x11": {"hardware_source": "BATTERY", "max_safe_value": 60.0, "system_flag": True},
    "0x15": {"hardware_source": "LOAD_RELAY", "max_safe_value": 20.0, "system_flag": False}
}

def consultar_registros():
    # Control numérico para evitar desbordamientos de memoria
    max_intentos = 5
    intentos = 0
    
    print("==================================================")
    print("          CONSULTA SEGURA - MPPT PHOCOS")
    print("==================================================")
    print("Instrucciones: Ingresa una dirección (ej: 0x10)")
    print("o un nombre (ej: BATTERY). Escriba 'salir' para terminar.\n")
    
    while intentos < max_intentos:
        intentos += 1
        print(f"--- Intento {intentos} de {max_intentos} ---")
        
        entrada = input("Ingrese dirección hexadecimal o nombre de registro: ").strip()
        
        # Opción de salida limpia
        if entrada.lower() == 'salir':
            print("Saliendo de consulta de forma segura.")
            break
            
        # 1. Búsqueda directa por llave hexadecimal usando .get()
        specs = mppt_phocos.get(entrada)
        clave_encontrada = entrada
        
        # 2. Si no se encuentra por llave directa, buscar de forma segura por el valor de 'hardware_source'
        if specs is None:
            for k, v in mppt_phocos.items():
                # Uso seguro de .get() en los diccionarios internos
                if v.get("hardware_source", "").lower() == entrada.lower():
                    specs = v
                    clave_encontrada = f"{entrada} (Dirección base: {k})"
                    break
        
        # Validación y despliegue ordenado de especificaciones
        if specs is not None:
            print(f"\n[✔] Registro encontrado para: {clave_encontrada}")
            print(f"    • Fuente de Hardware : {specs.get('hardware_source', 'No disponible')}")
            print(f"    • Valor Máximo Seguro: {specs.get('max_safe_value', 'No disponible')}")
            print(f"    • Bandera de Sistema : {specs.get('system_flag', 'No disponible')}\n")
        else:
            print(f"\n[x] Advertencia: La clave o nombre '{entrada}' no existe en el registro.\n")
            
    # Mensaje de control al alcanzar el límite numérico del ciclo
    if intentos >= max_intentos:
        print("\n[!] Límite máximo de consultas alcanzado.")
        print("[!] Ciclo finalizado por seguridad para evitar desbordamientos de memoria.")

if __name__ == "__main__":
    consultar_registros()