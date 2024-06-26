import matplotlib.pyplot as plt
from MembraneAnalysisToolbox.DiffusionAnalysis import DiffusionAnalysis

"""
this file is for testing and development purposes only
"""
paths = [
    str(nm) + "nm_NVT/simulation_" + str(s) + "/"
    for nm in [2, 3, 4, 6]
    for s in [1, 2, 3]
]

for path in paths:
    path = "/bigpool/users/ac130484/project/finished_sim/hex/poresize/" + path
    print("Path: " + path)

    # STEP 1: initialise the Data into the class
    DA = DiffusionAnalysis(
        topology_file=path + "topol.tpr",
        trajectory_file=path + "traj.xtc",
        analysed_max_step_size_ps=200,
        results_dir=path + "analysis/",
        verbose=True,
        L=180,
    )

    print(DA)

    # STEP 2: Find z_lower and validate by eye
    print("Analysis of the membrane z-dimension")
    DA.find_membrane_location_hexstructure(mem_selector="resname C")
    print("\tz_lower: " + str(DA.z_lower))
    fig, ax = DA.create_hist_for_axis(["resname HEX and name C1"], 2)
    ax.axvline(DA.z_lower, color="r", linestyle="--", label="z_lower")
    ax.axvline(DA.z_lower + DA.L, color="g", linestyle="--", label="z_upper")
    ax.legend()
    DA.save_fig_to_results(fig=fig, name="x_hist_hex_boarders")
    plt.show()
    # DA.save_trajectories()

    # STEP 3: analyse passage times and calculate diffusion coefficient
    # Hex analysis
    print("\nHEX analysis")
    ffs, ffe = DA.calc_passagetimes(["resname HEX and name C1"])
    print("\tpassages: " + str(len(ffs)))
    D_hex = DA.calc_diffusion(list(ffe - ffs))
    print("\tDiffusioncoefficient: " + str(D_hex).replace(".", ","))
    plt.show()

    # Dod analysis
    print("\nDOD analysis")
    ffs, ffe = DA.calc_passagetimes(["resname DOD and name C2"])
    print("\tpassages: " + str(len(ffs)))
    D_dod = DA.calc_diffusion(list(ffe - ffs))
    print("\tDiffusioncoefficient: " + str(D_dod).replace(".", ","))
    plt.show()
    print("\n\n\n")
