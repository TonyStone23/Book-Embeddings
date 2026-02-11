import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Circle

plt.rcParams['mathtext.fontset'] = 'custom'
plt.rcParams['mathtext.rm'] = 'Times New Roman'

def drawEdge(e, ax):
    v, u = e.vu()
    vp = v.spot()
    up = u.spot()
    center = (abs((vp + up)/2), 0)
    width = abs(vp - up)
    height = abs(vp-up)/2
    # needs cleaned up
    if e.page() == 0:
        arc = Arc(center, width, height, angle = 0, theta1=0, theta2=180, edgecolor='black', lw = 1)
    if e.page() == 1:
        arc = Arc(center, width, -height, angle = 0, theta1=0, theta2=180, edgecolor='green', lw = 1)
    if e.page() == 2:
        arc = Arc(center, width, -height, angle = 0, theta1=0, theta2=180, edgecolor='blue', lw = 1)
    ax.add_patch(arc)

def drawVertex(u, ax):
    circle = Circle((u.spot(), 0), .15, edgecolor = 'black', facecolor = 'white')
    ax.add_patch(circle)
    ax.text(u.spot(), 0, f"$V_{u.name()}$", fontsize=12, color='black', ha='center', va='center')

def see(G):
    fig, ax = plt.subplots()
    for e in G.E():
        drawEdge(e, ax)
        print("drawing edge")

    for v in G.V():
        drawVertex(v, ax)
        print("Drawing vertex")

    ax.set_aspect('equal')
    ax.autoscale_view()
    ax.axis('off')
    plt.show()