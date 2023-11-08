#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from rclpy.task import Future

class LaserAngleAndDistance: #класс угол-расстояние
    
    def __init__(self, angle, range):
        self.angle = angle
        self.range = range

    def toStr(self):
        s = "Angle: " + str(self.angle) + " Distance: " + str(self.range)
        return s
    
    def get_angle(self):
        return self.angle
    
    def get_range(self):
        return self.range
    
    
class Very_talkative_Node(Node):
    def __init__(self):
        self.f = Future()
        super().__init__("Talkative_Node")
        self.laser_subscriber_ = self.create_subscription(LaserScan, "/scan", self.laser_callback, 10)
        self.cmd_vel_pub_ = self.create_publisher(Twist, "/cmd_vel", 10)
    def laser_callback(self, msg: LaserScan):
        self.get_logger().info("I am very talkative node!") 
        self.f.set_result(1)
        
       
class LaserScanSubscriberNode(Node):
    def __init__(self):
        self.st1 = Future()
        self.st2 = Future()
        self.st3 = Future()
        self.st4 = Future()
        super().__init__("Laser_subscriber")
        self.laser_subscriber_ = self.create_subscription(LaserScan, "/scan", self.laser_callback, 10)
        self.cmd_vel_pub_ = self.create_publisher(Twist, "/cmd_vel", 10)

    def get_st1(self):
        return self.st1
    
    def get_st2(self):
        return self.st1
    
    def get_st3(self):
        return self.st1
    
    def get_st4(self):
        return self.st1

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
        
        
        #self.get_logger().info(self.AngRangeList[5].toStr()) #вывод для проверки

        #------------------------------------------------- закончили обработку входных данных
        
class TurnToRightSide(LaserScanSubscriberNode):
    
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
        
        
        #self.get_logger().info(self.AngRangeList[5].toStr()) #вывод для проверки

        #------------------------------------------------- закончили обработку входных данных
        minlenind = ranges.index(min(ranges))
        msg = Twist()
        
        d = abs(self.AngRangeList[minlenind].get_angle() - self.AngRangeList[0].get_angle()) 
        if not(0.0 <= d < 0.2):
            msg.angular.z = 0.35
        else:
            msg.angular.z = 0.0
            self.st1.set_result(1)
        self.get_logger().info(str(self.AngRangeList[minlenind].get_angle()) + " " + str(self.AngRangeList[0].get_angle()))
        self.cmd_vel_pub_.publish(msg)    
            
class GoForward(LaserScanSubscriberNode):

  
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
        
        
        #self.get_logger().info(self.AngRangeList[5].toStr()) #вывод для проверки

        #------------------------------------------------- закончили обработку входных данных
        self.need_indexes = [i for i in range(-3, 3+1)]
        min_acceptable_range = min(self.AngRangeList[i].get_range() for i in self.need_indexes)
        self.get_logger().info(str(min_acceptable_range))
        msg = Twist()
        if min_acceptable_range > 0.6:
            msg.linear.x = 1.0
            self.get_logger().info("Riding...")
        else:
            msg.linear.x = 0.0
            self.st2.set_result(1)
            self.get_logger().info("I am near the wall")
        self.cmd_vel_pub_.publish(msg)

class TurnAlongTheWall(LaserScanSubscriberNode):
    
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
        
        
        #self.get_logger().info(self.AngRangeList[5].toStr()) #вывод для проверки

        #------------------------------------------------- закончили обработку входных данных
        minlenind = ranges.index(min(ranges))
        msg = Twist()
        
        d = abs(self.AngRangeList[minlenind].get_angle() - self.AngRangeList[0].get_angle()) 
        if not(6.28 - 3.14/2 - 0.2 <= d < 6.28 - 3.14/2 ):
            msg.angular.z = 0.35
        else:
            msg.angular.z = 0.0
            self.st3.set_result(1)
        self.get_logger().info(str(self.AngRangeList[minlenind].get_angle()) + " " + str(self.AngRangeList[0].get_angle()))
        self.cmd_vel_pub_.publish(msg)   
        

def main(args=None):
    rclpy.init(args=args)
    #nodet = Very_talkative_Node()
    #rclpy.spin_until_future_complete(node1, node1.f)

    node1 = TurnToRightSide() 
    rclpy.spin_until_future_complete(node1, node1.st1)

    node2 = GoForward()
    rclpy.spin_until_future_complete(node2, node2.st2)

    node3 = TurnAlongTheWall()
    rclpy.spin_until_future_complete(node3, node3.st3)
    #print(node2.AngRangeList[int(3.14)].get_angle())
    rclpy.shutdown()