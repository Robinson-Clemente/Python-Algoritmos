# Autor: Robinson Daniel Clemente Cordoba

# Se realiza algoritmo de ordenación ascendente de forma recursiva


#lista = [16, 15, 13, 12, 11, 19, 38, 37, 36,
        #35, 34, 33, 32, 8, 7, 6, 5, 4, 3, 2, 1]
         
#lista = [8,6,4,1,7,5,3,2,1]
lista = [1,2,1,2,1,2,1,2,1,2,1,2]
sublistas_clasificadas = []

def ordenarPar(indice0, indice1, sublista):
    if not (sublista[indice0] < sublista[indice1]):
        temporal = sublista[indice0]
        sublista[indice0] = sublista[indice1]
        sublista[indice1] = temporal

    return sublista

def ordenarPares(sublista):
    # Comparamos el primer par y el segundo par
    sublista = ordenarPar(0, 1, sublista)    
    return ordenarPar(2, 3, sublista) 
        
""" def ordenarTriplete(indice0, indice1, sublista):
    if not (sublista[indice0] < sublista[indice1]):       
            temporal = sublista[indice1]
            sublista.remove(temporal)
            sublista.insert(indice0, temporal)            
    return sublista """

# Este método debe ser llamado estando ya los pares ordenados

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

        sublista = ordenarPares(sublista)

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

        #ordenarPar(0, 1, sublista)

        # Procedemos a comparar con el extremo único
        # Primer elemento del par
        """
        if not (sublista[0] < sublista[2]):
            temporal = sublista[2]
            sublista.remove(temporal)
            sublista.insert(0, temporal)

        # Segundo elemento del primer par
        if not (sublista[1] < sublista[2]):
            temporal = sublista[2]
            sublista.remove(temporal)
            sublista.insert(1, temporal)
        """
            
        sublista = ordenarPar(0, 1, sublista)   
        sublista = ordenarPar(0, 2, sublista)   
        return ordenarPar(1, 2, sublista)

    elif len(sublista) == 2:
        return ordenarPar(0, 1, sublista)

    elif len(sublista) == 1:
        return sublista

    else:
        sublista = ordenarLista(sublista)
        return sublista

def insertarPorIzquierdaRecursivamente(punto_de_insercion, lista0, lista1):    
    if len(lista1) > 0:        
        lista0.insert(punto_de_insercion, lista1.pop(0))

    if len(lista1) > 0:
        punto_de_insercion += 1
        insertarPorIzquierdaRecursivamente(punto_de_insercion, lista0, lista1)

def insertarPorDerechaRecursivamente(lista0, lista1):    
    if len(lista1) > 0:        
        lista0.append(lista3.pop(0))

    if len(lista1) > 0:        
        insertarPorDerechaRecursivamente(lista0, lista1)

def encontrarUltimoExtremoMayorRepetido(contador, extremo_mayor, sublista0):
    numero = 0
    indice = (len(sublista0) - 1) - contador
        
    if contador == 0:
        numero = sublista0[len(sublista0) - 1]
    else:
        numero = sublista0[indice]                      
        
    if numero == extremo_mayor:
        return indice
    else:
        contador += 1     
        return encontrarUltimoExtremoMayorRepetido(contador, extremo_mayor, sublista0)

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
                """
                Como se insertó un número por izquierda, entonces debe actualizarse
                el índice para no perder el extremo menor temporal de referencia
                """
                indice += 1
                insercionIntermediaRecursiva(indice, lista0, lista1)                         

            """Caso cuando el número es mayor que el extremo menor, pero menor que el
            extremo mayor (extremo_menor < numero < extremo_mayor)"""
            if (extremo_menor_temporal < numero) and (extremo_mayor_temporal > numero):
                lista0.insert(indice+1, numero)
                """
                # El indice se actualiza ya que el extremo menor fue superado
                y se sabe que si hay un próximo numero será mayor que este nuevo
                extremo temporal
                """                
                indice = lista0.index(numero)
                insercionIntermediaRecursiva(indice, lista0, lista1)
                """ En este caso sí se actualiza el indice debido a que se sabe
                que el próximo numero (si lo hay) a evaluar es mayor que el recién ingresado """

            # Caso cuando el número es igual al extremo menor
            if extremo_menor_temporal == numero:
                lista0.insert(indice+1, numero) # indice+1 para que el insert lo añada delante del extremo menor
                indice = lista0.index(numero, indice+1) #para que retorne el index por delante del extremo menor
                #ya que al haber valores repetidos puede retornar un indice incorrecto
                insercionIntermediaRecursiva(indice, lista0, lista1)

            # Caso cuando el número es igual al extremo al extremo mayor
            if extremo_mayor_temporal == numero:
                lista0.insert(indice+2, numero) # indice para que el insert lo añada delante del extremo mayor
                indice = lista0.index(numero, indice+2) #para que retorne el index delante del extremo mayor
                #ya que al haber valores repetidos puede retornar un indice incorrecto
                insercionIntermediaRecursiva(indice, lista0, lista1)                

            #Caso cuando el número es mayor que ambos  extremos
            if (extremo_menor_temporal < numero) and (extremo_mayor_temporal < numero):
                """Debido a que el insert añade el elemento en la posición ante-
                rior a la dada, entonces por eso se añade (indice+1)+1) o indice+2. No se usa
                el método append porque no es lo mismo añadir adelante del nuevo número ingresado 
                que al final de la lista, ya cuando se añade un nuevo elemento, no siempre es
                al final de la lista. Tengo que verificar que esto es así.

                #Aquí hay un aspecto a corregir, tienes que validar que el extremo mayor no esté
                repetido, porque si es el caso, entonces tienes que añadir el número al final de
                la lista. Recuerda el extremo mayor es el número mayor de la lista independiente-
                mente si está repetido o no. Esto mismo debe analizarse para el extremo menor.

                """
                                                
                # Se deben hacer las pruebas para la inserción intermedia por izquierda con el extremo menor repetido
                
                """
                    Se verifica que el extremo mayor no esté repetido
                """
                                
                # Se verifica que exista un número después del extremo mayor temporal en la lista
                if (lista0.index(extremo_mayor_temporal)+1) < len(lista0):
                    proximo = lista0[lista0.index(extremo_mayor_temporal)+1]
                    if proximo == extremo_mayor_temporal:
                        # Este indice es el del extremo mayor temporal, no del menor como es común
                        indice_extremo_mayor = encontrarUltimoExtremoMayorRepetido(0, extremo_mayor_temporal, lista0)
                        lista0.insert(indice_extremo_mayor+1, numero) 
                    else:
                        lista0.insert((indice+2), numero)
                        indice = lista0.index(numero)
                        insercionIntermediaRecursiva(indice, lista0, lista1)

