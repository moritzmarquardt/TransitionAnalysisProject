import json

import matplotlib.pyplot as plt
from MembraneAnalysisToolbox.DiffusionAnalysis import DiffusionAnalysis

"""
this file is for testing and development purposes only
"""
"""
paths = [
    "/bigpool/users/ac130484/project/finished_sim/hex/poresize/"
    + str(nm)
    + "nm_NVT/simulation_"
    + str(s)
    + "/"
    for nm in [2, 3, 4, 6]
    for s in [1, 2, 3]
]
paths.append(
    "/bigpool/users/ac130484/project/finished_sim/hex/hexane_dodecane/hex_18_3_2_n/"
)
paths.append(
    "/bigpool/users/ac130484/project/finished_sim/hex/hexane_dodecane/hex_18_3_2_y_5/"
)
paths.append(
    "/bigpool/users/ac130484/project/finished_sim/hex/hexane_dodecane/hex_18_3_2_y_10/"
)
paths.append(
    "/bigpool/users/ac130484/project/finished_sim/hex/hexane_dodecane/hex_18_3_2_y_15/"
)
paths.append(
    "/bigpool/users/ac130484/project/finished_sim/hex/hexane_dodecane/hex_18_3_2_y_20/"
)
paths.append(
    "/bigpool/users/ac130484/project/finished_sim/hex/hexane_dodecane/hex_18_3_2_y_50/"
)
paths.append(
    "/bigpool/users/ac130484/project/finished_sim/hex/hexane_dodecane/hex_18_3_2_y_99/"
)

paths.append(
    "/bigpool/users/ac130484/project/finished_sim/hex/hexane_hexanole/hex_18_3_2_n/"
)
paths.append(
    "/bigpool/users/ac130484/project/finished_sim/hex/hexane_hexanole/hex_18_3_2_y_5/"
)
paths.append(
    "/bigpool/users/ac130484/project/finished_sim/hex/hexane_hexanole/hex_18_3_2_y_10/"
)
paths.append(
    "/bigpool/users/ac130484/project/finished_sim/hex/hexane_hexanole/hex_18_3_2_y_15/"
)
paths.append(
    "/bigpool/users/ac130484/project/finished_sim/hex/hexane_hexanole/hex_18_3_2_y_20/"
)
paths.append(
    "/bigpool/users/ac130484/project/finished_sim/hex/hexane_hexanole/hex_18_3_2_y_50/"
)
paths.append(
    "/bigpool/users/ac130484/project/finished_sim/hex/hexane_hexanole/hex_18_3_2_y_99/"
)

"""

paths = [
    "/bigpool/users/ac130484/project/finished_sim/hex/poresize/"
    + str(nm)
    + "nm_NVT/simulation_"
    + str(s)
    + "/"
    for nm in [3]
    for s in [1, 2, 3]
]
# paths = [
#     "/bigpool/users/ac130484/project/finished_sim/hex/hexane_dodecane/hex_18_3_2_n/"
# ]


def analyse_resname(selector: str, short: str):
    print(f"\n{short} analysis")

    DA.calc_passagetimes(selector)
    print(f"\t{short}-passages: " + str(len(DA.passageTimes[selector])))

    DA.save_passage_times_in_ns_to_txt(selector, short + "_passagetimes_in_ns.txt")

    DA.calc_diffusion(selector)
    print(f"\t{short}-Diffusioncoefficient: " + str(DA.D[selector]).replace(".", ","))

    fig_diff = DA.plot_diffusion(selector)
    DA.save_fig_to_results(fig=fig_diff, name="diffusion_" + short)


diff_coeffs = {}

for path in paths:
    print("Path: " + path)

    # STEP 1: initialise the Data into the class
    DA = DiffusionAnalysis(
        topology_file=path + "topol.tpr",
        trajectory_file=path + "traj.xtc",
        results_dir=path + "analysis/",
        analysis_max_step_size_ps=200,
        verbose=False,
        L=180,
    )

    print(DA)

    DA.find_membrane_location_hexstructure(mem_selector="resname C")
    print("\tz_lower: " + str(DA.z_lower))

    DA.verify_membrane_location(mem_selector="resname HEX and name C1")

    analyse_resname("resname HEX and name C1", "hex")

    analyse_resname("resname DOD and name C2", "dod")

    DA.store_results_json()
    diff_coeffs[path] = DA.D
    plt.show()
    print("\n\n\n")

print("\n\n\n RESULTS:")
print(json.dumps(diff_coeffs, indent=4))
