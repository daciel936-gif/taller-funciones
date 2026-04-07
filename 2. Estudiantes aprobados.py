def aprobados(estudiantes):
    return [nombre for nombre, nota in estudiantes if nota >= 3.0]


datos = [("Ana", 3.5), ("Luis", 2.9), ("Pedro", 4.0)]
print(aprobados(datos))
