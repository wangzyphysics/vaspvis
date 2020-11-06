import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Wedge
from matplotlib.collections import PatchCollection
import matplotlib.transforms as transforms

fig, ax = plt.subplots(figsize=(4,3), dpi=300)


# Height = 18 points
#  height = 18 * t

x = np.linspace(0,np.pi,12)
y = np.sin(x)
fractions = np.repeat(np.array([
    [0.2,0.1,0.7],
    [0.4,0.4,0.2],
    [0.3,0.3,0.4],
]), 4, axis=0)

r = (0.15 + 0.1 * np.cos(x))  * 70

ax.scatter(
    x,
    y,
    s=r,
    color='red',
    ec=None,
    zorder=0,
)

t = ax.get_figure().transFigure.transform([(0,0), (1,1)])
t = ax.get_figure().get_dpi() / ((t[1,1] - t[0,1]) * 72)

def draw_pie(r, x, y, fractions, colors):
    patches = []
    fractions = np.c_[np.zeros(fractions.shape[0]), fractions]
    fractions = fractions * 360
    for i in range(len(x)):
        trans = (fig.dpi_scale_trans + transforms.ScaledTranslation(x[i], y[i], ax.transData))
        wedges = [
            Wedge(
                (0,0),
                np.sqrt(r[i] / np.pi) / 72,
                np.sum(fractions[i][:j+1]),
                np.sum(fractions[i][:j+2]),
                color=colors[j],
                zorder=150,
                ec=None,
                transform=trans,
            ) for j in range(len(colors))
        ]
        patches.extend(wedges)

    return patches

patches = draw_pie(
    r=r,
    x=x,
    y=y,
    fractions=fractions,
    colors=['red', 'blue', 'green']
)

#  for i in range(len(x)):
    #  ax.plot(
        #  x[i],
        #  y[i] + 1,
        #  markersize=10,
        #  marker='o',
        #  linestyle='',
        #  zorder=10
    #  )
#  scat.get_marker()
#  wedge = Wedge((1,1), 0.1, 0, 270, ec="none")
#  patches.append(wedge)

#  collection = PatchCollection(patches, match_original=True)
#  collection.set_array(colors)
#  ax.add_collection(collection)
[ax.add_patch(i) for i in patches]
#  plt.axis('equal')
#  plt.axis('off')
#  plt.xlim(-10,10)
#  plt.ylim(-10,10)
plt.tight_layout()

#  plt.show()

#  plt.show()
plt.savefig('test.png')