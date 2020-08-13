# Mech-Eye_python_interface
This is official Python interface for Mech-Eye cameras. 

## Features 

By using this api, you can easily control your mech_eye cameras in python programs. The features of this API are as follows:

* Connect to your camera in your LANS.
* Set and get cameras parameters like exposure time, period and so on.
* Get color image and depth image as a numpy array.
* Get point cloud data as the format defined in open3d, a python lib which can deal with point clouds.

## Dependency

These python libraries are needed:

* opencv_python
* protobuf
* open3d

All these you can install with pip.

## Usage

Just clone this project and run main.py.

Make sure all .py files are in the same directory.

main.py is an sample to show you how to use API.