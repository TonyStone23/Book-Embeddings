from graph import *

#---
# Tarjan depth first search # Needs to be updated, does not traverse entire graph
def dfs(u, visited = set()): 
    visited.add(u)
    print("found ", u.name())
    start = u.halfedge()
    e = start

    while True:
        u = e.twin().v()
        if u not in visited:
            dfs(u, visited)
        
        e.twin().next()

        if e == start:
            break
    return

def expand(outerface, G, active, binding, level, spine, i = 0):
    vs, hs = outerface.walk() 

    for h in hs:
        level.add(h)
        level.add(h.twin())

    for v in vs:
        active.remove(v) # Peel outer cycle

    return

def fourPage(G):
    active = set(G.V())
    binding = set()
    level = set()
    spine = []
    outerface = G.outerface()

    expand(outerface, G, active, binding, level, spine)