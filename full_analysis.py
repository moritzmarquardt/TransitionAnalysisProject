import MembraneAnalysisToolbox.TransitionPathAnalysis as mat
import matplotlib.pyplot as plt

'''
this file is for testing and development purposes only
'''

path = "/bigpool/users/ac130484/project/finished_sim/hex/poresize/2nm_NVT/simulation_3/"

Analysis2nm_1 = mat.TransitionPathAnalysis( 
    topology_file = path + 'topol.tpr', 
    trajectory_file = path + 'traj.xtc',
    membrane_selectors = ['C'],
    solvent_selectors = ['HEX and name C1', 'DOD and name C2'],
    verbose = True
)
z_lower = 235
z_upper = 415
# z_lower, z_upper = Analysis2nm_1.find_membrane_coords()
Analysis2nm_1.inspect(["HEX and name C1"])
Analysis2nm_1.inspect(['HEX and name C1', 'DOD and name C2'])
ffs, ffe, indizes = Analysis2nm_1.calc_passagetimes(["HEX and name C1"], z_lower, z_upper)
print(ffs)
print(ffe)
print(indizes)
D = Analysis2nm_1.calc_diffusion(list(ffe-ffs), L = z_lower - z_upper, T = 296)
print(D)
plt.show()
# Analysis2nm_1.plot_passagetimedist("HEX")
# Analysis2nm_1.plot_rand3dtrajs("HEX")
# Analysis2nm_1.plot_startpoints("HEX")
plt.show()
