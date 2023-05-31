# Autor: Robinson Daniel Clemente Cordoba

# Se realiza algoritmo de ordenación ascendente de forma recursiva


lista = [16, 15, 13, 12, 11, 19, 38, 37, 36,
        35, 34, 33, 32, 8, 7, 6, 5, 4, 3, 2, 1]
         
#lista = [8,6,4,1,7,5,3,2,1]
listas_clasificadas = []

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
        listas_clasificadas.append(sublista_izq)
        print("Sublista izq: ", sublista_izq)

    sublista_der = ordenarAscendentemente(sublista_der)

    if sublista_der is not None:
        listas_clasificadas.append(sublista_der)
        print("Sublista der: ", sublista_der)
    # Hacer el ajuste para que los finalistas ingresen solo en una lista

def insertarPorIzquierdaRecursivamente(punto_de_insercion, lista0, lista1):    
    if len(lista1) > 0:        
        lista0.insert(punto_de_insercion, lista1.pop(0))

    if len(lista1)>0:
        punto_de_insercion += 1
        insertarPorIzquierdaRecursivamente(punto_de_insercion, lista0, lista1)

def insertarPorDerechaRecursivamente(lista0, lista1):    
    if len(lista1) > 0:        
        lista0.append(lista3.pop(0))

    if len(lista1) > 0:        
        insertarPorDerechaRecursivamente(lista0, lista1)
        
#def insertarPorIzquierdaSimple(lista0, lista1):
#    lista0.insert(0, lista1[:])

def insercionIntermediaRecursiva(indice, lista0, lista1):

    if indice < (len(lista0)-1):
        extremo_menor_temporal = lista0[indice]
        extremo_mayor_temporal = lista0[indice+1]
        if len(lista1) >= 1:
            numero = lista1.pop(0)

            """ Se cae en cuenta que se puede utilizar el número nuevo insertado a la lista
            como recurso para ordenar correctamente la lista. Además se sabe que
            el próximo número a ingresar es mayor que el recién ingresado """
            
            # Caso cuando el número es menor que ambos extremos
            if (extremo_menor_temporal > numero) and (extremo_mayor_temporal > numero):
                lista0.insert(indice, numero)
                insercionIntermediaRecursiva(indice, lista0, lista1)
                """Aquí el indice no se aumenta/actualiza debido a que el numero insertado
                   es menor que ambos extremos"""                

            """Caso cuando el número es mayor que el extremo menor, pero menor que el
            extremo mayor (extremo_menor < numero < extremo_mayor)"""
            if (extremo_menor_temporal < numero) and (extremo_mayor_temporal > numero):
                lista0.insert(indice+1, numero)
                indice = lista0.index(numero)
                insercionIntermediaRecursiva(indice, lista0, lista1)
                """ En este caso sí se actualiza el indice debido a que se sabe
                que el próximo numero (si lo hay) a evaluar es mayor que el recién ingresado """

            #Caso cuando el número es mayor que ambos  extremos
            if (extremo_menor_temporal < numero) and (extremo_mayor_temporal < numero):
                """Debido a que el insert añade el elemento en la posición ante-
                rior a la dada, entonces por eso se añade (indice+1)+1) o indice+2. No se usa
                el método append porque no es lo mismo añadir adelante del nuevo
                número ingresado que al final de la lista, ya cuando se añade un
                nuevo elemento, no siempre es al final de la lista.
                 """
                lista0.insert((indice+1)+1, numero)
                indice = lista0.index(numero)
                insercionIntermediaRecursiva(indice, lista0, lista1)


print("Antes: ", lista)
ordenarLista(lista)
print("|-----------------------------|")
# print("Después: ", lista)
print("|------------- FINALISTAS ----------------|")
print(lado_izq)
