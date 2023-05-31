# Autor: Robinson Daniel Clemente Cordoba

# Se realiza algoritmo de ordenación ascendente de forma recursiva


lista = [16, 15, 13, 12, 11, 19, 38, 37, 36,
         35, 34, 33, 32, 8, 7, 6, 5, 4, 3, 2, 1]
# lista = [8,6,4,7,5,3]
lado_izq = []
lado_der = []


def ordenarPar(sublista):
    if not (sublista[0] < sublista[1]):
        temporal = sublista[0]
        sublista[0] = sublista[1]
        sublista[1] = temporal

        return sublista


def ordenarPares(sublista):
    # Comparamos el primer par
    if not (sublista[0] < sublista[1]):
        temporal = sublista[0]
        sublista[0] = sublista[1]
        sublista[1] = temporal

    # Comparamos el otro par
    if not (sublista[2] < sublista[3]):
        temporal = sublista[2]
        sublista[2] = sublista[3]
        sublista[3] = temporal

        return sublista


# Este método debe ser llamado estando ya los pares ordenados


def ordenarEntrePares(sublista):
    pass


def dividirLista(lista):
    # Se divide la lista
    if len(lista) % 2 == 0:
        mitad = int(len(lista)/2)
        sublista_izq, sublista_der = lista[:mitad], lista[mitad:]
    else:
        mitad = int((len(lista)/2)+1)
        sublista_izq, sublista_der = lista[:mitad], lista[mitad:]

    temporal_list = []
    temporal_list.append(sublista_izq)
    temporal_list.append(sublista_der)

    return temporal_list


def ordenarAscendentemente(sublista):

    if len(sublista) == 4:

        ordenarPares(sublista)

        """
        Nos apoyamos en el extremos izquierdos de
        cada par para comparar eficientemente
        """
        if not (sublista[0] < sublista[2]):
            temporal = sublista[2]
            sublista.remove(temporal)
            sublista.insert(0, temporal)

        """
        Como hubo inserción al inicio de la lista entonces la
        referencia a los elementos es la anterior + 1

        Además, como se sabe que el elemento en la posición 0
        es menor que el próximo a comparar entonces este último
        nunca puede ser ubicado a la izquierda del mismo
        """
        if not (sublista[1] < sublista[3]):
            temporal = sublista[3]
            sublista.remove(temporal)
            sublista.insert(1, temporal)

        return sublista

    elif len(sublista) == 3:

        ordenarPar(sublista)

        # Procedemos a comparar con el extremo único
        # Primer elemento del par
        if not (sublista[0] < sublista[2]):
            temporal = sublista[2]
            sublista.remove(temporal)
            sublista.insert(0, temporal)

        # Segundo elemento del primer par
        if not (sublista[1] < sublista[2]):
            temporal = sublista[2]
            sublista.remove(temporal)
            sublista.insert(1, temporal)

        return sublista

    elif len(sublista) == 2:
        return ordenarPar(sublista)

    elif len(sublista) == 1:
        return sublista

    else:
        sublista = ordenarLista(sublista)
        return sublista


def ordenarLista(lista):

    sublistas = dividirLista(lista)
    sublista_izq = sublistas[0]
    sublista_der = sublistas[1]

    print("|-----------------------------|")
    sublista_izq = ordenarAscendentemente(sublista_izq)

    if sublista_izq is not None:
        lado_izq.append(sublista_izq)
        print("Sublista izq: ", sublista_izq)

    sublista_der = ordenarAscendentemente(sublista_der)

    if sublista_der is not None:
        lado_der.append(sublista_der)
        print("Sublista der: ", sublista_der)


print("Antes: ", lista)
ordenarLista(lista)
print("|-----------------------------|")
# print("Después: ", lista)
