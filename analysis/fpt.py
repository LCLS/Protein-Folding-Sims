import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import os, os.path

def get_fpt(states):
    initial = states[0]
    
    forward = len(states) / 10
    backward = len(states) / 10
    
    starting = len(states) / 10

    for i in range(0, len(states)):
        if states[i] != initial:
            forward = i / 10
            starting = i
            break

    for i in range(int(starting), len(states)):
        if states[i] == initial:
            backward = i / 10
            break

    return (forward, backward)

def analyze_helix_states(base):
    forward = []
    backward = []
    
    states = np.loadtxt(os.path.join(base, "state_helix_1.csv"))
    h = get_fpt(states)
    forward.append(h[0])
    backward.append(h[1])


    states = np.loadtxt(os.path.join(base, "state_helix_2.csv"))
    h = get_fpt(states)
    forward.append(h[0])
    backward.append(h[1])

    states = np.loadtxt(os.path.join(base, "state_helix_both.csv"))
    h = get_fpt(states)
    forward.append(h[0])
    backward.append(h[1])

    return (forward, backward)

def get_all_fpts(base):
    forward = []
    backward = []
    for path in os.listdir(os.path.abspath(base)):
        if os.path.isdir(path) and os.path.isfile(os.path.join(path, "state_helix_1.csv")):
            result = analyze_helix_states(path)
            forward.append(result[0])
            backward.append(result[1])

    return (forward, backward)

def plot_hist(data, title, outfile):
    plt.hist(data, bins=50, range=(0,1000))
    plt.title(title)
    plt.xlabel("First Passage Time (ns)")
    plt.ylabel("Count")
    plt.savefig(outfile, format="png")
    plt.clf()

def get_and_plot():
    result = get_all_fpts(os.getcwd())

    forward = np.array(result[0])
    np.savetxt("forward_fpts.csv", forward)
    backward = np.array(result[1])
    np.savetxt("backward_fpts.csv", backward)
    
    print(forward)

    plot_hist(forward[:,0], "Helix 1 Forward First Passage Times", "fwd_fpt_helix_1_hist.png")
    plot_hist(forward[:,1], "Helix 2 Forward First Passage Times", "fwd_fpt_helix_2_hist.png")
    plot_hist(forward[:,2], "Both Helices Forward First Passage Times", "fwd_fpt_helix_both_hist.png")


    plot_hist(backward[:,0], "Helix 1 Backward First Passage Times", "bwd_fpt_helix_1_hist.png")
    plot_hist(backward[:,1], "Helix 2 Backward First Passage Times", "bwd_fpt_helix_2_hist.png")
    plot_hist(backward[:,2], "Both Helices Backward First Passage Times", "bwd_fpt_helix_both_hist.png")


if __name__ == "__main__":
    get_and_plot()
