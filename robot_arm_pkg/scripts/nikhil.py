#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Header
from trajectory_msgs.msg import JointTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint

TARGET_POSITION = [2, 2, 2, 0]  # Adjust the target position as needed
TIME_TO_REACH_TARGET = 2.0  # Time (seconds) to reach the target position

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.position)
    pub = rospy.Publisher('arm_controller/command', JointTrajectory, queue_size=10)

    joints_traj = JointTrajectory()
    joints_traj.header = Header()
    joints_traj.header.stamp = rospy.Time.now()
    joints_traj.joint_names = ['base_joint', 'shoulder', 'elbow', 'wrist']
    
    # Use the received joint positions as the start position
    start_point = JointTrajectoryPoint()
    start_point.positions = [data.position[0], data.position[1], data.position[2], data.position[3]]
    start_point.time_from_start = rospy.Duration(0)
    joints_traj.points.append(start_point)

    # Set the target position
    target_point = JointTrajectoryPoint()
    target_point.positions = TARGET_POSITION
    target_point.time_from_start = rospy.Duration(TIME_TO_REACH_TARGET)
    joints_traj.points.append(target_point)

    pub.publish(joints_traj)
    rospy.loginfo("Trajectory published to move to the target position")

def listener():
    rospy.init_node('states', anonymous=True)
    rospy.Subscriber("joint_states", JointState, callback)

    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
