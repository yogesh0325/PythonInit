import numpy as np
import open3d as o3d

# set the size of the array
array_size = 500000
point_range = 15

# generate random values between -15 and 15 for x, y, and z coordinates
x = np.random.uniform(low=-point_range, high=point_range, size=array_size)
y = np.random.uniform(low=-point_range, high=point_range, size=array_size)
z = np.random.uniform(low=-point_range, high=point_range, size=array_size)

# stack the x, y, and z arrays together to form the final 500,000 x 3 array
final_array = np.column_stack((x, y, z))

points = o3d.utility.Vector3dVector(final_array)

cloud = o3d.geometry.PointCloud(points)
o3d.io.write_point_cloud('testing1.pcd', cloud, write_ascii=True)