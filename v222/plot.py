import numpy as np
import matplotlib.pyplot as plt

### values
eta_th_nominal = np.array([2.0, 1.6, 1.4, 1.2])
eta_th_error = 0.01
eta_eff_nominal = np.array([0.47, 0.29, 0.17, 0.08])
eta_eff_error = np.array([0.12, 0.04, 0.01, 0.01])
f = np.array([4.07, 4.88, 5.50, 5.95])
f_err = 0.02

### plotting
fig = plt.figure(figsize=(12,9))
ax = fig.add_subplot(111)
ax.errorbar(f, eta_th_nominal, yerr=eta_th_error, xerr=f_err, fmt='k.', label='$\eta_{th}$')
ax.errorbar(f, eta_eff_nominal, yerr=eta_eff_error, xerr=f_err, fmt='r.', label='$\eta_{eff}$')
ax.set_title('$Plot\ 1:\ \eta_{th}\ und\ \eta_{eff}\ vs.\ Frequenz\ f $')
ax.set_xlabel('$Frequenz\ f\ \mathrm{[Hz]}$')
ax.set_ylabel('$\eta_{th}\ und\ \eta_{eff}\ \mathrm{[\%]}$')
ax.grid(axis='both')
ax.legend(loc=0)
plt.savefig('plot1.pdf', dpi=200, format='pdf')
