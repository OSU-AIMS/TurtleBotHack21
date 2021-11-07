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






class EnvisionTarget():


    def __init__(self, pub_targetImage):
        """Initialize
            Setup Publishers as class variables.
        """

        # Setup connection to Publisher for Output Images
        self.pub_targetImage = pub_targetImage  


        # Tools
        self.bridge = CvBridge()




    def runner(self, data):

        """
        Callback function for image subscriber, every frame gets scanned for board and publishes to board_center topic
        (for robot movement) and board tile centers (for game state updates)
        :param camera_data: Camera data input from subscriber
        """
        

        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, desired_encoding = 'passthrough')

            scale_percent = 50 # percent of original size
            width = int(cv_image.shape[1] * scale_percent / 100)
            height = int(cv_image.shape[0] * scale_percent / 100)
            dim = (width, height)
  
            # resize image
            cv_image = cv2.resize(cv_image, dim, interpolation = cv2.INTER_AREA)

            hog = cv2.HOGDescriptor()
            hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


            print('scanning...')
            (regions, _) = hog.detectMultiScale(cv_image,
                                                winStride=(4, 4),
                                                padding=(8, 8),
                                                scale=1.02)

            # Drawing the regions in the Image
            for (x, y, w, h) in regions:
                cv2.rectangle(cv_image, (x, y),
                              (x + w, y + h),
                              (255, 0, 0), 2)
                print('person detected :)')


            # Drawing the regions in the Image
            #for (x, y, w, h) in LB:
            #    cv2.rectangle(cv_image, (x, y),
            #                  (x + w, y + h),
            #                  (0, 0, 0), 2)

            # Showing the output Image
            #cv2.imshow("Image", color)
            out_image = self.bridge.cv2_to_imgmsg(cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB), "bgr8")
            self.pub_targetImage.publish(out_image)



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


    # Setup ROS Publishers
    pub_target = rospy.Publisher("/processed_vision/target_image", Image, queue_size=15)


    # Setup Class
    visionClass = EnvisionTarget(pub_target)


    # Setup Listeners
    image_sub = rospy.Subscriber("/color/image_raw", Image, visionClass.runner)


    # Auto-Run until launch file is shutdown
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
    cv2.destroyAllWindows()




if __name__ == '__main__':
    main()
