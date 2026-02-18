from graph import *

#---
# Tarjan depth first search
def dfs(): # 
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