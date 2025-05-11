import numpy as np
data=np.load("prices.npy")

Q1=np.percentile(data,25)
Q2=np.percentile(data,55)
Q3=np.percentile(data,75)

print("Q1",Q1)
print("Q2",Q2)
print("Q3",Q3)

IQR=Q3-Q1
print("IQR",IQR)

L=Q1-1.5*IQR
U=Q3+1.5*IQR
print("lower bound",L)
print("upper bound",U)

if len(data[data>U]):
    print(data[data>U])
if len(data[data<L]):
    print(data[data<L])
    
# print(data[])/
# if 