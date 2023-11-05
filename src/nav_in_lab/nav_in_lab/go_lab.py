#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan

class LaserScanSubscriberNode(Node):

    def __init__(self):
        super().__init__("Laser_subscriber")
        self.laser_subscriber_ = self.create_subscription(LaserScan, "/scan", self.laser_callback, 10)

    def laser_callback(self, msg: LaserScan):
        self.get_logger().info(str(msg))

def main(args=None):
    rclpy.init(args=args)
    node = LaserScanSubscriberNode()
    rclpy.spin(node)
    rclpy.shutdown()