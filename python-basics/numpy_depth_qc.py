import numpy as np

depth = np.array([5, 12, 25, 8, 40, 18, 3, 30])
passing_depth = depth[depth >= 20]
print("Passing depths are:", passing_depth)
passing_position = passing_depth.size
print("The number of passing pasitions is:", passing_position)
total_depth_length = depth.size
percentage_passing = (passing_position / total_depth_length) * 100
print("Percentage of passing depth is:", percentage_passing)
