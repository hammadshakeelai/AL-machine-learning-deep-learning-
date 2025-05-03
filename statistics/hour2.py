import numpy as np
from scipy.stats import skew
from scipy.stats import skewtest
from scipy.stats import zscore
from scipy import stats as st
data = np.load("prices.npy")
print(data)
# data[-1]=160
print("variance=",np.var(data))
print("standard deviation=",np.std(data))
print("mean=",np.mean(data))
# Z=(X-u)/o~
print("zscore",zscore(data))
print((198.232*-.36)+223)#=mean+(std*zscore)
print((198.232*-.31)+223)#=mean+(std*zscore)
print((198.232*3.16)+223)#=mean+(std*zscore)
# if zscore that value is near to mean
# more the zscore the more outlier it is 

# z*o~+u=X
########
# percentile
print(250*.05)