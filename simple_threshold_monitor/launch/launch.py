from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='simple_threshold_monitor',
            executable='random_publisher',
            name='random_publisher',
            output='screen'  
        ),
        Node(
            package='simple_threshold_monitor',
            executable='threshold_subscriber',
            name='threshold_subscriber',
            output='screen'  
        ),
    ])
