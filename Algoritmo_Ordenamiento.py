# Autor: Robinson Daniel Clemente Cordoba

# Se realiza algoritmo de ordenación ascendente de forma recursiva

# Peor de los casos
lista = [9, 8, 7, 6, 5, 4, 3, 2, 1]

# Mejor de los casos

lista_prueba = []


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
    if not (sublista_izq[2] < sublista[3]):
        temporal = sublista[2]
        sublista[2] = sublista[3]
        sublista[3] = temporal

    return sublista


def ordenarAscendentemente(lista):

    # Se divide la lista
    if len(lista) % 2 == 0:
        mitad = int(len(lista)/2)
        sublista_izq, sublista_der = lista[:mitad], lista[mitad:]
    else:
        mitad = int((len(lista)/2)+1)
        sublista_izq, sublista_der = lista[:mitad], lista[mitad:]

    # Teniendo la lista divida entonces se procede con la lógica restante

    # Ordenamiento por izquierda
    if len(sublista_izq) == 4:
        ordenarPares(sublista_izq)
        """
        Nos apoyamos en el extremos izquierdos de
        cada par para comparar eficientemente
        """
        if not (sublista_izq[0] < sublista_der[2]):
            temporal = sublista_izq[2]
            sublista_izq.remove(temporal)
            sublista_izq.insert(0, temporal)

        """
        Como hubo inserción al inicio de la lista entonces la
        referencia a los elementos es la anterior + 1

        Además, como se sabe que el elemento en la posición 0
        es menor que el próximo a comparar ya que esa comparación ya 
        se efectuó entonces nunca puede ser ubicado a la izquierda del mismo
        """        
        if not (sublista_izq[1] < sublista_izq[3]):
            temporal = sublista_izq[3]
            sublista_izq.remove(temporal)
            sublista_izq.insert(1, temporal)

        return sublista_izq

    elif len(sublista_izq) == 3:
        ordenarPar(sublista_izq)

        # Procedemos a comparar con el extremo único
        # Primer elemento del par
        if not (sublista_izq[0] < sublista_izq[2]):
            temporal = sublista_izq[2]
            sublista_izq.remove(temporal)
            sublista_izq.insert(0, temporal)

        # Segundo elemento del par
        if not (sublista_izq[1] < sublista_izq[2]):
            temporal = sublista_izq[2]
            sublista_izq.remove(temporal)
            sublista_izq.insert(1, temporal)

        return sublista_izq

    elif len(sublista_izq) == 2:
        return organizarPares(sublista_izq)

    elif len(sublista_izq) == 1:
        return sublista_izq

    else:
        sublista_izq = ordenarAscendentemente(sublista_izq)

    global lista_prueba
    lista_prueba = sublista_izq


print("Antes: ", lista)
ordenarAscendentemente(lista)
print("Sublista izq: ", lista_prueba)
