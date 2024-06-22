import MembraneAnalysisToolbox.TransitionPathAnalysis as TPA
import matplotlib.pyplot as plt

'''
this file is for testing and development purposes only
'''
# paths = [str(nm) + "nm_NVT/simulation_" + str(s) + "/" for nm in [2,3,4,6] for s in [1,2,3]]
paths = [str(nm) + "nm_NVT/simulation_" + str(s) + "/" for nm in [6] for s in [2,3]]

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
    z_lower = Analysis2nm_1.find_z_lower_hexstruc(mem_selector = "resname C", L=L)
    print("Analysis of the membrane z-dimension")
    print("\tz_lower: " + str(z_lower))
    Analysis2nm_1.inspect(["resname HEX and name C1"], z_lower, L)

    # STEP 3: analyse passage times and calculate diffusion coefficient
    # Hex analysis
    print("\nHEX analysis")
    ffs, ffe, indizes = Analysis2nm_1.calc_passagetimes(["resname HEX and name C1"], z_lower, L)
    print("\tpassages: " + str(len(ffs)))
    D = Analysis2nm_1.calc_diffusion(list(ffe-ffs), L, T = 296)
    print("\tDiffusioncoefficient: " + str(D).replace(".",","))
    plt.show()

    # Dod analysis
    print("\tDOD analysis")
    ffs, ffe, indizes = Analysis2nm_1.calc_passagetimes(["resname DOD and name C2"], z_lower, L)
    print("\tpassages: " + str(len(ffs)))
    D = Analysis2nm_1.calc_diffusion(list(ffe-ffs), L, T = 296)
    print("\tDiffusioncoefficient: " + str(D).replace(".",","))
    plt.show()
