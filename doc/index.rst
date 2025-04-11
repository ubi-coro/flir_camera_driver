# ROS Teledyne FLIR camera drivers

<a href="https://www.flir.com/browse/industrial/machine-vision-cameras/">
   <img src="doc/flir.png" />
</a>

This repository contains ROS2 packages for machine vision cameras made by Teledyne FLIR (formerly known as PointGrey).

> [!NOTE]
> 
> This software is *not supported* by Teleydyne FLIR.

# Packages

## Spinnaker camera driver

A camera driver supporting USB3 and GIGE cameras that has been successfully used for Blackfly, Blackfly S, Chameleon, and Grasshopper cameras. It should work with any FLIR camera that supports the Spinnaker SDK. See the [spinnaker_camera_driver](spinnaker_camera_driver/doc/index.rst) for more.

<a href="https://build.ros2.org/job/Hbin_uJ64__spinnaker_camera_driver__ubuntu_jammy_amd64__binary/">
   <img src="https://build.ros2.org/buildStatus/icon?job=Hbin_uJ64__spinnaker_camera_driver__ubuntu_jammy_amd64__binary&subject=Humble" />
</a>
<a href="https://build.ros2.org/job/Ibin_uJ64__spinnaker_camera_driver__ubuntu_jammy_amd64__binary/">
   <img src="https://build.ros2.org/buildStatus/icon?job=Ibin_uJ64__spinnaker_camera_driver__ubuntu_jammy_amd64__binary&subject=Iron" />
</a>
<a href="https://build.ros2.org/job/Jbin_uN64__spinnaker_camera_driver__ubuntu_noble_amd64__binary/">
   <img src="https://build.ros2.org/buildStatus/icon?job=Jbin_uN64__spinnaker_camera_driver__ubuntu_noble_amd64__binary&subject=Jazzy" />
</a>
<a href="https://build.ros2.org/job/Rbin_uN64__spinnaker_camera_driver__ubuntu_noble_amd64__binary/">
   <img src="https://build.ros2.org/buildStatus/icon?job=Rbin_uN64__spinnaker_camera_driver__ubuntu_noble_amd64__binary&subject=Rolling" />
</a>

## Spinnaker synchronized camera driver

Based on the spinnaker_camera_driver package, this driver is specifically designed for cameras that are hardware triggered by an external pulse. Images triggered by the same external pulse will have identical ROS header time stamps. See the [spinnaker_synchronized_camera_driver](spinnaker_synchronized_camera_driver/doc/index.rst) for more.

<a href="https://build.ros2.org/job/Hbin_uJ64__spinnaker_synchronized_camera_driver__ubuntu_jammy_amd64__binary/">
   <img src="https://build.ros2.org/buildStatus/icon?job=Hbin_uJ64__spinnaker_synchronized_camera_driver__ubuntu_jammy_amd64__binary&subject=Humble" />
</a>
<a href="https://build.ros2.org/job/Ibin_uJ64__spinnaker_synchronized_camera_driver__ubuntu_jammy_amd64__binary/">
   <img src="https://build.ros2.org/buildStatus/icon?job=Ibin_uJ64__spinnaker_synchronized_camera_driver__ubuntu_jammy_amd64__binary&subject=Iron" />
</a>
<a href="https://build.ros2.org/job/Jbin_uN64__spinnaker_synchronized_camera_driver__ubuntu_noble_amd64__binary/">
   <img src="https://build.ros2.org/buildStatus/icon?job=Jbin_uN64__spinnaker_synchronized_camera_driver__ubuntu_noble_amd64__binary&subject=Jazzy" />
</a>
<a href="https://build.ros2.org/job/Rbin_uN64__spinnaker_synchronized_camera_driver__ubuntu_noble_amd64__binary/">
   <img src="https://build.ros2.org/buildStatus/icon?job=Rbin_uN64__spinnaker_synchronized_camera_driver__ubuntu_noble_amd64__binary&subject=Rolling" />
</a>
            
## FLIR camera description

Package with [meshes and urdf](flir_camera_description/README.md) files.

<a href="https://build.ros2.org/job/Hbin_uJ64__flir_camera_description__ubuntu_jammy_amd64__binary/">
   <img src="https://build.ros2.org/buildStatus/icon?job=Hbin_uJ64__flir_camera_description__ubuntu_jammy_amd64__binary&subject=Humble" />
</a>
<a href="https://build.ros2.org/job/Ibin_uJ64__flir_camera_description__ubuntu_jammy_amd64__binary/">
   <img src="https://build.ros2.org/buildStatus/icon?job=Ibin_uJ64__flir_camera_description__ubuntu_jammy_amd64__binary&subject=Iron" />
</a>
<a href="https://build.ros2.org/job/Jbin_uN64__flir_camera_description__ubuntu_noble_amd64__binary/">
   <img src="https://build.ros2.org/buildStatus/icon?job=Jbin_uN64__flir_camera_description__ubuntu_noble_amd64__binary&subject=Jazzy" />
</a>
<a href="https://build.ros2.org/job/Rbin_uN64__flir_camera_description__ubuntu_noble_amd64__binary/">
   <img src="https://build.ros2.org/buildStatus/icon?job=Rbin_uN64__flir_camera_description__ubuntu_noble_amd64__binary&subject=Rolling" />
</a>

## FLIR camera messages

Package with with [image exposure and control messages](flir_camera_msgs/README.md). These are used by the [spinnaker_camera_driver](spinnaker_camera_driver/doc/index.rst).

<a href="https://build.ros2.org/job/Hbin_uJ64__flir_camera_msgs__ubuntu_jammy_amd64__binary/">
   <img src="https://build.ros2.org/buildStatus/icon?job=Hbin_uJ64__flir_camera_msgs__ubuntu_jammy_amd64__binary&subject=Humble" />
</a>
<a href="https://build.ros2.org/job/Ibin_uJ64__flir_camera_msgs__ubuntu_jammy_amd64__binary/">
   <img src="https://build.ros2.org/buildStatus/icon?job=Ibin_uJ64__flir_camera_msgs__ubuntu_jammy_amd64__binary&subject=Iron" />
</a>
<a href="https://build.ros2.org/job/Jbin_uN64__flir_camera_msgs__ubuntu_noble_amd64__binary/">
   <img src="https://build.ros2.org/buildStatus/icon?job=Jbin_uN64__flir_camera_msgs__ubuntu_noble_amd64__binary&subject=Jazzy" />
</a>
<a href="https://build.ros2.org/job/Rbin_uN64__flir_camera_msgs__ubuntu_noble_amd64__binary/">
   <img src="https://build.ros2.org/buildStatus/icon?job=Rbin_uN64__flir_camera_msgs__ubuntu_noble_amd64__binary&subject=Rolling" />
</a>
