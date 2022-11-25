
#ENUNCIADO: Se requiere implementar un grafo no dirigido, para almacenar las siete maravillas arquitectonicas modernas y naturales del mundo. Para ello, se pide:
#De cada maravilla se conoce su nombre, su localización y el tipo( natural o arquitectónica).
#Cada una debe estar relacionada con las otras seis de su tipo, para lo cual se conoce la distancia entre ellas.
#hallar el arbol de expansión minima de cada tipo de maravilla.
#determinar si existen paises que tengan maravillas arquitectónicas y naturales.
#determinar si algun pais tiene mas de una maravilla de cada tipo.


class NodoArista(object):
    def __init__(self, peso, destino):
        self.peso= peso #peso: peso de la arista
        self.destino = destino
        self.sig = None

class NodoVertice(object):
    def __init__(self, nombre, pais, tipo):
        self.nombre = nombre
        self.pais = pais
        self.tipo = tipo
        self.sig= None 
        self.visitado = False
        self.adyacentes = Arista()

class Grafo():
    def __init__(self, dirigido=False):
        self.inicio = None 
        self.tam = 0
        self.dirigido = dirigido

class Arista():
    def __init__(self):
        self.inicio = None 
        self.tam = 0
    
def insertar_vertice(grafo, nombre, pais, tipo):
    nodo= NodoVertice(nombre, pais, tipo) 
    if grafo.inicio == None or grafo.inicio.nombre > nombre:  #si la lista esta vacia o el dato es menor que el primero
        nodo.sig = grafo.inicio 
        grafo.inicio = nodo 
    else:
        ant= grafo.inicio #insertamos al principio
        act= grafo.inicio.sig #actualizamos el inicio
        while act != None and act.nombre < nombre:  
            ant= act 
            act= act.sig
        nodo.sig= act 
        ant.sig= nodo
    grafo.tam += 1


def insertar_arista(grafo, origen, destino, peso):
    nodo= NodoArista(peso, destino)
    origen= buscar_vertice(grafo, origen)[0]  
    destino= buscar_vertice(grafo, destino)[0]

    if origen.adyacentes.inicio == None:
        nodo.sig = origen.adyacentes.inicio
        origen.adyacentes.inicio = nodo
    else:
        ant = origen.adyacentes.inicio
        act= origen.adyacentes.inicio.sig
        while act != None:
            ant = act
            act = act.sig
        nodo.sig = act
        ant.sig = nodo
    origen.adyacentes.tam += 1
    return grafo


def buscar_vertice(grafo, dato):
    sol = []
    aux = grafo.inicio
    while aux is not None:
        if aux.nombre != dato and dato not in aux.pais and aux.tipo != dato:
            aux = aux.sig
        else:
            sol.append(aux)
            aux = aux.sig
    return sol

def kruskal(grafo, tipo):
    arbol = Grafo()
    arbol.dirigido = True
    arbol.inicio = grafo.inicio
    arbol.tam = grafo.tam
    aristas = []
    for i in range(grafo.tam):
        aux = grafo.inicio
        while aux is not None:
            if aux.tipo == tipo:
                aux2 = aux.adyacentes.inicio
                while aux2 is not None:
                    aristas.append((aux2.peso, aux.nombre, aux2.destino))
                    aux2 = aux2.sig
            aux = aux.sig
    aristas.sort()
    for i in range(len(aristas)):
        if buscar_vertice(arbol, aristas[i][1])[0].visitado == False or buscar_vertice(arbol, aristas[i][2])[0].visitado == False:
            arbol = insertar_arista(arbol, aristas[i][1], aristas[i][2], aristas[i][0])
            buscar_vertice(arbol, aristas[i][1])[0].visitado = True
            buscar_vertice(arbol, aristas[i][2])[0].visitado = True
    return arbol

#determinar si existen paises que tengan maravillas arquitectónicas y naturales.
def pais_con_maravilla_arquitectonica_y_natural(grafo):
    lista = []
    aux = grafo.inicio
    while aux is not None:
        if aux.tipo == "Arquitectonica":
            lista.append(aux.pais)
        aux = aux.sig
    aux = grafo.inicio
    while aux is not None:
        if aux.tipo == "Natural" and aux.pais in lista:
            lista.append(aux.pais)
        aux = aux.sig
    return lista

#determinar si algun pais tiene mas de una maravilla de cada tipo.

#def pais_con_mas_de_una_maravilla(grafo):
    #esta no la necesitamos pues hay solo una en cada pais
   

