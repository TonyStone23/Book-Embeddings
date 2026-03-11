from build import *
from draw import *
import random as r
r.seed(23)

#---
# Online Algorithm
def recurse(v, pages, spine):
    spine.append(v)
    v.spot(spine.index(v))
    tocolor = {}

    next = None
    for e in v.edges():
        u = e.u(v)
        if u not in spine and next is None:
            e.page(0)
            next = u
        elif u.spot() is None:
            continue
        else:
            tocolor[abs(v.spot() - u.spot())] = e

    # Coloring
    while tocolor:
        shortest = min(tocolor.keys())
        e = tocolor.pop(shortest)
        u = e.u(v)
        for page in pages:
            available = pages[page]
            available = available + [1] * (len(spine) - len(available))
            if available[u.spot()] == 1 and available[v.spot()] == 1:
                e.page(page)
                pages[page] = available[:u.spot() + 1] + [0] * (v.spot() - u.spot() - 1) + [1]
                break
        
        if e.page() is None:
            newPage = len(pages)
            pages[newPage] = [1] * len(spine[:u.spot() + 1]) + [0] * (v.spot() - u.spot() - 1) + [1]
            e.page(newPage)

    # Recursive call
    if next is not None:
        pages, spine = recurse(next, pages, spine)

    return pages, spine

def online(G):
    v = r.choice(G.V())
    pages = {0:[]}
    spine = []
    while len(spine) < len(G.V()):
        v = r.choice([v for v in G.V() if v not in spine])
        pages, spine = recurse(v, pages, spine)

#---
# Testing
G = Build.triangular(9)
G.show()
online(G)
draw(G)