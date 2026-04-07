carrito = []

def agregar_producto(nombre, precio):
    carrito.append({"nombre": nombre, "precio": precio})

def total(descuento=0):
    suma = sum(p["precio"] for p in carrito)
    return suma * (1 - descuento)

# Ejemplo
agregar_producto("Camisa", 50000)
agregar_producto("Pantalón", 80000)
print(total(0.1))  # 10% descuento