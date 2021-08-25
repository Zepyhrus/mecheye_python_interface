#!/usr/bin/env python
from CameraClient import CameraClient, ImageType, Command, CameraIntri
import sys
import cv2
import numpy as np
import os
import open3d

import matplotlib.pyplot as plt
plt.rcParams['figure.autolayout'] = True

SAVE_PATH = "data"

if __name__ == '__main__':

    camera = CameraClient()
    save_file = True
    # camera ip should be modified to actual ip address
    camera_ip = "192.168.1.13"
    # always set ip before do anything else
    if not camera.connect(camera_ip):
        exit(-1)
    # # get some camera info like intrincis, ip, id and Version
    # intri = camera.getCameraIntri()
    # print ("Camera Info: %s" % (camera.getCameraInfo()))
    # print ("Camera ID: %s" % (camera.getCameraId()))
    # print ("Version: %s" % (camera.getCameraVersion()))

    # # capture depth image and color image and save them
    # depth = camera.captureDepthImg()
    # color = camera.captureColorImg()

    # if len(depth) == 0 or len(color) == 0:
    #     exit(-2)

    # if save_file:
    #     if not os.path.exists(SAVE_PATH):
    #         os.makedirs(SAVE_PATH)
    #     cv2.imwrite(SAVE_PATH + "/mechmind_depth.png", depth)
    #     cv2.imwrite(SAVE_PATH + "/mechmind_color.jpg", color)
    # # set some parameters of camera, you can refer to parameters' names in Mech_eye


    print(camera.setParameter("scan2dExposureTime", 100)) # set exposure time to 20ms
    print(camera.getParameter("scan2dExposureTime"))
    # get rgb point cloud. Using open3d to store and visualize the cloud.
    pcd = camera.captureCloud()

    # p = np.asarray(pcd.points)
    # plt.hist(p[:, 2], np.arange(100)/100)
    # plt.show()

    open3d.visualization.draw_geometries([pcd])


    # # set some parameters of camera, you can refer to parameters' names in Mech_eye
    # print(camera.setParameter("scan2dExposureMode",0)) # set exposure mode to Timed
    # print(camera.getParameter("scan2dExposureMode"))

    # # get rgb point cloud. Using open3d to store and visualize the cloud.
    # pcd = camera.captureCloud()
    # open3d.visualization.draw_geometries([pcd])

    # print(camera.setParameter("scan2dExposureTime",20)) # set exposure time to 20ms
    # print(camera.getParameter("scan2dExposureTime"))

    # # get rgb point cloud. Using open3d to store and visualize the cloud.
    # pcd = camera.captureCloud()
    # open3d.visualization.draw_geometries([pcd])
    exit(0)
