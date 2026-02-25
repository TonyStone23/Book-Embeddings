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

        # This needs to keep track of blocks, and label edges as binding or not
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

def expand(C):
    return

def bookify(graph):
    binding = {True: set(), False: set()}
    inactive = set()
    spine = []

    outerface = graph.outerface()
    vs, hs = outerface.walk()

    # These are level edges
    for h in hs: 
        binding[False].add(h)
        binding[False].add(h.twin())

    # Peel outer cycle
    for v in vs:
        inactive.add(v)
        spine.append(v)
        for o in v.outedges():
            if o not in binding[False] and o not in binding[True]: # an unlabeled edge that is not a level edge is a binding edge
                binding[True].add(o)
                binding[True].add(o.twin())
    
    # Find root vertex a
    a = set([e.twin().v() for e in spine[0].outedges()]).pop()

    blocks = dfs(a, inactive) # Determine blocks
    for b in blocks: # Just for checking
        bv = []
        for v in b:
            bv.append(v.name())
        print(f"block {blocks.index(b)}: {bv}")

    # Root block 
    expand() 
    return spine

#----
# Testing
graph = Build.triangular(8)

graph.show()
#graph.faces()

bookify(graph)
