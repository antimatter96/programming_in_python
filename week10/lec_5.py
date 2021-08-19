# numpy

# NUMPY arrays are homogenous
# [1, "2"] not allowed

# in nested list
# inner lists should be of the same size

# python list -> non contigous
# numpy -> contigous

# can do element wise operation in numpy

# can do arithmetic operations

# 
# ndarray

a = [42]
b = [1,2]
c = [[1,2,3], [1,2,3]]
d = [ [[1,2,3], [1,2,3]], [[1,2,3], [1,2,3]] ]

# a , b, c , d are considered as 1D lists by Python 
# they are just nested

import numpy as np

a_new = np.array(a)
b_new = np.array(b)
c_new = np.array(c)
d_new = np.array(d)

print(a_new, a_new.ndim)
print(b_new, b_new.ndim)
print(c_new, c_new.ndim)
print(d_new, d_new.ndim)
