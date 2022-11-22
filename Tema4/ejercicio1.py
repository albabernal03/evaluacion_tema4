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
        if i== len(lista_nodos)-1: #Si llegamos al final de la lista y no hemos insertado el nodo, lo insertamos al final de la lista
            lista_nodos.append(nodo)
            break
    return lista_nodos

def arbol_huffman(simbolos, frecuencias):
    '''Funcion que crea un arbol de huffman a partir de una lista de simbolos y una lista de frecuencias'''
    nodos=[]
    for i in range(len(simbolos)):
        nodos.append(nodoArbol(simbolos[i], frecuencias[i])) #con esto creamos una lista de nodos con los simbolos y frecuencias(desordenados)
    nodos= ordenar_nodos(nodos) #ordenamos la lista de nodos
    while len(nodos)>1: #mientras haya mas de un nodo en la lista
        nodo= nodoArbol('XX', nodos[0].frecuencia + nodos[1].frecuencia) #creamos un nodo padre con la suma de las frecuencias de los dos primeros nodos
        nodo.izquierda= nodos[0] #el primer nodo de la lista pasa a ser el hijo izquierdo del nodo padre
        nodo.derecha= nodos[1] #el segundo nodo de la lista pasa a ser el hijo derecho del nodo padre
        nodos[0].padre= nodo #el nodo padre pasa a ser el padre del primer nodo de la lista
        nodos[1].padre= nodo #el nodo padre pasa a ser el padre del segundo nodo de la lista
        nodos= nodos[2:] #eliminamos los dos primeros nodos de la lista
        nodos= insertar_nodo(nodos, nodo) #insertamos el nodo padre en la lista de nodos

    return nodos[0] #devolvemos el nodo raiz del arbol

def buscar(raiz, clave):
    '''Funcion que busca un simbolo en el arbol de huffman'''
    pos= None

    if raiz is not None:
        if raiz.simbolo == clave:
            pos= raiz
            return pos
        if pos is None:
            pos= buscar(raiz.izquierda, clave)
        if pos is None:
            pos= buscar(raiz.derecha, clave)
    return pos

def comprimir(mensaje,raiz):
    codigo=[]
    mensaje

