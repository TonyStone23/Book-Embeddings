#from embedding import *
from build import Build
from embedding import *
from draw import * 

#---
# Testing
G = Build.complete(9)
#G = Build.triangular(9)
#G = Build.binaryTree(7)
online(G)
draw(G)