#EN EL SIGUIENTE EJERCICIO SE NOS PIDE CREAR TRES ARBOLES, UNO CON LOS NOMBRE, NUMERO Y DEBILIDAD

#Cogemos el csv y lo dividimos en una lista de listas
import csv
with open('/Users/hectorbernaltrujillo/Documents/informática/Programación python/ff/evaluacion_tema4/Tema4/pokemon.csv', 'r') as f:
    reader = csv.reader(f)
    lista = list(reader)

#Creamos una lista con los nombres de los pokemons
nombres = []
for i in range(1, len(lista)):
    nombres.append(lista[i][1])

#Creamos una lista con los numeros de los pokemons
numeros = []
for i in range(1, len(lista)):
    numeros.append(lista[i][0])

#Creamos una lista con las debilidades de los pokemons
debilidades = []
for i in range(1, len(lista)):
    debilidades.append(lista[i][2])



