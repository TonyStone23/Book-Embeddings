from graph import *

#---
# Builder
def buildEdge(v, u):
    h_ = Halfedge(v)
    _h = Halfedge(u)

    h_.twin(_h)
    _h.twin(h_)
    return h_, _h

def buildFace(name, h):
    f = Face(name)
    f.halfedge(h)
    return f

def trinagulate(n):
    graph = Graph()
    verteces = graph.V()
