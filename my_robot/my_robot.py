#! /usr/bin/env python3
import rclpy
from rclpy.node import Node

class Mynode(Node):
    def __init__(self):
        super().__init__("first_Ros_node")
        self.create_timer(1,self.timer)
        self.counter_= 0
        

    def timer(self):

        self.get_logger().info("my_first_node")


def main(args=None):
    rclpy.init(args=args)
    node = Mynode()
    #continue to run and to keep the node alive
    rclpy.spin(node)
    rclpy.shutdown()

if __name__== '__main__':
    main()
