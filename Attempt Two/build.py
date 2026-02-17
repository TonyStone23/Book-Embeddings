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

def trinagulate(graph, face):
    return

class Build:
    def triangular(n):
        graph = Graph()
        vs = graph.V()
        es = graph.E()
        fs = graph.F()
        
        v = Vertex(0)
        u = Vertex(1)
        w = Vertex(2)
        vs += [v, u, w]
        
        h1_, _h1 = buildEdge(v, u)
        h2_, _h2 = buildEdge(u, w)
        h3_, _h3 = buildEdge(w, v)
        es += [h1_, h2_, h3_, _h1, _h2, _h3]

        h1_.next(h2_)
        h2_.next(h3_)
        h3_.next(h1_)

        _h1.next(_h2)
        _h2.next(_h3)
        _h3.next(_h1)

        f1 = Face(0)
        f2 = Face(1)
        f1.halfedge(h1_)
        f2.halfedge(_h1)
        fs += [f1, f2]
        graph.outerface(f1)
        
        return graph

G = Build.triangular(3)
G.show()