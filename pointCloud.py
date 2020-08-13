import open3d
import numpy as np
import cv2
 

def getRGBCloud(color,depth):
 
	test_pcd = open3d.geometry.PointCloud()  # 定义点云
	
	color.flatten()
	color = color / 256
	color.resize(int(np.size(color)/3),3)
	depth.flatten()
	depth = depth * 0.001
	depth.resize(int(np.size(depth)/3),3)
	test_pcd.points = open3d.utility.Vector3dVector(depth)  # 定义点云坐标位置
	test_pcd.colors = open3d.utility.Vector3dVector(color)  # 定义点云的颜色
	return test_pcd