def encontrarUltimoNumeroIndiceRepetido(contador, numero_indice, sublista0):
    
    numero = 0
   
    indice = (len(sublista0) - 1) - contador
        
    if contador == 0:
        numero = sublista0[len(sublista0) - 1]
    else:
        numero = sublista0[indice]                      
        
    if numero == numero_indice:
        return indice
    else:
        contador += 1     
        return encontrarUltimoNumeroIndiceRepetido(contador, numero_indice, sublista0)

def insercionIntermediaRecursivaMejorada(indice, numero, sublista0, sublista1):

    if indice < (len(sublista0) - 1) and len(sublista1) >= 1:
        """ Corresponde tratar el caso cuando la lista0 tiene menos elementos que la lista1
        y ya se llegó al final """

        """ Se cae en cuenta que se puede utilizar el número nuevo insertado a la lista
        como recurso para ordenar correctamente la lista. Además se sabe que
        el próximo número a ingresar es mayor que el recién ingresado """

        # Caso cuando el número es menor que el índice (se debe tratar el caso de índice repetido)
        # Sea el número menor o igual al número del indice, se inserta por izquierda
        if numero <= sublista0[indice]:
            sublista0.insert(indice, numero)
            # Como se insertó un nuevo número, se necesita actualizar el indice
            indice += 1
            numero = sublista1.pop(0)
            insercionIntermediaRecursivaMejorada(
                indice, numero, sublista0, sublista1)
        # Caso cuando el número es mayor al índice (se debe tratar el caso de índice repetido)
        elif numero > sublista0[indice]:
            # Se verifica que el indice está actualizado correctamente (por causa de repetidos)
            if sublista0[indice] == sublista0[indice+1]:
                indice = encontrarUltimoNumeroIndiceRepetido(
                    0, sublista0[indice], sublista0)                
                insercionIntermediaRecursivaMejorada(
                    indice, numero, sublista0, sublista1)
            else:
                if numero < sublista0[indice+1]:
                    sublista0.insert(indice+1, numero)
                    numero = sublista1.pop(0)
                    # Se aumenta nuevamente el indice para que se ubique adecuadamente
                    indice += 1
                    insercionIntermediaRecursivaMejorada(
                        indice, numero, sublista0, sublista1)
                elif numero == sublista0[indice+1]:
                    sublista0.insert(indice+1, numero)
                    numero = sublista1.pop(0)
                    indice += 1
                    insercionIntermediaRecursivaMejorada(
                        indice, numero, sublista0, sublista1)
                else:
                    # Aquí el aumento +1 del indice cubre solo el aspecto de la actualización
                    indice += 1
                    insercionIntermediaRecursivaMejorada(
                        indice, numero, sublista0, sublista1)
        """
        Caso cuando se está en el último elemento de la primera lista pero la segunda
        todavía tiene elementos.
        """
    elif indice == (len(sublista0) - 1) and len(sublista1) >= 1:        
        if numero > sublista0[indice]:
            sublista0.append(numero)            
            insertarPorDerechaRecursivamente(sublista0, sublista1)
        else:
            sublista0.insert(indice, numero)
            indice += 1
            numero = sublista1.pop(0)
            insercionIntermediaRecursivaMejorada(
                indice, numero, sublista0, sublista1)

    elif indice == (len(sublista0) - 1) and len(sublista1) == 0:
        if numero <= sublista0[indice]:
            sublista0.insert(indice, numero)
        else:
            sublista0.append(numero)
                        
    elif indice < (len(sublista0)) and len(sublista1) == 0:
        
        if numero > sublista0[indice] and numero < sublista0[indice+1]:
            sublista0.insert(indice+1, numero)            
        elif numero > sublista0[indice] and numero > sublista0[indice+1]:
            """
            Aquí se podría llamar a un método que empiece a aumentar el indice
            hasta que consiga el numero que es mayor que él y lo agrege delante
            de este, sino lo consigue, entonces se usa lista0.append(numero)
            """
            sublista0.insert(indice+2, numero)                        
        else:
            sublista0.insert(indice, numero)                   

