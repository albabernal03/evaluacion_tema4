#ARBOL DE HUFFMAN
#DATOS:
# 1. Diccionario de simbolos y frecuencias: {A:0.2, F:0.17, 1:0.13, 3:0.21, O:0.05, M:0.09, T:0.15 }

#En primer lugar compruebo que la suma de las frecuencias es 1, si no lo fuera tendría que normalizarlas. Sin embargo, en este caso ya lo están.

#PASAMOS AL CODIGO:

class nodoArbol(object):
    '''Clase para crear un nodo de un arbol'''
    def __init__(self, simbolo,frecuencia):
        self.simbolo= simbolo
        self.frecuencia= frecuencia
        self.izquierda= None
        self.derecha= None
        self.padre= None

def  ordenar_nodos(lista_nodos):
    '''Ordenamos la lista tanto por frecuencia como alfabeticamente'''
    lista_nodos= sorted(lista_nodos, key=lambda x: x.simbolo)
    lista_nodos= sorted(lista_nodos, key=lambda x: x.frecuencia)
    return lista_nodos  

def insertar_nodo(lista_nodos, nodo):
    for i in range(len(lista_nodos)):
        if nodo.frecuencia < lista_nodos[i].frecuencia:
            lista_nodos.insert(i, nodo)
        