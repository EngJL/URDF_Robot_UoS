# URDF_Robot_UoS
There are two main robot URDF files located in this repository, one called 8track.URDF and model.URDF.
They are launched by 8track.launch and Gazebo.launch respectively.
The model.urdf has just the robot with the sensors implemented and the 8track.urdf has the same but with the 8track environment included.
In the URDF files the pathways for the collision and visual files may have to be changed dependent on usage, but as long as the files are within the package, there shouldn't be a problem.
rviz.rviz can be loaded into rviz after running the robot in Gazebo to automatically detect the sensor data produced.
A control_node.py file is written for possible implementation of the movement of the robot, unless a better workaround is found.
