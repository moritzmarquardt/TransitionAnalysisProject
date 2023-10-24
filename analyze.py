import numpy as np
import matplotlib.pyplot as plt
import TransitionanalysisForMembranes.funcs as tfm
import TransitionanalysisForMembranes.plot as tfmp
import time

start = time.time()
# root_path = 'C:/Users/marqu/projects/TFM/tfm-analysis/'
# paths for wsl vs code enviroment (when you open the foolder/workspace in wsl mode)
# postfix = '_nojump'
# postfix als dateiendung:
# _all sind alle trajs, _nojump sind die trajs ohne pbc jumps, '' ist random trajs
# print(postfix)

####################################
#           DODECANE(cubic)        #
####################################
x = np.loadtxt("./data/cubic/x_dod_c2.xvg", comments="@", unpack=True)[1:, :]
y = np.loadtxt("./data/cubic/y_dod_c2.xvg", comments="@", unpack=True)[1:, :]
z = np.loadtxt("./data/cubic/z_dod_c2.xvg", comments="@", unpack=True)[1:, :]
x_nojump = np.loadtxt("./data/cubic/x_dod_c2_nojump.xvg", comments="@", unpack=True)[
    1:, :
]
y_nojump = np.loadtxt("./data/cubic/y_dod_c2_nojump.xvg", comments="@", unpack=True)[
    1:, :
]
z_nojump = np.loadtxt("./data/cubic/z_dod_c2_nojump.xvg", comments="@", unpack=True)[
    1:, :
]
timeline = np.loadtxt("./data/cubic/x_dod_c2.xvg", comments="@", unpack=True)[0, :]


####################################
#            HEXANE(cubic)         #
####################################
# x = np.loadtxt("./data/cubic/x_hex_c1.xvg", comments="@", unpack=True)[1:, :]
# y = np.loadtxt("./data/cubic/y_hex_c1.xvg", comments="@", unpack=True)[1:, :]
# z = np.loadtxt("./data/cubic/z_hex_c1.xvg", comments="@", unpack=True)[1:, :]
# x_nojump = np.loadtxt("./data/cubic/x_hex_c1_nojump.xvg", comments="@", unpack=True)[1:, :]
# y_nojump = np.loadtxt("./data/cubic/y_hex_c1_nojump.xvg", comments="@", unpack=True)[1:, :]
# z_nojump = np.loadtxt("./data/cubic/z_hex_c1_nojump.xvg", comments="@", unpack=True)[1:, :]
# timeline = np.loadtxt("./data/cubic/x_hex_c1.xvg", comments="@", unpack=True)[0, :]

# ####################################
# #           90DODECANE(cubic)      #
# ####################################
# x = np.loadtxt("./data/90deg/90_dei_c2_x.xvg", comments="@", unpack=True)[1:, :]
# y = np.loadtxt("./data/90deg/90_dei_c2_y.xvg", comments="@", unpack=True)[1:, :]
# z = np.loadtxt("./data/90deg/90_dei_c2_z.xvg", comments="@", unpack=True)[1:, :]
# timeline = np.loadtxt("./data/90deg/90_dei_c2_x.xvg", comments="@", unpack=True)[0, :]

####################################
#            90HEXANE(cubic)       #
####################################
# x = np.loadtxt("./data/90deg/90_hex_c1_x.xvg", comments="@", unpack=True)[1:, :]
# y = np.loadtxt("./data/90deg/90_hex_c1_y.xvg", comments="@", unpack=True)[1:, :]
# z = np.loadtxt("./data/90deg/90_hex_c1_z.xvg", comments="@", unpack=True)[1:, :]
# timeline = np.loadtxt("./data/90deg/90_hex_c1_x.xvg", comments="@", unpack=True)[0, :]


print("number of trajs: " + str(np.size(x[:, 0])))
print("number of timesteps: " + str(np.size(x[0, :])))

# GET PASSAGES AND TRANSITION DURATION
zbounds = [20.5, 38.5]  # von sofia
ffs, ffe, indizes = tfm.dur_dist_improved(z, zbounds)
print("passages: " + str(ffs.size))

# Durchgangszeiten verteilung plotten
plt.figure("Verteilung der Durchgangszeiten")
plt.title("Verteilung der Durchgangszeiten")
tfmp.plot_dist(ffe - ffs, number_of_bins=30, max_range=1000)
plt.xlabel("Durchgangszeiten")
plt.ylabel("relative Häufigkeit")


x_passages_nojump = x_nojump[indizes]
y_passages_nojump = y_nojump[indizes]
z_passages_nojump = z_nojump[indizes]

# GET HORIZONTAL DISTANCES
distances = tfm.calc_hor_dist(x_passages_nojump, y_passages_nojump, ffs, ffe)
print("Gesamte horizontale Distanz: " + str(np.sum(distances)))

# Verteilung der horizontal zurückgelegten Strecke
plt.figure("Verteilung der horizontal zurückgelegten Strecke")
tfmp.plot_dist(distances, number_of_bins=30, max_range=800)
plt.xlabel("horizontal zurück gelegte Strecke")
plt.ylabel("relative Häufigkeit")


x_passages = x[indizes]
y_passages = y[indizes]
z_passages = z[indizes]

# GET DIRECT TRANSITIONS
direct = tfm.path_cat(x_passages, y_passages, ffs, ffe)
print("Anzahl direkte Durchgänge: " + str(np.size(direct)))


print("elapsed time: " + str(time.time() - start))
plt.show()
