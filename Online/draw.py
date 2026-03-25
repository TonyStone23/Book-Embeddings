import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Circle
import matplotlib as mpl

plt.rcParams['mathtext.fontset'] = 'custom'
plt.rcParams['mathtext.rm'] = 'Times New Roman'
colors = mpl.color_sequences['tab20']

def drawEdge(e, ax):

    color = e.page()
    v, u = e.vu()
    vp = v.spot()
    up = u.spot()
    center = (abs((vp + up)/2), 0)
    width = abs(vp - up)
    height = abs(vp-up)/2

    if color == None:
        arc = Arc(center, width, height, angle = 0, theta1=0, theta2=180, edgecolor='red', lw = 1, linestyle = '--')
    else:
        if color % 2 == 1:
            height *= -1
        arc = Arc(center, width, height, angle = 0, theta1=0, theta2=180, edgecolor = colors[color], lw = 1)

    # # needs cleaned up
    # if e.page() == None:
    #     arc = Arc(center, width, height, angle = 0, theta1=0, theta2=180, edgecolor='red', lw = 1)
    # if e.page() == 0:
    #     arc = Arc(center, width, height, angle = 0, theta1=0, theta2=180, edgecolor='black', lw = 1)
    # if e.page() == 1:
    #     arc = Arc(center, width, -height, angle = 0, theta1=0, theta2=180, edgecolor='green', lw = 1)
    # if e.page() == 2:
    #     arc = Arc(center, width, -height, angle = 0, theta1=0, theta2=180, edgecolor='blue', lw = 1)
    # if e.page() == 3:
    #     arc = Arc(center, width, -height, angle = 0, theta1=0, theta2=180, edgecolor='orange', lw = 1)
    # if e.page() == 4:
    #     arc = Arc(center, width, -height, angle = 0, theta1=0, theta2=180, edgecolor='yellow', lw = 1)

    ax.add_patch(arc)

def drawVertex(u, ax):
    circle = Circle((u.spot(), 0), .15, edgecolor = 'black', facecolor = 'white')
    ax.add_patch(circle)
    ax.text(u.spot(), 0, f"$V_{{{u.name()}}}$", fontsize=12, color='black', ha='center', va='center')

def draw(G):
    fig, ax = plt.subplots()
    for e in G.E():
        drawEdge(e, ax)

    for v in G.V():
        drawVertex(v, ax)

    ax.set_aspect('equal')
    ax.autoscale_view()
    ax.axis('off')
    plt.show()