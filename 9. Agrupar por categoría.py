def agrupar(productos):
    dic = {}
    for nombre, categoria in productos:
        dic.setdefault(categoria, []).append(nombre)
    return dic

print(agrupar([("Manzana", "Fruta"), ("Zanahoria", "Verdura")]))