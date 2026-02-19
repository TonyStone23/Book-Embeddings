from graph import *
from build import *

#---
# Tarjan depth first search
def dfs(u, inactive=None, parent=None, path=None, blocks=None, visited=None, discovery=None, lowlink=None):
    if inactive is None:
        inactive = set()
    if path is None: 
        path = []
    if blocks is None: 
        blocks = []
    if visited is None: 
        visited = {}
    if discovery is None: 
        discovery = {}
    if lowlink is None: 
        lowlink = {}

    visited[u] = True
    discovery[u] = len(discovery) + 1
    lowlink[u] = len(discovery) + 1

    start = u.halfedge()
    e = start
    while True:
        v = e.twin().v()

        if v not in inactive:
            if v != u and v not in visited:
                path.append(e)
                blocks = dfs(v, inactive, u, path, blocks, visited, discovery, lowlink)
                lowlink[u] = min(lowlink[u], lowlink[v])

                if lowlink[v] >= discovery[u]:
                    block = set()
                    while True:
                        p = path.pop()
                        block.add(p.v())
                        block.add(p.twin().v())
                        if p == e:
                            break
                    blocks.append(block)

            elif v != parent and discovery[v] < discovery[u]:
                lowlink[u] = min(lowlink[u], discovery[v])  # Back edge

        e = e.twin().next()
        if e == start:
            break

    return blocks

def expand(outerface, graph, inactive=None, color=None, binding=None, spine=None):
    if inactive is None: 
        inactive = set()
    if color is None: 
        color = {}
    if binding is None: 
        binding = {True: set(), False: set()}
    if spine is None: 
        spine = []

    vs, hs = outerface.walk()

    for h in hs: # These are level edges
        binding[False].add(h)
        binding[False].add(h.twin())

    for v in vs:
        inactive.add(v) # Peel outer cycle
        spine.append(v)
        outedges = v.outedges()
        for o in outedges:
            if o not in binding[False] and o not in binding[True]: # an unlabeled edge that is not a level edge is a binding edge
                binding[True].add(o)
                binding[True].add(o.twin())

    print(f"Level edges: {[e.show() for e in binding[False]]}")
    print(f"Binding edges: {[e.show() for e in binding[True]]}")

    print(f"{[e.show() for e in set(graph.E()) - binding[False] - binding[True]]}")
    
    print(f"spine: {[v.name() for v in spine]}")
    
    u = (set(graph.V()) - inactive).pop()

    blocks = dfs(u, inactive)
    for b in blocks:
        bv = []
        for v in b:
            bv.append(v.name())
        print(f"block {blocks.index(b)}: {bv}")

    return

def bookify(graph):
    outerface = graph.outerface()
    expand(outerface, graph)

#----
# Testing
graph = Build.triangular(6)

graph.show()
#graph.faces()

bookify(graph)
