!conda list | grep numpy
!conda --version
!python -m pip list | grep numpy
!pip install numpy
import numpy as np
a = 0
p_list = [1.5, 2, 3, "4"]
array = np.array(p_list)
print(array)
type(array)
p_list = [[[1,2],
          [12,2],
          [13,1],
          [4, 1],
          [9, 3],
          [67,1]]]
array = np.array(p_list)
array.shape
ones = np.ones((32, 3, 3), dtype="float32")
ones.shape
zeroes = np.zeros([2,2], dtype='int8')
zeroes
white_img = np.full((10,10, 1), 56)
np.eye(5, 5)
list(range(0, 10, 3))

numbers = np.arange(10, 20, 1)
numbers
even_indexes = np.arange(0, 10, 2)
print(even_indexes)
numbers[even_indexes]
np.linspace(10, 15, 20)
np.random.rand(3, 3, 3, 1)
random_ints = np.random.randint(5, 128, size=(5,6), dtype='int8')
random_ints.dtype
random_ = np.random.randn(5, 3)
random_.mean()
random_.std()
random_.dtype

np.random.randint(0, 10, size=5)
np.random.seed(100)
np.random.randint(0, 10, size=5)
np.random.randint(0, 10, size=5)
np.random.seed(100)
np.random.randint(0, 10, size=5)
np.random.randint(0, 10, size=5)
a = np.array([1, 2, 3])  
a.shape
a = np.array([1, 2, 3])  
b = 5                   
print(a * b)  # Output: [6 7 8]
a = np.array([[1, 2], [2, 2], [3, 2]])   # Shape: (3, 1)
a.shape
b = np.array([ 20, 30])  	# Shape: (3,)
b.shape
# Broadcast shapes: (3, 1) + (1, 3) => (3, 3)
result = a + b
result.shape
result
result
a * b
a
a = np.arange(0, 10, 1)
print(a)
a[1:5: 2]
a[::-1]
a = np.random.randint(-10, 10, size=(5,5))
a
a[1:4,1:4] = 5
a
a % 2 == 0
a[a > 0]
a[a < 0] = 0
a
a = np.ones((6,6))
a
a.reshape((12, 3))
a.reshape((2, 3, 2, 3))
a.max()
a.min()
a.argmin()
a.argmax()
a.shape
a.dtype
a.size
a.ndim
a.shape
np.expand_dims(a, axis=-1).shape
images = np.empty((32, 512, 512))
images.shape
new_images = np.expand_dims(images, axis=-1)
new_images.shape
new_images.squeeze().shape
