# Autor: Robinson Daniel Clemente Cordoba

# Se realiza algoritmo de ordenación ascendente de forma recursiva

lista = [16, 15, 13, 12, 11, 19, 38, 37, 36,
       35, 34, 33, 32, 8, 7, 6, 5, 4, 3, 2, 1]
         
#lista = [8,6,4,1,7,7,7,7,1,7,7,7,5,3,2,1]
#lista = [1,2,3,1,2,3,12,3,1,2,3,5,4,1]
#lista = [1,2,3,4,5,6,7,8,9]
#lista.reverse()
#lista = []
sublistas_clasificadas = []

def ordenarPar(indice0, indice1, sublista):
    if not (sublista[indice0] < sublista[indice1]):
        temporal = sublista[indice0]
        sublista[indice0] = sublista[indice1]
        sublista[indice1] = temporal
        
    return sublista

def ordenarParEspecial(indice0, indice1, sublista):
    if not (sublista[indice0] < sublista[indice1]):
        temporal = sublista[indice1]
        sublista.pop(indice1)
        sublista.insert(indice0, temporal)
        
    return  sublista 

def ordenarPares(sublista):
    # Comparamos el primer par y el segundo par
    sublista = ordenarPar(0, 1, sublista)    
    return ordenarPar(2, 3, sublista)

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

def ordenarAscendentemente(lado, sublista):
    if len(sublista) == 4:        
        sublista = ordenarPares(sublista)
        """
        A causa de las pruebas realizadas se utiliza el método
        'ordenarParEspecial' debido a que en algunos casos de
        ordenación resulta más eficiente.
        
        Por ejemplo: si la sublista = [1,2,2,1] el método ya mencionado
        logrará el mismo objetivo más eficientemente.        
        """                  
        #Se comparan los menores entre los pares      
        sublista = ordenarParEspecial(0, 2, sublista)
        #Se comparan los mayores entre los pares         
        sublista = ordenarParEspecial(1, 3, sublista)
        #Se compara el mayor del primer par con el menor del segundo par 
        sublista = ordenarParEspecial(1, 2, sublista)        
        sublistas_clasificadas.append(sublista)
        print("Sublista", lado, ":", sublista)        
    elif len(sublista) == 3:
        """
        Se ordena el primer par y luego se compara cada elemento de dicho par con el
        el último elemento.
        """                
        sublista = ordenarParEspecial(0, 1, sublista)   
        sublista = ordenarParEspecial(0, 2, sublista)   
        sublista = ordenarParEspecial(1, 2, sublista)
        sublistas_clasificadas.append(sublista)
        print("Sublista", lado, ":", sublista) 
    elif len(sublista) == 2:
        sublista = ordenarPar(0, 1, sublista)
        sublistas_clasificadas.append(sublista)
        print("Sublista", lado, ":", sublista) 
    elif len(sublista) == 1:
        sublistas_clasificadas.append(sublista)
        print("Sublista", lado, ":", sublista)             
    else:
        generarSublistas(sublista)                

def insertarPorIzquierdaRecursivamente(punto_de_insercion, lista0, lista1):    
    if len(lista1) > 0:        
        lista0.insert(punto_de_insercion, lista1.pop(0))

    if len(lista1) > 0:
        punto_de_insercion += 1
        insertarPorIzquierdaRecursivamente(punto_de_insercion, lista0, lista1)

def insertarPorDerechaRecursivamente(lista0, lista1):    
    if len(lista1) > 0:        
        lista0.append(lista1.pop(0))

    if len(lista1) > 0:        
        insertarPorDerechaRecursivamente(lista0, lista1)
        
"""
Este método busca el último numero repetido del indice actual (la busqueda se
hace de derecha a izquierda). Este método no es usado debido a que hace parte
de la lógica del método insercionIntermediaRecursivaMejorada el cual fue reem-
plazado por el método insercionIntermediaRecursivaSimplificada.
"""
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

"""
Este método busca el próximo número de la lista de izquierda a derecha(a partir
del indice dado) que sea mayor que el numero a insertar.
"""
def encontrarProximoMayorIgual(indice, numero, sublista0):    
    if numero <= sublista0[indice]:
        return indice
    else:
        """
        Aquí se verifica que el indice a retornar no se salga del rango  de la
        lista
        """       
        if (indice+1) < len(sublista0):
            indice += 1
            return encontrarProximoMayorIgual(indice, numero, sublista0)
        else:
            return indice
