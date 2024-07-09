import json

import matplotlib.pyplot as plt
from MembraneAnalysisToolbox.DiffusionAnalysis import DiffusionAnalysis

path = input("Enter the path to the simulation: ")
print("Path: " + path)


def analyse_resname(selector: str, short: str):
    print(f"\n{short} analysis")

    DA.calc_passagetimes(selector)
    print(f"\t{short}-passages: " + str(len(DA.passageTimes[selector])))

    DA.save_passage_times_in_ns_to_txt(selector, short + "_passagetimes_in_ns.txt")

    DA.calc_diffusion(selector)
    print(f"\t{short}-Diffusioncoefficient: " + str(DA.D[selector]).replace(".", ","))

    fig_diff = DA.plot_diffusion(selector)
    DA.save_fig_to_results(fig=fig_diff, name="diffusion_" + short)


# STEP 1: initialise the Data into the class
DA = DiffusionAnalysis(
    topology_file=path + "topol.tpr",
    trajectory_file=path + "traj.xtc",
    results_dir=path + "analysis/",
    analysis_max_step_size_ps=200,
    verbose=True,
    L=180,
)

print(DA)

DA.find_membrane_location_hexstructure(mem_selector="resname C")
print("\tz_lower: " + str(DA.z_lower))

DA.verify_membrane_location(mem_selector="resname HEX and name C1")

analyse_resname("resname HEX and name C1", "hex")

analyse_resname("resname DOD and name C2", "dod")

DA.store_results_json()
plt.show()
print("\n\n\n RESULTS:")
print(json.dumps(DA.D, indent=4))
