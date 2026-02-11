from graph import *
import numpy.random as r; r.seed(23)

#---
# Binary tree helper
def bt(v, n, V, E, i=0):
    lt = (n -1) // 2
    rt = n - 1 - lt

    if n <= 1:
        return i
    
    if lt > 0:
        i += 1
        l = Vertex(i)
        V.append(l)
        el = Edge(v, l)
        E.append(el)
        i = bt(l, lt, V, E, i)

    if rt > 0:
        i += 1
        r = Vertex(i)
        V.append(r)
        er = Edge(v, r)
        E.append(er)
        i = bt(r, rt, V, E, i)

    return i

#---
# Triangulator
def triangulate(f, V, E, i):
    v, u, w, = f
    x = Vertex(i)
    V.append(x)
    E += [Edge(x, v),
          Edge(x, u),
          Edge(x, w)]

    f1 = (x, v, u)
    f2 = (x, u, w)
    f3 = (x, w, v)

    return f1, f2, f3

#---
# Builder
class Build:
    #---
    # Binary Tree
    def binaryTree(n):
        G = Graph()
        V = G.V()
        v = Vertex(0)
        V.append(v)
        E = G.E()
        bt(v, n, V, E)

        return G
    
    #---
    # Maximal Planar graph
    def triangular(n):
        G = Graph()
        V = G.V()
        E = G.E()
        v = Vertex(0)
        u = Vertex(1)
        w = Vertex(2)
        V += [v, u, w]
        E += [Edge(v, u),
              Edge(u, w),
              Edge(w, v)]
        
        faces = [(v, u, w)]

        for i in range(3, n):
            f = faces[r.randint(0, len(faces))]
            f1, f2, f3 = triangulate(f, V, E, i)
            faces += [f1, f2, f3]
    
        return G

            
            
    
    # More graph classes