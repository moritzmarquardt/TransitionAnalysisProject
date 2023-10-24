import numpy as np
import os
'''
STEP 1:
- After receiving files, store them as numpy arrays for better further handling and processing
- The files (that end with xvg - so trajectory files) are stored into the same folder with the same name but with the ending .npy
'''

print("store .xvg files as .npy")
path = 'sim_data/20231017/'
files = os.listdir(path)


for f in files:
    if f.endswith(".xvg"):
        file = np.loadtxt(path + f, comments="@", unpack=True)
        trajectories = file[1:, :]  # because first column is the timeline
        number_of_traj = trajectories[:, 0].size
        print("number of trajectories: " + str(number_of_traj))
        np.save(
            path + f.split('.')[0] + ".npy",
            trajectories,
        )
        if not os.path.isfile(path + "timeline.npy"): # only create timeline once
            timeline = file[0, :]
            np.save(
                path + "timeline.npy",
                timeline,
            )
        else:
            print("timeline.npy already exists")
