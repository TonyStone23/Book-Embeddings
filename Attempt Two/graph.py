#---
# Doubly-connected linked list representation

#---
# Vertex
class Vertex:
    def __init__(self, name):
        self.__name = name
        self.__halfedge = None

    def name(self):
        return self.__name
    
    def halfedge(self, halfedge=None):
        if halfedge is not None:
            self.__halfedge = halfedge
        return self.__halfedge

#---
# Halfedge
class Halfedge:
    def __init__(self, v):
        self.__v = v
        self.__twin = None
        self.__previous = None
        self.__next = None
        self.__face = None
        return
    
    def v(self):
        return self.__v
    
    def twin(self, twin=None):
        if twin is not None:
            self.__twin = twin
        return self.__twin

    def next(self, next=None):
        if next is not None:
            self.__next = next
            next.__previous = self
        return self.__next
    
    def face(self, face=None):
        if face is not None:
            self.__face = face
        return self.__face

#---
# Face
class Face:
    def __init__(self):
        self.__halfedge = None
        return

    def halfedge(self, halfedge=None):
        if halfedge is not None:
            self.__halfedge = halfedge
        return self.__halfedge
    
    def show(self):
        h1 = self.__halfedge
        h2 = h1.next()
        h3 = h2.next()
        return h1.v().name(), h2.v().name(), h3.v().name()
        
#---
# Graph
class Graph:
    def __init__(self):
        self.__V = []
        self.__E = []
        self.__F = []
        self.__outerface = None

    def V(self, v=None):
        if v is not None:
            self.__V.append(v)
        return self.__V
    
    def E(self, e=None):
        if e is not None:
            self.__E.append(e)
        return self.__E
    
    def F(self, f=None):
        if f is not None:
            self.__F.append(f)
        return self.__F
    
    def removeFace(self, f):
        self.__F.remove(f)
    
    def outerface(self, of):
        if of is not None:
            self.__outerface = of
        return self.__outerface
    
    def show(self):
            print(f"Vertices: \n    {str([v.name() for v in self.__V])[1:-1]}")
            print(f"Faces: \n    outer: {self.__outerface.show()}\n    inner: {str([f.show() for f in self.__F if f != self.__outerface])[1:-1]}")

    def update(self, V=None, E=None, F=None):
        if V is not None:
            self.__V += V
        if E is not None:
            self.__E += E
        if F is not None:
            self.__F += F

    