from graph import *

#---
# Helper functions
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
# Builder
class Build:
    
    def binaryTree(n):
        v = Vertex(0)
        G = Graph()
        V = G.V()
        V.append(v)
        E = G.E()
        bt(v, n, V, E)

        return G
    
    # More graph classes