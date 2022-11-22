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
        nodo.izquierda.padre= nodo #el padre del nodo izquierdo es el nodo padre
        nodo.derecha= nodos[1] #el segundo nodo de la lista pasa a ser el hijo derecho del nodo padre
        nodo.derecha.padre= nodo #el padre del nodo derecho es el nodo padre
        nodos=insertar_nodo(nodos, nodo) #insertamos el nodo padre en la lista de nodos
        nodos.pop(1) #eliminamos el primer nodo de la lista
        nodos.pop(0) #eliminamos el segundo nodo de la lista
    return nodos[0] #devolvemos el unico nodo que queda en la lista, que sera la raiz del arbol

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

def codificar(mensaje,raiz):
    '''Funcion que codifica un simbolo en el arbol de huffman'''
    codigo=[]
    mensaje= mensaje[::-1]
    for m in mensaje:
        nodo= buscar(raiz, m)
        while nodo.padre is not None:
            if nodo.padre.izquierda==nodo:
                codigo.append('0')
            else:
                codigo.append('1')
            nodo= nodo.padre
        codigo= codigo[::-1]
        return ''.join(codigo)


def decodificar(codigo,raiz):
    '''Funcion que decodifica un codigo en el arbol de huffman'''
    mensaje=[]
    nodo= raiz
    for c in codigo:
        if nodo.derecha is None: #si el nodo no tiene hijo derecho
            mensaje.append(nodo.simbolo) #añadimos el simbolo del nodo al mensaje
            nodo= raiz #volvemos al nodo raiz
        if c=='0':
            nodo= nodo.izquierda
        else:
            nodo= nodo.derecha
    mensaje.append(nodo.simbolo)
    mensaje= ''.join(mensaje)

    return mensaje

#TODO: REVISAR CODIGO
def main():
    simbolos= ['A', 'F', '1', '3', 'O', 'M', 'T']
    frecuencias= [0.2, 0.17, 0.13, 0.21, 0.05, 0.09, 0.15]
    raiz= arbol_huffman(simbolos, frecuencias)
    mensaje= 'AFO3'
    codigo= codificar(mensaje, raiz)
    print(codigo)
    mensaje= decodificar(codigo, raiz)
    print(mensaje)

if __name__ == '__main__':
    main()

