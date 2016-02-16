import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

### values
eta_th_nominal = np.array([2.0, 1.6, 1.4, 1.2])
eta_th_error = 0.01
eta_eff_nominal = np.array([0.47, 0.29, 0.17, 0.08])
eta_eff_error = np.array([0.12, 0.04, 0.01, 0.01])
f = np.array([4.07, 4.88, 5.50, 5.95])
f_err = 0.02

### linear fit
def lin_reg(x, k, d):
    return k*x+d

# eta_th
popt_th, pcov_th = curve_fit(lin_reg, f, eta_th_nominal)
popt_th_err = np.sqrt(np.diag(pcov_th))

# eta_eff
popt_eff, pcov_eff = curve_fit(lin_reg, f, eta_eff_nominal)
popt_eff_err = np.sqrt(np.diag(pcov_eff))
print(popt_th, popt_th_err)
print(popt_eff, popt_eff_err)

# value string
values = r'$Linearer\ Fit1:$' + "\n" + r'$  k_1 = -0.42\pm0.02\ \mathrm{[\%/Hz]}$' + "\n" + r'$  d_1 = 3.68\pm0.13\ \mathrm{[\%]}$' + "\n\n" + r'$Linearer\ Fit2:$' + "\n" + r'$  k_2 = -0.21\pm0.01\ \mathrm{[\%/Hz]}$' + "\n" + r'$  d_2 = 1.31\pm0.03\ \mathrm{[\%]}$'

### plotting
fig = plt.figure(figsize=(12,9))
ax = fig.add_subplot(111)
ax.errorbar(f, eta_th_nominal, yerr=eta_th_error, xerr=f_err, fmt='k.', label='$\eta_{th}$')
ax.errorbar(f, eta_eff_nominal, yerr=eta_eff_error, xerr=f_err, fmt='r.', label='$\eta_{eff}$')
ax.plot(f, lin_reg(f, *popt_th), 'k--', label='$Linearer\ Fit1:\ k_1*f+d_1$')
ax.plot(f, lin_reg(f, *popt_eff), 'r--', label='$Linearer\ Fit2:\ k_2*f+d_2$')
ax.text(5.55, 1.52, values)
ax.set_title('$Plot\ 1:\ \eta_{th}\ und\ \eta_{eff}\ vs.\ Frequenz\ f $')
ax.set_xlabel('$Frequenz\ f\ \mathrm{[Hz]}$')
ax.set_ylabel('$\eta_{th}\ und\ \eta_{eff}\ \mathrm{[\%]}$')
ax.grid(axis='both')
ax.legend(loc=0)
plt.savefig('plot1.pdf', dpi=200, format='pdf')

