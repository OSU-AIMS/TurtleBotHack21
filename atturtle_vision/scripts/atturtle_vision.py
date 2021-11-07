#!/usr/bin/env python3

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
import cv2
#import imutils



def runner(data):

    """
    Callback function for image subscriber, every frame gets scanned for board and publishes to board_center topic
    (for robot movement) and board tile centers (for game state updates)
    :param camera_data: Camera data input from subscriber
    """
    

    try:
        pub = rospy.Publisher("/color/image_raw", Image, queue_size=10)
        bridge = CvBridge()
        cv_image = bridge.imgmsg_to_cv2(data, desired_encoding = 'passthrough')
        #cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        #LBDet = cv2.CascadeClassifier('haarcascade_lowerbody.xml')

        hog = cv2.HOGDescriptor()
        hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

        while(True):

            #color = imutils.resize(cv_image,
            #                       width=min(400, color.shape[1]))

            #color = cv2.cvtColor(color, cv2.COLOR_BGR2GRAY)
            #LB = LBDet.detectMultiScale(cv_image,1.1,4)
            #UB = UPDet.detectMultiScale(color,1.05,5)
            #FB = FBDet.detectMultiScale(color,1.1,4)
            (regions, _) = hog.detectMultiScale(cv_image,
                                                winStride=(4, 4),
                                                padding=(4, 4),
                                                scale=1.05)

            # Drawing the regions in the Image
            for (x, y, w, h) in regions:
                cv2.rectangle(cv_image, (x, y),
                              (x + w, y + h),
                              (255, 0, 0), 2)
                print(x)
                print(y)


            # Drawing the regions in the Image
            #for (x, y, w, h) in LB:
            #    cv2.rectangle(cv_image, (x, y),
            #                  (x + w, y + h),
            #                  (0, 0, 0), 2)

            # Showing the output Image
            #cv2.imshow("Image", color)
            out_image = bridge.cv2_to_imgmsg(cv_image, "bgr8")
            pub.publish(out_image)










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
    image_sub = rospy.Subscriber("/color/image_raw", Image, runner)


    # Auto-Run until launch file is shutdown
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
    cv2.destroyAllWindows()




if __name__ == '__main__':
    main()
