from itertools import combinations
from itertools import product
from itertools import repeat
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure ()
ax = fig.gca (projection = '3d')
points = product (* repeat ((-1, 1), 3))
for p1, p2 in combinations (points, 2):
    if [* map (sum, zip (p1, p2))]. count (0) == 1:
       ax.plot3D (* zip (p1, p2), color = "b")
plt.show ()

check
