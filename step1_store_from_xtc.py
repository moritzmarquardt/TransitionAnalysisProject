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

# select c1 atoms of the hex and dod molecules because otherwise 
# the passages of each oof the molecuele atoms are being counted
hex = u.select_atoms("resname HEX and name C1") 
dod = u.select_atoms("resname DOD and name C1")

nth = 20
timesteps = int(np.ceil(u.trajectory.n_frames/nth))
hex_traj = np.zeros((hex.n_atoms, timesteps, 3))
dod_traj = np.zeros((dod.n_atoms, timesteps, 3))
timeline = np.zeros(timesteps)
for i,ts in enumerate(u.trajectory[::nth]):
    hex_traj[:,i,:] = hex.positions
    dod_traj[:,i,:] = dod.positions
    timeline[i] = ts.time

for i,j in enumerate(["x", "y", "z"]):
    print("save " + j + " trajectories")
    np.save(
        save_path + "hex_traj_" + j + ".npy",
        hex_traj[:,:,i],
    )
    print(hex_traj[:,:,i].shape)
    np.save(
        save_path + "dod_traj_" + j + ".npy",
        dod_traj[:,:,i],
    )
    print(dod_traj[:,:,i].shape)

    
print("save timeline")
np.save(save_path + "timeline.npy", timeline)
print("saving is done")