#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class DrawSquareNode(Node):

    def __init__(self):
        super().__init__("draw_square")
        self.cmd_vel_pub_ = self.create_publisher(Twist, "/diffdrive_controller/cmd_vel_unstamped", 10)
        self.timer_ = self.create_timer(0.02, self.send_velocity_command)
        self.get_logger().info("Draw square node has been started")

    def send_velocity_command(self):
        msg = Twist()
        msg.linear.x = -3.0
        msg.angular.z = 0.5 * 3.14
        self.cmd_vel_pub_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = DrawSquareNode()
    rclpy.spin(node)
    rclpy.shutdown()