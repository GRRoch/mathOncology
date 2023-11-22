# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Define constants
alpha_p = 0.4621
alpha_q = 0.4621
a_0 = 10 * 10 ** (-9)  # 10-35 nanomoles
theta_1 = 0.8
omega_1 = 1.18  # Varies from 1.18-1.35
omega_2 = 0.25  # Varies from 0.25-1
delta_p = 0.3812
delta_q = 0.4765
K = 0.10


# Define theta_p:
def theta_p(a):
    return theta_1 + (1 - theta_1) * a / (a + K)


# Define omega_p:
def omega_p(a):
    return omega_1 + (1 - omega_1) * a / (a + K)

def omega_q(a):
    return omega_2 + (1 - omega_2) * a / (a + K)

# Define diffyq
def sysODE(y, t):
    p, q = y
    dydt = [alpha_p * theta_p(a_0) * p - delta_p*omega_p(a_0)*p, alpha_q*q-delta_q*omega_q(a_0)*q]
    return dydt

# initial data
t_0 = 0.0
t_end = 12.0
y0 = [1,0.1]

# Time range
t = np.linspace(t_0,t_end,1000)
Delta_t = (t_end-t_0)/1000

sol = odeint(sysODE, y0, t)

plt.plot(t, sol[:,0],'b', label='p(t)')
plt.plot(t, sol[:,1],'p', label='q(t)')
plt.legend(loc='best')
plt.xlabel('time')
plt.grid()
plt.show()