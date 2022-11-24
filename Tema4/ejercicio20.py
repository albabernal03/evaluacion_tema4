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





