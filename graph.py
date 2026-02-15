class Vertex:
    def __init__(self, num):
        self.__name = num
        self.__edges = set()
        self.__spot = num
        self.__discovery = 0
        self.__lowlink = 0
        pass

    def add(self, edge):
        self.__edges.add(edge)

    def name(self, newName=None):
        if newName is not None:
            self.__name = newName
        return self.__name

    def edges(self):
        return self.__edges
    
    def spot(self, newSpot=None):
        if newSpot is not None:
            self.__spot = newSpot
        return self.__spot
    
    def discovery(self, discovery=None):
        if discovery is not None:
            self.__discovery = discovery
        return self.__discovery
    
    def lowlink(self, lowlink=None):
        if lowlink is not None:
            self.__lowlink = lowlink
        return self.__lowlink

class Edge:
    def __init__(self, v, u):
        self.__vu = (v, u)
        self.__name = f"{v.name()}{u.name()}"
        self.__page = 0

        u.add(self)
        v.add(self)

    def vu(self):
        return self.__vu
    
    def name(self, newName=None):
        if newName is not None:
            self.__name = newName
        return self.__name
    
    def page(self, newPage=None):
        if newPage is not None:
            self.__page = newPage
        return self.__page

class Graph:
    def __init__(self):
        self.__V = []
        self.__E = []
        pass

    def V(self, v = None):
        if v is not None:
            self.__V.append(v)
        return self.__V
    
    def E(self, e = None):
        if e is not None:
            self.__E.append(e)
        return self.__E

    def show(self):
        for e in self.__E:
            print(f"{e.name()}--{e}")

    def clean(self):
        for v in self.__V:
            v.discovery(0)
            v.lowlink(0)

    #---
    # Graph operations -- for utility, not necessarily 'real' operations
    def __sub__(self, other): 
        difference = Graph()
        difference.__V = list(set(self.__V) - set(other.__V))
        difference.__E = list(set(self.__E) - set(other.__E))
        for e in difference.__E:
            v, u = e.vu
            if not (v in difference.__V and u in difference.__V):
                difference.__E.remove(e)
        return difference
    
    def __and__(self, other):
        intersection = Graph()
        intersection.__V = list(set(self.__V) & set(other.__V))
        intersection.__E = list(set(self.__E) & set(other.__E))
        return intersection
