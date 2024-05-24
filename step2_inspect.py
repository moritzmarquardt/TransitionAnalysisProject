import numpy as np
import matplotlib.pyplot as plt
import MembraneAnalysisToolbox.funcs as tfm
import MembraneAnalysisToolbox.plot as tfmp
'''
STEP 2:
- inspect the received data
- Choose boundaries,
- check for timeline
- plot sample trajectories for plausibility analysis
'''

path = '/bigpool/users/ac130484/project/finished_sim/hex/poresize/2nm_NVT/simulation_3/analysis/'
print(path)
prefix = "dod_traj_"
x = np.load(path + prefix + "x.npy")
y = np.load(path + prefix + "y.npy")
z = np.load(path + prefix + "z.npy")
timeline = np.load(path + "timeline.npy")
print("step size in ps: " + str(timeline[2]-timeline[1]))
print("number of timesteps: " + str(np.size(x[0, :])))
print("sim duration (in ns if step size is in ps): " + str(np.size(x[0, :])*(timeline[2]-timeline[1])/1000))

# print(timeline[:100],timeline[-100:-1])
print("max z-value: " + str(np.max(z)) + "; min z-value: " + str(np.min(z)))
print("number of trajs: " + str(np.size(x[:, 0])))

plt.figure("x_dist")
plt.hist(x.flatten(), bins=100, density=True)
plt.xlabel("x")
plt.ylabel("Frequency")
plt.title("Histogram of x")
plt.savefig(path + prefix + 'x_dist.png')

plt.figure("y_dist")
plt.hist(y.flatten(), bins=100, density=True)
plt.xlabel("y")
plt.ylabel("Frequency")
plt.title("Histogram of y")
plt.savefig(path + prefix + 'y_dist.png')

plt.figure("z_dist")
plt.hist(z.flatten(), bins=100, density=True)
plt.xlabel("z")
plt.ylabel("Frequency")
plt.title("Histogram of z")
plt.savefig(path + prefix + 'z_dist.png')

rand_trajs = np.random.randint(0,str(np.size(x[:, 0])),size=(2))

plt.figure("z_rand_trajs")
for i in rand_trajs:
    tfmp.plot_1dtraj(z[i, :])
plt.savefig(path + prefix + 'z_rand_trajs.png')

plt.figure("x_rand_trajs")
for i in rand_trajs:
    tfmp.plot_1dtraj(x[i, :])
plt.savefig(path + prefix + 'x_rand_trajs.png')

plt.figure("y_rand_trajs")
for i in rand_trajs:
    tfmp.plot_1dtraj(y[i, :])
plt.savefig(path + prefix + 'y_rand_trajs.png')

plt.show()