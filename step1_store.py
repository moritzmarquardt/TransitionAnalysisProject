import numpy as np
import os
'''
STEP 1:
- After receiving files, store them as numpy arrays for better further handling and processing
- The files (that end with xvg - so trajectory files) are stored into the same folder with the same name but with the ending .npy
'''

print("store .xvg files as .npy")
path = 'sim_data/20231120/'
files = os.listdir(path)

i = 0
for f in files:
    if f.endswith(".xvg"):
        print("store trajectory file nr. " + str(i + 1))
        file = np.loadtxt(path + f, comments="@", unpack=True)
        trajectories = file[1:, :]  # because first column is the timeline
        print("number of trajectories: " + str(trajectories[:, 0].size))
        print("number of timesteps: " + str(trajectories[0, :].size))
        np.save(
            path + f.split('.')[0] + ".npy",
            trajectories,
        )
        if i == 0: # only create timeline once
            print("store timeline")
            timeline = file[0, :]
            np.save(
                path + "timeline.npy",
                timeline,
            )
        i = i + 1