"""
Método desusado se conserva por motivos comparativos (véase y compárese con el
método insercionIntermediaRecursivaSimplificada).
"""
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
        
        """if numero > sublista0[indice] and numero < sublista0[indice+1]:
            sublista0.insert(indice+1, numero)            
        elif numero > sublista0[indice] and numero > sublista0[indice+1]:
        """
        """
            Aquí se podría llamar a un método que empiece a aumentar el indice
            hasta que consiga el numero que es mayor que él y lo agrege delante
            de este, sino lo consigue, entonces se usa lista0.append(numero)
            
            La idea anterior se podría lograr con el método
            encontrarUltimoNumeroIndiceRepetido
        """
        """             sublista0.insert(indice+2, numero)                                  
        elif numero < sublista0[indice] and numero < sublista0[indice+1]:
            sublista0.insert(indice, numero)
        elif numero <= sublista0[indice] and numero < sublista0[indice+1]:
             sublista0.insert(indice, numero)
        elif numero <= sublista0[indice] and numero <= sublista0[indice+1]:
            sublista0.insert(indice, numero)
        """        
        
        indice = encontrarProximoMayorIgual(indice, numero, sublista0)
        sublista0.insert(indice, numero)

def insercionIntermediaRecursivaSimplificada(indice, sublista0, sublista1):
    """
    A diferencia del método anterior, al limitarse el uso de sublista1.pop(0)
    dentro del condicional y dentro del presente método hace que el código
    solo necesite de un condicional, ya que el cambio de estado del tamaño
    de la lista solo ocurre dentro de estos.
        
    Este método usa una lógica mucho más sencilla para realizar la inserción:
    Simplemente busca de izquierda a derecha (a partir del valor del indice)
    el número mayor al sacado de la sublista1 y lo inserta dependiendo si el
    numero indice es mayor o menor o igual.
    """        
    if (indice < len(sublista0)) and (len(sublista1) >= 1):    
        numero = sublista1.pop(0)
        indice = encontrarProximoMayorIgual(indice, numero, sublista0)
        """
        Aquí no importa si el número está repetido porque si el numero
        a insertar es menor o igual la inserción se haría en la primera ocurrencia
        de numeros repetidos de la sublista0. Ni tampoco si el numero a insertar
        es mayor, porque como siempre el métodoencontrarProximoMayorIgual busca
        el mayor o igual y si este no existe, entonces retorna el índice del 
        último valor comparado (el cual es el mayor) para permitir la inserción
        intermedia por derecha.
        """
        if numero <= sublista0[indice]:
            sublista0.insert(indice, numero)
            insercionIntermediaRecursivaSimplificada(indice, sublista0, sublista1)
        else:            
            sublista0.insert(indice+1, numero)
            insercionIntermediaRecursivaSimplificada(indice, sublista0, sublista1)
                 
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
    else:   
        insercionIntermediaRecursivaSimplificada(0, sublista0, sublista1)
    
    return sublista0

def generarSublistas(lista):     
    sublistas = dividirLista(lista)
    sublista_izq = sublistas[0]
    sublista_der = sublistas[1]        
    
    # Por izquierda    
    ordenarAscendentemente("izq", sublista_izq)
        
    # Por derecha    
    ordenarAscendentemente("der", sublista_der)
   
def fusionarSublistas(finalistas):    
    if len(finalistas) > 1:        
        lista = evaluarExtremosEInsertar(finalistas.pop(0), finalistas.pop(0))
        finalistas.append(lista)
        fusionarSublistas(finalistas)
               
def iniciar():    
    if len(lista) > 1:               
        print("|---------------- ANTES ----------------|")
        print(lista)
        print("|--------------- FINALISTAS ---------------|")
        generarSublistas(lista)
        print("Finalistas: ", sublistas_clasificadas)
        print("|------------- LISTA ORDENADA -------------|")    
        fusionarSublistas(sublistas_clasificadas)
        print(sublistas_clasificadas[0])                
    elif len(lista) == 1:
        print("La lista necesita al menos 2 elementos")
    else:
        print("La lista está vacía")    
        
iniciar()

