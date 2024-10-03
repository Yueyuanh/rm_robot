#!/usr/bin/env python3.8
# _*_ coding: utf-8 _*_

import sys
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

from sensor_msgs.msg import Joy
from scipy.spatial.transform import Rotation as R

def move_arm_to_grasp_target():

    # 初始化moveit_commander和rospy节点
    moveit_commander.roscpp_initialize(sys.argv)

    rospy.init_node('workflow', anonymous=True)
    # 初始化需要使用的对象

    group_name = "arm" # 替换为你的机械臂group名称

    group = moveit_commander.MoveGroupCommander(group_name)


    # 设置目标位置1
    target_pose = geometry_msgs.msg.Pose()
    target_pose.position.x = -0.1 # 请根据实际情况设置目标位置的x坐标
    target_pose.position.y = 0.2 # 请根据实际情况设置目标位置的y坐标
    target_pose.position.z = 0.5 # 请根据实际情况设置目标位置的z坐标


    roll = 0
    pitch = 0
    yaw = 0.0

    rotation=R.from_euler("xyz",[roll,pitch,yaw])
    quaternion=rotation.as_quat()

    # 设置目标姿态
    target_pose.orientation.x = quaternion[0] # 替换为目标姿态的x分量
    target_pose.orientation.y = quaternion[1] # 替换为目标姿态的y分量
    target_pose.orientation.z = quaternion[2] # 替换为目标姿态的z分量
    target_pose.orientation.w = quaternion[3] # 替换为目标姿态的w分量

    rospy.loginfo(target_pose)

    group.set_pose_target(target_pose)
    # 规划并执行路径
    plan = group.go()

    rospy.loginfo("***step-1 over!***")

    rospy.sleep(2)

 # 设置目标位置2
    target_pose = geometry_msgs.msg.Pose()
    target_pose.position.x = -0.1 # 请根据实际情况设置目标位置的x坐标
    target_pose.position.y = 0.2 # 请根据实际情况设置目标位置的y坐标
    target_pose.position.z = 0.5 # 请根据实际情况设置目标位置的z坐标


    roll = 0
    pitch = 0
    yaw = 0

    rotation=R.from_euler("xyz",[roll,pitch,yaw])
    quaternion=rotation.as_quat()

    # 设置目标姿态
    target_pose.orientation.x = quaternion[0] # 替换为目标姿态的x分量
    target_pose.orientation.y = quaternion[1] # 替换为目标姿态的y分量
    target_pose.orientation.z = quaternion[2] # 替换为目标姿态的z分量
    target_pose.orientation.w = quaternion[3] # 替换为目标姿态的w分量

    rospy.loginfo(target_pose)

    group.set_pose_target(target_pose)
    # 规划并执行路径
    plan = group.go()

    rospy.loginfo("***step-2 over!***")

    group.stop() # 停止所有剩余的运动
    group.clear_pose_targets()



    # 关闭moveit
    moveit_commander.roscpp_shutdown()


if __name__ == '__main__':

    try:
        move_arm_to_grasp_target()
    except rospy.ROSInterruptException:
        raise