import numpy as np
import matplotlib.pyplot as plt

def data_and_curve():
    n = np.array([20, 15, 39, 71, 65, 54, 87, 37, 86, 92, 93, 106, 58, 86, 26, 73, 62, 46, 32,
                  21, 15, 22, 18])
    sd = np.array([226, 173, 362, 381, 709, 1054, 1164, 2591, 2567, 3176, 3278, 3371,
                   3598, 3521, 3737, 3704, 3686, 5206, 5326, 4805, 4463, 6279, 4455])
    mass = np.array([400, 330, 470, 491, 852, 1440, 1251, 4638, 3780, 4377, 5916,
                     5940, 8762, 6927, 13130, 11600, 9735, 15120, 13585, 14170, 16550,
                     17970, 19865])
    time = np.arange(4, 27, 1)
    E = sd / np.sqrt(n)
    G0 = 0.789
    alpha = 0.107
    N0 = 18.4
    t = np.arange(4, 30.1, 0.1)
    N_t = N0 * np.exp(G0 / alpha * (1 - np.exp(-alpha * t)))

    # Figure 1
    plt.figure(1)
    plt.rcParams['axes.labelsize'] = 18
    plt.plot(t, N_t, 'k', label='Model')
    plt.errorbar(time, mass, E, fmt='ko', label='Experimental Data')
    plt.title('(A)')
    plt.ylabel('Tumor mass (mg)')
    plt.xlabel('Time (days)')
    plt.ylim([0, 2.5e4])
    plt.xlim([0, 30])
    plt.legend()
    plt.show()

    # Figure 2
    plt.figure(2)
    plt.rcParams['axes.labelsize'] = 18
    plt.semilogy(time, mass, 'ko', label='Experimental Data')
    plt.semilogy(t, N_t, 'k', label='Model')
    plt.title('(B)')
    plt.ylabel('log tumor mass')
    plt.xlabel('Time (days)')
    plt.legend()
    plt.show()

# Call the function
data_and_curve()
