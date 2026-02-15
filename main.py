from embedding import *
from build import Build
from draw import * 


#---
# Testing Block decomposition
#G = Build.triangular(8)
G = Build.binaryTree(3)
see(G)
T = blockify(G)
for B in T:
    see(G & B)