from build import *
from draw import *
import random as r
r.seed(23)

#---
# Online
def dfs(v, pages, spine):
    spine.append(v)
    v.spot(spine.index(v))
    tocolor = {}

    # Recursive calls
    for e in v.edges():
        u = e.u(v)
        if u not in spine:
            print("recursion")
            e.page(0)
            pages, spine = dfs(u, pages, spine)
        else:
            tocolor[abs(v.spot() - u.spot())] = e

    # coloring
    print(f"finishing vertex at {spine.index(v)}")
    while tocolor:
        shortest = min(tocolor.keys())
        e = tocolor.pop(shortest)
        u = e.u(v)
        if u.spot() < v.spot():
            for page in pages:
                available = pages[page]
                available = available + [1] * (len(spine) - len(available))
                if available[u.spot()] == 1 and available[v.spot()] == 1:
                    print(f"available: {page, available} -- coloring {e} from u({u.spot()}) to v({v.spot()})")
                    e.page(page)
                    pages[page] = available[:u.spot() + 1] + [0] * (v.spot() - u.spot() - 1) + available[v.spot():]
                    break
            if e.page() is None:
                print("needs a new page")
                newColor = len(pages)
                pages[newColor] = [1] * len(spine[:u.spot() + 1]) + [0] * (v.spot() - u.spot() - 1) + [1]
                e.page(newColor)
                print(e.page())
                print(pages)

    return pages, spine


def online(G):
    #G = Graph()
    v = r.choice(G.V())#;v = Vertex() # for colors, delete me
    pages = {0:[]}
    spine = []
    while len(spine) < len(G.V()):
        pages, spine = dfs(v, pages, spine)

    return G
#---
# Testing
G = Build.triangular(4)
G.show()
G = online(G)
draw(G)