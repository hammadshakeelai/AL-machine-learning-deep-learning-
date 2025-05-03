import numpy as np
# a = np.array([1,2,3])
# print(a)#[1 2 3]
# print(a.ndim)#1     // .ndim  asks dimensions   // get Dimension
# print(a.shape)#(3,)      //tell row into columns    // get Type
# print(a.dtype)#int64     //tells data type and byte size // get Type
# ###
# a = np.array([[3.0,4.0,9.0],[4.0,2.0,1.0]])
# print(a)#[[3. 4. 9.] [4. 2. 1.]]
# print(a.ndim)#2     // .ndim  asks dimensions
# print(a.shape)#(2, 3)      //tell row into columns 
# print(a.dtype)#float64
# ###
# a = np.array([1,2,3])
# b = np.array([3,2,4])
# print(a*b)#[ 3  4 12]
# ###
# a = np.array([1,2,3], dtype='int16')
# #to force a data type onto an array
# print(a.itemsize)#tells byte size // for int16  itemsize=2 bytes
# ###
# print(a.size)# ask array size
# ###
# a = np.array([1,2,3])
# #    arr size * element size
# print(a.size * a.itemsize)#24  // to tell size of full array in byte
# # alternative
# print(a.nbytes)#24  // to tell size of full array in byte
# ###
# to access a specific element [r, c]
# a =np.array([[1,1,2,3,4,2,3],[1,2,3,4,8,3,2]])
# print(a[1,2])#3 //get element
# print(a[1,:]) # get row
# print(a[1,]) # get row
# print(a[1]) # get row
# print(a[:,1]) # get column
# # a[ start: end: step]
# print(a[0,2:4:2])#also negetive step works fine too
# a[1,6]=20
# print(a[1,6])
##
# a[:,2]=5#so whole column of 2 is now comprised of 5's
# print(a[:,2])
# a[:,2]=[1,2]
# print(a[:,2])
# ###
# b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# print(b[0,1,1])
# b = np.array([[[0,1],[2,3]],[[4,5],[6,7]]])
# print(b[0,1,1])
# b = np.array([[[0,1],[2,3]],[[4,5],[6,7]]])
# print(b)
# # [ [[0 1] [2 3]]

# #   [[4 5] [6 7]] ]
# print(b[0,1,:])#to get inner inner list// first row second list
# # [2 3]
# print(b[:,1,:])#to get full second column
# # [[2 3]
# #  [6 7]]
# b[:,1,:]=[[7,6],[3,2]]# to replace values of  
# a=np.zeros((2,2,2))
# print(a)
# a=np.ones((2,2,2),dtype='int8')
# print(a)
# a=np.full((2,2),99,dtype='float16')
# print(a)
# b=np.array([[1,2],[3,4]])#-----
# a=np.full(b.shape,4)
# print(a)
# a=np.full_like(b,4)
# print(a)
# a=np.random.rand(2,3)
# a=np.random.random_sample(b.shape)
# print(a)
# a=np.random.randint(2,7,size=(3,4))#7 is exclusive 2is inclusive
# print(a)
# a=np.identity(3)#math linear algebra identity
# print(a)
# arr=np.array([[1,2,3],[4,5,6]])
# r1 = np.repeat(arr,3,axis=0)#to rePEAT AN ARRAY
# r1 = np.repeat(arr,3,axis=1)#to repeat inside the array
# print(r1)
# a=np.ones((5,5))
# print(a)
# z=np.zeros((3,3))
# z[1,1]=9
# print(z)
# a[1:4,1:4]=z
# a[1:-1,1:-1]=z
# print(a)
# [[1. 1. 1. 1. 1.]
#  [1. 0. 0. 0. 1.]
#  [1. 0. 9. 0. 1.]
#  [1. 0. 0. 0. 1.]
#  [1. 1. 1. 1. 1.]]
###### copying array
# a=np.array([1,2,3])
# b=a.copy()
# b[0]=100
# print(a)
# print(b)
###
# a=np.array([1,2,3])
# a=a+2#plus with all elements
# print(a)
# a=a-2#minus with all elements
# print(a)
# a=a*2#multiple with all elements
# print(a)
# a=a/2#divide with all elements
# print(a)
# b=np.array([2,3,4])
# print(a+b)
# print(a*b)
# print(a/b)
# print(a**b)
# print(a**2)
# print(np.sin(a))
# print(np.cos(a))
# print(np.tan(a))
# print(np.tanh(a))
########linear algebra
# a=np.ones((2,3))
# a=np.empty((2,3))
# b=np.full((3,2),2)
# # print(a)
# # print(b)
# # # [[1. 1. 1.]
# # #  [1. 1. 1.]]
# # # [[2 2]
# # #  [2 2]
# # #  [2 2]]
# print(np.matmul(a,b))#multiply matrices
###
# c=np.identity(3)
# print(np.linalg.det(c))#find determinent
# #######
# #### INVERSE OF A MATRIX
# a=np.array([[1,2,3],[2,4,1],[6,9,0]])
# print(np.linalg.inv(a))
# ########
#STATISTICS
# stats = np.array([[1,2,3],[4,5,6]])
# print(np.min(stats))#find min
# print(np.min(stats,axis=1))#find min column
# print(np.min(stats,axis=0))#find min row
# print(np.max(stats))#find max
# print(np.max(stats,axis=1))#find max column
# print(np.max(stats,axis=0))#find max row
# before =np.array([[1,2,3],[4,5,6]])
# after = before.reshape((6,1))
# print(after)
# after = before.reshape((2,3,1))
# print(after)
# # [[[1]
# #   [2]
# #   [3]]

