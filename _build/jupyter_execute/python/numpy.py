#!/usr/bin/env python
# coding: utf-8

# # Numpy
# 
# Numpy is a Python library for scientific computing. It provides high-performance multidimensional arrays and matrices, and efficient tools for working with these objects.

# In[1]:


import numpy as np


# ## Create numpy arrays

# A basic way to create a `np.array` is to use the array function. It takes a list as an argument and returns a numpy array.

# In[2]:


a = np.array([1, 2, 3])
print(a)


# In numpy, there are many methods to create arrays. For example, `np.arange` creates an array of integers, `np.zeros` creates an array of zeros, and `np.ones` creates an array of ones.

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


# `np.linspace` creates an array of evenly spaced numbers over a specified interval.

# In[9]:


np.linspace(0, 1, 6)


# `np.eye` creates an matrix with ones on the diagonal and zeros elsewhere. You can also make non-square identity matrices by specifying the number of rows and columns.

# In[10]:


np.eye(3, 5)


# In[11]:


np.eye(5) # This is the same as np.identity(5)


# In[12]:


np.identity(5)


# `np.emtpy` creates an array of uninitialized (arbitrary) data of the given shape and dtype. It is used when you want to create an array and then fill it with data later. It is faster than creating an array of zeros or ones using `np.zeros` or `np.ones`.

# In[13]:


np.empty(10)


# `np.zeros_like`, `np.ones_like`, `np.empty_like` create arrays of zeros, ones, or uninitialized data with the same shape and dtype as the given array.

# In[14]:


a = np.array([[1, 2, 3],
              [4, 5, 6]])

np.zeros_like(a)


# ## Manipulating arrays

# In[15]:


# Append 4 to a
a = np.array([1, 2, 3])
b = np.append(a, 4)
print(b)


# In[16]:


# Delete a[1]
a = np.array([1, 2, 3])
b = np.delete(a, 1)
print(b)


# In[17]:


# Sort a
a = np.array([3, 2, 1])
b = np.sort(a)
print(b)


# In[18]:


# Concatenate two arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.concatenate((a, b))
print(c)


# In[19]:


# Reshape an array
a = np.array([1, 2, 3, 4, 5, 6])
print('a.shape ', a.shape)
b = a.reshape(2, 3)
print('b = ', b)
print('b.shape ', b.shape)


# In[20]:


# Conditional selection
a = np.array([1, 2, 3, 4, 5, 6])
print(a > 3)
print(a[a > 3])


# In[21]:


# Slice an array
a = np.array([1, 2, 3, 4, 5, 6])
# print from a[1] to a[3], not including a[4](=5)
print(a[1:4])


# ## Arithmetic operations

# In[22]:


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


# In[23]:


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


# In[24]:


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


# In[25]:


# Dot product
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
print(np.dot(a, b))


# ## [Learn more about numpy](https://numpy.org/doc/stable/user/absolute_beginners.html)
