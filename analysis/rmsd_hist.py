import numpy as np

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import os
import os.path

if __name__ == "__main__":
    both = None # np.array([])
    h1 = None # np.array([])
    h2 = None # np.array([])
    
    for path in os.listdir():
        fpath = os.path.join(path, "rmsd_helix_both.csv")
        if os.path.isfile(fpath):
            rmsd = np.loadtxt(fpath)
            if both is not None:
                np.concatenate((both, rmsd))
            else:
                both = rmsd
        
        fpath = os.path.join(path, "rmsd_helix_1.csv")
        if os.path.isfile(fpath):
            rmsd = np.loadtxt(fpath)
            if h1 is not None:
                np.concatenate((h1, rmsd))
            else:
                h1 = rmsd
        
        fpath = os.path.join(path, "rmsd_helix_2.csv")
        if os.path.isfile(fpath):
            rmsd = np.loadtxt(fpath)
            if h2 is not None:
                np.concatenate((h2, rmsd))
            else:
                h2 = rmsd

    plt.hist(both, bins=50)
    plt.title("hp24stab Both Helices RMSD Distribution")
    plt.xlabel("RMSD $\AA$")
    plt.ylabel("Count")

    plt.savefig("rmsd_distro_helix_both.png", format="png")

    plt.clf()

    plt.hist(h1, bins=50)
    plt.title("hp24stab Helix 1 RMSD Distribution")
    plt.xlabel("RMSD $\AA$")
    plt.ylabel("Count")

    plt.savefig("rmsd_distro_helix_1.png", format="png")

    plt.clf()

    plt.hist(h2, bins=50)
    plt.title("hp24stab Helix 2 RMSD Distribution")
    plt.xlabel("RMSD $\AA$")
    plt.ylabel("Count")

    plt.savefig("rmsd_distro_helix_2.png", format="png")

    plt.clf()
