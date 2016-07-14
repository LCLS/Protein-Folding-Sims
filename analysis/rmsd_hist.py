import numpy as np

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import os
import os.path

if __name__ == "__main__":
    rmsds = None
    for path in os.listdir():
        fpath = os.path.join(path, "rmsd_helix_both.csv")
        if os.path.isfile(fpath):
            rmsd = np.loadtxt(fpath)
            
            if rmsds is not None:
                np.concatenate((rmsds, rmsd))
            else:
                rmsds = rmsd

    plt.hist(rmsds, bins=50)
    plt.title("hp24stab Both Helices RMSD Distribution")
    plt.xlabel("RMSD $\AA$")
    plt.ylabel("Count")

    plt.savefig("rmsd_distro_helix_both.png", format="png")
