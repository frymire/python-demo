import numpy as np

# Create a NumPy array
array = np.array([1, 2, 3, 4, 5])
print("NumPy array:", array)

# Basic array operations
print("Sum of array elements:", np.sum(array))
print("Mean of array elements:", np.mean(array))
print("Maximum element:", np.max(array))
print("Minimum element:", np.min(array))

# Element-wise operations
array2 = np.square(array)
print("Squared array:", array2)

# Matrix operations
matrix = np.array([[1, 2], [3, 4]])
print("Matrix:")
print(matrix)
matrix_transposed = np.transpose(matrix)
print("Transposed matrix:")
print(matrix_transposed)

# Perform eigendecomposition
eigenvalues, eigenvectors = np.linalg.eig(matrix)
print("Eigenvalues:")
print(eigenvalues)
print("Eigenvectors:")
print(eigenvectors)

# Perform LU factorization. P is the permutation matrix,
# L is the lower triangular matrix, and U is the upper triangular matrix
import scipy.linalg as la
P, L, U = la.lu(matrix)
print("Permutation Matrix (P):")
print(P)
print("Lower Triangular Matrix (L):")
print(L)
print("Upper Triangular Matrix (U):")
print(U)

# Create a symmetric positive definite matrix (replace with your own matrix)
A = np.array([[10, 2, 3],
              [2, 11, 4],
              [3, 4, 12]])
print("Cholesky Factor (L):")
print(np.linalg.cholesky(A))  # lower triangular Cholesky factor


# Array indexing and slicing
print("Element at index 2:", array[2])
print("Slicing from index 1 to 3:", array[1:4])

# NumPy arrays can be multidimensional
multi_dim_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Multidimensional array:")
print(multi_dim_array)

# Accessing specific elements in a multidimensional array
print("Element at row 2, column 1:", multi_dim_array[1, 0])

# NumPy also provides functions for creating arrays
zeros_array = np.zeros((2, 3))  # Create a 2x3 array filled with zeros
print("Zeros array:")
print(zeros_array)

ones_array = np.ones((3, 2))    # Create a 3x2 array filled with ones
print("Ones array:")
print(ones_array)

# Reshaping arrays
arr_reshaped = array.reshape((1, 5))
print("Reshaped array:")
print(arr_reshaped)

# NumPy also supports random number generation
random_array = np.random.rand(3, 3)  # Create a 3x3 array of random numbers
print("Random array:")
print(random_array)
