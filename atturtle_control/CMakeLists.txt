cmake_minimum_required(VERSION 3.5)
project(atturtle_control)

find_package(catkin REQUIRED
  COMPONENTS roscpp rospy std_msgs nav_msgs)

catkin_package()
include_directories(${catkin_INCLUDE_DIRS})


install(
  DIRECTORY launch scripts src
  DESTINATION share/${PROJECT_NAME}
)

add_executable(odomPublisher src/odom_publisher.cpp)

