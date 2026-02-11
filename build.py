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
# build a cycle
def cycle(start, V, E, n, i):
    v = start
    for _ in range(n-1):
        u = Vertex(i)
        V.append(u)
        E.append(Edge(v, u))
        v = u
        i += 1
    E.append(Edge(v, start))

    return u, i

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
    # H graph from Yannakakis
    def H(f, k):
        G = Graph()
        V = G.V()
        v = Vertex(0)
        V.append(v)
        E = G.E()
        i = 1
        for _ in range(f): # inner graph I
            v, i = cycle(v, V, E, 3 if r.random() > .5 else 4, i)
        
        # K cycle around I
        cycle(V[0], V, E, k, i)

        
        return G

            
            
    
    # More graph classes