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


    group.set_named_target('zero')
    rospy.loginfo("***start to zero!***")
    group.go()
    rospy.loginfo("***zero over!***")

    rospy.sleep(2)



    group.stop() # 停止所有剩余的运动
    group.clear_pose_targets()



    # 关闭moveit
    moveit_commander.roscpp_shutdown()


if __name__ == '__main__':

    try:
        move_arm_to_grasp_target()
    except rospy.ROSInterruptException:
        raise