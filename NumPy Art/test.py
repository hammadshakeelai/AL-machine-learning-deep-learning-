import numpy as np

# Step 1: Create a 3D array of shape (2, 3, 4) with random integers between 0 and 9
arr = np.random.randint(0, 10, size=(2, 3, 4))
print("Original array:\n", arr)

# Step 2: Find the mean along axis 1
mean_axis1 = np.mean(arr, axis=1)
print("\nMean along axis 1:\n", mean_axis1)

# Step 3: Multiply the array by 3
arr_multiplied = arr * 3
print("\nArray multiplied by 3:\n", arr_multiplied)

# Step 4: Add a scalar (say +5) and subtract another random array of the same shape
scalar = 5
another_arr = np.random.randint(0, 5, size=(2, 3, 4))  # another random array
arr_modified = arr_multiplied + scalar - another_arr
print("\nArray after adding scalar and subtracting another array:\n", arr_modified)

# Step 5: Transpose to shape (3, 2, 4)
arr_transposed = np.transpose(arr_modified, (1, 0, 2))
print("\nTransposed array (shape (3, 2, 4)):\n", arr_transposed)

# Step 6: Sum along axis 0
arr_sum_axis0 = np.sum(arr_transposed, axis=0)
print("\nSum along axis 0:\n", arr_sum_axis0)
