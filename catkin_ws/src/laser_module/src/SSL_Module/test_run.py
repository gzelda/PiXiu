# -*- coding: utf-8 -*-
"""
@Brief: This is a test run script
@Version: Test Run 1.0.0
@author: Wang Yunkai
"""

import numpy as np
from visionmodule import VisionModule
from actionmodule import ActionModule

MULTI_GROUP = '224.5.23.2'
VISION_PORT = 10005
ACTION_IP = '10.12.225.78'
ACTION_PORT = 1030
ROBOT_ID = 6

def angle_normalize(angle):
        if angle > np.pi:
            angle -= 2*np.pi
        elif angle < -np.pi:
            angle += 2*np.pi
        return angle
    
def target_policy(theta):
    if abs(theta) < 5./180 * np.pi:
        vel = 2
    elif abs(theta) < 10./180 * np.pi:
        vel = 1.0
    elif abs(theta) < 30./180 * np.pi:
        vel = 0.5
    else:
        vel = 0
    return [vel, -theta]

def run_loop(vision, sender):
    action = [0, 0]
    while True:
        for _ in range(8):
            vision.get_info(ROBOT_ID)

        #robot2ball_dist = np.sqrt((vision.robot_info[0]-vision.ball_info[0])**2 + (vision.robot_info[1]-vision.ball_info[1])**2)
        robot2ball_theta = np.arctan2((vision.ball_info[1] - vision.robot_info[1]), (vision.ball_info[0] - vision.robot_info[0]))
        delt_theta = robot2ball_theta - vision.robot_info[2]
        delt_theta = angle_normalize(delt_theta)
        
        action = target_policy(delt_theta)
        action[0] = np.clip(action[0], -3, 3)
        action[1] = np.clip(action[1], -2, 2)
        #print(robot2ball_theta/np.pi*180, vision.robot_info[2]/np.pi*180, delt_theta/np.pi*180)
        print(action)
        
        sender.send_action(ROBOT_ID, vx=action[0], vy=0, w=action[1])
    
    
if __name__ == '__main__':
    vision = VisionModule(MULTI_GROUP, VISION_PORT)
    sender = ActionModule(ACTION_IP, ACTION_PORT)
    run_loop(vision, sender)
    
