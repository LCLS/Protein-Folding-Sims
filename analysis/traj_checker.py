import os, os.path
import mdtraj

if  __name__ == "__main__":
    for path in os.listdir('.'):
        if os.path.isdir(path) and os.path.isfile(os.path.join(path, 'trajectory.dcd')):
            print(path)
            traj = mdtraj.load(os.path.join(path, 'trajectory.dcd'), top='input.pdb')
