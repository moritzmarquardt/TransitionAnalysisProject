import numpy as np
import matplotlib.pyplot as plt
import MembraneAnalysisToolbox.funcs as tfm
import MembraneAnalysisToolbox.plot as tfmp

path = "sim_data/20231120/"
prefix = "dod_c2_"
x = np.load(path + prefix + "x.npy")
y = np.load(path + prefix + "y.npy")
z = np.load(path + prefix + "z.npy")
timeline = np.load(path + "timeline.npy")


zbounds = [20.5, 38.5]  # obtained with the inspect data script
xbounds = [1.5, 3, 6, 7.5, 10.5, 12, 15, 16.5]


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


distances = tfm.calc_hor_dist(x_passages,y_passages,ffs,ffe)
print("Gesamte Distanz: " + str(np.sum(distances)))
np.save(path + prefix + "distances_hor.npy", distances)
