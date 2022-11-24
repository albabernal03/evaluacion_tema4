import csv 

with open('/Users/hectorbernaltrujillo/Documents/informática/Programación python/ff/evaluacion_tema4/Tema4/pokemon.csv', 'r') as f:
    reader = csv.reader(f)
    lista = list(reader)

#CREAMOS UNA LISTA CON LOS NOMBRES:
nombres= []
for i in range(1, len(lista)): 
    nombres.append(lista[i][1])

#CREAMOS UNA LISTA CON LOS NUMEROS:
numeros= []
for i in range(1, len(lista)): 
    numeros.append(lista[i][0])

#CREAMOS UNA LISTA CON LAS DEBILIDADES:
debilidades= []
for i in range(1, len(lista)):
    debilidades.append(lista[i][2])

    
