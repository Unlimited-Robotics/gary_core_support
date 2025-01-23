
from PyQt5.QtCore import QObject, QThread, pyqtSignal
import can
from motor_class import motor_class


class all_motor_class(QObject):

    def __init__(self):
        super().__init__()
        self.Right_arm_mot_1 = motor_class("right_shoulder_rail_joint  ", 0x149, 1)
        self.Right_arm_mot_2 = motor_class("right_shoulder_FR_joint  ", 0x148, 1)
        self.Right_arm_mot_3 = motor_class("right_shoulder_RL_joint  ", 0x147, 1)
        self.Right_arm_mot_4 = motor_class("right_bicep_twist_joint    ", 0x146, 1)
        self.Right_arm_mot_5 = motor_class("right_bicep_FR_joint      ", 0x145, 1)
        self.Right_arm_mot_6 = motor_class("right_elbow_twist_joint   ", 0x144, 1)
        self.Right_arm_mot_7 = motor_class("right_elbow_FR_joint      ", 0x143, 1)
        self.Right_arm_mot_8 = motor_class("right_wrist_joint             ", 0x142, 1)
        self.Right_arm_mot_9 = motor_class("right_gripper                  ", 0x141, 1)
        self.Right_linear = self.Right_arm_mot_1

        self.Left_arm_mot_1 = motor_class("left_shoulder_rail_joint  ", 0x153, 1)
        self.Left_arm_mot_2 = motor_class("left_shoulder_FR_joint  ", 0x152, 1)
        self.Left_arm_mot_3 = motor_class("left_shoulder_RL_joint  ", 0x151, 1)
        self.Left_arm_mot_4 = motor_class("left_bicep_twist_joint    ", 0x150, 1)
        self.Left_arm_mot_5 = motor_class("left_bicep_FR_joint      ", 0x14F, 1)
        self.Left_arm_mot_6 = motor_class("left_elbow_twist_joint   ", 0x14E, 1)
        self.Left_arm_mot_7 = motor_class("left_elbow_FR_joint      ", 0x14D, 1)
        self.Left_arm_mot_8 = motor_class("left_wrist_joint             ", 0x14C, 1)
        self.Left_arm_mot_9 = motor_class("left_gripper                  ", 0x14B, 1)
        self.Left_linear = self.Left_arm_mot_1

        self.wheel_mot_1 = motor_class("wheel_FL_joint", 0x142, 0)
        self.wheel_mot_2 = motor_class("wheel_RL_joint", 0x141, 0) #51 ad f9 ff
        self.wheel_mot_3 = motor_class("wheel_FR_joint", 0x143, 0) #af 52 06 00
        self.wheel_mot_4 = motor_class("wheel_RR_joint", 0x144, 0)

        self.wheel_cart = motor_class("cart motor", 0x146, 0)

        self.linears_list = [self.Right_linear, self.Left_linear]

        self.step_motors_list = [self.Right_linear, self.Left_linear, self.wheel_cart]

        self.wheels_list = [self.wheel_mot_1,
                            self.wheel_mot_2,
                            self.wheel_mot_3,
                            self.wheel_mot_4]

        self.Right_arm_list = [self.Right_arm_mot_1,
                               self.Right_arm_mot_2,
                               self.Right_arm_mot_3,
                               self.Right_arm_mot_4,
                               self.Right_arm_mot_5,
                               self.Right_arm_mot_6,
                               self.Right_arm_mot_7,
                               self.Right_arm_mot_8,
                               self.Right_arm_mot_9]

        self.Left_arm_list = [self.Left_arm_mot_1,
                              self.Left_arm_mot_2,
                              self.Left_arm_mot_3,
                              self.Left_arm_mot_4,
                              self.Left_arm_mot_5,
                              self.Left_arm_mot_6,
                              self.Left_arm_mot_7,
                              self.Left_arm_mot_8,
                              self.Left_arm_mot_9]


