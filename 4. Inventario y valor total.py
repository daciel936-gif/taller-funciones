inventario = {
    "manzana": {"precio": 1000, "cantidad": 5},
    "pera": {"precio": 800, "cantidad": 3}
}

def valor_total(inv):
    total = 0
    for producto in inv.values():
        total += producto["precio"] * producto["cantidad"]
    return total

print(valor_total(inventario))