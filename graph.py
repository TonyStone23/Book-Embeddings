class Vertex:
    def __init__(self, num):
        self.__name = num
        self.__edges = set()
        self.__spot = num
        pass

    def add(self, edge):
        self.__edges.add(edge)

    def name(self):
        return self.__name

    def edges(self):
        return self.__edges
    
    def spot(self, newSpot=None):
        if newSpot is not None:
            self.__spot = newSpot
        else:
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
    
    def name(self):
        return self.__name
    
    def page(self, newPage=None):
        if newPage is not None:
            self.__page = newPage
        else:
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
    
    def makeGraph(self, n, m):
        
        # Generate up to a fully connected graph
        if m > (n * (n-1)/2):
            print("Too many edges")
            return
        
        # Generate a minimum of a path graph
        if m < n - 1:
            print("Not enough edges")
            return
        
        for i in range(n):
            v = Vertex(i)
            v.spot(i)
            self.__V.append(v)

        vi = 0
        ui = 0
        edges = 0
        while edges < m:
            v = self.__V[vi % n]
            u = self.__V[ui % n]

            if (v != u) and (bool(v.edges() & u.edges()) == False):
                self.__E.append(Edge(v, u))
                vi += 1
                ui += 1
                edges += 1
            else:
                ui += 1

    def show(self):
        for e in self.__E:
            print(f"{e.name()}")

#----------------
# Testing
# G = Graph()
# G.makeGraph(4, 6)

#----------------
# Graph Drawing
# from draw import *
# see(G)
