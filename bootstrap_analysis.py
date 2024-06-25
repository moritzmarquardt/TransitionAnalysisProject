import MembraneAnalysisToolbox.TransitionPathAnalysis as TPA
import matplotlib.pyplot as plt
import numpy as np

'''
this file is for testing and development purposes only of the bootstrapping function in the TPAnalysis class
'''
# paths = [str(nm) + "nm_NVT/simulation_" + str(s) + "/" for nm in [2,3,4,6] for s in [1,2,3]]
paths = ["3nm_NVT/simulation_2/"]

for path in paths:
    path = "/bigpool/users/ac130484/project/finished_sim/hex/poresize/" + path
    print("Path: " + path)

    # STEP 1: initialise the Data into the class
    Analysis2nm_1 = TPA.TransitionPathAnalysis( 
        topology_file = path + 'topol.tpr', 
        trajectory_file = path + 'traj.xtc',
        verbose = True
    )
    L = 180

    # STEP 2: Find z_lower and validate by eye
    print("Analysis of the membrane z-dimension")
    # z_lower = Analysis2nm_1.find_z_lower_hexstruc(mem_selector = "resname C", L=L)
    z_lower = 233.23501586914062
    print("\tz_lower: " + str(z_lower))



    # STEP 3: Calculate the diffusion coefficient from all the time
    # ffs, ffe, indizes = Analysis2nm_1.calc_passagetimes(["resname HEX and name C1"], z_lower, L)
    # D = Analysis2nm_1.calc_diffusion(list(ffe-ffs), L)
    D = 16.709077586864158
    print("\nDiffusioncoefficient (benchmark 10 000ns): " + str(D).replace(".",","))

        
    # BOOTSTRAPPING
    # bootstrap_diffs = Analysis2nm_1.bootstrap_diffusion("resname HEX and name C1", z_lower, L, n_bootstraps = 100, plot = False)
    # print("\nBootstraped Diffusion Coefficients: " + str(bootstrap_diffs))
    
    bootstrap_diffs = Analysis2nm_1.bootstrapping_diffusion(
        selector = "resname HEX and name C1", 
        bootstrap_sample_length_ns = 1000, 
        n_bootstraps = 1000, 
        z_lower = z_lower, 
        L = L, 
        plot = False
        )
    print("\nBootstraped Diffusion Coefficients: " + str(bootstrap_diffs))


    plt.hist(bootstrap_diffs)
    plt.axvline(D, color='r', linestyle='dashed', linewidth=1)


    print("mean: " + str(np.mean(bootstrap_diffs)))
    print("std: " + str(np.std(bootstrap_diffs)))
    print("standard error of the mean: " + str(np.std(bootstrap_diffs)/np.sqrt(len(bootstrap_diffs))))

    plt.show()

