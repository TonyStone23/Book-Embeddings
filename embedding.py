from graph import *

#---
# Find initial 'outer' cycle K 
def init(G):
    return # K, an outer face of G

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
    for a in C:
        for e in a.edges():
            v, u = e.vu()
            if v in B or u in B:
                A.append(a)
    return A

#---
# Recursive expansion
def expand(C, G, L, i):
    I = C - G
    if I == 0:
        return # Base Case
    T = blockify(I)
    for B in T:
        A = dominators(B, C)
        for a in A:
            i = L.index(a)
        expand(B, G & B, L, i) # Recursive call

#---
# Embedder
class Embed:
    # Four Page Algorithm
    def fourPage(G):
        return
    