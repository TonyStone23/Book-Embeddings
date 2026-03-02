from build import *
from draw import *
import random as r
r.seed(23)

#---
# Online
def online(G):
    line = []
    for v in G.V():
        line.append(v)
    r.shuffle(line)
    return line

#---
# Testing
G = Build.triangular(7)
line = online(G)
draw(G)