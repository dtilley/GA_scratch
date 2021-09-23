from scipy.stats import lognorm
import matplotlib.pyplot as plt

rand_s_1 = lognorm.rvs(s=1.0, size=1000)
rand_s_half = lognorm.rvs(s=0.5, size=1000)
rand_s_quarter = lognorm.rvs(s=0.25, size=1000)

plt.hist(rand_s_1,label='s=1')
plt.hist(rand_s_half,label='s=0.5')
plt.hist(rand_s_quarter,label='s=0.25')
plt.legend()
plt.show()
