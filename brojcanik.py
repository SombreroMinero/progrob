import rospy
from std_msgs.msg import Int32

def brojcanik():
    pub = rospy.Publisher('broj', Int32, queue_size=10)
    rospy.init_node('brojcanik', anonymous=True)
    rate = rospy.Rate(2) # 10hz
    i = -1
    while not rospy.is_shutdown():
        i += 1
        rospy.loginfo(i)
        pub.publish(i)
        rate.sleep()

if __name__ == '__main__':
    try:
        brojcanik()
    except rospy.ROSInterruptException:
        pass
