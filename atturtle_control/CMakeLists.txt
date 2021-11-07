cmake_minimum_required(VERSION 3.5)
project(atturtle_description)

find_package(catkin REQUIRED)

catkin_package()

install(
  DIRECTORY launch scripts
  DESTINATION share/${PROJECT_NAME}
)
