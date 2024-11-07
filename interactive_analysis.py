import json

import matplotlib.pyplot as plt
from MembraneAnalysisToolbox.DiffusionAnalysis import DiffusionAnalysis
from MembraneAnalysisToolbox.MembraneStructures import (
    CubicMembrane,
    HexagonalMembrane,
    Solvent,
)

path = input("Enter the path to the simulation: ")
print("Path: " + path + "\n")
membrane_type = input(
    "Enter the type of membrane (cubic (C) or hexagonal (H) or solvent (S)): "
)


def analyse_resname(selector: str, short: str):
    print(f"\n{short} analysis")

    DA.calc_passagetimes(selector)
    print(f"\t{short}-passages: " + str(len(DA.passageTimes[selector])))
    # DA.plot_passagetimedist(selector)

    DA.save_passage_times_in_ns_to_txt(selector, short + "_passagetimes_in_ns.txt")

    DA.calc_diffusion(selector)
    print(f"\t{short}-Diffusioncoefficient: " + str(DA.D[selector]).replace(".", ","))
    fig_diff = DA.plot_diffusion(selector)
    DA.save_fig_to_results(fig=fig_diff, name="diffusion_" + short)

    DA.plot_starting_points("resname HEX and name C1")


hexagonal_structure = HexagonalMembrane(
    selector="resname C",
    L=180,
)

cubic_structure = CubicMembrane(
    selector="resname C",
    cube_arrangement=(2, 2, 2),
    cube_size=90,
    pore_radius=15,
)

solvent_structure = Solvent(
    lowerZ=None,
    upperZ=None,
)

structure = None
if membrane_type == "C":
    structure = cubic_structure
elif membrane_type == "H":
    structure = hexagonal_structure
elif membrane_type == "S":
    structure = solvent_structure
    solvent_structure.lowerZ = input("Enter the lower Z value: ")
    solvent_structure.upperZ = input("Enter the upper Z value: ")
else:
    raise ValueError("Invalid input for membrane_type")


# STEP 1: initialise the Data into the class
DA = DiffusionAnalysis(
    topology_file=path + "topol.tpr",
    trajectory_file=path + "traj.xtc",
    results_dir=path + "analysis/",
    analysis_max_step_size_ps=200,
    verbose=True,
    membrane=structure,
)

print(DA)

DA.find_membrane_location()
DA.print_membrane_location()
DA.verify_membrane_location()
plt.show()


analyse_resname("resname HEX and name C1", "hex")

analyse_resname("resname DOD and name C2", "dod")

DA.store_results_json()
print(DA)
plt.show()
print("\n\n\n\n\n")
