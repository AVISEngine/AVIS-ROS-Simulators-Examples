#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import CompressedImage
from cv_bridge import CvBridge
import cv2

bridge = CvBridge()

def callback(data):
    frame = bridge.imgmsg_to_cv2(data, "bgr8")
    '''
    TODO:Implementation
    '''
    cv2.imshow("window", frame)
    cv2.waitKey(10)

def receive():
    rospy.Subscriber("/drone/front_camera/image_raw/compressed", CompressedImage, callback)
    rospy.spin()

if __name__ == "__main__":
    rospy.init_node("receiveImage" , anonymous=True)
    try:
        receive()
    except rospy.ROSInterruptException: pass