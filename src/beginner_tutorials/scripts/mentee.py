#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo('No I am so hungry')
    

def mentee():
    rospy.init_node('mentee',anonymous=True)
    rospy.Subscriber('food',String, callback)
    rospy.spin()
    
if __name__ =='__main__':
    mentee()

