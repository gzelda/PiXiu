import numpy as np
import socialforce
import random
import logging

def test_opposing():
    initial_state = np.array([
        [0.0, 0.0, 1.0, 0.0, 0.0, 10.0],
        [-0.3, 10.0, -1.0, 0.0, -0.3, 0.0],
    ])
    s = socialforce.Simulator(initial_state)
    states = np.stack([s.step().state.copy() for _ in range(21)])

    # visualize
    print('')
    with socialforce.show.canvas('docs/opposing.png') as ax:
        ax.set_xlabel('x [m]')
        ax.set_ylabel('y [m]')

        for ped in range(2):
            x = states[:, ped, 0]
            y = states[:, ped, 1]
            ax.plot(x, y, '-o', label='ped {}'.format(ped), markersize=2.5)
        ax.legend()

if __name__ == '__main__':
    test_opposing()