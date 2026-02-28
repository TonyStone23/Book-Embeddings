#---
# Doubly-connected linked list representation

#---
# Imports
import random as r
r.seed(23)

#---
# Vertex
class Vertex:
    def __init__(self, name):
        self.name = name
        self.halfedge = None
        self.active = True
        

#---
# Halfedge
class Halfedge:
    def __init__(self, v):
        self.v = v
        self.twin = None
        self.previous = None
        self.next = None
        self.face = None
        self.color = None
        self.active = True
        

#---
# Face
class Face:
    def __init__(self, h):
        self.halfedge = h
        self.outer = False
        
#---
# Graph
class Graph:
    def __init__(self):
        self.V = []
        self.E = []
        self.F = []
        self.outerface = None
        

#---
# Build Planar Graph
def buildEdge(v, u):
    vu = Halfedge(v)
    uv = Halfedge(u)

    vu.twin = uv
    uv.twin = vu
    return vu, uv

class Build:
    def triangulate(graph, f, i):
        vu = f.halfedge
        uw = vu.next
        wv = uw.next

        v = vu.v # v -> u
        u = uw.v # u -> w
        w = wv.v # w -> v
        x = Vertex(i)

        xv, vx = buildEdge(x, v)
        xu, ux = buildEdge(x, u)
        xw, wx = buildEdge(x, w)
        x.halfedge = xv

        xv.next = vu
        vu.next = ux
        ux.next = xv

        xw.next = wv
        wv.next = vx
        vx.next = xw 

        xu.next = uw
        uw.next = wx
        wx.next = xu

        f1 = Face(xv)
        xv.face = f1
        vu.face = f1
        ux.face = f1

        f2 = Face(xw)
        xw.face = f2
        wv.face = f2
        vx.face = f2

        f3 = Face(xu)
        xu.face = f3
        uw.face = f3
        wx.face = f3

        graph.F.remove(f)
        graph.V += [x]
        graph.E += [xv, vx, xu, ux, xw, wx]
        graph.F += [f1, f2, f3]

        return
    def triangular(n):
        graph = Graph()
        
        v = Vertex(0)
        u = Vertex(1)
        w = Vertex(2)
        
        vu, uv = buildEdge(v, u)
        uw, wu = buildEdge(u, w)
        wv, vw = buildEdge(w, v)

        v.halfedge = vu
        u.halfedge = uw
        w.halfedge = wv

        vu.next = uw
        uw.next = wv
        wv.next = vu

        uv.next = vw
        vw.next = wu
        wu.next = uv

        f1 = Face(vu)
        vu.face = f1
        uw.face = f1
        wv.face = f1

        f2 = Face(uv)
        uv.face = f2
        wu.face = f2
        vw.face = f2

        graph.V += [v, u, w]
        graph.E += [vu, uw, wv, uv, wu, vw]
        graph.F += [f1, f2]

        for i in range(3, n):
            f = r.choice(graph.F)
            Build.triangulate(graph, f, i)

        return graph
    
graph = Build.triangular(4)

print(
    "Vertices", [v.name for v in graph.V], "\n"
    "Halfedges", [(h.v.name, h.twin.v.name) for h in graph.E], "\n"
    "Faces", [(f.halfedge.v.name, f.halfedge.next.v.name, f.halfedge.next.next.v.name) for f in graph.F], "\n"
)