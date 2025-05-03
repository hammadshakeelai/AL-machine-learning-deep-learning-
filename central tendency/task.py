import numpy as np
from scipy.stats import mode
# from scipy import stats as st
a=np.load("prices.npy")
print("mean=",np.mean(a))
print("median=",np.median(a))
# print(mode(a))#most frequent value /frequency-data best for repitative data 
# mode is the most frequent value

m=mode(a)
print("mode=",m.mode)
# outlier
print("outlier=",a[-1])
# remove outlier
b=a.copy()
b[b>200]=160
print(b)
# campare how outlier distorts mean
print("m1=",np.mean(b),"\nm2=",np.mean(a))
print("difference=",round(abs(np.mean(b)-np.mean(a)),2))
print("difference=",round(abs(np.mean(b)-np.mean(a))/np.mean(b)*100,2)," %")
# which answer is better for central tendency measure for this case mean median ? why ?

print("median is better as its anwser was closer to actual answer/better central tendency measure accuracy")
# outlier in data ruins mean// mean is sensitive to outliers
# else mean is best
# outlier forces us to use median
# mean is best for symmetrical data 

# mean~median
# than data is symmetrical
# else is skewed to one side
# mostly irregular data