import mdtraj
import numpy as np
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import os
import os.path

if __name__ == "__main__":
    topfile = sys.argv[1]
    reffile = sys.argv[2]
    title = sys.argv[3]
    outfile = sys.argv[4]

    for path in os.listdir():
        if os.path.isdir(path) and os.path.isfile(os.path.join(path, 'trajectory.dcd')):
            traj = mdtraj.load(os.path.join(path,'trajectory.dcd'), top=topfile)
            ref = mdtraj.load(reffile)

            atoms1 = traj.topology.select("backbone and index 32 to 120")
            atoms2 = traj.topology.select("backbone and index 174 to 338")
            atoms3 = traj.topology.select("backbone and index 32 to 338") # np.concatenate((atoms1, atoms2))

            rmsd_1 = (mdtraj.rmsd(traj, ref, atom_indices=atoms1, frame=0, precentered=False)) * 10
            np.savetxt("rmsd_helix_1.csv", rmsd_1)

            rmsd_2 = mdtraj.rmsd(traj, ref, atom_indices=atoms2) * 10
            np.savetxt("rmsd_helix_2.csv", rmsd_2)

            rmsd_both = mdtraj.rmsd(traj, ref, atom_indices=atoms3) * 10
            np.savetxt("rmsd_helix_both.csv", rmsd_both)

            x = np.array([i/10 for i in range(0,len(rmsd_1))])

            p_both = plt.plot(x, rmsd_both, label="Both Helices and Connecting Region")
            p_1 = plt.plot(x, rmsd_1, label="Helix 1")
            p_2 = plt.plot(x, rmsd_2, label="Helix 2")

            plt.title(title)
            plt.xlabel("ns")
            plt.ylabel("RMSD ($\AA$)")
            plt.legend(handles=[p_both, p_1, p_2], labels=["Both Helices and Connecting Region", "Helix 1", "Helix 2"])
            plt.savefig(outfile, format="png")

            plt.clf()

