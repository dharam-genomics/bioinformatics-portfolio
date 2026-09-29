import numpy as np

def depth_qc(depth, minimum_depth):
    pass_pos = depth[depth >= minimum_depth]
    depth_size = depth.size
    pass_count = pass_pos.size
    percentage = (pass_count / depth_size) * 100
    return pass_pos, pass_count, percentage

depth = np.array([5, 12, 25, 8, 40, 18, 3, 30])

pass_position, pass_count, result = depth_qc(depth, 30)

print(pass_position, pass_count, result)
