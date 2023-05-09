#!/usr/bin/env python
# coding: utf-8

# # Numpy
# 
# Numpy is a Python library for scientific computing. It provides high-performance multidimensional arrays and matrices, and efficient tools for working with these objects.

# In[1]:


import numpy as np


# ## Create numpy arrays

# A basic way to create an array is to use the function `np.array()`. It takes a list as an argument and returns a numpy array.

# In[2]:


a = np.array([1, 2, 3])
print(a)


# In numpy, there are many methods to create arrays. For example, `np.arange()` creates an array of integers, `np.zeros()` creates an array of zeros, and `np.ones()` creates an array of ones.

# In[3]:


np.arange(10)


# In[4]:


np.arange(1, 10, 2)


# In[5]:


np.zeros(10)


# In[6]:


np.zeros((3, 5))


# In[7]:


np.ones(10)


# In[8]:


np.ones((3, 5))


# `np.random.??` makes random arrays.
# 
# `np.random.rand()` makes an array of random numbers from the uniform distribution between 0 and 1.
# 
# `np.random.randn()` makes an array of random numbers from the standard normal distribution.
# 
# `np.random.randint(low, high, size)` makes an array of random integers between low and high.
# 
# `np.random.choice(a, size, replace=True, p=None)` makes an array of random numbers from the list a.

# In[9]:


print('np.random.rand(5) = ', np.random.rand(5), sep='\n', end='\n\n')

print('np.random.randn(5) = ', np.random.randn(5), sep='\n', end='\n\n')

print('np.random.rand(3, 5) = ', np.random.rand(3, 5), sep='\n', end='\n\n')

print('np.random.randint(low=1, high=10, size=5) = ', np.random.randint(low=1, high=10, size=5), end='\n\n')

print('np.random.randint(10) = ', np.random.randint(10), end='\n\n')

print('np.random.randint(1, 10, (3, 5)) = ', np.random.randint(1, 10, (3, 5)), sep='\n')

print("np.random.choice(['a', 'b', 'c'], 10) = ", np.random.choice(['a', 'b', 'c'], 10), sep='\n', end='\n\n')


# `np.linspace(start, stop, num, endpoint=True)` creates an array of evenly spaced numbers over a specified interval. This can be useful for plotting functions.

# In[10]:


np.linspace(0, 1, 6)


# `np.eye()` creates an matrix with ones on the diagonal and zeros elsewhere. You can also make non-square identity matrices by specifying the number of rows and columns.

# In[11]:


np.eye(3, 5)


# In[12]:


np.eye(5) # This is the same as np.identity(5)


# In[13]:


np.identity(5)


# `np.emtpy()` creates an array of uninitialized (arbitrary) data of the given shape and dtype. It is used when you want to create an array and then fill it with data later. It is faster than creating an array of zeros or ones using `np.zeros()` or `np.ones()`.

# In[14]:


np.empty(10)


# `np.zeros_like(()`, `np.ones_like()`, `np.empty_like()` create arrays of zeros, ones, or uninitialized data with the same shape and dtype as the given array.

# In[15]:


a = np.array([[1, 2, 3],
              [4, 5, 6]])

np.zeros_like(a)


# In[16]:


np.full((3, 5), 3)


# In[17]:


np.fromfunction(lambda i, j: i + j, (3, 5))


# ## Manipulating arrays

# In[18]:


# Append 4 to a
a = np.array([1, 2, 3])
b = np.append(a, 4)
print(b)


# In[19]:


# Delete a[1]
a = np.array([1, 2, 3])
b = np.delete(a, 1)
print(b)


# In[20]:


# Sort a
a = np.array([3, 2, 1])
b = np.sort(a)
print(b)


# In[21]:


# Concatenate two arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.concatenate((a, b))
print(c)


# In[22]:


# Reshape an array
a = np.array([1, 2, 3, 4, 5, 6])
print('a.shape ', a.shape)
b = a.reshape(2, 3)
print('b = ', b)
print('b.shape ', b.shape)


# In[23]:


# Conditional selection
a = np.array([1, 2, 3, 4, 5, 6])
print(a > 3)
print(a[a > 3])


# In[24]:


# Slice an array
a = np.array([1, 2, 3, 4, 5, 6])
# print from a[1] to a[3], not including a[4](=5)
print(a[1:4])


# ## Arithmetic operations on arrays

# In[25]:


a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

# Addition
print(a + b)

# Subtraction
print(a - b)

# Multiplication
print(a * b)

# Division
print(a / b)


# In[26]:


a = np.array([1, 2, 3, 4])

# Add a scalar to each element
print('a + 2 = ', a + 2)

# Subtract a scalar from each element
print('a - 2 = ', a - 2)

# Multiply a scalar to each element
print('a * 2 = ', a * 2)

# Divide each element by a scalar
print('a / 2 = ', a / 2)

# Take the square root of each element
print('a ** 0.5 = ', np.sqrt(a))

# Take the square of each element
print('a ** 2 = ', a ** 2)

# Take the log of each element
print('np.log(a) = ', np.log(a))

# Take the exponential of each element
print('np.exp(a) = ', np.exp(a))

# Take the sin of each element
print('np.sin(a) = ', np.sin(a))

# Take the cos of each element
print('np.cos(a) = ', np.cos(a))


# In[27]:


a = np.array([1, 2, 3, 4, 5])

# Maximum
print('max = ', a.max())

# Minimum
print('min = ', a.min())

# Argmax
print('argmax = ', a.argmax())

# Argmin
print('argmin = ', a.argmin())

# Sum
print('sum = ', a.sum())

# Mean
print('mean = ', a.mean())

# Standard deviation
print('std = ', a.std())

# Variance
print('var = ', a.var())


# In[28]:


# Dot product
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
print(np.dot(a, b))


# ## Matrix operations

# In[29]:


a = np.array([[1, 2, 3],
              [4, 5, 6]])
b = np.array([[7, 8],
              [9, 10],
              [11, 12]])

# Matrix multiplication
print(np.dot(a, b), end='\n\n')

print(a.dot(b), end='\n\n')

print(a @ b, end='\n\n')


# In[30]:


a = np.array([[1, 2, 3],
              [4, 6, 8],
              [7, 11, 13]])

# Transpose
print('a.T = ', a.T, sep='\n', end='\n\n')

# Trace
print('np.trace(a) = ', np.trace(a), end='\n\n')

# Determinant
print('np.linalg.det(a) = ', np.linalg.det(a), end='\n\n')

# Inverse
print('np.linalg.inv(a) = ', np.linalg.inv(a), sep='\n', end='\n\n')


# `np.linalg.???` is a module for linear algebra. `linalg` can also be called from `scipy` as `scipy.linalg.???`.

# In[31]:


# Eigenvalues and eigenvectors
eigvals, eigvecs = np.linalg.eig(a)
print('eigvals = ', eigvals, sep='\n', end='\n\n')
print('eigvecs = ', eigvecs, sep='\n', end='\n\n')

print('a = ', eigvecs @ np.diag(eigvals) @ np.linalg.inv(eigvecs), sep='\n', end='\n\n')


# In[32]:


# Singular value decomposition
U, S, V = np.linalg.svd(a)
print('U = ', U, sep='\n', end='\n\n')
print('S = ', S, sep='\n', end='\n\n')
print('V = ', V, sep='\n', end='\n\n')

print('a = ', U @ np.diag(S) @ V, sep='\n', end='\n\n')


# ## [Learn more about numpy](https://numpy.org/doc/stable/user/absolute_beginners.html)
