# inspct file that has routines and workflow to inspect trajectories
# shoukd be possible too read out boundaries,
# verify data
import numpy as np
import matplotlib.pyplot as plt
from functions.plot import *
from functions.funcs import *

# x = np.load("sim_data/20231017/dod_c2_x.npy")
# y = np.load("sim_data/20231017/dod_c2_y.npy")
z = np.load("sim_data/20231017/dod_c2_z.npy")
timeline = np.load("sim_data/20231017/timeline.npy")

zbounds = [20.5, 38.5]  # von sofia

sele = 11199  # Stichprobe einer Trajektorie
plt.figure()
indizes = np.load("indizes.npy")[:10]
for i in indizes:
    plot_1dtraj(z[i, :])
plot_hor_bounds(zbounds)
plt.savefig('plots/sele_trajs.png')


'''
[11720  5172 12002  5097 17222 12088 17339  1000 15186 10174   846 19531
    10 16956  7137  6830  4397 16663  8048 13131  8850 20704 29182  7103
 12543 30121 21810 11675 10347  2256 36455]
[ 5520  2045 11199 11702 21558  9945 13233 12488 12534  5948 11471 12031
 10927  1779 13462 13551 21919 17150 14410 12182  5128 21016 20562 22163
 18382 17928 16822 12308  5667 15934 19101]
passages: 31
'''

#Z-traj plotten
'''sel = 10
plt.figure("Z-trajectorie des " + str(sel) + ". Durchgangs")
tfmp.plot_1dtraj(z_dod_passages[sel])
tfmp.plot_hor_bounds(zbounds)
tfmp.plot_point(ffs[sel],z_dod_passages[sel,ffs[sel]])
tfmp.plot_point(ffe[sel],z_dod_passages[sel,ffe[sel]])
plt.xlabel("Zeitschritte")
plt.ylabel("Z-Wert")'''

#plotten einer 3d trajectorie
'''sel = 10
fig = plt.figure("3d trajektorie des " + str(sel) + ". Durchgangs")
ax = fig.add_subplot(projection='3d')
tfmp.plot_3dtraj(ax, x_dod_passages[sel][ffs[sel]:ffe[sel]+1],y_dod_passages[sel][ffs[sel]:ffe[sel]+1],z_dod_passages[sel][ffs[sel]:ffe[sel]+1]) #++1 so that the last timestep is also included
tfmp.plot_3dpoints(ax, x_dod_passages[sel,ffs[sel]],y_dod_passages[sel,ffs[sel]],z_dod_passages[sel,ffs[sel]]) #starting point
tfmp.plot_3dpoints(ax, x_dod_passages[sel,ffe[sel]],y_dod_passages[sel,ffe[sel]],z_dod_passages[sel,ffe[sel]]) #end point
tfmp.plot_3dbounds(ax, xbounds)'''


#Durchgangszeten verteilung plotten
'''plt.figure("Verteilung der Durchgangszeiten")
tfmp.plot_dist(ffe-ffs,number_of_bins=30, max_range=1000)
plt.xlabel("Durchgangszeiten")
plt.ylabel("relative Häufigkeit")'''

# plot starting points
'''fig = plt.figure("plotten aller Startpunkte")
ax = fig.add_subplot(projection='3d')
tfmp.plot_3dpoints(ax,x_dod_passages[np.arange(np.size(x_dod_passages,0)),ffs+1],y_dod_passages[np.arange(np.size(x_dod_passages,0)),ffs+1],z_dod_passages[np.arange(np.size(x_dod_passages,0)),ffs+1]) #ugly way of getting the point. maybe there is a better way
'''