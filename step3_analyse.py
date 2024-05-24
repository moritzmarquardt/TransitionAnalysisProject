import numpy as np
import MembraneAnalysisToolbox.funcs as tfm

path = '/bigpool/users/ac130484/project/finished_sim/hex/poresize/2nm_NVT/simulation_3/analysis/'
prefix = "dod_traj_"
x = np.load(path + prefix + "x.npy")
y = np.load(path + prefix + "y.npy")
z = np.load(path + prefix + "z.npy")
timeline = np.load(path + "timeline.npy")


zbounds = [240, 400]  # obtained with the inspect data script
# xbounds = [1.5, 3, 6, 7.5, 10.5, 12, 15, 16.5]


# GET PASSAGES AND TRANSITION DURATION

ffs, ffe, indizes = tfm.dur_dist_improved(z, zbounds)
np.save(path + prefix + "indizes_transition.npy",indizes)
np.save(path + prefix + "ffs_transition.npy",ffs)
np.save(path + prefix + "ffe_transition.npy",ffe)
print(ffs)
print(ffe)
print(indizes)
print("passages: " + str(ffs.size))

x_passages = x[indizes]
y_passages = y[indizes]
z_passages = z[indizes]

np.save(path + prefix + "x_passages.npy", x_passages)
np.save(path + prefix + "y_passages.npy", y_passages)
np.save(path + prefix + "z_passages.npy", z_passages)


# distances = tfm.calc_hor_dist(x_passages,y_passages,ffs,ffe)
# print("Gesamte Distanz: " + str(np.sum(distances)))
# np.save(path + prefix + "distances_hor.npy", distances)