def crear_grafo(grafo):
    insertar_vertice(grafo, "Chichen Itza", "Mexico", "Arquitectonica")
    insertar_vertice(grafo, "Machu Picchu", "Peru", "Arquitectonica")
    insertar_vertice(grafo, "Petra", "Jordania", "Arquitectonica")
    insertar_vertice(grafo, "Coliseo", "Italia", "Arquitectonica")
    insertar_vertice(grafo, "Taj Mahal", "India", "Arquitectonica")
    insertar_vertice(grafo, "Cristo Redentor", "Brasil", "Arquitectonica")
    insertar_vertice(grafo, "Gran Muralla China", "China", "Arquitectonica")

    insertar_vertice(grafo, "Rio Amazonas", "Brasil", "Natural")
    insertar_vertice(grafo, "Cataratas del Iguazu", "Argentina", "Natural")
    insertar_vertice(grafo, "Cataratas Victoria", "Zambia", "Natural")
    insertar_vertice(grafo, "Monte Everest", "Nepal", "Natural")
    insertar_vertice(grafo, "Cueva de las Manos", "Argentina", "Natural")
    insertar_vertice(grafo, "Cueva de las Maravillas", "Mexico", "Natural")
    insertar_vertice(grafo, "Cueva de las Ventanas", "Argentina", "Natural")

    insertar_arista(grafo, "Chichen Itza", "Machu Picchu", 1000)
    insertar_arista(grafo, "Chichen Itza", "Petra", 2000)
    insertar_arista(grafo, "Chichen Itza", "Coliseo", 3000)
    insertar_arista(grafo, "Chichen Itza", "Taj Mahal", 4000)
    insertar_arista(grafo, "Chichen Itza", "Cristo Redentor", 5000)
    insertar_arista(grafo, "Chichen Itza", "Gran Muralla China", 6000)
    
    insertar_arista(grafo, "Machu Picchu", "Chichen Itza", 1000)
    insertar_arista(grafo, "Machu Picchu", "Petra", 2000)
    insertar_arista(grafo, "Machu Picchu", "Coliseo", 3000)
    insertar_arista(grafo, "Machu Picchu", "Taj Mahal", 4000)
    insertar_arista(grafo, "Machu Picchu", "Cristo Redentor", 5000)
    insertar_arista(grafo, "Machu Picchu", "Gran Muralla China", 6000)

    insertar_arista(grafo, "Petra", "Chichen Itza", 2000)
    insertar_arista(grafo, "Petra", "Machu Picchu", 2000)
    insertar_arista(grafo, "Petra", "Coliseo", 3000)
    insertar_arista(grafo, "Petra", "Taj Mahal", 4000)
    insertar_arista(grafo, "Petra", "Cristo Redentor", 5000)
    insertar_arista(grafo, "Petra", "Gran Muralla China", 6000)


    insertar_arista(grafo, "Coliseo", "Chichen Itza", 3000)
    insertar_arista(grafo, "Coliseo", "Machu Picchu", 3000)
    insertar_arista(grafo, "Coliseo", "Petra", 3000)
    insertar_arista(grafo, "Coliseo", "Taj Mahal", 4000)
    insertar_arista(grafo, "Coliseo", "Cristo Redentor", 5000)
    insertar_arista(grafo, "Coliseo", "Gran Muralla China", 6000)


    insertar_arista(grafo, "Taj Mahal", "Chichen Itza", 4000)
    insertar_arista(grafo, "Taj Mahal", "Machu Picchu", 4000)
    insertar_arista(grafo, "Taj Mahal", "Petra", 4000)
    insertar_arista(grafo, "Taj Mahal", "Coliseo", 4000)
    insertar_arista(grafo, "Taj Mahal", "Cristo Redentor", 5000)
    insertar_arista(grafo, "Taj Mahal", "Gran Muralla China", 6000)


    insertar_arista(grafo, "Cristo Redentor", "Chichen Itza", 5000)
    insertar_arista(grafo, "Cristo Redentor", "Machu Picchu", 5000)
    insertar_arista(grafo, "Cristo Redentor", "Petra", 5000)
    insertar_arista(grafo, "Cristo Redentor", "Coliseo", 5000)
    insertar_arista(grafo, "Cristo Redentor", "Taj Mahal", 5000)
    insertar_arista(grafo, "Cristo Redentor", "Gran Muralla China", 6000)


    insertar_arista(grafo, "Gran Muralla China", "Chichen Itza", 6000)
    insertar_arista(grafo, "Gran Muralla China", "Machu Picchu", 6000)
    insertar_arista(grafo, "Gran Muralla China", "Petra", 6000)
    insertar_arista(grafo, "Gran Muralla China", "Coliseo", 6000)
    insertar_arista(grafo, "Gran Muralla China", "Taj Mahal", 6000)
    insertar_arista(grafo, "Gran Muralla China", "Cristo Redentor", 6000)


    insertar_arista(grafo, "Rio Amazonas", "Cataratas del Iguazu", 1000)
    insertar_arista(grafo, "Rio Amazonas", "Cataratas Victoria", 2000)
    insertar_arista(grafo, "Rio Amazonas", "Monte Everest", 3000)
    insertar_arista(grafo, "Rio Amazonas", "Cueva de las Manos", 4000)
    insertar_arista(grafo, "Rio Amazonas", "Cueva de las Maravillas", 5000)
    insertar_arista(grafo, "Rio Amazonas", "Cueva de las Ventanas", 6000)

    insertar_arista(grafo, "Cataratas del Iguazu", "Rio Amazonas", 1000)
    insertar_arista(grafo, "Cataratas del Iguazu", "Cataratas Victoria", 2000)
    insertar_arista(grafo, "Cataratas del Iguazu", "Monte Everest", 3000)
    insertar_arista(grafo, "Cataratas del Iguazu", "Cueva de las Manos", 4000)
    insertar_arista(grafo, "Cataratas del Iguazu", "Cueva de las Maravillas", 5000)
    insertar_arista(grafo, "Cataratas del Iguazu", "Cueva de las Ventanas", 6000)

    insertar_arista(grafo, "Cataratas Victoria", "Rio Amazonas", 2000)
    insertar_arista(grafo, "Cataratas Victoria", "Cataratas del Iguazu", 2000)
    insertar_arista(grafo, "Cataratas Victoria", "Monte Everest", 3000)
    insertar_arista(grafo, "Cataratas Victoria", "Cueva de las Manos", 4000)
    insertar_arista(grafo, "Cataratas Victoria", "Cueva de las Maravillas", 5000)
    insertar_arista(grafo, "Cataratas Victoria", "Cueva de las Ventanas", 6000)

    insertar_arista(grafo, "Monte Everest", "Rio Amazonas", 3000)
    insertar_arista(grafo, "Monte Everest", "Cataratas del Iguazu", 3000)
    insertar_arista(grafo, "Monte Everest", "Cataratas Victoria", 3000)
    insertar_arista(grafo, "Monte Everest", "Cueva de las Manos", 4000)
    insertar_arista(grafo, "Monte Everest", "Cueva de las Maravillas", 5000)
    insertar_arista(grafo, "Monte Everest", "Cueva de las Ventanas", 6000)


    insertar_arista(grafo, "Cueva de las Manos", "Rio Amazonas", 4000)
    insertar_arista(grafo, "Cueva de las Manos", "Cataratas del Iguazu", 4000)
    insertar_arista(grafo, "Cueva de las Manos", "Cataratas Victoria", 4000)
    insertar_arista(grafo, "Cueva de las Manos", "Monte Everest", 4000)
    insertar_arista(grafo, "Cueva de las Manos", "Cueva de las Maravillas", 5000)
    insertar_arista(grafo, "Cueva de las Manos", "Cueva de las Ventanas", 6000)

    insertar_arista(grafo, "Cueva de las Maravillas", "Rio Amazonas", 5000)
    insertar_arista(grafo, "Cueva de las Maravillas", "Cataratas del Iguazu", 5000)
    insertar_arista(grafo, "Cueva de las Maravillas", "Cataratas Victoria", 5000)
    insertar_arista(grafo, "Cueva de las Maravillas", "Monte Everest", 5000)
    insertar_arista(grafo, "Cueva de las Maravillas", "Cueva de las Manos", 5000)
    insertar_arista(grafo, "Cueva de las Maravillas", "Cueva de las Ventanas", 6000)

    insertar_arista(grafo, "Cueva de las Ventanas", "Rio Amazonas", 6000)
    insertar_arista(grafo, "Cueva de las Ventanas", "Cataratas del Iguazu", 6000)
    insertar_arista(grafo, "Cueva de las Ventanas", "Cataratas Victoria", 6000)
    insertar_arista(grafo, "Cueva de las Ventanas", "Monte Everest", 6000)
    insertar_arista(grafo, "Cueva de las Ventanas", "Cueva de las Manos", 6000)
    insertar_arista(grafo, "Cueva de las Ventanas", "Cueva de las Maravillas", 6000)

    return grafo

#hallar el arbol de expansión minima de cada tipo de maravilla.

#determinar si existen paises que tengan maravillas arquitectónicas y naturales.



def main():
    grafo = Grafo()
    grafo = crear_grafo(grafo)
    print("El grafo creado es: ")
    print(grafo)
    print("El arbol de expansión minima de las maravillas arquitectónicas es: ")
    print(kruskal(grafo, "Arquitectonica"))
    print("El arbol de expansión minima de las maravillas naturales es: ")
    print(kruskal(grafo, "Natural"))
    print("Los paises que tienen maravillas arquitectónicas y naturales son: ")
    print(pais_con_maravilla_arquitectonica_y_natural(grafo))
    print("Los paises que tienen maravillas arquitectónicas y naturales son: ")
    print(pais_con_maravilla_arquitectonica_y_natural(grafo))






  

main()



