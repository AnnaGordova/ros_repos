#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan

class LaserAngleAndDistance: #класс угол-расстояние
    
    def __init__(self, angle, dist):
        self.angle = angle
        self.dist = dist

    def toStr(self):
        s = "Angle: " + str(self.angle) + " Distance: " + str(self.dist)
        return s
    
class LaserScanSubscriberNode(Node):

    def __init__(self):
        super().__init__("Laser_subscriber")
        self.laser_subscriber_ = self.create_subscription(LaserScan, "/scan", self.laser_callback, 10)

    def laser_callback(self, msg: LaserScan):
        self.angle_min = msg.angle_min #задаем поля для углов
        self.angle_max = msg.angle_max
        self.angle_increment = msg.angle_increment
        
        ranges = msg.ranges #список расстояний
        angle_list = [] #список углов
        temp = self.angle_min
        while temp <= self.angle_max: #заполняем спсиок промежуточных значений углов 
            angle_list.append(temp)
            temp += self.angle_increment

        self.AngRangeList = [] #спсиок объектов класса угол-расстояние
   
        for i in range(0, len(angle_list)): #заполянем
            self.AngRangeList.append(LaserAngleAndDistance(angle_list[i], ranges[i]))
        
        '''
        for i in range(0, len(self.AngRangeList)): # вывод для красоты
            self.get_logger().info(self.AngRangeList[i].toStr())'''
        
        
        self.get_logger().info(self.AngRangeList[5].toStr()) #вывод для проверки
        

        
        

def main(args=None):
    rclpy.init(args=args)
    node = LaserScanSubscriberNode()
    rclpy.spin(node)
    rclpy.shutdown()