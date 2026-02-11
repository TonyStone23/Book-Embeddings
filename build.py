from graph import *

#---
# Helper functions
def bt(v, n, V, E):
    global i
    r = n // 2
    l = n - r
    print(i, "l: ",l,"r: ", r)

    if n <= 1:
        u = Vertex(i)
        i += 1
        V.append(u)
        return u, i
    
    if l >= 1:
        print("going left")
        lu = bt(v, l, V, E)
        if lu is not None:
            lu, i = lu
            el = Edge(v, lu)
            E.append(el)

    if r >= 1:
        print("going right")
        ru = bt(v, r, V, E)
        if ru is not None:
            ru, i = ru
            er = Edge(v, ru)
            E.append(er)

#---
# Builder
class Build:
    
    def binaryTree(n):
        v = Vertex(0)
        global i
        i = 0
        global V; V = []
        global E; E = []
        bt(v, n, V, E)
        G = Graph(V, E)

        return G
    
    # More graph classes