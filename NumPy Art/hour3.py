import numpy as np
n=np.array([1,2,3,4])
np.save("my_numpy_array.npy",n)
np.savez("my_numpy_array2.npz",n,n*2,n+2)

# n[:2]=0
# n*=2
# print(n)
#.npy for numpy file storage - single array
#.npz for numpy file storage - multiple array

# np.random.randint(0,255,size(512,512))

arr = np.load("my_numpy_array.npy")
print(arr)
arr2,arr3,arr4 = np.load("my_numpy_array2.npz")
print(arr2,arr3,arr4)