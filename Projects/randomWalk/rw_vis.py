import matplotlib.pyplot as plt
from Projects.randomWalk.rw import RandomWalk


rw = RandomWalk()
rw.fillWalk()

#plt.figure(figsize=(4, 2), dpi=300)

pnum = list(range(rw.num_points))

plt.scatter(rw.x_val, rw.y_val, c=pnum, cmap=plt.cm.inferno, s=5)

plt.scatter(rw.x_val[-1], rw.y_val[-1], c='red', s=45)
plt.scatter(rw.x_val[0], rw.y_val[0], c='green', s=45)
plt.show()