import csv 

with open('/Users/hectorbernaltrujillo/Documents/informática/Programación python/ff/evaluacion_tema4/Tema4/pokemon.csv', 'r') as f:
    reader = csv.reader(f)
    lista = list(reader)

#CREAMOS UNA LISTA CON LOS NOMBRES:
nombres= []
for i in range(1, len(lista)):  
    nombres.append(lista[i][1]) #Cogemos la columna 1 que es la de los nombres

#CREAMOS UNA LISTA CON LOS NUMEROS:
numeros= []
for i in range(1, len(lista)): 
    numeros.append(lista[i][0]) #Cogemos la columna 0 que es la de los numeros

#CREAMOS UNA LISTA CON LAS DEBILIDADES:
debilidades= []
for i in range(1, len(lista)): 
    debilidades.append(lista[i][2]) #Cogemos la columna 2 que es la de las debilidades


#CREAMOS EL ARBOL:

class nodoArbol(object):
    
    def __init__(self, info):
        self.info = info
        self.izq = None
        self.der = None

def insertar_nodo(raiz, dato):
    if raiz == None:
        raiz = nodoArbol(dato)
    elif dato < raiz.info:
        raiz.izq = insertar_nodo(raiz.izq, dato)
    else:
        raiz.der = insertar_nodo(raiz.der, dato)
    return raiz

def buscar(raiz,clave):
    pos= None 
    if raiz != None:
        if clave == raiz.info:
            pos = raiz
        elif clave < raiz.info:
            pos = buscar(raiz.izq,clave)
        else:
            pos = buscar(raiz.der,clave)
    return pos

def inorden(raiz): #Recorrido inorden: esta funcion nos debuelve una lista con los datos del arbol en orden de menor a mayor
    if raiz != None:
        inorden(raiz.izq)
        print(raiz.info)
        inorden(raiz.der)
        
