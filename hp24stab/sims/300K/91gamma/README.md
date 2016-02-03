File input.pdb is an unfolded hp24stab, and it was produced as follows:

1) run_oops 4cz4 > 4cz4.pdt
was run to generate 1 unfolded structure (only backbone, no side chains)
run_oops is executable of RCG (random-coil-generator) out of U. of Chicago:
http://unfolded.uchicago.edu/dloads.html
http://godzilla.uchicago.edu/cgi-bin/unfolded.cgi

2) scwrl4 -i 4cz4.pdt -h > 4cz4-scwrl4-noh.pdb
was run to generate side chains but ignoring hydrogens
http://dunbrack.fccc.edu/scwrl4/

3) pdbfixer 4cz4-scwrl4-noh.pdb > 4cz4-sc-fixed.pdb
was run to fix the pdb
https://github.com/pandegroup/pdbfixer

4) python minimizePDB.py 4cz4-sc-fixed.pdb > output.pdb
minimized the PDB using OpenMM 6.3.1 and produced output.pdb
with amber99sb.xml and amber99_obc.xml

5) python simulateUnfoldedPDB.py input.pdb
input.pdb is the output.pdb from step #4


File folded.pdb is 4cz4.pdb without the ACE and NME HETATMs 
run by pdbfixer

simulateFoldedPdb.py shows how to run a simulation of folded.pdb

# TPR Creation
1) pdb2gmx -ignh -f input.pdb -o villin.gro -p villin.top -water none -ff amber99sb

2) editconf -f villin.gro -o villin_box.gro -c -d 1.0 -bt cubic

3) grompp -f md.mdp -c villin_box.gro -p villin.top -o villin.tpr
