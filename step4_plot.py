# inspct file that has routines and workflow to inspect trajectories
# shoukd be possible too read out boundaries,
# verify data
import numpy as np
import matplotlib.pyplot as plt
import MembraneAnalysisToolbox.funcs as tfm
import MembraneAnalysisToolbox.plot as tfmp

path = "./sim_data/20231017/"
prefix = "dod_c2_"
x_passages = np.load(path + prefix + "x_passages.npy")
y_passages = np.load(path + prefix + "y_passages.npy")
z_passages = np.load(path + prefix + "z_passages.npy")
ffs = np.load(path + prefix + "ffs_transition.npy")
ffe = np.load(path + prefix + "ffe_transition.npy")
distances = np.load(path + prefix + "distances_hor.npy") 
timeline = np.load(path + "timeline.npy")


zbounds = [20.5, 38.5]  # obtained with the inspect data script
xbounds = [1.5, 3, 6, 7.5, 10.5, 12, 15, 16.5]

# plt.figure("passages")
# for traj in z_passages:
#     tfmp.plot_1dtraj(traj)
# plt.savefig(path + prefix + 'z_passages.png')


plt.figure("Verteilung der Durchgangszeiten")
print(ffe-ffs)
print(ffs)
tfmp.plot_dist(ffe-ffs,number_of_bins=10, max_range=np.max(ffe-ffs))
plt.xlabel("Durchgangszeiten")
plt.ylabel("relative Häufigkeit")

#Verteilung der horizontal zurückgelegten Strecke
plt.figure("Verteilung der quer zurückgelegten Strecke")
tfmp.plot_dist(distances,number_of_bins=30,max_range=np.max(distances))
plt.xlabel("horizontale strecke dodecane")
plt.ylabel("relative Häufigkeit")

direct = tfm.path_cat(x_passages,y_passages,ffs,ffe)
print("direkt Durchgänge: " + str(direct))


#plotten einer 3d trajectorie
# sel = 1
kernel_size = 1000
kernel = np.ones(kernel_size) / kernel_size
fig = plt.figure("3d trajektorien")
ax = fig.add_subplot(projection='3d')
for sel in range(20):
    #glätten
    x_passages_sel = np.convolve(x_passages[sel],kernel, mode='valid')
    y_passages_sel = np.convolve(y_passages[sel],kernel, mode='valid')
    z_passages_sel = np.convolve(z_passages[sel],kernel, mode='valid')
    tfmp.plot_3dtraj(ax, x_passages_sel[::1000],y_passages_sel[::1000],z_passages_sel[::1000]) #++1 so that the last timestep is also included
    # tfmp.plot_3dpoints(ax, x_passages_sel[ffs[sel]],y_passages_sel[ffs[sel]],z_passages_sel[ffs[sel]]) #starting point
    # tfmp.plot_3dpoints(ax, x_passages_sel[ffe[sel]],y_passages_sel[ffe[sel]],z_passages_sel[ffe[sel]]) #end point
tfmp.plot_3dbounds(ax, zbounds)


#Z-traj plotten
'''
sel = 10
plt.figure("Z-trajectorie des " + str(sel) + ". Durchgangs")
tfmp.plot_1dtraj(z_dod_passages[sel])
tfmp.plot_hor_bounds(zbounds)
tfmp.plot_point(ffs[sel],z_dod_passages[sel,ffs[sel]])
tfmp.plot_point(ffe[sel],z_dod_passages[sel,ffe[sel]])
plt.xlabel("Zeitschritte")
plt.ylabel("Z-Wert")
'''




#Durchgangszeten verteilung plotten
'''plt.figure("Verteilung der Durchgangszeiten")
tfmp.plot_dist(ffe-ffs,number_of_bins=30, max_range=1000)
plt.xlabel("Durchgangszeiten")
plt.ylabel("relative Häufigkeit")'''

# plot starting points
fig = plt.figure("plotten aller Startpunkte")
ax = fig.add_subplot(projection='3d')
tfmp.plot_3dpoints(ax,x_passages[np.arange(np.size(x_passages,0)),ffs+1],y_passages[np.arange(np.size(x_passages,0)),ffs+1],z_passages[np.arange(np.size(x_passages,0)),ffs+1]) #ugly way of getting the point. maybe there is a better way
# tfmp.plot_3dpoints(ax,x_passages[np.arange(np.size(x_passages,0)),ffs+200],y_passages[np.arange(np.size(x_passages,0)),ffs+200],z_passages[np.arange(np.size(x_passages,0)),ffs+200]) #ugly way of getting the point. maybe there is a better way
# tfmp.plot_3dpoints(ax,x_passages[np.arange(np.size(x_passages,0)),ffs+3000],y_passages[np.arange(np.size(x_passages,0)),ffs+3000],z_passages[np.arange(np.size(x_passages,0)),ffs+3000]) #ugly way of getting the point. maybe there is a better way

plt.show()
