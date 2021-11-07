#!/usr/bin/env python

#
# Control Interface from ROS to Arduino
#
# ##################################### #
#
# 1. command recieved on left or right motor topic
# 2. send serial message to arduino
# 3. recieve serial message from arduino
# 4. publish encoder positions from recieved message to odom topic.
#
#


## Imports
import rospy
from std_msgs.msg import Int32

import serial
from time import sleep



class ArduinoControlInterface():
    """
        control

    """


    def __init__(serialObj, pub_leftOdom, pub_rightOdom):
        self.serialObj = serialObj
        self.pub_leftOdom = pub_leftOdom
        self.pub_rightOdom = pub_rightOdom


    def cmdRunner(self, data, whichmotor):
        """
        Callback function. Whenever command recieved on ROS topic, push command along Serial Interface.
        (for robot movement) and board tile centers (for game state updates)
        :param camera_data: Camera data input from subscriber
        """
        
        try:


            # Build Command Message
            command = "M" + whichmotor + data
            print(command)



            # Send Command Message





            # Recieve Encoder Message
            


            # Convert from encoder to Odom travel




            # Publish encoder to topic
            # self.pub_leftOdom = 
            # self.pub_rightOdom = 






        except rospy.ROSInterruptException:
            exit()
        except KeyboardInterrupt:
            exit()





def main():
    """
    Main Script
    """


    # Setup Serial Connection to Arduino MicroController
    # portAddress = rospy.
    portAddress = '/dev/ttyACM0'
    ser = serial.Serial(port=portAddress, baudrate=115200, write_timeout=0.1)
    rospy.loginfo(ser.name)


    # Setup Node
    rospy.init_node('ArduinoController/sendCommand', anonymous=False)
    rospy.loginfo(">> ArduinoController: Node Created for Command Sender")


    # Setup Publisher
    pub_leftOdom = rospy.Publisher("/atturtle/leftwheel/odom", Int32, queue_size=15)
    pub_rightOdom = rospy.Publisher("/atturtle/rightwheel/odom", Int32, queue_size=15)


    # Setup Class
    ctrl = ArduinoControlInterface(ser, pub_leftOdom, pub_rightOdom)


    # Setup Listeners
    sub_leftwheel = rospy.Subscriber("/atturtle/leftwheel/command", Int32, ctrl.cmdRunner('L'))
    sub_rightwheel = rospy.Subscriber("/atturtle/rightwheel/command", Int32, ctrl.cmdRunner('R'))


    # Auto-Run until launch file is shutdown
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
    cv2.destroyAllWindows()



if __name__ == '__main__':
    main()
