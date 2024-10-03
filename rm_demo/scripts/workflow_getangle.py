#!/usr/bin/env python3.8
# _*_ coding: utf-8 _*_

import sys
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

from sensor_msgs.msg import Joy
from scipy.spatial.transform import Rotation as R

pi=3.1415926
pi2=pi/2



# 初始化moveit_commander和rospy节点
moveit_commander.roscpp_initialize(sys.argv)

rospy.init_node('workflow', anonymous=True)
# 初始化需要使用的对象

group_name = "arm" # 替换为你的机械臂group名称

group = moveit_commander.MoveGroupCommander(group_name)

def return_current_angle():

    current_pose = group.get_current_pose()
    print(current_pose)
    # rotation_q=R.from_quat(current_pose.orientation)
    # euler_angle=rotation_q.as_euler("xyz",degrees=False)
    # rospy.loginfo(euler_angle)



if __name__ == '__main__':

    try:
        while True:
            return_current_angle()
    except rospy.ROSInterruptException:
        raise