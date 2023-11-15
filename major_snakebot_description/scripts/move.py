#!/usr/bin/env python3
from __future__ import print_function 
import rospy 
import actionlib 
from control_msgs.msg import FollowJointTrajectoryAction, FollowJointTrajectoryGoal 
from std_msgs.msg import Float64 
from trajectory_msgs.msg import JointTrajectoryPoint 
import sys
import time
def move_robot_arm(joint_values):
 
  
  arm_client = actionlib.SimpleActionClient('arm_controller/follow_joint_trajectory', FollowJointTrajectoryAction)
 
 
  arm_client.wait_for_server() 
    
  arm_goal = FollowJointTrajectoryGoal()
 
 
  arm_goal.trajectory.joint_names = ['head_joint', 'joint1','joint2']
   
  # Create a trajectory point   
  point = JointTrajectoryPoint()
 
  # Store the desired joint values
  point.positions = joint_values
 
  # Set the time it should in seconds take to move the arm to the desired joint angles
  point.time_from_start = rospy.Duration(0.5)
 
  # Add the desired joint values to the goal
  arm_goal.trajectory.points.append(point)
 
  # Define timeout values
  exec_timeout = rospy.Duration(10)
  prmpt_timeout = rospy.Duration(5)
 
  # Send a goal to the ActionServer and wait for the server to finish performing the action
  arm_client.send_goal_and_wait(arm_goal, exec_timeout, prmpt_timeout)
 
 
if __name__ == '__main__':
  """
  Main method.
  """
  try:
    # Initialize a rospy node so that the SimpleActionClient can
    # publish and subscribe over ROS.
    rospy.init_node('send_goal_to_arm_py')
    
    move_robot_arm([-1.16, -1.08, 0.37])

 
    # Move the joints of the robot arm to the desired angles in radians

    
  except rospy.ROSInterruptException:
    print("Program interrupted before completion.", file=sys.stderr)