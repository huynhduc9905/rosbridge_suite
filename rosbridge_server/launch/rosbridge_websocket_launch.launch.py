import os
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import AnyLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # Define node
    rosbridge = Node(
        package='rosbridge_server',
        executable='rosbridge_websocket',
        name='rosbridge_websocket',
        output='screen'
    )

    # Get the directory of your package
    package_dir = get_package_share_directory('rosbridge_server')

    # Define the path to your XML file
    xml_launch_file = os.path.join(package_dir, 'launch', 'rosbridge_websocket_launch.xml')

    # Include the XML launch file
    include_xml_launch = IncludeLaunchDescription(
        AnyLaunchDescriptionSource(xml_launch_file)
    )

    # Create launch description
    return LaunchDescription([
        include_xml_launch
    ])
