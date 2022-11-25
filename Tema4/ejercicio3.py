class nodoArista(object):
    '''Clase nodo arista, que contiene la informacion de la arista y el nodo destino'''
    def __init__(self,info,destino):
        '''Constructor de la clase nodoArista'''
        self.info = info
        self.destino = destino
        self.sig = None

class nodoVertice(object):
    '''Clase nodo vertice, que contiene la informacion del vertice y la lista de aristas'''
    def __init__(self,info):
        '''Constructor de la clase nodoVertice'''
        self.info = info
        self.sig= None
        self.visitado = False
        self.adyacente= Arista()

class grafo(object):
    def __init__(self,info):
        
