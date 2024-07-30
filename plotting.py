import matplotlib.pyplot as plt
from MembraneAnalysisToolbox.DiffusionAnalysis import DiffusionAnalysis
from MembraneAnalysisToolbox.MembraneStructures import CubicMembrane, HexagonalMembrane

"""
this is the same code as the ipynb file to run the code and make the plots interactive
Ipynb is good for dev, because it is possible to load all the data and then change the code in the plot cell, it is much faster
"""


path = "/bigpool/users/ac130484/project/cubic_box_hex_dod/18_2_3_n/sim_1/"
# path = "/bigpool/users/ac130484/project/finished_sim/hex/poresize/2nm_NVT/simulation_1/"
print("Path: " + path + "\n")


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


# STEP 1: initialise the Data into the class
DA = DiffusionAnalysis(
    topology_file=path + "topol.tpr",
    trajectory_file=path + "traj.xtc",
    results_dir=path + "analysis/",
    analysis_max_step_size_ps=200,
    verbose=True,
    membrane=cubic_structure,
)

print(DA)

DA.find_membrane_location()
DA.print_membrane_location()
DA.verify_membrane_location()

selector = "resname HEX and name C1"
short = "hex"

DA.calc_passagetimes(selector)
print(f"\t{short}-passages: " + str(len(DA.passageTimes[selector])))
DA.plot_passagetimedist(selector)

DA.calc_diffusion(selector)
print(f"\t{short}-Diffusioncoefficient: " + str(DA.D[selector]).replace(".", ","))
fig_diff = DA.plot_diffusion(selector)

DA.create_rand_passages_plot("resname HEX and name C1", 1)

DA.plot_starting_points("resname HEX and name C1")


# This is a possibility to extract the code from a jupyter notebook
# That's how this file was created
"""
from json import load

filename = "plotting.ipynb"
with open(filename) as fp:
    nb = load(fp)
code = ""
for cell in nb["cells"]:
    if cell["cell_type"] == "code":
        source = "".join(line for line in cell["source"] if not line.startswith("%"))
        code += source + "\n"

print(code)
"""
