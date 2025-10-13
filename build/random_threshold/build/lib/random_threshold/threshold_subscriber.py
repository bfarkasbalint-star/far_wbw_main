import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class ThresholdSubscriber(Node):
    def __init__(self):
        super().__init__('threshold_subscriber')
        self.subscription = self.create_subscription(
            Float32,
            'random_value',
            self.listener_callback,
            10)
        self.threshold = 50.0
        self.get_logger().info("ThresholdSubscriber started. Threshold = 50.0")

    def listener_callback(self, msg):
        value = msg.data
        if value > self.threshold:
            self.get_logger().warn(f'⚠️ Value {value:.2f} exceeds threshold {self.threshold}')
        else:
            self.get_logger().info(f'Value OK: {value:.2f}')

def main(args=None):
    rclpy.init(args=args)
    node = ThresholdSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()