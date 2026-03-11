from graph import *
import random as r
r.seed(23)

#---
# Tarjan depth first search
def dfs(u, parent=None, inactive=None, path=None, tree=None, visited=None, discovery=None, lowlink=None, time = None):
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
    if time is None:
        time = [0]

    visited[u] = True
    time[0] += 1
    discovery[u] = time[0]
    lowlink[u] = time[0]

    start = u.halfedge
    e = start
    while True:
        v = e.twin.v
        if v.active:

            if parent is not None and e is parent.twin:
                e = e.twin.next
                if e == start:
                    break
                continue

            if v not in visited:
                path.append(e)
                dfs(v, e, inactive, path, tree, visited, discovery, lowlink, time)

                lowlink[u] = min(lowlink[u], lowlink[v])

                if lowlink[v] >= discovery[u]:
                    block = Block()
                    while True:
                        p = path.pop()
                        block.cycle.add(p)
                        if p == e:
                            break
                    tree.blocks.append(block)

            elif discovery[v] < discovery[u]:
                path.append(e)
                lowlink[u] = min(lowlink[u], discovery[v])  # Back edge

        e = e.twin.next
        if e == start:
            break

    return tree

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

graph = Build.triangular(5)
show(graph)

outerFace = graph.F[0]
outerFace.outer = True

vs = walk(outerFace)
for v in vs:
    v.active = False

print(F"Outer face: {[v.name for v in vs]}")
u = r.choice([u for u in set(graph.V) - set(vs)])

tree = dfs(u)
for i, b in enumerate(tree.blocks):
    print(f"block {i}: {[(e.v.name, e.twin.v.name) for e in b.cycle]}")