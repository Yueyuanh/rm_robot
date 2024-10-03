#!/usr/bin/env python3.8
# _*_ coding: utf-8 _*_

import sys
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

import pygame
from scipy.spatial.transform import Rotation as R

axis_id = {
    "LX": 0,  # Left stick axis x
    "LY": 1,  # Left stick axis y
    "RX": 2,  # Right stick axis x
    "RY": 3,  # Right stick axis y
}

button_id = {
    "Y": 0,
    "B": 1,
    "A": 2,
    "X": 3,
    "LB": 4,  #L1
    "RB": 5,  #R1
    "LT": 6,  #L2
    "RT": 7,  #R2
    "SELECT": 8,
    "START": 9,
}

roll =0
pitch = 0
yaw = 0



pygame.init()
pygame.joystick.init()
joystick_count=pygame.joystick.get_count()
if(joystick_count == 0):
    print("没有手柄")
    exit()

joystick=pygame.joystick.Joystick(0)
joystick.init()


# 初始化moveit_commander和rospy节点
moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('workflow', anonymous=True)
# 初始化需要使用的对象
group_name = "arm" # 替换为你的机械臂group名称
group = moveit_commander.MoveGroupCommander(group_name)
# rospy.INFO("init")
print("init")
#机械臂初始化
# group.set_named_target('zero')
# group.go()

scale=0.1



def joystick_control():
        for event in pygame.event.get():
            if event.type == pygame.JOYAXISMOTION:
                # 获取左摇杆数据 (轴 0 和轴 1 控制 x 和 y 方向)
                left_stick_x = joystick.get_axis(0)
                left_stick_y = joystick.get_axis(1)

                # 获取右摇杆数据 (轴 3 控制 z 轴旋转)
                right_stick_x = joystick.get_axis(3)

                print(joystick.get_axis(axis_id["LX"]))




def move_arm_to_grasp_target():

    print("start")
    # 设置目标位置
    target_pose = geometry_msgs.msg.Pose()
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.JOYAXISMOTION:
            # if(joystick.get_button(button_id["LB"])==0):
            target_pose.position.x += float(joystick.get_axis(axis_id["LX"])*scale)# 
            target_pose.position.y += float(joystick.get_axis(axis_id["LY"])*scale)# 
            target_pose.position.z += float(joystick.get_axis(axis_id["RX"])*scale) # 

            print(joystick.get_axis(0))
            print(joystick.get_axis(axis_id["LY"]))
    # else:
    #     roll  +=joystick.get_axis(axis_id["LX"])*scale
    #     pitch +=joystick.get_axis(axis_id["LY"])*scale
    #     yaw   +=joystick.get_axis(axis_id["RX"])*scale
         
    

    rotation=R.from_euler("xyz",[roll,pitch,yaw])
    quaternion=rotation.as_quat()
    # 设置目标姿态
    target_pose.orientation.x = quaternion[0] # 替换为目标姿态的x分量
    target_pose.orientation.y = quaternion[1] # 替换为目标姿态的y分量
    target_pose.orientation.z = quaternion[2] # 替换为目标姿态的z分量
    target_pose.orientation.w = quaternion[3] # 替换为目标姿态的w分量

    # rospy.loginfo(target_pose)

    # group.set_pose_target(target_pose)
    # # 规划并执行路径
    # group.go()


    # group.stop() # 停止所有剩余的运动
    # group.clear_pose_targets()

    # # 关闭moveit
    # moveit_commander.roscpp_shutdown()


def main():
    while True:
          move_arm_to_grasp_target()
        #   joystick_control()
    # group.stop() # 停止所有剩余的运动
    # group.clear_pose_targets()

    # # # 关闭moveit
    # moveit_commander.roscpp_shutdown()


if __name__ == '__main__':

    try:
        # move_arm_to_grasp_target()
        main()
    except rospy.ROSInterruptException:
        raise