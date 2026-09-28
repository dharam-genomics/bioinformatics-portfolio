import numpy as np
sample = np.array([["sample1", 10, 20, 30, 40],["sample2", 100, 200, 201,23], ["sample3", 12, 13, 14, 111]])
print(sample)
print(sample.ndim)
print(sample.shape)
print(sample[2,:])
print(sample[:,3])
print(sample.dtype)
