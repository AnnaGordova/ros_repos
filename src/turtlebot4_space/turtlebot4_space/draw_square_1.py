#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math
import time






class DrawSquareNode(Node):
    my_angle_z = 0

    def __init__(self):
        super().__init__("draw_square")
        self.cmd_vel_pub_ = self.create_publisher(Twist, "/diffdrive_controller/cmd_vel_unstamped", 10)
        #self.timer_ = self.create_timer(0.02, self.send_velocity_command)
        self.get_logger().info("Draw square 1 node has been started")

        start = time.time()
        while time.time() - start < 5:
            self.send_velocity_command_out()
        self.get_logger().info("I am free!")
        
        while True:
            self.send_velocity_command_out_rotate()

    def send_velocity_command(self):
        msg = Twist()
        msg.linear.x = -3.0
        msg.angular.z = 0.5 * 3.14
        self.cmd_vel_pub_.publish(msg)

    def send_velocity_command_out(self):
        msg = Twist()
        msg.linear.x = -3.0
        self.cmd_vel_pub_.publish(msg)

    def send_velocity_command_out_rotate(self):
        msg = Twist()
        msg.angular.z = math.pi
        self.cmd_vel_pub_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = DrawSquareNode()
    rclpy.spin(node)
    rclpy.shutdown()