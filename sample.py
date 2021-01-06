#!/usr/bin/env python
from CameraClient import CameraClient, ImageType, Command, CameraIntri
import sys
import cv2
import numpy as np
import os
import open3d

SAVE_PATH = "D:"

if __name__ == '__main__':

    camera = CameraClient()
    save_file = True
    # camera ip should be modified to actual ip address
    camera_ip = "192.168.3.226"
    # always set ip before do anything else
    if not camera.connect(camera_ip):
        exit(-1)
    # get some camera info like intrincis, ip, id and Version
    intri = camera.getCameraIntri()
    print ("Camera Info: %s" % (camera.getCameraInfo()))
    print ("Camera ID: %s" % (camera.getCameraId()))
    print ("Version: %s" % (camera.getCameraVersion()))

    # capture depth image and color image and save them
    depth = camera.captureDepthImg()
    color = camera.captureColorImg()
<<<<<<< HEAD
    depth = camera.captureDepthImg()  #depth data
    # save depth data
    with open('output.yaml', 'w') as f:
        yaml.dump({"depth_data": np.array(depth)}, f)
    # read depth data
    with open('output.yaml', 'r') as f:
        depth_data = np.array(yaml.load(f,Loader=yaml.Loader)['depth_data'])
        print(depth_data)
    
=======

>>>>>>> parent of 5b4f4b6 (增加深度信息使用注释)
    if len(depth) == 0 or len(color) == 0:
        exit(-2)

    if save_file:
        if not os.path.exists(SAVE_PATH):
            os.makedirs(SAVE_PATH)
        # The data format of the depth map saved by opencv is uint8, the black area represents no depth information, and the white area represents depth information; 
        # if you need to use depth data, directly use the depth in line 29 of the program "depth = camera.captureDepthImg()"
        cv2.imwrite(SAVE_PATH + "/mechmind_depth.png", depth)
        cv2.imwrite(SAVE_PATH + "/mechmind_color.jpg", color)
    # set some parameters of camera, you can refer to parameters' names in Mech_eye

    # get rgb point cloud. Using open3d to store and visualize the cloud.
    pcd = camera.captureCloud()
    open3d.visualization.draw_geometries([pcd])
    # set some parameters of camera, you can refer to parameters' names in Mech_eye
    print(camera.setParameter("scan2dExposureMode",0)) # set exposure mode to Timed
    print(camera.getParameter("scan2dExposureMode"))
    print(camera.setParameter("scan2dExposureTime",20)) # set exposure time to 20ms
    print(camera.getParameter("scan2dExposureTime"))
    exit(0)
<<<<<<< HEAD
    
=======
>>>>>>> parent of 5b4f4b6 (增加深度信息使用注释)
