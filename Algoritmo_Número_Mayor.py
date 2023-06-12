#Autor: Robinson Daniel Clemente Cordoba

#Se clasifica el número mayor de una lista dada de forma recursiva

"""
Notas: - Este código necesita ser mejorado. Solo basta el método desarrollado
para recorrer tanto por izquierda como por derecha.
"""

lista = [-100,21,23,24,101,6,7,8,9,71,17,500]
lista = [1,2]
def clasificarMayorFormaUno(lista):   
    # Se procede a dividir la lista a la mitad entera
    mitad = 0
    
    if len(lista) % 2 == 0:
        # Se parte a la mitad la lista cuando tiene tamaño par
        mitad = len(lista) / 2        
    else:
         # Se parte la lista teniendo en cuenta el tamaño impar
        """Al yo colocar length + 1 hago que la mitad más pequeña quede
        del lado derecho"""
        mitad = (len(lista)+1) / 2

    # Pasamos el resultado float a integer 
    mitad = int(mitad)       
    # Sublista para la primera mitad
    sublista_izq = lista[:mitad]
    # Sublista para la segunda mitad
    sublista_der = lista[mitad:]

    #Se profundiza por izquierda
    mayor_izq = 0  
    
    #como se llego a length igual a 2 significa que es momento de comparar        
    if len(sublista_izq) == 2:        
        if sublista_izq[0] > sublista_izq[1]:            
            mayor_izq = sublista_izq[0]            
        else:            
            mayor_izq = sublista_izq[1] 
        """
        se trata el caso cuando la división genera una sublista de tamaño impar menor a 3,
        es decir cuando el tamaño de la sublista es igual a 1.
        """
               
    elif len(sublista_izq) == 1:
        if sublista_izq[0] > mayor_izq:            
            mayor_izq = sublista_izq[0]
        """
        Como el length no es igual a 1 ni a 2, entonces
        es necesario seguir diviendo la sublista
        """    
    else:                
        mayor_izq = clasificarMayorFormaUno(sublista_izq)
                
    #Se profundiza por derecha
    mayor_der = 0  
    
    if len(sublista_der) == 2:        
        if sublista_der[0]>sublista_der[1]:                        
            mayor_der = sublista_der[0]            
        else:            
            mayor_der = sublista_der[1]               
    elif len(sublista_der) == 1:
        if sublista_der[0] > mayor_der:            
            mayor_der = sublista_der[0]     
    else:
        mayor_der = clasificarMayorFormaUno(sublista_der)        
            
    if mayor_izq > mayor_der:                
        return mayor_izq
    else:                
        return mayor_der

def encontrarMayorFormaDos(indice, mayor, sublista0):
    if indice < len(sublista0):
        if sublista0[indice] > mayor:
            mayor = sublista0[indice]
            indice += 1
            mayor = encontrarMayorFormaDos(indice, mayor, sublista0)
        else:
            indice += 1
            mayor = encontrarMayorFormaDos(indice, mayor, sublista0)
    return mayor

def iniciar():
    if len(lista) > 1:
        print("|-------------------- PRIMER MÉTODO --------------------|")
        resultado = clasificarMayorFormaUno(lista)
        print("El número clasificado es:", resultado)
        print("|-------------------- SEGUNDO MÉTODO --------------------|")
        resultado = encontrarMayorFormaDos(0, 0, lista)
        print("El número clasificado es:", resultado)
    else:
        print("La lista necesita al menos 2 elementos")
                
iniciar()
