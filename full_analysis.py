import MembraneAnalysisToolbox.TransitionPathAnalysis as mat
import matplotlib.pyplot as plt

'''
this file is for testing and development purposes only
'''

path = "/bigpool/users/ac130484/project/finished_sim/hex/poresize/2nm_NVT/simulation_1/"

Analysis2nm_1 = mat.TransitionPathAnalysis( 
    topology_file = path + 'topol.tpr', 
    trajectory_file = path + 'traj.xtc',
    verbose = True
)
z_lower = 235
L = 180
# z_lower, z_upper = Analysis2nm_1.find_membrane_coords()
# Analysis2nm_1.inspect(["resname HEX and name C1"])
Analysis2nm_1.inspect(["resname C"])
# Analysis2nm_1.inspect(['resname HEX and name C1', 'resname DOD and name C2'])
ffs, ffe, indizes = Analysis2nm_1.calc_passagetimes(["resname HEX and name C1"], z_lower, L)
print(len(ffs))
print(ffs)
print(ffe)
print(indizes)
D = Analysis2nm_1.calc_diffusion(list(ffe-ffs), L, T = 296)
print(D)
plt.show()
# Analysis2nm_1.plot_passagetimedist("resname HEX and name C1")
# Analysis2nm_1.plot_rand3dtrajs("resname HEX and name C1")
# Analysis2nm_1.plot_startpoints("resname HEX and name C1")
plt.show()
