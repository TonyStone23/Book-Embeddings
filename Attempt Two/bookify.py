from graph import *
from build import *

#---
# Tarjan depth first search
def dfs(u, inactive, visited = set(), path = [], time = 0): 

    time += 1 # Increment time
    start = u.halfedge() #starting edge
    e = start

    while True:
        u = e.twin().v()
        if u not in visited and u not in inactive: # Only traverse 'active' vertices
            visited.add(u) 
            path.append(e)
            print("found ", u.name())
            dfs(u, inactive, visited, path, time + 1)

        e = e.twin().next()

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

def bookify(G):
    active = set(G.V())
    binding = set()
    level = set()
    spine = []
    outerface = G.outerface()

    expand(outerface, G, active, binding, level, spine)

graph = Build.triangular(5)
graph.show()

dfs(graph.V()[3], set())