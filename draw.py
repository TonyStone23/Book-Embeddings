import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Circle

plt.rcParams['mathtext.fontset'] = 'custom'
plt.rcParams['mathtext.rm'] = 'Times New Roman'

def drawEdge(e, ax, color = 'black'):
    v, u = e.vertices()
    vp = v.position()
    up = u.position()
    center = (abs((vp + up)/2), 0)
    width = abs(vp - up)
    height = abs(vp-up)/2
    arc = Arc(center, width, height, angle = 0, theta1=0, theta2=180, edgecolor=color, lw = 1)
    ax.add_patch(arc)

def drawVertex(u, ax):
    circle = Circle((u.position(), 0), .15, edgecolor = 'black', facecolor = 'white')
    ax.add_patch(circle)
    ax.text(u.position(), 0, f"$V_{u.name()}$", fontsize=12, color='black', ha='center', va='center')

def see(G):
    fig, ax = plt.subplots()
    for e in G.getE():
        drawEdge(e, ax)

    for v in G.getV():
        drawVertex(v, ax)
    ax.set_aspect('equal')
    ax.autoscale_view()
    ax.axis('off')
    plt.show()