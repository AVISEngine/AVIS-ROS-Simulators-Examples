#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
import cv2
import time

def drive():
    velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    # Init Twist values
    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    # Get parameters from input
    while not rospy.is_shutdown():
        # Your implementation can be here
        vel_msg.linear.x = 3
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 2

        velocity_publisher.publish(vel_msg)

if __name__ == "__main__":
    rospy.init_node("control" , anonymous=True)
    try:
        drive()
    except rospy.ROSInterruptException: pass