# #  [[4]
# #   [5]
# #   [6]]]
# #VEERTICALLY STACKING VECTORS
# v1 = np.array([1,2,3,4])
# v2 = np.array([5,6,7,8])
# print(np.vstack([v1,v2,v1+v2]))#extend
# #HORIZONTALLY STACKING VECTORS
# h1 = np.ones((1,2))
# h2 = np.full((3,2),3)
# print(np.hstack([v1,v2,v1+v2]))#extend
# ##CSV
# import csv
# with open("data.txt",'w') as w:
#   # w.write("1,2,3,4,5,6,7,8\n1,2,3,4,67,88,7,5\n2,3,5,3,4,86,466,4")
# a=np.genfromtxt('data.txt',delimiter=',')#-----------------------------------
# a=a.astype('int16')
# print(a)
# ##BOOLEAN MASKING AND ADVANCED INDEXING
# print(a>23)
# # [[False False False False False False False False]
# #  [False False False False  True  True False False]
# #  [False False False False False  True  True False]]
# print(a[a>23])#index with a condition
# # [ 67.  88.  86. 466.]
# b=np.array([1,2,3,4,5,6,7,8,9])
# print(b[[1,2,8]])#index with a list
# print(np.any(a>25,axis=0))
# print(np.any(a>25,axis=1))
# # [False False False False  True  True  True False]
# # [False  True  True]
# print((a>50)&(a<100) )
# # [[False False False False False False False False]
# #  [False False False False  True  True False False]
# #  [False False False False False  True False False]]
# print(~(a>50)&(a<100) ) # use ~ to reverse / not !
# [[ True  True  True  True  True  True  True  True]
#  [ True  True  True  True False False  True  True]
#  [ True  True  True  True  True False False  True]]
# a=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25],[26,27,28,29,30]])
# a[0:4,1:7]
# a[[0,1,2,3],[1,2,3,4]]
# a[[0,4,5],3:]
# a = np.eye(3,k=0)
# print(a)#prints identity
# a = np.eye(3,k=-1)
# print(a)#
# a = np.eye(3,k=1)
# print(a)#
# a = np.eye(3,k=2)
# print(a)#
# a[a==0]=2
# print(a)#
# a[a>1]=9
# print(a)#
# a[0]=3
# print(a)
# a[:2,2]=4
# print(a)
# a=np.sort(a)#to sort array
# print(a)
# a=np.sort(a,axis=0,kind="mergesort")#to sort array
# print(a)
# a=np.sort(a,axis=0,kind="heapsort")#to sort array
# print(a)
# b=a.view()
# np.arange(0, 10, 2)#[0, 2, 4, 6, 8]
# np.linspace(0, 1, 5)#[0.  , 0.25, 0.5 , 0.75, 1.  ]
# np.eye(3)#identity thats shiftable and and variable / not square forced
# ########
# np.random.rand(2, 3)
# # array([[0.37454012, 0.95071431, 0.73199394],
# #        [0.59865848, 0.15601864, 0.15599452]])
# np.random.randint(1, 10, size=(3, 3))
# # array([[8, 7, 3],
# #        [7, 2, 5],
# #        [4, 1, 7]])
# np.random.randn(3)#array([ 0.49671415, -0.1382643 ,  0.64768854])
# np.random.randint(1, 10, size=(3,3))
# # array([[7, 4, 8],
# #        [5, 7, 3],
# #        [7, 2, 5]])
# np.random.seed(42)
# print(np.random.rand(3))
# # [0.37454012 0.95071431 0.73199394]
#####
#####
# --- argmax and argmin ---
# arr = np.array([1, 7, 3, 9, 5])

