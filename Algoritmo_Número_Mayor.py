#Autor: Robinson Daniel Clemente Cordoba

#Se clasifica el número mayor de una lista dada de forma recursiva

lista = [-100,21,23,24,101,6,7,8,9,71,17,102]

def clasificarMayor(lista):

    # Se procede a dividir la lista a la mitad entera    

    mitad = 0

    if len(lista)%2==0:
        # Se parte a la mitad la lista cuando tiene tamaño par
        mitad = len(lista)/2        
    else:
         # Se parte a la lista teniendo en cuenta el tamaño impar
        """Al yo colocar length + 1 hago que la mitad más pequeña quede
        del lado derecho"""
        mitad = (len(lista)+1)/2

    # Pasamos el resultado float a integer 
    mitad = int(mitad)

    
    # Sublista para la primera mitad
    sub_lista_izq = lista[:mitad]
    # Sublista para la segunda mitad
    sub_lista_der = lista[mitad:]

    #Se profundiza por izquierda
    mayor_izq = 0  
    """
    como se llego a length igual a 2 significa que es
    momento de comparar
    """
    if len(sub_lista_izq) == 2:
        if sub_lista_izq[0]>sub_lista_izq[1]:
            mayor_izq = sub_lista_izq[0]            
        else:
            mayor_izq = sub_lista_izq[1] 
        """
        se trata el caso cuando la división genera una sublista de tamaño impar menor a 3,
        es decir cuando el tamaño de la sublista es igual a 1
        """           
    elif len(sub_lista_izq) == 1:
        mayor_izq = sub_lista_izq[0]
        """
        Como el length no es igual a 1 ni a 2, entonces
        es necesario seguir diviendo la sublista
        """
    else:
        mayor_izq = clasificarMayor(sub_lista_izq)
        
    #Se profundiza por derecha
    mayor_der = 0  

    if len(sub_lista_der) == 2:
        if sub_lista_der[0]>sub_lista_der[1]:
            mayor_der = sub_lista_der[0]            
        else:
            mayor_der = sub_lista_der[1]            
    elif len(sub_lista_der) == 1:
        mayor_der = sub_lista_der[0]       
    else:
        mayor_der = clasificarMayor(sub_lista_der)
    
    if mayor_izq > mayor_der:
        return mayor_izq
    else:
        return mayor_der


print("|-------------------- EJECUCIÓN --------------------|")

resultado = clasificarMayor(lista)
print("El número clasificado es: ", resultado)


