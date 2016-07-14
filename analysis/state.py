import sys
import numpy as np

import os
import os.path

import argparse

def parse_args(args=None):
    parser = argparse.ArgumentParser()

    parser.add_argument("--h1",
            default=None,
            type=float,
            help='RMSD threshold to helix 1'
            )
    parser.add_argument("--h2",
            default=None,
            type=float,
            help='RMSD threshold to helix 2'
            )

    parser.add_argument("--hboth",
            default=None,
            type=float,
            help='RMSD threshold to both helices'
            )

    return parser.parse_args(args)

if __name__ == "__main__":
    args = parse_args()

    for path in os.listdir():
        fname = os.path.join(path, 'rmsd_helix_1.csv')
        if os.path.isdir(path) and os.path.isfile(fname) and args.h1 is not None:
            rmsd = np.loadtxt(fname)
            state = list(map(lambda x: 1 if x < args.h1 else 0, rmsd))
            np.savetxt(os.path.join(path, 'state_helix_1.csv'), np.array(state).astype(int), fmt="%d")
        
        fname = os.path.join(path, 'rmsd_helix_2.csv')
        if os.path.isdir(path) and os.path.isfile(fname) and args.h2 is not None:
            rmsd = np.loadtxt(fname)
            state = list(map(lambda x: 1 if x < args.h2 else 0, rmsd))
            np.savetxt(os.path.join(path, 'state_helix_2.csv'), np.array(state).astype(int), fmt="%d")
        
        fname = os.path.join(path, 'rmsd_helix_both.csv')
        if os.path.isdir(path) and os.path.isfile(fname) and args.hboth is not None:
            rmsd = np.loadtxt(fname)
            state = list(map(lambda x: 1 if x < args.hboth else 0, rmsd))
            np.savetxt(os.path.join(path, 'state_helix_both.csv'), np.array(state).astype(int), fmt="%d")
