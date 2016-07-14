import sys
import numpy as np

import os
import os.path

if __name__ == "__main__":
    for path in os.listdir():
        fpath = os.path.join(path, "rmsd_helix_2.csv")
        if os.path.isfile(fpath):
            rmsd = np.loadtxt(fpath)
            threshold = 2.5

            state = list(map(lambda x: 1 if x < threshold else 0, rmsd))
            #print(state[547]) 
            np.savetxt(os.path.join(path, "state_helix_2.csv"), np.array(state).astype(int), fmt="%d")
