from graph import *

#---
# Builder
def buildEdge(v, u):
    vu = Halfedge(v)
    uv = Halfedge(u)

    vu.twin(uv)
    uv.twin(vu)
    return vu, uv

def buildFace(h):
    f = Face()
    f.halfedge(h)
    return f

def trinagulate(graph, f, i):
    vu = f.halfedge()
    uw = vu.next()
    wv = uw.next()

    v = vu.v() # v -> u
    u = uw.v() # u -> w
    w = wv.v() # w -> v
    x = Vertex(i)

    xv, vx = buildEdge(x, v)
    xu, ux = buildEdge(x, u)
    xw, wx = buildEdge(x, w)

    xv.next(vu)
    vu.next(ux)
    xu.next(uw)
    uw.next(wx)
    xw.next(wv)
    wv.next(vx)

    f1 = buildFace(xv)
    f2 = buildFace(xu)
    f3 = buildFace(xw)

    graph.removeFace(f)
    graph.update([x], [xv, vx, xu, ux, xw, wx], [f1, f2, f3])

    return

class Build:
    def triangular(n):
        graph = Graph()
        
        v = Vertex(0)
        u = Vertex(1)
        w = Vertex(2)
        
        vu, uv = buildEdge(v, u)
        uw, wu = buildEdge(u, w)
        wv, vw = buildEdge(w, v)

        vu.next(uw)
        uw.next(wv)
        wv.next(vu)
        uv.next(wu)
        wu.next(vw)
        vw.next(uv)

        f1 = buildFace(vu)
        f2 = buildFace(uv)
        graph.outerface(f1)

        graph.update([v, u, w], [vu, uw, wv, uv, wu, vw], [f1, f2])

        for i in range(3, n):
            trinagulate(graph, graph.F()[-1], i)

        return graph

G = Build.triangular(4)
G.show()