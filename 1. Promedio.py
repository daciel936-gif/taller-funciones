def analizar_notas(notas):
    promedio = sum(notas) / len(notas)
    return promedio, max(notas), min(notas)

# Ejemplo
notas = [3.5, 4.2, 2.8, 5.0]
print(analizar_notas(notas))