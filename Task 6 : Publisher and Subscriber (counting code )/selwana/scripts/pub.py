#!/usr/bin/env python

import rospy
from std_msgs.msg import Char
    
def talker():
        pub = rospy.Publisher('chatter', Char, queue_size=10)
        rospy.init_node('talker', anonymous=False)
        rate = rospy.Rate(10) # 10hz
        i=0
        counter=0
        while not rospy.is_shutdown():
        
             counter = counter + 1 
             rospy.loginfo(counter)
             pub.publish(counter)
             rate.sleep()
             i=i+1
         
if __name__ == '__main__':
       try:
           talker()
       except rospy.ROSInterruptException:
          pass


