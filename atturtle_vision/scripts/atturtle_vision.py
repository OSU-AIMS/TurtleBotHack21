#!/usr/bin/env python

#
#
#
#
#
#
#
#
#






## Imports
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError




def runner(data):
    """
    Callback function for image subscriber, every frame gets scanned for board and publishes to board_center topic
    (for robot movement) and board tile centers (for game state updates)
    :param camera_data: Camera data input from subscriber
    """
    

    try:

        # YOUR CODE HERE!



    except rospy.ROSInterruptException:
        exit()
    except KeyboardInterrupt:
        exit()








def main():
    """
    Main Runner.
    This script should only be launched via a launch script or when the Camera Node is already open.
    """

    # Setup Node
    rospy.init_node('vision', anonymous=False)
    rospy.loginfo(">> Vision Processor Node Successfully Created")


    # Setup Listeners
    image_sub = rospy.Subscriber("/camera/color/image_raw", Image, runner)


    # Auto-Run until launch file is shutdown
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
    cv2.destroyAllWindows()




if __name__ == '__main__':
    main()
