from embedding import *
from build import Build
from draw import * 


#---
# Testing
G = Build.triangular(7)
v = G.V()[0]
for e in v.edges():
    print(e.u(v).name())

see(G)
Embed.fourPage(G)
see(G)