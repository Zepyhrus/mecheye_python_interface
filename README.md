# Mech-Eye_python_interface
This is official Python interface for Mech-Eye cameras. 

## Introduction

This camera interface is developped by python. We use ZeroMQ library to connect camera devices in the LANs. And Google protobuf is used to pack and unpack data from networks.

## Features 

By using this api, you can easily control your mech_eye cameras in python programs. The features of this API are as follows:

* Connect to your camera in your LANS.
* Set and get cameras parameters like exposure time, period and so on.
* Get color image and depth image as a numpy array.
* Get point cloud data as the format defined in open3d, a python lib which can deal with point clouds.

## Dependency

We ran and tested this API on Python3. These python libraries are needed:

* opencv_python
* protobuf
* open3d

All these you can install with pip, by following command:

```
pip3 install opencv-python protobuf open3d
```



## Usage

Just clone this project and run main.py.

Do not change .py files arrangement.

main.py is an sample to show you how to use API.