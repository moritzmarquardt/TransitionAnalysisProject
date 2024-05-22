import numpy as np
import MDAnalysis as mda

'''
STEP 1:
- store the numpy files of x,y,z trajectories for both solvents from a traj.xtc file
- it is assumed that the traj.xtc file is in the same folder as the topol.tpr file
- The files (that end with xvg - so trajectory files) are stored into the same folder with the same name but with the ending .npy
'''

print("store traj.xtc file as .npy files")
path = '/bigpool/users/ac130484/project/finished_sim/hex/poresize/2nm_NVT/simulation_3/'
save_path = path + "analysis/"
# save_path = "sim_data/temp/"


u = mda.Universe(path + "topol.tpr", path + 'traj.xtc')

hex = u.select_atoms("resname HEX")
dod = u.select_atoms("resname DOD")

hex_traj = np.zeros((u.trajectory.n_frames, hex.n_atoms , 3))
dod_traj = np.zeros((u.trajectory.n_frames, dod.n_atoms , 3))
timeline = np.zeros(u.trajectory.n_frames)
for ts in u.trajectory:
    hex_traj[ts.frame,:,:] = hex.positions
    dod_traj[ts.frame,:,:] = dod.positions
    timeline[ts.frame] = ts.time

for i,j in enumerate(["x", "y", "z"]):
    np.save(
        save_path + "hex_traj_" + j + ".npy",
        hex_traj[:,:,i],
    )
    np.save(
        save_path + "dod_traj_" + j + ".npy",
        dod_traj[:,:,i],
    )

np.save(save_path + "timeline.npy", timeline)