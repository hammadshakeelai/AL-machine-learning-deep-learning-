# variance === sigma ** 2 === ( sum of (every value - mean) ) ** 2 / len of ( values )
# standard deviation = sigma === (variance) ** 0.5
# np.var(data)
# dr taimur laal
# uniform distribution
# normal distribution / standard deviation - but std.var == 1,has values between -1 - 1,mean =0
# we do standardise data and reduce bigger value bigger power error
# at cost of data loss 
# np.std(data)
# std gives where the majority of values are
# unit deviation
# z-score
# co-efficient of variance (cv)- unit less || for camparing values of different scale
import numpy as np
from scipy import stats as st
# random_100=np.random.standard_normal(1000)*100

# print("mean=",np.mean(random_100))
# print("median=",np.median(random_100))
# print("mode=",st.mode(random_100).mode)
# print("standard deviation=",np.std(random_100))
# print("coeffient of variance=",np.std(random_100)/np.mean(random_100))
# #
# random_4=np.random.standard_normal(1000)

# print("mean=",np.mean(random_4))
# print("median=",np.median(random_4))
# print("mode=",st.mode(random_4).mode)
# print("standard deviation=",np.std(random_4))
# print("coeffient of variance=",np.std(random_4)/np.mean(random_4))
# cv 0 equal distance 
from scipy.stats import skew
from scipy.stats import skewtest
data=np.array([-2,-2,-1,-1,-1,0,10,40,100,110,120,500])
print(skew(data))
print(skewtest(data))
#  if a data is right skew / positive skewnes
# creates problem when standardised
# labeled skewed = class imbalance
# balance class = ratio same of labeled data
# imbalance creates biased disicions acoording to ratio of labeled data
# random over/under sampling