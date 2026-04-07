def aprobados(estudiantes):
    return [nombre for nombre, nota in estudiantes if nota >= 3.0]

# Ejemplo
datos = [("Ana", 3.5), ("Luis", 2.9), ("Pedro", 4.0)]
print(aprobados(datos))