class Vertex:
    def __init__(self, num):
        self.__name = num
        self.__edges = set()
        self.__spot = num
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

    def V(self):
        return self.__V
    
    def E(self):
        return self.__E

    def show(self):
        for e in self.__E:
            print(f"{e.name()}--{e}")

#---
# Testing
# G = Graph()
# G.makeGraph(4, 6)

#---
# Graph Drawing
# from draw import *
# see(G)
