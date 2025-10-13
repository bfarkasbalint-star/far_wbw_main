import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class ThresholdSubscriber(Node):
    def __init__(self, threshold=50.0):
        super().__init__('threshold_subscriber')
        self.threshold = threshold
        self.subscription = self.create_subscription(
            Float32,
            '/random_value',
            self.listener_callback,
            10
        )

    def listener_callback(self, msg):
        if msg.data > self.threshold:
            self.get_logger().info(f'Threshold exceeded: {msg.data:.2f}')
        else:
            self.get_logger().info(f'OK: {msg.data:.2f}')

def main(args=None):
    rclpy.init(args=args)
    node = ThresholdSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
