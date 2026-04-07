def analizar_temperaturas(datos):
    resultado = {}
    for ciudad, temps in datos.items():
        resultado[ciudad] = {
            "max": max(temps),
            "min": min(temps)
        }
    return resultado

# Ejemplo
temps = {
    "Bogotá": [18, 20, 17],
    "Cali": [30, 32, 28]
}
print(analizar_temperaturas(temps))