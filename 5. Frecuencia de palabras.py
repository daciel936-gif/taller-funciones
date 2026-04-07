def frecuencia_palabras(lista):
    dic = {}
    for palabra in lista:
        dic[palabra] = dic.get(palabra, 0) + 1
    return dic

print(frecuencia_palabras(["hola", "adios", "hola"]))