# # Find index of maximum and minimum
# max_index = np.argmax(arr)
# min_index = np.argmin(arr)

# print("Original array:", arr)
# print("Index of maximum value:", max_index)  # 3
# print("Index of minimum value:", min_index)  # 0

# # --- expand_dims ---
# # Add a new axis
# arr_expanded_row = np.expand_dims(arr, axis=0)  # Shape becomes (1, 5)
# arr_expanded_col = np.expand_dims(arr, axis=1)  # Shape becomes (5, 1)

# print("\nExpanded along axis=0 (row):\n", arr_expanded_row)
# print("Shape:", arr_expanded_row.shape)

# print("\nExpanded along axis=1 (column):\n", arr_expanded_col)
# print("Shape:", arr_expanded_col.shape)

# # --- squeeze ---
# # Remove extra dimensions
# arr_with_extra_dims = np.array([[[1, 2, 3]]])  # Shape (1, 1, 3)
# arr_squeezed = np.squeeze(arr_with_extra_dims)  # Shape becomes (3,)

# print("\nArray with extra dimensions:\n", arr_with_extra_dims)
# print("Shape:", arr_with_extra_dims.shape)

# print("\nAfter squeeze:\n", arr_squeezed)
# print("Shape:", arr_squeezed.shape)
#####
# arr = np.array([1, 2, 3])

# # Expand along axis=0 → becomes a row
# arr_expanded_row = np.expand_dims(arr, axis=0)
# print("Expanded along axis=0 (row):\n", arr_expanded_row)
# print("Shape:", arr_expanded_row.shape)

# # # Expand along axis=1 → becomes a column
# # arr_expanded_col = np.expand_dims(arr, axis=1)
# # print("\nExpanded along axis=1 (column):\n", arr_expanded_col)
# # print("Shape:", arr_expanded_col.shape)
# # Expanded along axis=0 (row):
# # [[1 2 3]]
# # Shape: (1, 3)

# # Expanded along axis=1 (column):
# # [[1]
# #  [2]
# #  [3]]
# # Shape: (3, 1)
#######import numpy as np

# arr_with_extra_dims = np.array([[[1, 2, 3]]])  # shape (1,1,3)

# # Squeeze to remove dimensions of size 1
# arr_squeezed = np.squeeze(arr_with_extra_dims)

# print("Original array with extra dimensions:\n", arr_with_extra_dims)
# print("Shape:", arr_with_extra_dims.shape)

# print("\nAfter squeeze:\n", arr_squeezed)
# print("Shape:", arr_squeezed.shape)
# # Original array with extra dimensions:
# # [[[1 2 3]]]
# # Shape: (1, 1, 3)

# # After squeeze:
# # [1 2 3]
# # Shape: (3,)
########
# print("Shape:", arr_squeezed.shape)#
# b = np.append(a, [4, 5])
# b = np.delete(a, 1) # Delete element
# c = np.concatenate((a, b))#a.extend(b)
