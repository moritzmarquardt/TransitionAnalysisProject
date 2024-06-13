import MembraneAnalysisToolbox.TransitionPathAnalysis as mat
import matplotlib.pyplot as plt

'''
this file is for testing and development purposes only
'''

path = "/bigpool/users/ac130484/project/finished_sim/hex/poresize/3nm_NVT/simulation_1/"

Analysis2nm_1 = mat.TransitionPathAnalysis( 
    topology_file = path + 'topol.tpr', 
    trajectory_file = path + 'traj.xtc',
    verbose = True
)
L = 180
z_lower = Analysis2nm_1.find_z_lower_hexstruc(mem_selector = "resname C", L=L)
print("z_lower: " + str(z_lower))
Analysis2nm_1.inspect(["resname HEX and name C1"], z_lower, L)
Analysis2nm_1.inspect(["resname C"], z_lower, L)

# Hex analysis
print("Hex analysis")
ffs, ffe, indizes = Analysis2nm_1.calc_passagetimes(["resname HEX and name C1"], z_lower, L)
print("passages: " + str(len(ffs)))
D = Analysis2nm_1.calc_diffusion(list(ffe-ffs), L, T = 296)
print("Diffusioncoefficient: " + str(D))
plt.show()
# Analysis2nm_1.plot_passagetimedist("resname HEX and name C1")
# Analysis2nm_1.plot_rand3dtrajs("resname HEX and name C1")
# Analysis2nm_1.plot_startpoints("resname HEX and name C1")
plt.show()

# Dod analysis
print("Dod analysis")
ffs, ffe, indizes = Analysis2nm_1.calc_passagetimes(["resname DOD and name C2"], z_lower, L)
print("passages: " + str(len(ffs)))
D = Analysis2nm_1.calc_diffusion(list(ffe-ffs), L, T = 296)
print("Diffusioncoefficient: " + str(D))
plt.show()
# Analysis2nm_1.plot_passagetimedist("resname HEX and name C1")
# Analysis2nm_1.plot_rand3dtrajs("resname HEX and name C1")
# Analysis2nm_1.plot_startpoints("resname HEX and name C1")
plt.show()
