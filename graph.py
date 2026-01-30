class Vertex:
    def __init__(self, num):
        self.num = num
        self.es = set()
        self.spot = num
        pass

    def add(self, edge):
        self.es.add(edge)

    def name(self):
        return self.num

    def edges(self):
        return self.es
    
    def position(self, newPosition = None):
        if newPosition is not None:
            self.spot = newPosition
        else:
            return self.spot

class Edge:
    def __init__(self, v, u):
        self.vu = (v, u)
        self.e = f"{v.name()}{u.name()}"
        u.add(self)
        v.add(self)

    def vertices(self):
        return self.vu
    
    def name(self):
        return self.e

class Graph:
    def __init__(self):
        self.V = []
        self.E = []
        pass

    def getV(self):
        return self.V
    
    def getE(self):
        return self.E
    
    def makeGraph(self, n, m):
        for i in range(n):
            v = Vertex(i)
            v.position(i)
            self.V.append(v)

        vi = 0
        ui = 0
        edges = 0
        while edges < m:
            v = self.V[vi % n]
            u = self.V[ui % n]

            if (v != u) and (bool(v.edges() & u.edges()) == False):
                self.E.append(Edge(v, u))
                vi += 1
                ui += 1
                edges += 1
            else:
                ui += 1

    def show(self):
        for e in self.E:
            print(f"{e.name()}")

    def swap(self, i, j):
        v, u = self.V[i], self.V[j]
        temp = v.position()
        v.position(u.position())
        u.position(temp)

# Test
G = Graph()
G.makeGraph(10, 20)
G.swap(2, 4)

from draw import *
see(G)