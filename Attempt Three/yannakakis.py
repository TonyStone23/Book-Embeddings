from graph import *
import random as r
r.seed(23)

#---
# Tarjan depth first search
def dfs(u, inactive=None, parent=None, path=None, tree=None, visited=None, discovery=None, lowlink=None):
    if inactive is None:
        inactive = set()
    if path is None: 
        path = []
    if tree is None: 
        tree = Tree()
    if visited is None: 
        visited = {}
    if discovery is None: 
        discovery = {}
    if lowlink is None: 
        lowlink = {}

    visited[u] = True
    discovery[u] = len(discovery) + 1
    lowlink[u] = len(discovery) + 1

    start = u.halfedge
    e = start
    while True:
        v = e.twin.v

        # This needs to keep track of blocks, and label edges as binding or not
        if v.active:
            if v != u and v not in visited:
                path.append(e)
                blocks = dfs(v, inactive, u, path, tree, visited, discovery, lowlink)
                lowlink[u] = min(lowlink[u], lowlink[v])

                if lowlink[v] >= discovery[u]:
                    block = Block()
                    while True:
                        p = path.pop()
                        block.cycle.add(p)
                        if p == e:
                            break
                    tree.blocks.append(block)

            elif v != parent and discovery[v] < discovery[u]:
                lowlink[u] = min(lowlink[u], discovery[v])  # Back edge

        e = e.twin.next
        if e == start:
            break

    return tree

#def classifyEdges(cycle):

#---
# Walk face
def walk(face):
    e = face.halfedge
    walk = [e.v]
    next = e.next
    while next != e:
        walk.append(next.v)
        next = next.next

    return walk
    
#---
# Testing

graph = Build.triangular(7)
show(graph)

outerFace = graph.F[0]
outerFace.outer = True

vs = walk(outerFace)
for v in vs:
    v.active = False

u = r.choice([u for u in set(graph.V) - set(vs)])

tree = dfs(u)
for i, b in enumerate(tree.blocks):
    print(f"block {i}: {[(e.v.name, e.twin.v.name) for e in b.cycle]}")