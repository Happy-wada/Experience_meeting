#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import rospy
from geometry_msgs.msg import Twist

def talker():
    rospy.init_node("teleop")
    pub = rospy.Publisher('cmd_vel_mux/input/teleop', Twist, queue_size=1)
    while not rospy.is_shutdown():
        vel = Twist()
        direction = raw_input ("push_keyboard:,,,")
        #前に進む
        if "" in direction:
            vel.linear.x = +
        #後ろに進む
        if "" in direction:
            vel.linear.x = -
        #右に曲がる
        if "" in direction:
            vel.angular.z = +
        #左に曲がる
        if "" in direction:
            vel.angular.z = -

        pub.publish(vel)

if __name__ == '__main__':
    talker()
class FeatureFromRecog():
    def __init__(self):
        # Service
        #self.height_srv = rospy.ServiceProxy('/person_feature/height_estimation', SetFloat)
        #服
        self.cloth_srv  = rospy.ServiceProxy('/person_feature/cloth_color', SetStr)
        #ズボン
        self.pants_srv = rospy.ServiceProxy('/person_feature/pants_color', SetStr)
        #顔
        self.skin_srv = rospy.ServiceProxy('/person_feature/skin_color', SetStr)
        #髪
        #self.hair_srv = rospy.ServiceProxy('/person_feature/hair_color', SetStr)
        # Value
        self.height      = "null"
        self.cloth_color = "null"
        self.skin_color = "null"
        self.pants_color = "null"
        #selk.hair_color = "null"
        self.mask ="null"
        #Topic
        #self.head_pub = rospy.Publisher('/servo/head', Float64, queue_size = 1)
        #self.bc = BaseControl()
    
    def getPansColor(self):
        self.pants_color = "null"
        self.pants_color = self.pants_srv().result
        
        if self.pants_color == '':
            return "none"

        else:
            return self.pants_color


    def getSkinColor(self):
        self.skin_color = "null"
        self.skin_color =  self.skin_srv().result
        
        if self.skin_color == '':
            return "none"
    #    else if self.skin_color == 'white':
    #        self.mask = "mask"
    #        return "none"
        
        else:
            return self.skin_color
    
    def getMask(self):
        self.mask = "null"
        self.mask = self.skin_srv().result

        if self.skin_color == 'white':
            self.mask = "wearing a mask"
            return "none"
        else:
            self.mask = "not wearing a mask"


    def getHairColo(self):
        self.hair_color = "null"
        self.hair_color = self.hair_srv().result
        if self.hair_color == '':
            return "none"
        else:
            return self.hair_color


    #def getHeight(self):
    #    self.head_pub.publish(0)
    #    self.base_control.translateDist(-0.5,0.2)
    #    
    #     height = SetFloat()
    #    height = self.height_srv()
    #    
    #    if height.data == -1:
    #        return False
    #    else:
    #        self.height = str(round(height.data))
    #        return self.height

    def getClothColor(self):
        self.cloth_color = "null"
        self.cloth_color = self.cloth_srv().result
        if self.cloth_color == '':
            return "none"
        else:
            return self.cloth_color
 def __init__(self):
        smach.State.__init__(self, outcomes = ['approach_finish'],
                             input_keys = ['g_count_in'])
        # Service
        self.gen_coord_srv = rospy.ServiceProxy('/human_coord_generator', SimpleTrg)
        self.ap_srv = rospy.ServiceProxy('/approach_person_server', StrTrg)
        self.navi_srv = rospy.ServiceProxy('navi_location_server', NaviLocation)
        self.navi_coord_srv = rospy.ServiceProxy('navi_coord_server', NaviCoord)
        # Topic
        self.head_pub = rospy.Publisher('/servo/head', Float64, queue_size = 1)
        self.bc = BaseControl()

    def execute(self, userdata):
        rospy.loginfo("Executing state: APPROACH_GUEST")
        # return 'approach_finish'
        guest_num = userdata.g_count_in
        guest_name = "human_" + str(guest_num)
        human_loc = rospy.get_param('/tmp_human_location')
        self.bc.rotateAngle(100,0.2)
        # tts_srv("Move to guest")
        wave_srv("/fmm/move_guest")
        
        rospy.sleep(0.5)
        self.navi_srv('fmm')

        if guest_num == 0:
            self.head_pub.publish(0)
            rospy.sleep(1.0)
            result = self.gen_coord_srv().result
            print(result)
            result = self.ap_srv(data = guest_name)    
        elif guest_num == 1:
            self.head_pub.publish(0)
            self.bc.rotateAngle(-55, 0.2)
            rospy.sleep(5.0)
            result = self.gen_coord_srv().result
            print(result)
            #self.bc.rotateAngle(-330,0.2)
            rospy.sleep(1.0)
            result = self.ap_srv(data = guest_name)
            # self.bc.rotateAngle(-10)
            # for i in range(3):
                # result = self.gen_coord_srv().result
                # if result:
                    # break
                # else:
                    # break
                    # self.bc.rotateAngle(-10)
        elif guest_num == 2:
            self.head_pub.publish(0)
            self.bc.rotateAngle(-50, 0.2)
            rospy.sleep(5.0)
            result = self.gen_coord_srv().result
            self.navi_coord_srv (loc_coord = human_1)

        else:
            pass
        #result = self.ap_srv(data = guest_name)
        #print(result)
        
        self.head_pub.publish(0)
         self.navi_coord_srv 
        if result:
            return 'approach_finish'
         
        else:
            return 'approach_finish'
