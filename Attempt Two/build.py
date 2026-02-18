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
    x.halfedge(xv)

    xv.next(vu)
    vu.next(ux)
    ux.next(xv)

    xw.next(wv)
    wv.next(vx)
    vx.next(xw)

    xu.next(uw)
    uw.next(wx)
    wx.next(xu)

    f1 = buildFace(xv)
    xv.face(f1)
    vu.face(f1)
    ux.face(f1)

    f2 = buildFace(xw)
    xw.face(f2)
    wv.face(f2)
    vx.face(f2)

    f3 = buildFace(xu)
    xu.face(f3)
    uw.face(f3)
    wx.face(f3)

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

        v.halfedge(vu)
        u.halfedge(uw)
        w.halfedge(wv)

        vu.next(uw)
        uw.next(wv)
        wv.next(vu)

        uv.next(vw)
        vw.next(wu)
        wu.next(uv)

        f1 = buildFace(vu)
        vu.face(f1)
        uw.face(f1)
        wv.face(f1)

        f2 = buildFace(uv)
        uv.face(f2)
        wu.face(f2)
        vw.face(f2)

        graph.outerface(f1)

        graph.update([v, u, w], [vu, uw, wv, uv, wu, vw], [f1, f2])

        for i in range(3, n):
            trinagulate(graph, graph.F()[-1], i)

        return graph

G = Build.triangular(50)
G.show()
print(G.outerface().walk())
print(G.F()[-1].walk())

v = G.V()[0]
for i, h in enumerate(v.outedges()):
    print(i, h, h.v().name())