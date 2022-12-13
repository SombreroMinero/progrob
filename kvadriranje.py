import rospy
from std_msgs.msg import Int32

def callback(data):
    rospy.loginfo(data.data*data.data)

def kvadriranje():
    rospy.init_node('kvadrat_broja', anonymous=True)

    rospy.Subscriber('broj', 32, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    kvadriranje()
