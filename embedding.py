from graph import *
from build import *

#---
# Find initial 'outer' cycle K 
def init(G):
    K = Graph()
    for i in range(0, 3):
        k = G.V()[i]
        K.V(k)
        
    E = set()
    for k in K.V():
        for e in k.edges():
            v, u = e.vu()
            if (v in K.V() and u in K.V()):
                E.add(e)
    E = list(E)
    for e in E:
        K.E(e)
    return K # an outer face of G

#---
# Tarjin depth-first search
def dfs(b, visited = set(), path = [], T = [], a = None, time = 0):

    visited.add(b)
    b.discovery(time)
    b.lowlink(time)
    time += 1

    for e in b.edges():
        for c in e.vu():
            if (b != c) and c not in visited:
                path.append(e)
                visited, path, T, time = dfs(c, visited, path, T, b, time)
                b.lowlink(min(b.lowlink(), c.lowlink()))
                if c.lowlink() >= b.discovery():
                    B = Graph()
                    V = set()
                    p = None
                    while True:
                        p = path.pop()
                        v, u = p.vu()
                        B.E(p)
                        V.add(v)
                        V.add(u)
                        if p == e:
                            break
                    for v in V:
                        B.V(v)
                    T.append(B)
            elif (c != a) and (c.discovery() < b.discovery()):
                path.append(e)
                b.lowlink(min(b.lowlink(), c.lowlink()))
    return visited, path, T, time

#---
# Decompose into blocks
def blockify(G):
    visted, path, T, time = dfs(G.V()[0])
    G.clean()
    return T # Return Tree

#---
# Determine interval of dominating vertices
def dominators(B, C):
    A = []
    for a in C.V():
        for e in a.edges():
            v, u = e.vu()
            if v in B.V() or u in B.V():
                A.append(a)
    return A

#---
# Recursive expansion
def expand(K, G, L, i = 0, l = 0):
    # insert vertices into list 
    k = K.V()[0]
    mL = []
    for e in K.E():
        k = l
        v, u = e.vu()
        if v == k:
            if u in K.V():
                mL.append(u)
                k = u
        else:
            if v in K.V():
                mL.append(v)
                k = v
    lL = L[0:i]
    rL = L[i:-1]
    L = lL + mL + rL
    # Get inner graph
    I = G - K
    if not I.V():
        return # Base Case
    
    # Block tree of I
    T = blockify(I)
    for B in T:
        A = dominators(B, K)
        for a in A:
            i = L.index(a)
        expand(B, G & B, L, i) # Recursive call
        # It cannot make a recursive call on graph B, it needs to be the outer face.
    return L

#---
# Update vertex spots
def arrange(L):
    if L is not None:
        for v in L:
            v.spot(L.index(v))

#---
# Embedder
class Embed:
    # Four Page Algorithm
    def fourPage(G):
        L = [] # Layout
        K = init(G) # Arbitrary outer face
        L = expand(K, G, L)

        arrange(L)
        return L
    
#---
# Testing
G = Build.triangular(7)
L = Embed.fourPage(G)