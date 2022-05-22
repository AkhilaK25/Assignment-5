import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

xk = np.arange(0,5)
pk = (1/256,3/64,27/128,27/64,81/256)
custm = stats.rv_discrete(name='custm', values=(xk, pk))

#plotting PMF
fig, ax = plt.subplots(1, 1)
ax.plot(xk, custm.pmf(xk), 'ro', ms=8, mec='b')
ax.vlines(xk, 0, custm.pmf(xk), colors='blue', linestyles='--', lw=2)

plt.title('PMF',fontsize = 18)
plt.xlabel('Value of X',fontsize = 14)
plt.ylabel('Probability',fontsize = 14)

plt.grid()
plt.show()