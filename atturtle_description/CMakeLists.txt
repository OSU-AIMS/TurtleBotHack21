cmake_minimum_required(VERSION 3.5)
project(atturtle_description)

find_package(catkin REQUIRED)

catkin_package()

install(
  DIRECTORY config launch meshes test urdf
  DESTINATION share/${PROJECT_NAME}
)
