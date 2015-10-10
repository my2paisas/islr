'''
2.3 Lab: Introduction to R
2.3.1 Basic Commands
'''
import numpy as np
import math

# R: x <- c(1,3,2,5)
x = np.array([1, 3, 2, 5])
# R: x
print x

# R: x = c(1,6,2)
x = np.array([1, 6, 2])
# R: y = c(1,4,3)
y = np.array([1, 4, 3])

# R: length(x)
print len(x)
# R: length(y)
print len(y)

# R: x+y
print x + y

# R: ls()
# dir() also lists the built-ins which begin and end with __ 
# and imported packages
print dir()

# R: rm(x,y)
del x, y
print dir()

# R: rm(list=ls())
# could not figure out meaningful python equivalent

# R: x=matrix(data=c(1,2,3,4), nrow=2, ncol=2)
# Note that squaring an R matrix does element-wise squaring
# and not matrix multiplication, so we use numpy arrays, 
# not numpy matrices
x = np.array([[1, 3], [2, 4]])
print x

# R: x=matrix(data=c(1,2,3,4), nrow=2, ncol=2, byrow=TRUE)
x = np.array([[1, 2], [3, 4]])
print x

# the book has used the original value, so use that
x = np.array([[1, 3], [2, 4]])

# R: sqrt(x)
print np.sqrt(x)

# R: x^2
print x ** 2

# R: x=rnorm(50)
x = np.random.normal(0, 1, 50)
print x
# R: y = x + rnorm(50, mean=50, sd=.1)
y = x + np.random.normal(50, .1, 50)
print y
# R: cor(x,y)
print np.corrcoef(x, y)[0][1]

# R: set.seed(1303)
np.random.seed(1303)
print np.random.normal(0, 1, 50)

# R: set.seed(3)
np.random.seed(3)
# R: y=rnorm(100)
y = np.random.normal(0, 1, 100)
# R: mean(y)
print np.mean(y)
# R: var(y)
print np.var(y)
# R: sqrt(var(y))
print math.sqrt(np.var(y))
# R: sd(y)
print np.std(y)