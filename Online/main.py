#from embedding import *
from build import Build
from embedding import *
from draw import * 

#---
# Testing
G = Build.complete(7)
#G = Build.triangular(7)
#G = Build.binaryTree(7)
online(G)
draw(G)