import numpy as np
import matplotlib.pyplot as plt
import MDAnalysis as mda
import scipy.optimize as spo
import time

# one timeframe in the gro file
gro_file_path = '/bigpool/users/ac130484/project/hex_box_hex_dod/hex_18_2_3_n/simulation/20fs.gro'
u = mda.Universe(gro_file_path)
c_atoms = u.select_atoms('resname C')
hex_atoms = u.select_atoms('resname HEX')
dod_atoms = u.select_atoms('resname DOD')
c_atomic_positions = c_atoms.positions
dod_atomic_positions = dod_atoms.positions
hex_atomic_positions = hex_atoms.positions

# several time frames in the gro file
# produce with echo 0 | gmx trjconv -f pathtosim/traj.xtc -s pathtosim/topol.tpr -dt 100000 -o traj_dt100ns.gro
'''gro_file_path = '/bigpool/users/ac130484/project/hex_box_hex_dod/hex_18_2_3_n/simulation/analyse_moritz/traj_dt100ns.gro'
u = mda.Universe(gro_file_path)
reader = mda.coordinates.memory.MemoryReader(u.trajectory)
all_positions = reader.read()

c_atoms_indices = u.select_atoms("resname C").indices
c_atomic_positions = all_positions[:, c_atoms_indices, :]
hex_atoms_indices = u.select_atoms("resname HEX").indices
hex_atomic_positions = all_positions[:, c_atoms_indices, :]
dod_atoms_indices = u.select_atoms("resname DOD").indices
dod_atomic_positions = all_positions[:, c_atoms_indices, :]'''

# gro_file_path = '/bigpool/users/ac130484/project/hex_box_hex_dod/hex_18_2_3_n/simulation/carbon_solvent_box_equi.gro'


# Set constraints on y and z directions
y_min, y_max = 27, 33  # Replace with your desired range
z_min, z_max = 250, 350  # Replace with your desired range

# plt.figure()
# plt.hist(hex_atomic_positions[:,0],bins=50)
# plt.figure()
# plt.hist(hex_atomic_positions[:,1],bins=50)
# plt.figure()
# plt.hist(hex_atomic_positions[:,2],bins=50)

# Filter positions based on y and z constraints
c_filtered_indices = np.where(
    (c_atomic_positions[:, 1] >= y_min) & (c_atomic_positions[:, 1] <= y_max) &
    (c_atomic_positions[:, 2] >= z_min) & (c_atomic_positions[:, 2] <= z_max)
)

dod_filtered_indices = np.where(
    (dod_atomic_positions[:, 1] >= y_min) & (dod_atomic_positions[:, 1] <= y_max) &
    (dod_atomic_positions[:, 2] >= z_min) & (dod_atomic_positions[:, 2] <= z_max)
)

hex_filtered_indices = np.where(
    (hex_atomic_positions[:, 1] >= y_min) & (hex_atomic_positions[:, 1] <= y_max) &
    (hex_atomic_positions[:, 2] >= z_min) & (hex_atomic_positions[:, 2] <= z_max)
)

c_filtered_x_positions = c_atomic_positions[c_filtered_indices, 0].flatten()
dod_filtered_x_positions = dod_atomic_positions[dod_filtered_indices, 0].flatten()
hex_filtered_x_positions = hex_atomic_positions[hex_filtered_indices, 0].flatten()

# Compute histograms
bins = 50
c_hist, c_bin_edges = np.histogram(c_filtered_x_positions, bins=bins)
dod_hex_hist, dod_hex_bin_edges= np.histogram(np.append(dod_filtered_x_positions,hex_filtered_x_positions), bins=bins)

# chat gpt
def largest_interval_below_threshold(counts, bin_edges, threshold):

    largest_interval = None
    current_interval = None
    for i in range(len(bin_edges) - 1):
        bin_value = counts[i]
        if bin_value < threshold:
            if current_interval is None:
                current_interval = [bin_edges[i], bin_edges[i]]
            else:
                current_interval[1] = bin_edges[i]
        else:
            if current_interval is not None:
                if largest_interval is None or (current_interval[1] - current_interval[0] > largest_interval[1] - largest_interval[0]):
                    largest_interval = current_interval
                current_interval = None

    if current_interval is not None:
        if largest_interval is None or (current_interval[1] - current_interval[0] > largest_interval[1] - largest_interval[0]):
            largest_interval = current_interval

    return largest_interval

largest_interval_c = largest_interval_below_threshold(c_hist,c_bin_edges,3)


# optimisation problem
'''largest_interval_c = [0,1]
interval = spo.minimize'''

print(f"Largest interval with values below 30: {largest_interval_c}")
print(f"True pore size: {largest_interval_c[1]-largest_interval_c[0]}")


# Plot all histograms in one plot
plt.figure()
plt.axvline(x=largest_interval_c[0], color='red', linestyle='--')
plt.axvline(x=largest_interval_c[1], color='red', linestyle='--')
plt.plot(c_bin_edges[:-1], c_hist, label='C', linestyle='-', marker='o', markersize=3)
plt.plot(dod_hex_bin_edges[:-1], dod_hex_hist, label='DOD & HEX', linestyle='-', marker='o', markersize=3)

plt.xlabel('X-axis')
plt.ylabel('Frequency')
plt.title('Histogram Line Plot along the X-axis with Y and Z constraints for Residue Atoms')
plt.grid(True)
plt.legend()


# Show the plot for 2 seconds
plt.show()
time.sleep(2)
plt.close()
