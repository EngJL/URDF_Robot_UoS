#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def callback(data):
    # process the received velocity commands
    pass

def listener():
    rospy.init_node('my_robot', anonymous=True)
    rospy.Subscriber("cmd_vel", Twist, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()

