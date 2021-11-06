cmake_minimum_required(VERSION 3.5)
project(atturtle_vision)

find_package(catkin REQUIRED)

catkin_package()

install(DIRECTORY launch test scripts
    DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
    )