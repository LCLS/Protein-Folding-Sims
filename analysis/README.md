# MD Analysis Scripts
This directory contains scripts that walk down one level of a directory structure and perform a single action on each specified MD trajectory encountered.

## Example Usage
`cd path/to/directory/above/trajectory/files` (e.g., the directory containing all sim### files)

`python traj-checker.py`

`python rmsd.py input.pdb folded.pdb "hp24stab RMSD by ns" rmsd.png`

`python state.py --h1 2.25 --h2 3.0 --hboth 4.5`

`python rmsd_hist.py`

`python fpt.py`

## traj-checker.py
Load each trajectory in a directory structure and report any issues.

usage: `python traj-checker.py`

This will search each child directory of the cwd for a `trajectory.dcd` file and load the trajectory.

Output:

`filepath for trajectory`

`error message if error else continue`

## rmsd.py
Load each trajectory in a directory structure and calculate the RMSD (currently hard-coded for hp24stab both, h1, and h2)

usage: `python rmsd.py input.pdb folded.pdb <rmsd_plot_title> rmsd.png`

Records the RMSD to folded.pdb for each trajectory encountered, writes the RMSDs for the whole trajectory to file, and creates a a plot of those RMSDs in rmsd.png.

Output:

`rmsd_helix_both.csv`

`rmsd_helix_1.csv`

`rmsd_helix_2.csv`

`rmsd.png`

## state.py
Load each trajectory in a directory structure and calculate the state of each frame relative to an RMSD threshold (currently hard-coded for hp24stab both, h1, and h2).

usage `python state.py --h1 <threshold_helix_1> --h2 <threshold_helix_2> --hboth <threshold_both_helices>`

Creates an output file with a map `(rmsd < threshold ? 1 : 0)`, where 1 is folded and 0 is unfolded.

Output:

`states_helix_1.csv`

`states_helix_2.csv`

`states_helix_both.csv`

## rmsd\_hist.py
Create a histogram of all RMSDs for all trajectories in a directory structure (currently hard-coded for hp24stab both, h1, and h2).

usage: `python rmsd-hist.py`

Output: Three histograms: one for both helices, one for helix 1, and one for helix 2

## fpt.py
Plot the first passage time distribution of all trajectories in a directory structure (currently hard-coded for hp24stab both, h1, and h2).

Usage: `python fpt.py`

Output: Six histograms: two for both helices, two for helix 1, and two for helix 2

