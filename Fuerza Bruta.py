def generar_combinaciones(indices):
    resultado = [[]]
    for elemento in indices:
        nuevas = [sub + [elemento] for sub in resultado]
        resultado += nuevas
    return resultado

def fuerza_bruta_ladron(casas):
    n = len(casas)
    max_botin = 0
    mejor_combinacion = []

    todos_los_indices = list(range(n))
    todas_las_combinaciones = generar_combinaciones(todos_los_indices)

    for combinacion in todas_las_combinaciones:
        if not combinacion:
            continue  

        combinacion_ordenada = sorted(combinacion)
        es_valida = True
        for i in range(len(combinacion_ordenada) - 1):
            if combinacion_ordenada[i] + 1 == combinacion_ordenada[i + 1]:
                es_valida = False
                break

        if es_valida:
            botin = sum(casas[i] for i in combinacion)
            if botin > max_botin:
                max_botin = botin
                mejor_combinacion = combinacion

    print("Casas con sus respectivos botines:", casas)
    print("Botín máximo:", max_botin)
    print("Casas seleccionadas:")
    for i in sorted(mejor_combinacion):
        print(f"Índice: {i} - Botín: {casas[i]}")

casas = [-1, 0, 43, 0, -1]
fuerza_bruta_ladron(casas)
