import numpy as np
depth = np.array([5, 12, 25, 8, 40, 18, 3, 30])
print("All Depth:", depth)
print("Depth >= 20:", depth[depth >= 20])
print("Depth between 10 and 30:", depth[(depth >= 10) & (depth <= 30)])
print("Very low and very high depth:", depth[(depth < 5) |(depth > 30)])
