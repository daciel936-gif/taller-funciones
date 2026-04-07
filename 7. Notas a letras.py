def convertir_nota(nota):
    if nota >= 4.5:
        return "A"
    elif nota >= 4.0:
        return "B"
    elif nota >= 3.0:
        return "C"
    else:
        return "F"

def reporte(estudiantes):
    return [(nombre, convertir_nota(nota)) for nombre, nota in estudiantes]

print(reporte([("Ana", 4.6), ("Luis", 2.5)]))