import numpy as np
import MembraneAnalysisToolbox.funcs as tfm

path = '/hugepool/data/sofia_simulationen/carbon/finished_sim/hex/poresize/2nm_NVT/simulation_3/analysis/'

timeline = np.load(path + "timeline.npy")
zbounds = [240, 400]  # obtained with the inspect data script

for res in ["hex", "dod"]:
    prefix = res + "_traj_"

    x = np.load(path + prefix + "x.npy")
    y = np.load(path + prefix + "y.npy")
    z = np.load(path + prefix + "z.npy")

    # GET PASSAGES AND TRANSITION DURATION

    ffs, ffe, indizes = tfm.dur_dist_improved(z, zbounds)
    np.save(path + prefix + "indizes_transition.npy",indizes)
    np.save(path + prefix + "ffs_transition.npy",ffs)
    np.save(path + prefix + "ffe_transition.npy",ffe)
    # print(ffs)
    # print(ffe)
    # print(indizes)
    print(res + "-passages: " + str(ffs.size)) 


    # distances = tfm.calc_hor_dist(x_passages,y_passages,ffs,ffe)
    # print("Gesamte Distanz: " + str(np.sum(distances)))
    # np.save(path + prefix + "distances_hor.npy", distances)
