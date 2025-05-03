import numpy as np
# n = np.random.randint(0,256,size=(5,5))
# np.save("my_arraynumpy.npy",n)
m = np.load("my_arraynumpy.npy")
# print(m)
# print(np.sum(m==n)==(5*5))
###############
print(m,m*2)