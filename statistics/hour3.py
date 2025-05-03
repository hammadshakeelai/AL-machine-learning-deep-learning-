import numpy as np
# data=np.array([10,20,30,40,50,60,70,80,90,100])
# data*=3
# p25=np.percentile(data,25)#q1
# p50=np.percentile(data,50)#median
# p75=np.percentile(data,75)#q3
# print(p25)
# print(p50)
# print(p75)

# p25=np.percentile(data,3)#q1
# p50=np.percentile(data,33)#median
# p75=np.percentile(data,87)#q3
# print(p25)
# print(p50,type(p50))
# print(p75,type(p75))

# data=np.dot([10,20,30,40,50,60,70,80,90,100],3)
# print(data)
# quartile / into 4 pieces
# percentile / into 100 pieces

# axis ?
# linear?
# 25% values are less than Q1
# 50% values are less than Q2
# 75% values are less than Q3

# inter-quartile range __ IQR =Q3-Q1 #measure the middle 50% spread to detect outliers
# tukey's EDA brought fouth the 1.5
# lower_bound = Q1 - 1.5 * IQR
# upper_bound = Q3 - 1.5 * IQR

# high probably outlier are out of this range
 