def evaluarExtremosEInsertar(sublista0, sublista1):
    #Se definen los extremos de la primera sublista
    extremo_menor_0 = sublista0[0]
    extremo_mayor_0 = sublista0[len(sublista0)-1]

    #Se definen los extremos de la segunda sublista
    extremo_menor_1 = sublista1[0]
    extremo_mayor_1 = sublista1[len(sublista1)-1]
    """
    Caso cuando el extremo mayor de la sublista1 es menor que el extremo menor
    de la sublista0
    """
    if extremo_mayor_1 < extremo_menor_0:
        insertarPorIzquierdaRecursivamente(0, sublista0, sublista1)
        """
        Caso cuando el extremo menor de la sublista1 es mayor que el extremo mayor
        de la sublista0
        """        
    elif extremo_menor_1 > extremo_mayor_0:
        insertarPorDerechaRecursivamente(sublista0, sublista1)
        """
        independientemente si la inserción intermedia es por izquierda o por derecha,
        al utilizar un número como cota inferior y otro como cota superior, es posible determinar
        especificamente dónde va a ser insertado el número evaluado. Es por esto que la inser-
        ción intermedia no necesita especificar casos especificos (por izquierda o por derecha).
        """
    else:
        numero = sublista1.pop(0)
        insercionIntermediaRecursivaMejorada(0, numero, sublista0, sublista1)
        
    """
    #Este es el caso cuando la inserción intermedia se da por la izquierda        
    elif ((extremo_menor_0 >= extremo_menor_1 and extremo_menor_0 <= extremo_mayor_1) 
    and (extremo_mayor_0 > extremo_menor_1 and extremo_mayor_0 >= extremo_mayor_1)): 
        insercionIntermediaRecursiva(0, sublista0, sublista1)
    """    
    """
    #Este es el caso cuando la inserción intermedia se da por la derecha    
    elif ((extremo_menor_0 <= extremo_menor_1 and extremo_menor_0 <= extremo_mayor_1) 
    and (extremo_mayor_0 > extremo_menor_1 and extremo_mayor_0 <= extremo_mayor_1)):
        insercionIntermediaRecursiva(0, sublista0, sublista1)
    """
    
def ordenarLista(lista):

    sublistas = dividirLista(lista)
    sublista_izq = sublistas[0]
    sublista_der = sublistas[1]

    print("|-----------------------------|")
    sublista_izq = ordenarAscendentemente(sublista_izq)

    if sublista_izq is not None:
        sublistas_clasificadas.append(sublista_izq)
        print("Sublista izq: ", sublista_izq)
        

    sublista_der = ordenarAscendentemente(sublista_der)

    if sublista_der is not None:
        sublistas_clasificadas.append(sublista_der)
        print("Sublista der: ", sublista_der)
        
    
    """
        Es posible que aquí se añada la lógica para que al acabarse las llamadas
        entonces se ejecute la lógica para organizar los finalistas, así evito
        recorrer el "arbol" dos veces. Es decir, si cuando el proceso recursivo
        termina este empieza a devolverse de donde terminó, ¿por qué no aprove-
        char esa oportunidad para ser más eficiente? ¿O es más rápido utilizar 
        los hilos con la lista de sublistas clasificadas? ¿o por qué no utili-
        zar los hilos al menos en la división principal de la lista inicial?
    """

                        
print("Antes: ", lista)
ordenarLista(lista)
#print("|-----------------------------|")
# print("Después: ", lista)
print("|------------- FINALISTAS ----------------|")
print(sublistas_clasificadas)
