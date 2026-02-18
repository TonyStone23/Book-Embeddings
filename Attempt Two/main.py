from build import *
from embed import *

graph = Build.triangular(5)
graph.show()

dfs(graph.V()[0])