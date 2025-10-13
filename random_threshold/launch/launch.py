from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='random_threshold',
            executable='random_publisher',
            name='random_publisher'
        ),
        Node(
            package='random_threshold',
            executable='threshold_subscriber',
            name='threshold_subscriber'
        ),
    ])