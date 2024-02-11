import numpy as np
import matplotlib.pyplot as plt
import MDAnalysis as mda
import scipy.optimize as spo
import time

start = time.time()

# several time frames in the xtc file and tpr as topology file
u = mda.Universe('/bigpool/users/ac130484/project/hex_box_hex_dod/hex_18_2_3_n/simulation/20fs.tpr','/bigpool/users/ac130484/project/hex_box_hex_dod/hex_18_2_3_n/simulation/20fs.gro')
# u = mda.Universe('/bigpool/users/st166545/TPS/240130kri_new_sim/traj_firstframe.gro', '/bigpool/users/st166545/TPS/240130kri_new_sim/traj.xtc')
# u = mda.Universe('/bigpool/data/projects/Carbon_pores_Sofia/kri_with_vacuum_test/hex_18_3_2_n_vacuum/simulation_1/topol.tpr', '/bigpool/users/st166545/TPS/kri_with_vacuum_test_skip10.xtc')
print(u)


c_atoms = u.select_atoms('resname C')
hex_atoms = u.select_atoms('resname HEX')
dod_atoms = u.select_atoms('resname DOD')
print(c_atoms)

c_atomic_positions = np.zeros((u.trajectory.n_frames,len(c_atoms),3))
dod_atomic_positions = np.zeros((u.trajectory.n_frames,len(dod_atoms),3))
hex_atomic_positions = np.zeros((u.trajectory.n_frames,len(hex_atoms),3))
print(np.shape(c_atomic_positions))

print(u.trajectory)
print(u.trajectory.n_frames)
for ts in u.trajectory:
    # print(ts)
    # print(ts.frame)
    c_atomic_positions[ts.frame,:,:] = c_atoms.positions
    hex_atomic_positions[ts.frame,:,:] = hex_atoms.positions
    dod_atomic_positions[ts.frame,:,:] = dod_atoms.positions
    # print(dod_atoms.positions)


print("pos aquire done after: " + str(time.time()-start))

# Set constraints on y and z directions
y_min, y_max = 27, 33  # Replace with your desired range
z_min, z_max = 250, 400  # Replace with your desired range

# optional histogrmas to detect the bounds
'''plt.figure()
plt.hist(c_atomic_positions[:,:,0].flatten(),bins=50)
plt.figure()
plt.hist(c_atomic_positions[:,:,1].flatten(),bins=50)
plt.figure()
plt.hist(c_atomic_positions[:,:,2].flatten(),bins=50)
plt.show()'''

# Filter positions based on y and z constraints
c_filtered_indices = np.where(
    (c_atomic_positions[:,:, 1] >= y_min) & (c_atomic_positions[:,:, 1] <= y_max) &
    (c_atomic_positions[:,:, 2] >= z_min) & (c_atomic_positions[:,:, 2] <= z_max)
)
print(c_filtered_indices)

dod_filtered_indices = np.where(
    (dod_atomic_positions[:,:, 1] >= y_min) & (dod_atomic_positions[:,:, 1] <= y_max) &
    (dod_atomic_positions[:,:, 2] >= z_min) & (dod_atomic_positions[:,:, 2] <= z_max)
)

hex_filtered_indices = np.where(
    (hex_atomic_positions[:,:, 1] >= y_min) & (hex_atomic_positions[:,:, 1] <= y_max) &
    (hex_atomic_positions[:,:, 2] >= z_min) & (hex_atomic_positions[:,:, 2] <= z_max)
)

c_filtered_x_positions = c_atomic_positions[c_filtered_indices[0],c_filtered_indices[1], 0].flatten()
dod_filtered_x_positions = dod_atomic_positions[dod_filtered_indices[0],dod_filtered_indices[1], 0].flatten()
hex_filtered_x_positions = hex_atomic_positions[hex_filtered_indices[0],hex_filtered_indices[1], 0].flatten()

print("filtering done after: " + str(time.time()-start))


# Compute histograms
bins = 50
c_hist, c_bin_edges = np.histogram(c_filtered_x_positions, density=1, bins=bins)
dod_hex_hist, dod_hex_bin_edges= np.histogram(np.append(dod_filtered_x_positions,hex_filtered_x_positions), density=1, bins=bins)

print("hist calc done after: " + str(time.time()-start))


# Plot all histograms in one plot
plt.figure()
plt.plot(c_bin_edges[:-1], c_hist, label='C', linestyle='-', marker='o', markersize=3)
plt.plot(dod_hex_bin_edges[:-1], dod_hex_hist, label='DOD & HEX', linestyle='-', marker='o', markersize=3)

plt.xlabel('X-axis')
plt.ylabel('Frequency')
plt.title('Histogram Line Plot along the X-axis with Y and Z constraints for Residue Atoms')
plt.grid(True)
plt.legend()

plt.show()
