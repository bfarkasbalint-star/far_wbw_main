import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

class RandomPublisher(Node):
    def __init__(self):
        super().__init__('random_publisher')
        self.publisher_ = self.create_publisher(Float32, '/random_value', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)  # 1 Hz

    def timer_callback(self):
        msg = Float32()
        msg.data = random.uniform(0, 100)
        self.publisher_.publish(msg)
        self.get_logger().info(f'Published: {msg.data:.2f}')

def main(args=None):
    rclpy.init(args=args)
    node = RandomPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

