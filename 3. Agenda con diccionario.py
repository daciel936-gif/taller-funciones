agenda = {}

def agregar(nombre, telefono):
    agenda[nombre] = telefono

def buscar(nombre):
    return agenda.get(nombre, "No encontrado")

def eliminar(nombre):
    agenda.pop(nombre, None)


agregar("Ana", "123")
print(buscar("Ana"))
eliminar("Ana")
