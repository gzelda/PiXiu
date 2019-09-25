#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Revision $Id$

## Simple talker demo that listens to std_msgs/Strings published 
## to the 'chatter' topic

import rospy
import numpy as np
from queue import MyQueue
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan


class laserModule: 
    def __init__(self):
        self.poolMaxLen = 100
        self.queue = MyQueue(self.poolMaxLen)
        
    def getlastframe(self):
        size = self.queue.getSize() - 1
        return self.queue.getnumber(size)

    def callback(self, data):
        # URG-04LX-UG01 angle range 240
        # std_msgs/Header header
        # float32 angle_min -0.75 pi 
        # float32 angle_max 0.66666 pi
        # float32 angle_increment 360/1024
        # float32 time_increment
        # float32 scan_time
        # float32 range_min
        # float32 range_max
        # float32[] ranges
        # float32[] intensities
        # print(np.shape(data.ranges)) # <725> 45 of them are invalid
        #rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data)
        #print(np.shape(data.ranges[46:]))
        laserData = data.ranges[46:]
        if not self.queue.isFull():
            self.queue.inQueue(laserData)
        else:
            self.queue.outQueue()
            self.queue.inQueue(laserData)
        #print(self.queue.getSize())

    def listener(self):

        # In ROS, nodes are uniquely named. If two nodes with the same
        # name are launched, the previous one is kicked off. The
        # anonymous=True flag means that rospy will choose a unique
        # name for our 'listener' node so that multiple listeners can
        # run simultaneously.
        rospy.init_node('listener', anonymous=True)

        rospy.Subscriber('scan', LaserScan, self.callback)

        # spin() simply keeps python from exiting until this node is stopped
        rospy.spin()

if __name__ == '__main__':
    a = laserModule()
    a.listener()
