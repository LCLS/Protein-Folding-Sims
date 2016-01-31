from simtk.openmm.app import *
from simtk.openmm import *
from simtk.unit import *
from sys import stdout
outfreq = 1e5
simlength = 1e9
pdb = PDBFile('folded.pdb')
forcefield = ForceField('amber99sb.xml', 'amber99_obc.xml')
system = forcefield.createSystem(pdb.topology, nonbondedMethod=NoCutoff)
integrator = LangevinIntegrator(300*kelvin, 91/picosecond, 1*femtosecond)
platform=Platform.getPlatformByName('CUDA')
simulation = Simulation(pdb.topology, system, integrator,platform)
simulation.context.setPositions(pdb.positions)
simulation.reporters.append(PDBReporter('traj1.pdb',outfreq))
simulation.reporters.append(StateDataReporter('data.csv', outfreq0, step=True, potentialEnergy=True, totalEnergy=True, temperature=True))
simulation.step(1e9)

