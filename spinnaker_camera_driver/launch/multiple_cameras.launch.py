# -----------------------------------------------------------------------------
# Copyright 2022 Bernd Pfrommer <bernd.pfrommer@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
multiple_cameras.launch.py

This ROS 2 launch file initializes a composable node container for running multiple 
FLIR (Spinnaker-based) cameras within a single process space using intra-process communication.

The launch description defines two camera nodes, each instantiated with specific serial numbers, 
camera types, and ROS node names provided as launch arguments. These camera nodes share the 
same address space for efficient resource use and potential synchronization, though they run 
independently.

Key features:
- Uses composable nodes to optimize runtime performance via intra-process communication.
- Allows configuration of camera parameters, including exposure, gain, and trigger settings.
- Loads additional camera-specific parameters from a YAML file based on the camera type.
- Supports chunk data streaming for metadata such as timestamp, gain, and exposure time.

This launch file is tailored for stereo camera setups or other use cases requiring multiple
independent camera streams under a unified ROS node container.

Author: Bernd Pfrommer
License: Apache License 2.0
"""

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument as LaunchArg, OpaqueFunction
from launch.substitutions import LaunchConfiguration as LaunchConfig, PathJoinSubstitution, TextSubstitution
from launch_ros.actions import ComposableNodeContainer
from launch_ros.descriptions import ComposableNode
from launch_ros.substitutions import FindPackageShare

CAMERAS = [
    {"name": "left_wide", "serial": "H2825879", "type": "genie_nano"},
    {"name": "left_normal", "serial": "H2825877", "type": "genie_nano"},
    {"name": "middle_telephoto", "serial": "H2825876", "type": "genie_nano"},
    {"name": "right_normal", "serial": "H2825880", "type": "genie_nano"},
    {"name": "right_wide", "serial": "H2825878", "type": "genie_nano"},
]

camera_params = {
    'debug': False,
    'compute_brightness': True,
    'dump_node_map': False,
    'adjust_timestamp': True,
    'gain_auto': 'Off',
    'gain': 0,
    'exposure_auto': 'Off',
    'exposure_time': 9000,
    'line2_selector': 'Line2',
    'line2_v33enable': False,
    'line3_selector': 'Line3',
    'line3_linemode': 'Input',
    'trigger_selector': 'FrameStart',
    'trigger_mode': 'On',
    'trigger_source': 'Line3',
    'trigger_delay': 9,
    'trigger_overlap': 'ReadOut',
    'chunk_mode_active': True,
    'chunk_selector_frame_id': 'FrameID',
    'chunk_enable_frame_id': True,
    'chunk_selector_exposure_time': 'ExposureTime',
    'chunk_enable_exposure_time': True,
    'chunk_selector_gain': 'Gain',
    'chunk_enable_gain': True,
    'chunk_selector_timestamp': 'Timestamp',
    'chunk_enable_timestamp': True,
}

def make_camera_node(name: str, camera_type: str, serial: str) -> ComposableNode:
    """
    Creates a composable node configuration for a camera driver.

    Args:
        name: The name of the camera node.
        camera_type: The type of the camera, used to determine the configuration file.
        serial: The serial number of the camera.
    
    Returns:
        ComposableNode: A configured composable node for the spinnaker_camera_driver.
    """
    parameter_file = PathJoinSubstitution([
        FindPackageShare('spinnaker_camera_driver'),
        'config',
        f'{camera_type}.yaml'
    ])

    node = ComposableNode(
        package='spinnaker_camera_driver',
        plugin='spinnaker_camera_driver::CameraDriver',
        name=name,
        parameters=[camera_params, {'parameter_file': parameter_file, 'serial_number': serial}],
        remappings=[
            ('~/control', '/exposure_control/control'),
        ],
        extra_arguments=[{'use_intra_process_comms': True}],
    )
    return node


def launch_setup(context): #, *args, **kwargs):
    """Create multiple camera."""
    composable_nodes = []
    for cam in CAMERAS:
        ros_name = LaunchConfig(f"{cam['name']}_name").perform(context)
        cam_type = LaunchConfig(f"{cam['name']}_type").perform(context)
        serial = LaunchConfig(f"{cam['name']}_serial").perform(context)
        composable_nodes.append(make_camera_node(ros_name, cam_type, serial))

    container = ComposableNodeContainer(
        name='multi_camera_container',
        namespace='',
        package='rclcpp_components',
        executable='component_container',
        composable_node_descriptions=composable_nodes,
        output='screen',
    )
    return [container]


def generate_launch_description():
    """Launch 5 FLIR cameras with descriptive names, types, and serials."""

    launch_args = []

    for cam in CAMERAS:
        launch_args.extend([
            LaunchArg(
                f"{cam['name']}_name",
                default_value=TextSubstitution(text=cam['name']),
                description=f"ROS node name for camera {cam['name']}"
            ),
            LaunchArg(
                f"{cam['name']}_serial",
                default_value=TextSubstitution(text=cam['serial']),
                description=f"Serial number for camera {cam['name']}"
            ),
            LaunchArg(
                f"{cam['name']}_type",
                default_value=TextSubstitution(text=cam['type']),
                description=f"Type of camera {cam['name']}"
            ),
        ])

    launch_args.append(OpaqueFunction(function=launch_setup))
    return LaunchDescription(launch_args)
