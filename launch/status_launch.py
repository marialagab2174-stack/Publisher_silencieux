from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='publisher_silencieux',
            executable='status_node',
            name='robot_status_checker',
            output='screen'
        )
    ])
