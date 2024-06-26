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

    print("Analysis of the membrane z-dimension")
    DA.find_membrane_location_hexstructure(mem_selector="resname C")
    print("\tz_lower: " + str(DA.z_lower))

    fig_hist, ax_hist = DA.create_hist_for_axis(["resname HEX and name C1"], 2)
    ax_hist.axvline(DA.z_lower, color="r", linestyle="--", label="z_lower")
    ax_hist.axvline(DA.z_lower + DA.L, color="g", linestyle="--", label="z_upper")
    ax_hist.legend()
    DA.save_fig_to_results(fig=fig_hist, name="x_hist_hex_borders")

    print("\nHEX analysis")

    ffs, ffe = DA.calc_passagetimes(["resname HEX and name C1"])
    print("\tpassages: " + str(len(ffs)))

    D_hex = DA.calc_diffusion(list(ffe - ffs))
    print("\tDiffusioncoefficient: " + str(D_hex).replace(".", ","))

    fig_hex_diff = DA.plot_diffusion(list(ffe - ffs), D_hex)
    DA.save_fig_to_results(fig=fig_hex_diff, name="diffusion_hex")

    print("\nDOD analysis")

    ffs, ffe = DA.calc_passagetimes(["resname DOD and name C2"])
    print("\tpassages: " + str(len(ffs)))

    D_dod = DA.calc_diffusion(list(ffe - ffs))
    print("\tDiffusioncoefficient: " + str(D_dod).replace(".", ","))

    fig_dod_diff = DA.plot_diffusion(list(ffe - ffs), D_dod)
    DA.save_fig_to_results(fig=fig_dod_diff, name="diffusion_dod")

    DA.save_trajectories_if_notthere()

    plt.show()
    print("\n\n\n")
