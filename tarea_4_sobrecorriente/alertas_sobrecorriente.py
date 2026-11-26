# Historial de lecturas de corriente
historial_corriente = [
    1.5, 2.0, 12.8, 4.5, 30.2, 1.1
] * 5000


# Funcion de busqueda original
def buscar_valor_critico_original(valor):
    existe = False

    for lectura in historial_corriente:
        if lectura == valor:
            existe = True

    if existe and valor > 25.0:
        print(
            "ALERTA DE SOBRECORRIENTE DETECTADA: "
            "EL VALOR SUPERA LOS LIMITES"
        )

    return existe


# Estructura optimizada para consultas
lecturas_registradas = set(historial_corriente)


# Funcion de busqueda optimizada
def buscar_valor_critico_optimizado(valor):
    existe = valor in lecturas_registradas

    if existe and valor > 25.0:
        print(
            "ALERTA DE SOBRECORRIENTE DETECTADA: "
            "EL VALOR SUPERA LOS LIMITES"
        )

    return existe


# Pruebas de funcionamiento
if __name__ == "__main__":
    print("PRUEBAS DEL SISTEMA DE ALERTAS")

    print(
        "Busqueda original:",
        buscar_valor_critico_original(30.2)
    )

    print(
        "Busqueda optimizada:",
        buscar_valor_critico_optimizado(30.2)
    )

    print(
        "Lectura no registrada:",
        buscar_valor_critico_optimizado(99.0)
    )
  
