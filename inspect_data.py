# inspct file that has routines and workflow to inspect trajectories
# shoukd be possible to read out boundaries,
# verify data
import numpy as np
import matplotlib.pyplot as plt
from functions.plot import *
from functions.funcs import *
import matplotlib
'''
STEP 2:
- inspect the received data
- Choose boundaries,
- check for timeline
- plot sample trajectories for plausibility analysis
'''

path = "sim_data/20231017/"
prefix = "dod_c2_"
x = np.load(path + prefix + "x.npy")
y = np.load(path + prefix + "y.npy")
z = np.load(path + prefix + "z.npy")
timeline = np.load(path + "timeline.npy")

print("max z-value: " + str(np.max(z)) + "; min z-value: " + str(np.min(z)))

print("number of trajs: " + str(np.size(x[:, 0])))
print("number of timesteps: " + str(np.size(x[0, :])))

plt.figure()
plot_dist(x, max_range=50)
plt.savefig(path + prefix + 'x_dist.png')

plt.figure()
plot_dist(y, max_range=50)
plt.savefig(path + prefix + 'y_dist.png')

plt.figure()
plot_dist(z, max_range=50)
plt.savefig(path + prefix + 'z_dist.png')

plt.show()


'''
zbounds = [20.5, 38.5]  # von sofia
xbounds = [1.5, 3, 6, 7.5, 10.5, 12, 15, 16.5]


sele = 100  # Stichprobe einer Trajektorie
plt.figure()
for i in range(30):
    plot_1dtraj(z[sele + i, :])
plot_hor_bounds(zbounds)
plt.savefig(path + 'sele_trajs.png')

plt.figure()
plot_1dtraj(x[sele, :])
plot_1dtraj(y[sele, :])
plt.savefig(path + '1d_trajs_sele_xy.png')

# GET PASSAGES AND TRANSITION DURATION

ffs, ffe, indizes = dur_dist_improved(z, zbounds)
np.save(path + "indizes_transition.npy",indizes)
np.save(path + "ffs_transition.npy",indizes)
np.save(path + "ffe_transition.npy",indizes)
print(ffs)
print(ffe)
print(indizes)
print("passages: " + str(ffs.size))

x_dod_passages = x[indizes]
y_dod_passages = y[indizes]
z_dod_passages = z[indizes]

distances = calc_hor_dist(x_dod_passages,y_dod_passages,ffs,ffe)
print("Gesamte Distanz: " + str(np.sum(distances)))
np.save(path + "distances_hor.npy", distances)

#Verteilung der horizontal zurückgelegten Strecke
plt.figure("dodecane Verteilung der quer zurückgelegten Strecke")
plot_dist(distances,number_of_bins=30,max_range=800)
plt.xlabel("horizontale strecke dodecane")
plt.ylabel("relative Häufigkeit")

direct = path_cat(x_dod_passages,y_dod_passages,ffs,ffe)
print("direkt Durchgänge: " + str(direct))
plt.show()

'''