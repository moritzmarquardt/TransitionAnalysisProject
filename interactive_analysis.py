import json

import matplotlib.pyplot as plt
from MembraneAnalysisToolbox.DiffusionAnalysis import DiffusionAnalysis
from MembraneAnalysisToolbox.MembraneStructures import (
    CubicMembrane,
    HexagonalMembrane,
    Solvent,
)

path = input("Enter the path to the simulation (the path has to end with '/'): ")
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

    DA.plot_starting_points(selector)


structure = None
if membrane_type == "C":
    structure = CubicMembrane(
        selector="resname C",
        cube_arrangement=(2, 2, 2),
        cube_size=90,
        pore_radius=15,
    )
elif membrane_type == "H":
    L = input(
        "Enter the length of the membrane in A or press enter to select the default of 180: "
    )
    if L == "":
        L = 180
    else:
        L = int(L)
    structure = HexagonalMembrane(
        selector="resname C",
        L=L,
    )
elif membrane_type == "S":
    lowerZ = int(input("Enter the lower Z value: "))
    upperZ = int(input("Enter the upper Z value: "))
    L = upperZ - lowerZ
    structure = Solvent(
        lowerZ=lowerZ,
        upperZ=upperZ,
        L=L,
    )

else:
    raise ValueError("Invalid input for membrane_type")


# STEP 1: initialise the Data into the class
DA = DiffusionAnalysis(
    topology_file=path + "topol.tpr",
    trajectory_file=path + "traj.xtc",
    results_dir=path + "analysis/",
    analysis_max_step_size_ps=20,
    verbose=True,
    membrane=structure,
)

print(DA)

if isinstance(DA.membrane, Solvent):
    DA.print_membrane_location()
else:
    DA.find_membrane_location()
    DA.print_membrane_location()
    DA.verify_membrane_location()
plt.show()

wants_to_analyse = True
print("Analyse the transitions of atoms here:")
while wants_to_analyse:
    resname = input("Enter the resname (example: HEX): ")
    name = input("Enter the name (example: C1): ")
    selector = f"resname {resname} and name {name}"
    short = resname.lower() + "_" + name.lower()
    analyse_resname(selector, short)

    wants_to_analyse = (
        input(
            "\n\n\n Do you want to analyse the transitions of another resname? (y/n) "
        )
        == "y"
    )

# analyse_resname("resname HEX and name C1", "hex")

# analyse_resname("resname DOD and name R2", "dod")

DA.store_results_json()
print(DA)
plt.show()
print("\n\n\n\n\n")
