def votacion(votos, candidatos):
    conteo = {c: 0 for c in candidatos}
    invalidos = 0

    for voto in votos:
        if voto in conteo:
            conteo[voto] += 1
        else:
            invalidos += 1

    total_validos = sum(conteo.values())
    ganador = max(conteo, key=conteo.get)
    porcentaje = (conteo[ganador] / total_validos) * 100 if total_validos > 0 else 0

    return ganador, porcentaje, invalidos

#wj1
votos = ["Ana", "Luis", "Ana", "Pedro", "X"]
candidatos = ["Ana", "Luis", "Pedro"]
print(votacion(votos, candidatos))  
def votacion(votos, candidatos):
    conteo = {c: 0 for c in candidatos}
    invalidos = 0

    for voto in votos:
        if voto in conteo:
            conteo[voto] += 1
        else:
            invalidos += 1

    total_validos = sum(conteo.values())
    ganador = max(conteo, key=conteo.get)
    porcentaje = (conteo[ganador] / total_validos) * 100 if total_validos > 0 else 0

    return ganador, porcentaje, invalidos
#ej2
votos = ["Ana", "Luis", "Ana", "Pedro", "X"]
candidatos = ["Ana", "Luis", "Pedro"]
print(votacion(votos, candidatos))