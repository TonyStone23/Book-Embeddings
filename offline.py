def printMatrix(matrix):
    for row in matrix:
        print(row, "\n")

def rotateMatrix(matrix):
    rotation = [[matrix[1][0], matrix[0][0]],[matrix[1][1],matrix[0][1]]]
    return rotation

def checkMatrix(matrix):

    zero = [[0, 0], [0, 0]]
    r1 = rotateMatrix(matrix)
    r2 = rotateMatrix(r1)
    if matrix == r1 and matrix == r2 and matrix != zero:
        print("2 x 2")
        return True

    return False

def matrixSort(G):
    #Turn into adjacency list
    n = len(G.getV())
    em = [([""] * n) for _ in range(n)]
    visual = [([""] * n) for _ in range(n)]
    
    # establish edges
    edges = G.getE()
    for e in edges:
        v, u = e.vertices()
        visual[v.position()][u.position()] = 1
        visual[u.position()][v.position()] = 1
        em[v.position()][u.position()] = e
        em[u.position()][v.position()] = e

    printMatrix(visual)

    # This needs to be changed, it should make an alteration to the first vertex that it can.

    for i in range(1, n-1):
        for j in range(1, n-1):
            if i < j:
                # Check the 2x2 areas an edge belongs to
                print(i, j)
                matrices = [[visual[i-1][j-1:j+1], visual[i][j-1:j+1]],
                            [visual[i-1][j:j+2], visual[i][j:j+2]],
                            [visual[i][j-1:j+1], visual[i+1][j-1:j+1]],
                            [visual[i][j:j+2], visual[i+1][j:j+2]]]
                           
                for m in matrices:
                    print(m)
                    if checkMatrix(m):
                        e = em[i][j]
                        e.page(e.page() + 1)
                        visual[i][j] += 1

    printMatrix(visual)

#--------------
# Testing
from graph import *
G = Graph()
G.makeGraph(4, 6)

matrixSort(G)

from draw import *
see(G)