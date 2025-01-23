from PyQt5.QtCore import QObject, QThread, pyqtSignal
from PyQt5.QtCore import QObject, QThread, pyqtSignal
import can
import sys
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow
import can
import ctypes
import os
import struct
import can.interfaces.pcan
from sys import platform
import datetime
import time
from PyQt5.QtCore import QObject, QThread, pyqtSignal
import struct
import time
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow
import can
import ctypes
import os
import struct
import can.interfaces.pcan
from sys import platform
import datetime
import time
from PyQt5.QtCore import QObject, QThread, pyqtSignal
import struct
from PyQt5.QtCore import QObject, QThread, pyqtSignal
import time
from PyQt5.QtCore import QObject, QThread, pyqtSignal
import can
from PyQt5.QtCore import QObject, QThread, pyqtSignal
import struct
import time
from sys import platform
from PyQt5.QtCore import QObject, QThread, pyqtSignal
import struct
import time
import datetime
from PyQt5.QtCore import QObject, QThread, pyqtSignal
import struct
import time
from PyQt5.QtCore import QObject, QThread, pyqtSignal
import struct
import time
from sys import platform
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from PyQt5 import QtWidgets
from qt_design1 import Ui_qt_designer_save1
# Start of all_data_entries.py



class all_data_entries_class(QObject):

    def __init__(self, update_label, ui):
        super().__init__()
        self.label_bat_percentage = data_entry(ui.bat_percentage, "battery charge percentage [%]", 'decimal', 0x104, 0x22, update_label, 1, 100,ui.bat_percentage_passfail)
        self.label_bat_current = data_entry(ui.bat_current, "current", '2s', 0x104, 0x20, update_label, -8000, 8000, ui.bat_current_passfail)
        self.label_bat_voltage = data_entry(ui.bat_voltage, "voltage", 'decimal', 0x104, 0x1F, update_label, 35000, 50000, ui.bat_voltage_passfail)
        self.label_bat_error_count = data_entry(ui.bat_error_count, "error count (0-128)", 'decimal', 0x104, 0x5B, update_label, 0, 4, ui.bat_error_count_passfail)
        self.label_bat_temp = data_entry(ui.bat_temp, "temperature", 'decimal', 0x104, 0x1E, update_label, 15, 40, ui.bat_temp_passfail)
        self.label_bat_cell1 = data_entry(ui.bat_cell1, "cell1 voltage", 'decimal', 0x104, 0x37, update_label, 3200, 4100, ui.bat_cell1_passfail)
        self.label_bat_cell2 = data_entry(ui.bat_cell2, "cell2 voltage", 'decimal', 0x104, 0x36, update_label, 3200, 4100, ui.bat_cell2_passfail)
        self.label_bat_cell3 = data_entry(ui.bat_cell3, "cell3 voltage", 'decimal', 0x104, 0x35, update_label, 3200, 4100, ui.bat_cell3_passfail)
        self.label_bat_cell4 = data_entry(ui.bat_cell4, "cell4 voltage", 'decimal', 0x104, 0x34, update_label, 3200, 4100, ui.bat_cell4_passfail)
        self.label_bat_cell5 = data_entry(ui.bat_cell5, "cell5 voltage", 'decimal', 0x104, 0x33, update_label, 3200, 4100, ui.bat_cell5_passfail)
        self.label_bat_cell6 = data_entry(ui.bat_cell6, "cell6 voltage", 'decimal', 0x104, 0x32, update_label, 3200, 4100, ui.bat_cell6_passfail)
        self.label_bat_cell7 = data_entry(ui.bat_cell7, "cell7 voltage", 'decimal', 0x104, 0x31, update_label, 3200, 4100, ui.bat_cell7_passfail)
        self.label_bat_cell8 = data_entry(ui.bat_cell8, "cell8 voltage", 'decimal', 0x104, 0x30, update_label, 3200, 4100, ui.bat_cell8_passfail)
        self.label_bat_cell9 = data_entry(ui.bat_cell9, "cell9 voltage", 'decimal', 0x104, 0x2F, update_label, 3200, 4100, ui.bat_cell9_passfail)
        self.label_bat_cell10 = data_entry(ui.bat_cell10, "cell10 voltage", 'decimal', 0x104, 0x2E, update_label, 3200, 4100, ui.bat_cell10_passfail)
        self.label_bat_cell11 = data_entry(ui.bat_cell11, "cell11 voltage", 'decimal', 0x104, 0x2D, update_label, 3200, 4100, ui.bat_cell11_passfail)
        self.label_bat_cell12 = data_entry(ui.bat_cell12, "cell12 voltage", 'decimal', 0x104, 0x2C, update_label, 3200, 4100, ui.bat_cell12_passfail)
        self.label_bat_state_health = data_entry(ui.bat_state_health, "state of health", 'decimal', 0x104, 0x38, update_label, 60, 100,ui.bat_state_health_passfail)
        self.label_ver_top_board = data_entry(ui.ver_top_board, "top board version", 'ascii', 0x103, 0x60, update_label, 0, 0, ui.empty_versions_passfail)
        self.label_ver_top_code = data_entry(ui.ver_top_code, "top code version", 'ascii', 0x103, 0X00, update_label, 0, 0, ui.empty_versions_passfail)
        self.label_ver_bot_board = data_entry(ui.ver_bot_board, "bottom board version", 'ascii', 0x104, 0x61, update_label, 0, 0, ui.empty_versions_passfail)
        self.label_ver_bot_code = data_entry(ui.ver_bot_code, "bottom code version", 'ascii', 0x104, 0X00, update_label, 0, 0, ui.empty_versions_passfail)
        self.label_ver_nic_code = data_entry(ui.ver_nic_code, "nicla sense me code version", 'ascii', 0x102, 0X00, update_label, 0, 0, ui.empty_versions_passfail)
        self.label_ver_nic_board = data_entry(ui.ver_nic_board, "nicla sense me board version", 'ascii', 0x102, 0x62, update_label, 0, 0, ui.empty_versions_passfail)
        self.label_states_buttons = data_entry(ui.states_buttons, "button states", 'binary', 0x104, 0x52, update_label, 0, 0, ui.states_passfail_empty)
        self.label_states_chest = data_entry(ui.states_chest, "chest button pressed time", 'float', 0x103, 0x1B, update_label, 0, 500, ui.states_chest_passfail)
        self.label_states_relay = data_entry(ui.states_relay, "charging relay state (ON = connected)", 'onoff', 0x104, 0x57, update_label, 0, 0, ui.states_passfail_empty)
        self.label_states_arms_61 = data_entry(ui.states_arms_61, "arms 6.1v power", 'onoff', 0x103, 0x59, update_label, 0, 0, ui.states_passfail_empty)
        self.label_states_wheel_61 = data_entry(ui.states_wheel_61, "wheels 6.1v power", 'onoff', 0x104, 0x58, update_label, 0, 0, ui.states_passfail_empty)

        self.label_nicla_pitch = data_entry(ui.nicla_pitch, "pitch", 'float', 0x102, 0x0D, update_label, -3.2, 3.2, ui.nicla_pitch_passfail)
        self.label_nicla_roll = data_entry(ui.nicla_roll, "roll", 'float', 0x102, 0x0E, update_label, -3.2, 3.2, ui.nicla_roll_passfail)
        self.label_nicla_heading = data_entry(ui.nicla_heading, "heading", 'float', 0x102, 0x0F, update_label, 0, 6.2, ui.nicla_heading_passfail)
        self.label_nicla_barometer = data_entry(ui.nicla_barometer, "barometer", 'float', 0x102, 0x5A, update_label, 600, 2000, ui.nicla_barometer_passfail)

        self.label_srftemp_temp1 = data_entry(ui.srftemp_temp1, "temperature sensor 1", 'float', 0x103, 0x10, update_label, 15, 40, ui.srftemp_temp1_passfail)
        self.label_srftemp_temp2 = data_entry(ui.srftemp_temp2, "temperature sensor 2", 'float', 0x103, 0x11, update_label, 15, 40, ui.srftemp_temp2_passfail)
        self.label_srftemp_temp3 = data_entry(ui.srftemp_temp3, "temperature sensor 3", 'float', 0x103, 0x12, update_label, 15, 40, ui.srftemp_temp3_passfail)
        self.label_srftemp_temp4 = data_entry(ui.srftemp_temp4, "temperature sensor 4", 'float', 0x103, 0x13, update_label, 15, 40, ui.srftemp_temp4_passfail)
        self.label_srftemp_srf1 = data_entry(ui.srftemp_srf1, "srf 1", 'float', 0x104, 0x16, update_label, 1, 600, ui.srftemp_srf1_passfail)
        self.label_srftemp_srf2 = data_entry(ui.srftemp_srf2, "srf 2", 'float', 0x104, 0x19, update_label, 1, 600, ui.srftemp_srf2_passfail)

        self.data_entries = {
            0: [[]],
            1: [
                [
                    self.label_bat_percentage,
                    self.label_bat_current,
                    self.label_bat_voltage,
                    self.label_bat_temp,
                    self.label_bat_error_count
                ],
                [
                    self.label_bat_cell1,
                    self.label_bat_cell2,
                    self.label_bat_cell3,
                    self.label_bat_cell4,
                    self.label_bat_cell5,
                    self.label_bat_cell6,
                    self.label_bat_cell7,
                    self.label_bat_cell8,
                    self.label_bat_cell9,
                    self.label_bat_cell10,
                    self.label_bat_cell11,
                    self.label_bat_cell12,
                    self.label_bat_state_health
                ],
                [
                    self.label_ver_top_board,
                    self.label_ver_top_code,
                    self.label_ver_bot_board,
                    self.label_ver_bot_code,
                    self.label_ver_nic_board,
                    self.label_ver_nic_code
                ],
                [
                    self.label_states_buttons,
                    self.label_states_chest,
                    self.label_states_relay,
                    self.label_states_arms_61,
                    self.label_states_wheel_61
                ],
                [
                    self.label_nicla_pitch,
                    self.label_nicla_roll,
                    self.label_nicla_heading,
                    self.label_nicla_barometer
                ],
                [
                    self.label_srftemp_temp1,
                    self.label_srftemp_temp2,
                    self.label_srftemp_temp3,
                    self.label_srftemp_temp4,
                    self.label_srftemp_srf1,
                    self.label_srftemp_srf2
                ]
            ],
            2: [[]],
        }


# End of all_data_entries.py

# Start of all_motors_class_def.py



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




# End of all_motors_class_def.py

# Start of bad_can_page_variables.py





class bad_can_variables_class(QObject):

    def __init__(self, general_messages_label, can0_label, can0_button, can1_label, can1_button, canbus_good_label, continue_button, main_widget):
        super().__init__()
        self.general_messages_label = general_messages_label
        self.can0_label = can0_label
        self.can0_button = can0_button
        self.can1_label = can1_label
        self.can1_button = can1_button
        self.canbus_good_label = canbus_good_label
        self.continue_button = continue_button
        self.main_widget = main_widget





# End of bad_can_page_variables.py

# Start of bottom_test_class.py


class bottom_test_data(QObject):
    update_label_signal = pyqtSignal(object, str)  # Signal to send label and text
    update_button_signal = pyqtSignal(object, int)  # Signal to send label and text

    def __init__(self, srf1, srf2, battery_pct, battery_voltage, battery_error, data_label, passfail_label, button_object, general_functions):

        super().__init__()
        self.update_button_signal.connect(general_functions[0])
        self.button_object = button_object
        self.data_label_object = data_label
        self.data_label_object.setWordWrap(True)
        self.passfail_label_object = passfail_label
        self.fetch_canbus_data = general_functions[1]
        self.send_can_message = general_functions[2]
        self.update_label_signal.connect(general_functions[3])
        self.finish_signal = general_functions[4]
        self.srf1_label = srf1
        self.srf2_label = srf2
        self.battery_pct_label = battery_pct
        self.battery_voltage_label = battery_voltage
        self.battery_error_label = battery_error
        self.test_registers_list = [
            self.srf1_label,
            self.srf2_label,
            self.battery_pct_label,
            self.battery_voltage_label,
            self.battery_error_label
        ]
        self.tests_data = [0,0,0,0,0]
        self.tests_fails = [0,0,0,0,0]
        self.test_results = "not run yet"
        self.passfail = "unknown"
        self.update_results()



    def update_results(self):
        """Emit a signal to update the label's text."""
        self.update_label_signal.emit(self.data_label_object, self.test_results)
        self.update_label_signal.emit(self.passfail_label_object, self.passfail)

    def finish_test(self):
        self.finish_signal()


    def make_passfail(self):
        self.test_results = "THE FOLLOWING REGISTERS FAILED:   "
        timeout_cnt = 0
        for register_index in range(len(self.test_registers_list)):
            self.test_registers_list[register_index].make_passfail()

            if "FAIL" in self.test_registers_list[register_index].passfail:
                if (not self.test_results == "THE FOLLOWING REGISTERS FAILED:   "):
                    self.test_results += ",     "
                self.test_results += self.test_registers_list[register_index].name
                self.passfail = "FAIL"

            if self.tests_fails[register_index]:

                timeout_cnt += 1

        if (timeout_cnt > 0):
            if (timeout_cnt == len(self.test_registers_list)):
                self.test_results = "FAILED, ALL REQUESTS TIMED OUT, NO DATA RECEIVED FROM BOTTOM MICROCONTROLLER"
                self.passfail = "FAIL"
            else:
                self.test_results += "HAD SOME TIMEOUTS, TRY RUNNING THE TEST AGAIN"

        elif self.test_results == "THE FOLLOWING REGISTERS FAILED:   ":
            self.test_results = ""
            self.passfail = "PASS"


    def reset_test(self):
        self.test_results = ""
        self.tests_data = [0,0,0,0,0]
        self.tests_fails = [0,0,0,0,0]

    def run_test(self, var): #testing the bottom uCs
        for register_index in range(len(self.test_registers_list)):
            self.update_button_signal.emit(self.button_object, ((register_index) * 100) / len(self.test_registers_list))

            timeout,data = self.fetch_canbus_data(self.test_registers_list[register_index].device_id,self.test_registers_list[register_index].reg_id,300000, 0)
            time.sleep(0.1)
            if (timeout):
                print(self.test_registers_list[register_index].name, data)
                self.tests_fails[register_index] = 1
            else:
                self.tests_fails[register_index] = 0
            self.tests_data[register_index] = str(self.test_registers_list[register_index].make_data_not_text(data))

        self.update_button_signal.emit(self.button_object, 0)
        self.make_passfail()
        time.sleep(0.1)
        self.update_results()
        self.finish_test()
        return 1





# End of bottom_test_class.py

# Start of canbus.py







class CANBusWorker(QObject):

    update_button_signal = pyqtSignal(object, int)  # Signal to send label and text
    update_canstate_labels_signal = pyqtSignal()  # Signal to send label and text

    def __init__(self, get_current_page, get_current_subpage, get_current_test, data_entries, test_entries, update_button_func, bad_can_variables, update_canstate_labels):
        super().__init__()
        self.update_button_signal.connect(update_button_func)
        self.update_canstate_labels_signal.connect(update_canstate_labels)
        self.bad_can_variables = bad_can_variables
        self.get_current_page = get_current_page
        self.get_current_subpage = get_current_subpage
        self.get_current_test = get_current_test
        self.running = True
        self.test_entries = test_entries
        self.data_entries = data_entries          # Dictionary of data_entry instances
        self.test_finished = 0
        self.can_running0 = 0
        self.can_running1 = 0
        self.bus0 = 0
        self.bus1 = 0
        self.started_with_can_issue = 2
        self.force_can_page = 0
        self.attempt_can_connection(0)
        self.attempt_can_connection(1)
        self.bad_can_variables.continue_button.clicked.connect(lambda: self.force_no_can())
        self.bad_can_variables.can0_button.clicked.connect(lambda: self.attempt_can_connection(0))
        self.bad_can_variables.can1_button.clicked.connect(lambda: self.attempt_can_connection(1))
        self.forced_no_can = 0

    def update_label(self, label_object, text):
        """Update the label's text."""
        label_object.setText(text)

    def force_no_can(self):
        text = ""
        if (self.can_running0 == 0):
            text += "can0 is not running, most tests will NOT run "
        if (self.can_running1 == 0):
            text += "can1 is not running, arm related tests will NOT run"
        self.forced_no_can = 1
        self.update_label(self.bad_can_variables.general_messages_label, text)
        self.update_canstate_labels_signal.emit()
        self.force_can_page = 0

    def test_can_connection(self):
        try:
            if ("OFF" in str(self.bus0.state)):
                self.can_running0 = 0
                self.force_can_page = 1
                self.forced_no_can = 0
                self.bad_can_variables.main_widget.setCurrentIndex(1)
        except AttributeError:
            pass
        try:
            if ("OFF" in str(self.bus1.state)):
                self.can_running1 = 0
                self.force_can_page = 1
                self.forced_no_can = 0
                self.bad_can_variables.main_widget.setCurrentIndex(1)
        except AttributeError:
            pass


    def force_can_page_back(self):
        self.forced_no_can = 0
        self.force_can_page = 1
        self.bad_can_variables.main_widget.setCurrentIndex(1)

    def check_can_states(self):
        self.test_can_connection()
        if (self.forced_no_can):
            if not(self.bad_can_variables.main_widget.currentIndex() == 0):
                self.bad_can_variables.main_widget.setCurrentIndex(0)
            return 0
        if self.can_running0 == 0 or self.can_running1 == 0:
            self.bad_can_variables.main_widget.setCurrentIndex(1)
            try:
                state = str(self.bus0.state)
            except AttributeError:
                state = "not yet"
            if ("OFF" in state):
                self.update_label(self.bad_can_variables.can0_label, "can0: BUS OFF")
            elif self.can_running0 == 0:
                self.update_label(self.bad_can_variables.can0_label, "can0: NO CONNECTION")
            else:
                self.update_label(self.bad_can_variables.can0_label, "can0: CONNECTED")
            if self.can_running1 == 0:
                try:
                    state = str(self.bus1.state)
                except AttributeError:
                    state = "not yet"
                if ("OFF" in state):
                    self.update_label(self.bad_can_variables.can1_label, "can1: BUS OFF")
                elif "win" in platform:
                    self.update_label(self.bad_can_variables.can1_label, "can1: NO CAN1 ON WINDOWS")
                else:
                    self.update_label(self.bad_can_variables.can1_label, "can1: NO CONNECTION")
            else:
                self.update_label(self.bad_can_variables.can1_label, "can1: CONNECTED")
        else:
            self.forced_no_can = 1
            if not(self.started_with_can_issue == 0):
                self.bad_can_variables.canbus_good_label.setText("ALL EXPECTED CAN CONNECTED, CONTINUING")
                self.bad_can_variables.canbus_good_label.setStyleSheet("color: green;")
                time.sleep(1)
            self.bad_can_variables.main_widget.setCurrentIndex(0)
            self.update_canstate_labels_signal.emit()
        if (self.can_running0 == 1 and "win" in platform and not self.force_can_page):
            if not(self.started_with_can_issue == 0):
                self.bad_can_variables.canbus_good_label.setText("ALL EXPECTED CAN CONNECTED, CONTINUING")
                self.bad_can_variables.canbus_good_label.setStyleSheet("color: green;")
                time.sleep(1)
            self.forced_no_can = 1
            self.bad_can_variables.main_widget.setCurrentIndex(0)
            self.update_canstate_labels_signal.emit()
        return 1




    def attempt_can_connection(self, can_select):
        if (can_select == 0 and not self.can_running0):
            channel = 'can0'
            try:
                if platform == "linux" or platform == "linux2" or platform == "unix":
                    bustype = 'socketcan'
                    self.bus0 = can.Bus(channel=channel, interface=bustype, baudrate=1000000)
                elif "win" in platform:
                    self.bus0 = can.interface.Bus(bustype='pcan', channel='PCAN_USBBUS1', bitrate=1000000)

                self.can_running0 = 1
                self.started_with_can_issue -= 1
            except:
                print("CANBUS (can0) FAILED IN INITIALIZING")
                self.can_running0 = 0

        elif (can_select == 1 and not self.can_running1):
            channel = 'can1'
            try:
                if platform == "linux" or platform == "linux2" or platform == "unix":
                    bustype = 'socketcan'
                    self.bus1 = can.Bus(channel=channel, interface=bustype, baudrate=1000000)
                elif "win" in platform:
                    self.update_label(self.bad_can_variables.general_messages_label, "NO CAN1 ON WINDOWS, no arms or linears available (relevant tests will run on can0)")
                self.started_with_can_issue -= 1
            except:
                print("CANBUS (can1) FAILED IN INITIALIZING")
                self.can_running1 = 0

    def run(self):
        while self.running:
            if (self.check_can_states()):
                continue

            # Fetch CAN data
            # Get the current page

            current_test = self.get_current_test()
            current_page = self.get_current_page()
            current_subpage = self.get_current_subpage()
            if (self.run_test_when_needed(current_test)):
                continue


            if current_subpage is None:
                current_subpage = 0

            self.read_registers_data(current_page, current_subpage)



    def read_registers_data(self, current_page, current_subpage):
        if (not current_page in self.data_entries):
            time.sleep(0.2)
            return
        if (not current_subpage < len(self.data_entries[current_page])):
            time.sleep(0.2)
            return

        had_resp = 0
        for entry in self.data_entries[current_page][current_subpage]: #for whichever registers are currently showing
            if entry.device_id == 0x103:
                self.send_can_message(0x103, [0x50, 0x45, 0xFF, 0xFF, 0xFF, 0xFF, 0x00, 0xFF]) #if top, request that it doesn't forward the request

            failed, data = self.fetch_canbus_data(entry.device_id, entry.reg_id, 300000) #request the register
            if failed: #if timed out, set invalid
                entry.valid_data = 0
            else: #set "had response" to have a higher delay at the end (give time for the canbus to empty)
                had_resp = 1
                entry.valid_data = 1 #got the data
            entry.udate(data) #update the data in the object
            if (entry.reg_id == 0): #for the "code version" register, add extra delay to avoid data overlap
                time.sleep(0.1)
            time.sleep(0.02)
        if (had_resp): #add delay between data reads (per page, not per register ON the page), this is added only if not timed out because timeout is it's own delay
            time.sleep(0.2)

    def run_test(self,test_number): #direct to the current test logic
        # print(self.test_entries.keys())
        if (test_number in self.test_entries.keys()):
            if (self.test_entries[self.get_current_test()][0].run_test(self.test_entries[self.get_current_test()][1])):
                self.finish_test()
        else:
            print("test not yet created, crashing now ;) ...")
            crashvar = self.test_entries[1000]









    def finish_test(self):
        self.test_finished = 5

    def fetch_canbus_data_top(self, device_id, reg_id, timeout, can_selector):
        if (can_selector == 1):
            return self.fetch_canbus_data1(device_id, reg_id, timeout)
        elif (can_selector == 0):
            return self.fetch_canbus_data(device_id, reg_id, timeout)
        else:
            print("unecpected can select variable in fetch_canbus_data function: ", can_selector)

    def fetch_canbus_data(self,device_id,reg_id,timeout):
        start_time = self.get_time_delta([0,0,0])[1]
        time_send = start_time
        self.send_can_message(device_id, [0x53, 0x53, 0x02, reg_id, reg_id, 2, 0, 0])
        while self.get_time_delta(start_time)[0] < timeout:  # Process a limited number of iterations for testing
            if (self.get_time_delta(time_send)[0] >= 10000):
                time_send = self.get_time_delta(time_send)[1]
                self.send_can_message(device_id,[0x53,0x53,0x02,reg_id,reg_id,2,0,0])
                # print(self.get_time_delta(start_time)[0])
            # Attempt to receive a CAN message
            message = self.bus0.recv(0.01)  # Timeout in seconds.
            if message is None:
                continue  # No message received; try again.

            # Process the message if it matches the desired arbitration ID
            # if (reg_id == 0):
            #     expected_board_identifier = 0
            #     if (device_id == 0x103):
            #         expected_board_identifier = 0
            #     elif (device_id == 0x104):
            #         expected_board_identifier = 1
            #     elif (device_id == 0x102):
            #         expected_board_identifier = 2
            #     if not(message.data[1] == expected_board_identifier):
            #         continue
            if (message.arbitration_id == 0x105 and device_id > 0x100 and device_id < 0x106) or (message.arbitration_id == device_id and device_id > 0x106):
                # print(message.data[0], reg_id)
                if message.data[0] == reg_id:
                    data = str(message.data)
                    return [0,data]  # Return the data for further processing.
        return [1,"No relevant CAN data received."] # Fallback message if no data was found.

    def fetch_canbus_data1(self, device_id, reg_id, timeout):
        start_time = self.get_time_delta([0, 0, 0])[1]
        time_send = start_time
        self.send_can_message1(device_id, [0x53, 0x53, 0x02, reg_id, reg_id, 1, 0, 0])
        while self.get_time_delta(start_time)[0] < timeout:  # Process a limited number of iterations for testing
            if (self.get_time_delta(time_send)[0] >= 10000):
                time_send = self.get_time_delta(time_send)[1]
                self.send_can_message1(device_id,[0x53,0x53,0x02,reg_id,reg_id,1,0,0])
            # Attempt to receive a CAN message
            message = self.bus1.recv(0.1)  # Timeout in seconds.
            if message is None:
                continue  # No message received; try again.

            # Process the message if it matches the desired arbitration ID
            if message.arbitration_id == device_id:
                if message.data[0] == reg_id:
                    data = str(message.data)
                    return [0, data]  # Return the data for further processing.
        return [1, "No relevant CAN data received."]  # Fallback message if no data was found.

    def manual_can_fetch(self, request_message, reply_id, reply_first_byte, timeout, can_select):
        if (can_select == 0 and self.can_running0 == 0):
            return [1,[]]
        if (can_select == 1 and self.can_running1 == 0):
            can_select = 0
        start_time = self.get_time_delta([0, 0, 0])[1]
        while self.get_time_delta(start_time)[0] < timeout:  # Process a limited number of iterations for testing
            # print("receive")
            message = None
            if (can_select == 0):
                message = self.bus0.recv(0.1)  # Timeout in seconds.
            else:
                message = self.bus1.recv(0.1)  # Timeout in seconds.
            if message is None:
                continue  # No message received; try again.
            # Process the message if it matches the desired arbitration ID
            if message.arbitration_id == reply_id:
                if message.data[0] == reply_first_byte:
                    data = message.data
                    return [0, data]  # Return the data for further processing.
        time_send = self.get_time_delta(start_time)[1]

        if (can_select == 0):
            self.send_can_message(request_message.arbitration_id, request_message.data)
        else:
            self.send_can_message1(request_message.arbitration_id, request_message.data)
        while self.get_time_delta(start_time)[0] < timeout*2:  # Process a limited number of iterations for testing
            message = None
            if (self.get_time_delta(time_send)[0] >= 10000):
                time_send = self.get_time_delta(time_send)[1]
                if (can_select == 0):
                    self.send_can_message(request_message.arbitration_id,request_message.data)
                else:
                    self.send_can_message1(request_message.arbitration_id,request_message.data)
            if (can_select == 0):
                message = self.bus0.recv(0.1)  # Timeout in seconds.
            else:
                message = self.bus1.recv(0.1)  # Timeout in seconds.
            if message is None:
                continue  # No message received; try again.
            # Process the message if it matches the desired arbitration ID
            if message.arbitration_id == reply_id:
                if message.data[0] == reply_first_byte:
                    data = message.data
                    return [0, data]  # Return the data for further processing.
        return [1, []]  # Fallback message if no data was found.



    def send_can_message_top(self, arbitration_id, data, can_selector):
        if (can_selector == 1):
            return self.send_can_message1(arbitration_id, data)
        elif (can_selector == 0):
            return self.send_can_message(arbitration_id, data)
        else:
            print("unecpected can select variable in send_can_message function: ", can_selector)

    def send_can_message(self, arbitration_id, data):
        """Send a CAN message with the given arbitration ID and data."""
        if not self.can_running0:
            print("CAN bus is not initialized.")
            return
        try:
            # Create and send a CAN message
            message = can.Message(arbitration_id=arbitration_id, data=data, is_extended_id=False)
            self.bus0.send(message)
        except Exception as e:
            print(f"Error sending CAN message: {e}")

    def send_can_message1(self, arbitration_id, data):
        """Send a CAN message with the given arbitration ID and data."""

        if not self.can_running1:
            print("can1 is not initialized.")
            return
        try:
            # Create and send a CAN message
            message = can.Message(arbitration_id=arbitration_id, data=data, is_extended_id=False)
            self.bus1.send(message)
        except Exception as e:
            print(f"Error sending CAN message: {e}")

    def stop(self):
        self.running = False

    def run_test_when_needed(self, current_test):
        if (self.test_finished > 0):
            time.sleep(0.05)
            self.test_finished -= 1
            return 1
        if (not (current_test == 0 )):
            self.run_test(current_test)
            return 1
        return 0

    def get_time_delta(self, time_last_receive):
        time_S = int((datetime.datetime.now()).strftime("%S"))
        time_mS = int((datetime.datetime.now()).strftime("%f"))
        time_M = int((datetime.datetime.now()).strftime("%M"))
        delta = (time_M - time_last_receive[0]) * 60
        delta += time_S - time_last_receive[1]
        delta *= 1000000
        delta += time_mS - time_last_receive[2]
        time_receive = [time_M, time_S, time_mS]
        return [delta,time_receive]

# End of canbus.py

# Start of data_entries.py

typelist = ["float","decimal","2s", "binary", "ascii","onoff"]

class data_entry(QObject):
    update_label_signal = pyqtSignal(object, str)  # Signal to send label and text
    def __init__(self, label_object, name, datatype, device_id, reg_id, update_label_func, starndard_min, standard_max, passfail_label):
        super().__init__()
        self.label_object = label_object  # QLabel object
        self.passfail_label_object = passfail_label  # QLabel object
        self.name = name                  # Name associated with the label
        self.datatype = datatype          # Name associated with the label
        self.valid_data = 0
        self.starndard_min = starndard_min
        self.standard_max = standard_max
        self.device_id = device_id
        self.reg_id = reg_id
        self.passfail = ""

        if not datatype in typelist:
            print("type \""+ datatype+"\" is unsupported for label \""+name+"\"")
        self.data = "Not received yet"    # Initial data
        #self.update_label_signal = update_label_signal  # Signal to emit updates
        self.update_label_signal.connect(update_label_func)
        self.update_label()


    def udate(self, text):
        """Update the data and emit a signal to refresh the label."""
        self.data = text
        self.update_label()


    def update_label(self):
        """Emit a signal to update the label's text."""
        self.make_passfail()
        self.update_label_signal.emit(self.label_object, self.make_text())
        self.update_label_signal.emit(self.passfail_label_object, self.passfail)

    def makedatafloat(self):
        # Pack it into a byte format
        last_4_bytes = eval(self.data)[-4:]
        # Unpack the last 4 bytes as a float (using big-endian byte order '>' and 'f' for float)
        float_value = struct.unpack('<f', last_4_bytes)[0]
        return (float_value)

    def makedatadec(self):
        resultdec = 0
        for byte_idx in range(len(eval(self.data)[2:])):
            resultdec += int(eval(self.data)[2 + byte_idx]) * (256 ** ((6 - byte_idx) - 1))
        return resultdec

    def makedata2s(self):
        resultdec = 0
        for byte_idx in range(len(eval(self.data)[6:])):
            resultdec += int(eval(self.data)[6 + byte_idx]) * (256 ** ((2 - byte_idx) - 1))
        if resultdec > 32767:
            return "-"+str(65535-resultdec-1)
        return resultdec

    def makedatabinary(self):
        datastring = ""
        actual_data = eval(self.data)[2:]
        for databyte in actual_data:
            if databyte == 0:
                datastring+= "0 "
            else:
                datastring+= "1 "
        return (datastring)

    def makedataascii(self):
        datastring = ""
        actual_data = eval(self.data)[2:]
        for byte in actual_data:
            if not (byte == 0x00):
                datastring += chr(byte)
        return datastring

    def makedataonoff(self):
        actual_data = eval(self.data)[-1]
        if not (actual_data == 0x00):
            return "ON"
        return "OFF"

    def make_data_not_text(self, data_parse):
        self.data = data_parse
        if "received" in self.data:
            return "not yet received"
        if self.datatype == "float":
            return f"{self.makedatafloat()}"
        elif self.datatype == "decimal":
            return f"{self.makedatadec()}"
        elif self.datatype == "2s":
            return f"{self.makedata2s()}"
        elif self.datatype == "binary":
            return f"{self.makedatabinary()}"
        elif self.datatype == "ascii":
            return f"{self.makedataascii()}"
        elif self.datatype == "onoff":
            return f"{self.makedataonoff()}"
        return "parsing failed"

    def make_text(self):
        """Format the label text."""
        if not(self.valid_data):
            return f"{self.name}: {self.data}"
        if self.datatype == "float":
            return f"{self.name}: {self.makedatafloat()}"
        elif self.datatype == "decimal":
            return f"{self.name}: {self.makedatadec()}"
        elif self.datatype == "2s":
            return f"{self.name}: {self.makedata2s()}"
        elif self.datatype == "binary":
            return f"{self.name}: {self.makedatabinary()}"
        elif self.datatype == "ascii":
            return f"{self.name}: {self.makedataascii()}"
        elif self.datatype == "onoff":
            return f"{self.name}: {self.makedataonoff()}"
        return f"{self.name}: {self.data}"

    def make_passfail(self):
        if "received" in self.data:
            return ""
        if "chest button" in self.name:
            if float(self.make_data_not_text(self.data)) == 0:
                self.passfail = "UNKNOWN (likely due to never having been pressed) , press button to see if value changed"
                return "FAIL, press button to see if value changed"
        if (self.starndard_min == 0 and self.standard_max == 0):
            self.passfail = ""
            return ""
        data_numeral = float(self.make_data_not_text(self.data))
        if (data_numeral >= self.starndard_min and data_numeral <= self.standard_max):
            self.passfail = "PASS"
            return "PASS"
        self.passfail = "FAIL"
        return "FAIL"


# End of data_entries.py

# Start of leds_class_def.py



class leds_class(QObject):

    def __init__(self, red_slider, green_slider, blue_slider,
                 current_color_plate, button_white, button_green, button_blue, button_red, button_purple, button_turquoise,
                 head_off_button, head_wave_button, head_eyes_button, head_full_button,
                 chest_off_button, chest_blink_button, chest_loading_button, chest_full_button,
                 general_functions):
        super().__init__()
        # self.general_functions = general_functions
        self.send_can_message = general_functions[2]
        self.red_slider = red_slider
        self.green_slider = green_slider
        self.blue_slider = blue_slider
        self.current_color_plate  = current_color_plate
        self.button_white         = button_white
        self.button_green         = button_green
        self.button_blue          = button_blue
        self.button_red           = button_red
        self.button_purple        = button_purple
        self.button_turquoise     = button_turquoise

        self.head_off_button      = head_off_button
        self.head_wave_button     = head_wave_button
        self.head_eyes_button     = head_eyes_button
        self.head_full_button     = head_full_button
        self.chest_off_button     = chest_off_button
        self.chest_blink_button   = chest_blink_button
        self.chest_loading_button = chest_loading_button
        self.chest_full_button    = chest_full_button


        self.red_val = 0
        self.green_val = 0
        self.blue_val = 0

        self.red_slider.valueChanged.connect(lambda: self.update_color_from_slider(self.red_slider.value(), 0))
        self.green_slider.valueChanged.connect(lambda: self.update_color_from_slider(self.green_slider.value(), 1))
        self.blue_slider.valueChanged.connect(lambda: self.update_color_from_slider(self.blue_slider.value(), 2))

        self.set_color(255, 0, 255) #set initial color

        self.button_white.clicked.connect(lambda: self.set_color(255,255,255))
        self.button_green.clicked.connect(lambda: self.set_color(0,255,0))
        self.button_blue.clicked.connect(lambda: self.set_color(0,0,255))
        self.button_red.clicked.connect(lambda: self.set_color(255,0,0))
        self.button_purple.clicked.connect(lambda: self.set_color(255,0,255))
        self.button_turquoise.clicked.connect(lambda: self.set_color(0,255,128))

        self.head_off_button     .clicked.connect(lambda: self.send_leds(0, 0x00, 0x00, 0x00))
        self.head_wave_button    .clicked.connect(lambda: self.send_leds(0, 0x03, 0x00, 0x07))
        self.head_eyes_button    .clicked.connect(lambda: self.send_leds(0, 0xFF, 0x04, 0x02))
        self.head_full_button    .clicked.connect(lambda: self.send_leds(0, 0x01, 0x05, 0xFF))
        self.chest_off_button    .clicked.connect(lambda: self.send_leds(1, 0x00, 0x00, 0xFF))
        self.chest_blink_button  .clicked.connect(lambda: self.send_leds(1, 0x03, 0x00, 0x04))
        self.chest_loading_button.clicked.connect(lambda: self.send_leds(1, 0x0C, 0x00, 0x04))
        self.chest_full_button   .clicked.connect(lambda: self.send_leds(1, 0x0D, 0x00, 0xFF))



    def send_leds(self, head_chest_sel, motion_sel, reps, speed):
        if (head_chest_sel):
            head_chest_byte = 0x43
        else:
            head_chest_byte = 0x48
        self.send_can_message(0x103, [head_chest_byte, 0x4C, motion_sel, speed, reps*2, self.red_val, self.green_val, int((self.blue_val*4)/5)], 0)
        time.sleep(0.01)


    def update_shown_color(self):
        self.current_color_plate.setStyleSheet(f"background-color: rgb({self.red_val}, {self.green_val}, {self.blue_val}); color: black;")

    def update_color_from_slider(self, slider_value, color_select):
        if (color_select == 0):
            self.red_val = slider_value
        elif (color_select == 1):
            self.green_val = slider_value
        elif (color_select == 2):
            self.blue_val = slider_value
        self.update_shown_color()

    def set_color(self, red, green, blue):
        self.red_val = red
        self.green_val = green
        self.blue_val = blue

        self.red_slider.setValue(self.red_val)
        self.green_slider.setValue(self.green_val)
        self.blue_slider.setValue(self.blue_val)
        self.update_shown_color()





# End of leds_class_def.py

# Start of motor_class.py



class motor_class(QObject):

    def __init__(self, name, motor_id, can_select):
        super().__init__()
        self.name = name
        self.motor_id = motor_id
        self.can_selector = can_select
        self.request_type = 0x9C

    def is_my_response(self, response):
        if not (response.arbitration_id == self.motor_id):
            return 0
        if not (response.data[0] == self.request_type):
            return 0
        for index in range(1,len(response.data)):
            if not (response.data[index] == 0):
                return 1
        return 0

    def make_request(self):
        return can.Message(arbitration_id=self.motor_id, data=[self.request_type, 0, 0, 0, 0, 0, 0, 0], is_extended_id=False)

    def make_big_move_right(self):
        return can.Message(arbitration_id=self.motor_id, data=[0xA8, 0x00, 0xA8, 0x0C, 0x80, 0xC6, 0x13, 0x00], is_extended_id=False)

    def make_small_move_right(self):
        return can.Message(arbitration_id=self.motor_id, data=[0xA8, 0x00, 0xA8, 0x0C, 0xC0, 0x4B, 0x03, 0x00], is_extended_id=False)

    def make_small_move_left(self):
        return can.Message(arbitration_id=self.motor_id, data=[0xA8, 0x00, 0xA8, 0x0C, 0x40, 0xB4, 0xFC, 0xFF], is_extended_id=False)

    def make_big_move_left(self):
        return can.Message(arbitration_id=self.motor_id, data=[0xA8, 0x00, 0xA8, 0x0C, 0x80, 0x39, 0xEC, 0xFF], is_extended_id=False)

    def make_stop(self):
        return can.Message(arbitration_id=self.motor_id, data=[0x81, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)

    def make_read_pos_req(self):
        return can.Message(arbitration_id=self.motor_id, data=[0x92, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)

    def make_write_pos_req(self, response):
        return can.Message(arbitration_id=self.motor_id, data=[0xA4, 0x00, 0x00, 0x00, response[1], response[2], response[3], response[4]], is_extended_id=False)

    def make_spin(self):
        return can.Message(arbitration_id=self.motor_id, data=[0xA2, 0x00, 0x00, 0x00, 0xAF, 0x52, 0x06, 0x00], is_extended_id=False)

    def make_reverse(self):
        return can.Message(arbitration_id=self.motor_id, data=[0xA2, 0x00, 0x00, 0x00, 0x51, 0xAD, 0xF9, 0xFF], is_extended_id=False)

        # 51 ad f9 ff
        # af 52 06 00




# End of motor_class.py

# Start of motor_test_class.py



class motor_test_class(QObject):
    update_label_signal = pyqtSignal(object, str)  # Signal to send label and text
    finish_signal = pyqtSignal()  # Signal to send label and text
    update_button_signal = pyqtSignal(object, int)  # Signal to send label and text

    def __init__(self, all_motors,
                 wheels_data_label, wheels_button_object,
                 right_data_label, right_button_object,
                 left_data_label, left_button_object,
                 general_functions, general_messages_label_2):
        super().__init__()
        self.all_motors_object = all_motors
        self.update_button_signal.connect(general_functions[0])
        self.wheels_data_label     = wheels_data_label
        self.wheels_button_object  = wheels_button_object
        self.right_data_label      = right_data_label
        self.right_button_object   = right_button_object
        self.left_data_label       = left_data_label
        self.left_button_object    = left_button_object
        self.general_messages_label_2 = general_messages_label_2

        self.general_messages_label_2.setWordWrap(True)
        self.wheels_data_label.setWordWrap(True)
        self.right_data_label.setWordWrap(True)
        self.left_data_label.setWordWrap(True)

        self.fetch_canbus_data = general_functions[1]
        self.send_can_message = general_functions[2]
        self.update_label_signal.connect(general_functions[3])
        self.finish_signal = general_functions[4]
        self.manual_fetch = general_functions[5]
        self.get_can_state = general_functions[6];
        self.test_results = "not run yet"
        self.passfail = "unknown"
        self.update_results()





    def update_results(self):
        """Emit a signal to update the label's text."""
        pass
        # self.update_label_signal.emit(self.data_label_object, self.test_results)
        # self.update_label_signal.emit(self.passfail_label_object, self.passfail)

    def finish_test(self):
        self.finish_signal()

    #return 1 if passed, 0 if failed
    def test_motor_reply(self, motor_object):
        for x in range(3):
            failed, data = self.manual_fetch(motor_object.make_request(), motor_object.motor_id, motor_object.request_type, 50000, motor_object.can_selector)  # request the register
            if failed:  # if timed out, return 0
                continue
            else:
                for data_idx in range(1, len(data)):
                    if not data[data_idx] == 0:
                        return 1
        return 0

    def test_list(self, motor_list, data_label, button):
        result_text = ""
        cnt = 0
        for motor_object in motor_list:
            cnt += 1
            result_text += motor_object.name
            if (self.test_motor_reply(motor_object)):
                result_text += ": PASSED (id:" + str(motor_object.motor_id) + ")\n\n"
            else:
                result_text += ": FAILED (id:" + str(motor_object.motor_id) + ")\n\n"
            self.update_label_signal.emit(data_label, result_text)
            self.update_button_signal.emit(button, int((cnt*100)/len(motor_list)))
        self.update_button_signal.emit(button, 0)
        self.update_label_signal.emit(data_label, result_text)


    def run_test(self, var):
        if (var == 0):
            self.test_list(self.all_motors_object.wheels_list, self.wheels_data_label, self.wheels_button_object)

        elif (var == 1):
            self.test_list(self.all_motors_object.Left_arm_list, self.left_data_label, self.left_button_object)

        elif (var == 2):
            self.test_list(self.all_motors_object.Right_arm_list, self.right_data_label, self.right_button_object)

        self.finish_test()
        return 1

    def reset_test(self):
        self.test_results = ""

    #motor_select:  0-FL, 1-RL, 2-FR, 3-RR.
    #move_direction: 0-forwards, 1-stop, 2-reverse.
    def move_wheel(self, motor_select, move_direction):
        motor_to_move = self.all_motors_object.wheels_list[motor_select]
        if (motor_select <= 1):
            if move_direction == 0:
                message_to_send = motor_to_move.make_spin()
            elif move_direction == 2:
                message_to_send = motor_to_move.make_reverse()
            else:
                message_to_send = motor_to_move.make_stop()
        else:
            if move_direction == 0:
                message_to_send = motor_to_move.make_reverse()
            elif move_direction == 2:
                message_to_send = motor_to_move.make_spin()
            else:
                message_to_send = motor_to_move.make_stop()
        self.send_can_message(message_to_send.arbitration_id, message_to_send.data, motor_to_move.can_selector)

    #motor_select:  0-right, 1-left, 2-cart.
    #move_direction: 0-down/open big, 1-down/open small, 2-stop, 3-up/close small, 4-up/close big.
    def move_step(self, motor_select, move_direction):
        motor_to_move = self.all_motors_object.step_motors_list[motor_select]
        if ( "win" in platform):
            motor_to_move.can_selector = 0

        if move_direction == 0:
            message_to_send = motor_to_move.make_big_move_right()
        elif move_direction == 1:
            message_to_send = motor_to_move.make_small_move_right()
        elif move_direction == 3:
            message_to_send = motor_to_move.make_small_move_left()
        elif move_direction == 4:
            message_to_send = motor_to_move.make_big_move_left()
        else:
            message_to_send = motor_to_move.make_stop()
            self.send_can_message(message_to_send.arbitration_id, message_to_send.data, motor_to_move.can_selector)
            time.sleep(0.05)
            self.send_can_message(message_to_send.arbitration_id, message_to_send.data,  motor_to_move.can_selector)
            time.sleep(0.05)
            failed = 1
            for x in range(10):
                failed, data = self.manual_fetch(motor_to_move.make_read_pos_req(), motor_to_move.motor_id, motor_to_move.make_read_pos_req().data[0], 50000, motor_to_move.can_selector)  # request the register
                if failed:  # if timed out, return 0
                    continue
                else:
                    for data_idx in range(1, len(data)):
                        if not data[data_idx] == 0:
                            failed = 0
                            break
                    if not failed:
                        break
            if failed == 0:
                movepos_message = motor_to_move.make_write_pos_req(data)
                self.send_can_message(movepos_message.arbitration_id, movepos_message.data, motor_to_move.can_selector)
                time.sleep(0.05)
                self.send_can_message(movepos_message.arbitration_id, movepos_message.data, motor_to_move.can_selector)
                time.sleep(0.05)
                self.general_messages_label_2.setText("")

            else:
                self.general_messages_label_2.setText("BAD LOCATION ON \""+motor_to_move.name+"\", PLEASE PRESS STOP AGAIN UNTIL THIS IS GONE OR RESET THE ROBOT")
                self.general_messages_label_2.setStyleSheet("color: red;")



        # def make_read_pos_req(self):
        #     return can.Message(arbitration_id=self.motor_id, data=[0x92, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
        #                        is_extended_id=False)
        #
        # def make_write_pos_req(self, response):

        self.send_can_message(message_to_send.arbitration_id, message_to_send.data, 0)#motor_to_move.can_selector)








# End of motor_test_class.py

# Start of nicla_test_class.py


MAX_TIMING_DIFF = 3000

class nicla_test_data(QObject):
    update_label_signal = pyqtSignal(object, str)  # Signal to send label and text
    update_button_signal = pyqtSignal(object, int)  # Signal to send label and text

    def __init__(self, passfail_label, data_label, button_object, general_functions):
        super().__init__()
        self.update_button_signal.connect(general_functions[0])
        self.timing_history = []
        self.fail_count = 0
        self.button_object = button_object
        for i in range(150):
            self.timing_history.append(0)
        self.passfail_label_object = passfail_label  # QLabel object
        self.data_label_object = data_label  # QLabel object
        self.timing_average = 0
        self.timing_index = 0
        self.fetch_canbus_data = general_functions[1]
        self.send_can_message = general_functions[2]
        self.update_label_signal.connect(general_functions[3])
        self.finish_signal = general_functions[4]
        self.update_results()



    def update_results(self):
        """Emit a signal to update the label's text."""
        self.update_label_signal.emit(self.data_label_object, self.make_average())
        self.update_label_signal.emit(self.passfail_label_object, self.make_passfail())

    def finish_test_nicla(self):
        self.finish_signal()

    def make_average(self):
        sum_to_average = 0
        for x in self.timing_history:
            sum_to_average += x
        self.timing_average = (sum_to_average/150)
        self.timing_average = self.timing_average - (self.timing_average%0.01)
        if (self.timing_average == 0):
            return "not run yet"

        return ("average reply delay (expected below 4500): {:.2f}".format(self.timing_average))

    def make_passfail(self):
        cnt = 0
        for delay in self.timing_history:
            if (abs(delay-self.timing_average) >= MAX_TIMING_DIFF and delay > 8000):
                print(delay)
                cnt += 1
        if (self.timing_average == 0):
            return "unknown"
        if (self.timing_average == 999999):
            return "TIMEOUT FAIL, bad connection or bad nicla"
        if (cnt > 5 or self.timing_average < 300 or self.timing_average > 5000):
            return "FAIL, "+str(cnt)+"/150 (try again)"
        return "PASS"

    def get_timing_average(self):
        return self.timing_average

    def insert_delta(self, time_delta):
        self.timing_history[self.timing_index] = time_delta
        self.timing_index = ((self.timing_index) + 1) % 150

    def reset_test(self):
        for x in range(len(self.timing_history)):
            self.timing_history[x] = 0
        self.timing_index = 0
        self.timing_average = 0
        self.fail_count = 0

    def force_fail(self):
        for x in range(len(self.timing_history)):
            self.timing_history[x] = 999999

        self.timing_average = 999999

    def run_test(self, var):
        start_time = self.get_time_delta([0,0,0])[1]
        timeout,data = self.fetch_canbus_data(0x102,0x5A,15000, 0)
        time_delta = self.get_time_delta(start_time)[0]
        if (timeout):
            self.fail_count += 1

        returnval = 0
        self.insert_delta(time_delta)
        if (self.timing_index == 0):
            time.sleep(0.1)
            self.update_results()
            returnval = 1
            self.finish_test_nicla()
        if (self.fail_count >= 5):
            self.timing_index = 0
            self.force_fail()
            self.update_results()
            returnval = 1
            self.finish_test_nicla()
        self.update_button_signal.emit(self.button_object, (self.timing_index * 100)/150)
        return returnval

    def get_time_delta(self, time_last_receive):
        time_S = int((datetime.datetime.now()).strftime("%S"))
        time_mS = int((datetime.datetime.now()).strftime("%f"))
        time_M = int((datetime.datetime.now()).strftime("%M"))
        delta = (time_M - time_last_receive[0]) * 60
        delta += time_S - time_last_receive[1]
        delta *= 1000000
        delta += time_mS - time_last_receive[2]
        time_receive = [time_M, time_S, time_mS]

        return [delta,time_receive]


# End of nicla_test_class.py

# Start of physical_test_class_def.py



class physical_test_class(QObject):
    update_label_signal = pyqtSignal(object, str)  # Signal to send label and text
    finish_signal = pyqtSignal()  # Signal to send label and text
    update_button_signal = pyqtSignal(object, int)  # Signal to send label and text

    def __init__(self,
                 relay_test_button, relay_data_label,
                 fan_test_button, fan_data_label,
                 general_functions):
        super().__init__()

        self.update_button_signal.connect(general_functions[0])
        self.relay_test_button = relay_test_button
        self.relay_data_label = relay_data_label
        self.fan_test_button = fan_test_button
        self.fan_data_label = fan_data_label
        self.relay_data_label.setWordWrap(True)
        self.fan_data_label.setWordWrap(True)


        self.fetch_canbus_data = general_functions[1]
        self.send_can_message = general_functions[2]
        self.update_label_signal.connect(general_functions[3])
        self.finish_signal = general_functions[4]
        self.manual_fetch = general_functions[5]
        self.get_can_state = general_functions[6]
        self.update_text()





    def update_text(self):
        """Emit a signal to update the label's text."""
        self.update_label_signal.emit(self.relay_data_label, "make sure the BMS data is valid (bottom microcontroller test's \"error count\" register) and not currently charging")
        self.update_label_signal.emit(self.fan_data_label, "listen closely for the fan sounds")
        pass
        # self.update_label_signal.emit(self.data_label_object, self.test_results)
        # self.update_label_signal.emit(self.passfail_label_object, self.passfail)

    def finish_test(self):
        self.finish_signal()

    def relay_test(self):
        self.update_label_signal.emit(self.relay_data_label, "you should hear the relay switching now, make sure the BMS data is valid (bottom microcontroller test's \"error count\" register) and not currently charging")
        for x in range(5):
            self.update_button_signal.emit(self.relay_test_button, (x*20) + 10)
            self.send_can_message(0x104, [0x43, 0x52, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x00], 0)
            time.sleep(0.2)
            self.update_button_signal.emit(self.relay_test_button, (x+1)*20)
            self.send_can_message(0x104, [0x43, 0x52, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], 0)
            time.sleep(0.2)

        self.update_button_signal.emit(self.relay_test_button, 0)
        self.finish_test()
        self.update_label_signal.emit(self.relay_data_label, "TEST COMPLETE, if you did not year the relay, please make sure the BMS data is valid (bottom microcontroller test's \"error count\" register) and not currently charging")

        return 1

    def fan_test(self):
        self.update_label_signal.emit(self.fan_data_label, "you should hear the fan start spinning now")
        for x in range(20):
            self.update_button_signal.emit(self.fan_test_button, x*5)
            self.send_can_message(0x104, [0x21, 0x54, 0x54, 0x30, 0x3A, 0x30, 0x2E, 0x30], 0)
            time.sleep(0.1)
        self.update_button_signal.emit(self.fan_test_button, 0)
        self.finish_test()
        self.update_label_signal.emit(self.fan_data_label, "TEST COMPLETE, fan noise should go back down")
        for x in range(5):
            self.send_can_message(0x104, [0x21, 0x54, 0x54, 0x30, 0x33, 0x30, 0x2E, 0x30], 0)
            time.sleep(0.05)
        return 1

    def run_test(self, var):
        if (var == 0):
            self.relay_test()

        elif (var == 1):
            self.fan_test()

        self.finish_test()
        return 1

    def reset_test(self):
        pass










# End of physical_test_class_def.py

# Start of top_test_class.py


class top_test_data(QObject):
    update_label_signal = pyqtSignal(object, str)  # Signal to send label and text
    update_button_signal = pyqtSignal(object, int)  # Signal to send label and text

    def __init__(self, temp1, temp2, temp3, temp4, data_label, passfail_label, button_object, general_functions):
        super().__init__()
        self.update_button_signal.connect(general_functions[0])
        self.button_object = button_object
        self.data_label_object = data_label
        self.data_label_object.setWordWrap(True)
        self.passfail_label_object = passfail_label
        self.passfail_label_object.setWordWrap(True)
        self.fetch_canbus_data = general_functions[1]
        self.send_can_message = general_functions[2]
        self.update_label_signal.connect(general_functions[3])
        self.finish_signal = general_functions[4]
        self.temp1_label = temp1
        self.temp2_label = temp2
        self.temp3_label = temp3
        self.temp4_label = temp4
        self.test_registers_list = [
            self.temp1_label,
            self.temp2_label,
            self.temp3_label,
            self.temp4_label
        ]
        self.tests_data = [0,0,0,0]
        self.tests_fails = [0,0,0,0]
        self.test_results = "not run yet"
        self.passfail = "unknown"
        self.update_results()




    def update_results(self):
        """Emit a signal to update the label's text."""
        self.update_label_signal.emit(self.data_label_object, self.test_results)
        self.update_label_signal.emit(self.passfail_label_object, self.passfail)

    def finish_test(self):
        self.finish_signal()


    def make_passfail(self):
        self.test_results = ""
        timeout_cnt = 0
        existing_temp_cnt = 0
        found_indexes = []
        for register_index in range(len(self.test_registers_list)):
            self.test_registers_list[register_index].make_passfail()
            if self.tests_fails[register_index]:
                timeout_cnt += 1
            elif "FAIL" in self.test_registers_list[register_index].passfail:
                self.passfail = "FAIL"
            else:
                existing_temp_cnt += 1
                found_indexes.append(register_index)

        if (timeout_cnt > 0):
            if (timeout_cnt == len(self.test_registers_list)):
                self.test_results = "FAILED, ALL REQUESTS TIMED OUT, NO DATA RECEIVED FROM TOP MICROCONTROLLER"
                self.passfail = "FAIL"
                return
            else:
                self.test_results = "HAD SOME TIMEOUTS, TRY RUNNING THE TEST AGAIN"
                self.passfail = "FAIL"

        if (existing_temp_cnt == 0):
            self.test_results = "FAILED: found "+ str(existing_temp_cnt)+"/"+str(len(self.test_registers_list))+" possible temperature sensors."
            first = 1
            for found_index in found_indexes:
                if not first:
                    self.test_results += ", "
                first = 0
                self.test_results += self.test_registers_list[found_index].name

        elif (existing_temp_cnt < len(self.test_registers_list)):
            self.passfail = "UNKNOWN, check sensor count and verify that head and chest LEDs start working "
            self.test_results = "found "+ str(existing_temp_cnt)+"/"+str(len(self.test_registers_list))+" possible temperature sensors. found in slots: \n"
            first = 1
            for found_index in found_indexes:
                if not first:
                    self.test_results += "\n, "
                first = 0
                self.test_results += self.test_registers_list[found_index].name

        elif self.test_results == "":
            self.test_results = ""
            self.passfail = "PASS"


    def reset_test(self):
        self.test_results = ""
        self.tests_data = [0,0,0,0]
        self.tests_fails = [0,0,0,0]

    def run_test(self, var):  # testing the bottom uCs
        for register_index in range(len(self.test_registers_list)):
            self.update_button_signal.emit(self.button_object,((register_index) * 100) / len(self.test_registers_list))

            timeout, data = self.fetch_canbus_data(self.test_registers_list[register_index].device_id,self.test_registers_list[register_index].reg_id, 205000, 0)
            time.sleep(0.1)
            if (timeout):
                self.tests_fails[register_index] = 1
            else:
                self.tests_fails[register_index] = 0
            self.tests_data[register_index] = str(self.test_registers_list[register_index].make_data_not_text(data))

        self.send_can_message(0x103, [0x48, 0x4C, 0x03, 0x07, 0x20, 0x80, 0x00, 0x80], 0)
        time.sleep(0.1)
        self.send_can_message(0x103, [0x43, 0x4C, 0x03, 0x04, 0x20, 0x80, 0x00, 0x80], 0)

        self.update_button_signal.emit(self.button_object, 0)
        self.make_passfail()
        time.sleep(0.1)
        self.update_results()
        self.finish_test()
        return 1


# End of top_test_class.py

# Start of main.py








class MainWindow(QMainWindow):
    data1 = 0
    def __init__(self):
        super().__init__()
        self.ui = Ui_qt_designer_save1()
        self.ui.setupUi(self)
        self.current_test = 0

        # Signal from CANBusWorker



        # self.ui.pushButton_5.clicked.connect(lambda: self.prev_page(self.ui.stackedWidget_2))
        # self.ui.pushButton_6.clicked.connect(lambda: self.next_page(self.ui.stackedWidget_2))

        # Connect buttons to switch pages
        #self.label1_entry = data_entry(self.ui.label, "buttons", 'binary', 0x104, 0x52, self.update_label, 0, 0)
        # self.label2_entry = data_entry(self.ui.label_2, "voltage(2s)", '2s compliment', 0x104, 0x1F, self.update_label)
        # self.label3_entry = data_entry(self.ui.label_3, "pct", 'decimal', 0x104, 0x22, self.update_label, 1, 100)

        # connect buttons to their functions
        self.define_buttons()

        # create all register definitions
        self.all_registers = all_data_entries_class(self.update_label, self.ui)

        self.all_menu_buttons = [self.ui.pushButton,
                                 self.ui.pushButton_2,
                                 self.ui.tests_page_microcontrollers_button,
                                 self.ui.tests_page_motors_button,
                                 self.ui.tests_page_physical_button,
                                 self.ui.read_battery,
                                 self.ui.read_battery_full,
                                 self.ui.read_versions,
                                 self.ui.read_buttons,
                                 self.ui.read_nicla,
                                 self.ui.read_SRF_temp,
                                 self.ui.pushButton_3,
                                 self.ui.manual_page_leds_select,
                                 self.ui.manual_page_motors_select]

        self.current_main_button = self.ui.pushButton
        self.current_sub_button = self.ui.tests_page_microcontrollers_button


        self.general_functions = [self.update_button_color_running,
                                  self.fetch_canbus_main,
                                  self.send_canbus_main,
                                  self.update_label,
                                  self.finish_test,
                                  self.manual_can_fetch_main,
                                  self.get_can_state,
                                  self.update_canstate_labels,
                                  self.color_selected_menu_buttons]


        self.all_motors = all_motor_class()

        self.leds_object = leds_class(self.ui.manual_leds_slider_red, self.ui.manual_leds_slider_green, self.ui.manual_leds_slider_blue,
                                      self.ui.manual_leds_color_show, self.ui.manual_leds_color_white, self.ui.manual_leds_color_green,
                                      self.ui.manual_leds_color_blue, self.ui.manual_leds_color_red, self.ui.manual_leds_color_purple, self.ui.manual_leds_color_turquoise,
                                      self.ui.manual_head_leds_off, self.ui.manual_head_leds_wave, self.ui.manual_head_leds_eyes, self.ui.manual_head_leds_full,
                                      self.ui.manual_chest_leds_off, self.ui.manual_chest_leds_blink, self.ui.manual_chest_leds_loading, self.ui.manual_chest_leds_full,
                                      self.general_functions)

        self.physical_tests = physical_test_class(self.ui.test_relay_button, self.ui.test_relay_label,
                                                  self.ui.test_fan_button, self.ui.test_fan_label, self.general_functions)


        self.make_tests()
        self.insert_test_variables()
        self.change_page(self.ui.stackedWidget, 1)
        self.change_page(self.ui.stackedWidget_2, 0)

        # self.make_motors()

        self.bad_can_vars = bad_can_variables_class(self.ui.general_messages_label, self.ui.can0_status_label, self.ui.can0_connect_button, self.ui.can1_status_label, self.ui.can1_connect_button, self.ui.canbus_good_label, self.ui.canbus_continue, self.ui.stackedWidget_main)
        # Start the CAN bus worker
        self.worker_thread = QThread()
        self.canbus_worker = CANBusWorker(self.get_current_page, self.get_current_subpage, self.get_current_test, self.all_registers.data_entries, self.test_variables, self.update_button_color_running, self.bad_can_vars, self.update_canstate_labels)



        self.canbus_worker.moveToThread(self.worker_thread)

        # Connect CANBusWorker signals

        self.worker_thread.started.connect(self.canbus_worker.run)
        self.worker_thread.start()

        # Clean up when the application closes
        self.destroyed.connect(self.cleanup)

    def get_current_page(self):
        """Return the current page index of the stacked widget."""
        return self.ui.stackedWidget.currentIndex()

    def get_can_state(self):
        """Return the current page index of the stacked widget."""
        return [self.canbus_worker.can_running0, self.canbus_worker.can_running1]

    def get_current_test(self):
        """Return the current running test."""
        if (not self.ui.stackedWidget.currentIndex() == 0):
            self.current_test = 0
        return self.current_test

    def get_current_subpage(self):
        # Traverse through all child widgets of 'self.stackedWidget'
        current_widget = self.ui.stackedWidget.currentWidget()
        if not current_widget:
            return 0  # Return -1 if no widget is displayed
        # Safely search for a nested QStackedWidget in the current widget
        sub_stack = current_widget.findChild(QtWidgets.QStackedWidget)
        if sub_stack:
            # Return the current index of the sub stacked widget (the nested QStackedWidget)
            return sub_stack.currentIndex()
        else:
            return 0  # Return -1 if no nested QStackedWidget is found

    def send_can(self, arbitration_id, data):
        """Send CAN data through the worker."""
        if self.worker_thread.isRunning():
            self.canbus_worker.send_can_message(arbitration_id, data)
        else:
            print("CAN worker thread is not running.")

    def update_label(self, label_object, text):
        """Update the label's text."""
        label_object.setText(text)
        if ("PASS" in text):
            label_object.setStyleSheet("color: green;")
        elif ("FAIL" in text):
            label_object.setStyleSheet("color: red;")
        elif ("UNKNOWN" in (text).upper()):
            label_object.setStyleSheet("color: blue;")
        else:
            label_object.setStyleSheet("color: black;")
        if ("FAIL" in text and "PASS" in text):
            label_object.setStyleSheet("color: blue;")

    def update_canstate_labels(self):
        """Update the label's text."""
        canstate0, canstate1 = self.get_can_state()
        if (canstate0 == 0):
            self.ui.test_wheels.setStyleSheet("color: red;")
            self.ui.test_wheels.setText("  test wheels (NO CAN0)  ")
            self.ui.test_nicla_communications.setStyleSheet("color: red;")
            self.ui.test_nicla_communications.setText("  nicla communication test  " + "\n(NO CAN0)")
            self.ui.test_bottom_uc.setStyleSheet("color: red;")
            self.ui.test_bottom_uc.setText("  test bottom uC  " + "\n(NO CAN0)")
            self.ui.test_top_uc.setStyleSheet("color: red;")
            self.ui.test_top_uc.setText("  test top uC  " + "\n(NO CAN0)")
            self.ui.motor_cart_big_open          .setStyleSheet("color: red;")
            self.ui.motor_cart_small_open        .setStyleSheet("color: red;")
            self.ui.motor_cart_stop              .setStyleSheet("color: red;")
            self.ui.motor_cart_small_close       .setStyleSheet("color: red;")
            self.ui.motor_cart_big_close         .setStyleSheet("color: red;")
        else:
            self.ui.test_wheels.setStyleSheet("color: black;")
            self.ui.test_wheels.setText("  test wheels  ")
            self.ui.test_nicla_communications.setStyleSheet("color: black;")
            self.ui.test_nicla_communications.setText("  nicla communication test  ")
            self.ui.test_bottom_uc.setStyleSheet("color: black;")
            self.ui.test_bottom_uc.setText("  test bottom uC  ")
            self.ui.test_top_uc.setStyleSheet("color: black;")
            self.ui.test_top_uc.setText("  test top uC  ")
            self.ui.motor_cart_big_open.setStyleSheet("color: black;")
            self.ui.motor_cart_small_open.setStyleSheet("color: black;")
            self.ui.motor_cart_stop.setStyleSheet("color: black;")
            self.ui.motor_cart_small_close.setStyleSheet("color: black;")
            self.ui.motor_cart_big_close.setStyleSheet("color: black;")
        if (canstate1 == 0 or "win" in platform):
            self.ui.test_right_arm.setStyleSheet("color: red;")
            self.ui.test_right_arm.setText("  test right arm   \n(NO CAN1, run on CAN0)")
            self.ui.test_left_arm.setStyleSheet("color: red;")
            self.ui.test_left_arm.setText("  test left arm   \n(NO CAN1, run on CAN0)")

            self.ui.motor_right_linear_big_up.setStyleSheet("color: red;")
            self.ui.motor_right_linear_small_up.setStyleSheet("color: red;")
            self.ui.motor_right_linear_stop.setStyleSheet("color: red;")
            self.ui.motor_right_linear_small_down.setStyleSheet("color: red;")
            self.ui.motor_right_linear_big_down.setStyleSheet("color: red;")

            self.ui.motor_left_linear_big_up.setStyleSheet("color: red;")
            self.ui.motor_left_linear_small_up.setStyleSheet("color: red;")
            self.ui.motor_left_linear_stop.setStyleSheet("color: red;")
            self.ui.motor_left_linear_small_down.setStyleSheet("color: red;")
            self.ui.motor_left_linear_big_down.setStyleSheet("color: red;")

        else:
            self.ui.test_right_arm.setStyleSheet("color: black;")
            self.ui.test_right_arm.setText("  test right arm  ")
            self.ui.test_left_arm.setStyleSheet("color: black;")
            self.ui.test_left_arm.setText("  test left arm  ")
            self.ui.motor_right_linear_big_up.setStyleSheet("color: black;")
            self.ui.motor_right_linear_small_up.setStyleSheet("color: black;")
            self.ui.motor_right_linear_stop.setStyleSheet("color: black;")
            self.ui.motor_right_linear_small_down.setStyleSheet("color: black;")
            self.ui.motor_right_linear_big_down.setStyleSheet("color: black;")

            self.ui.motor_left_linear_big_up.setStyleSheet("color: black;")
            self.ui.motor_left_linear_small_up.setStyleSheet("color: black;")
            self.ui.motor_left_linear_stop.setStyleSheet("color: black;")
            self.ui.motor_left_linear_small_down.setStyleSheet("color: black;")
            self.ui.motor_left_linear_big_down.setStyleSheet("color: black;")



    def finish_test(self):
        self.current_test = 0

    def prev_page(self, page_object):
        next_page = page_object.currentIndex()
        if next_page == 0:
            next_page = page_object.count()-1
        else:
            next_page -= 1
        page_object.setCurrentIndex(next_page)

    def next_page(self, page_object):
        next_page = page_object.currentIndex()
        if next_page == page_object.count()-1:
            next_page = 0
        else:
            next_page += 1
        page_object.setCurrentIndex(next_page)


    def cleanup(self):
        """Stop the worker thread."""
        self.canbus_worker.stop()
        self.worker_thread.quit()
        self.worker_thread.wait()

    def force_retry_can(self):
        self.ui.stackedWidget_main.setCurrentIndex(0)
        self.canbus_worker.forced_no_can = 0
        self.canbus_worker.force_can_page_back()

    def get_current_menu_buttons(self):
        current_main_index = self.ui.stackedWidget.currentIndex()
        current_sub_index = self.ui.tests_stack_widget.currentIndex()
        current_main_button = self.ui.pushButton
        current_sub_button = self.ui.tests_page_physical_button
        if (current_main_index == 0):
            current_main_button = self.ui.pushButton
            current_sub_index = self.ui.tests_stack_widget.currentIndex()
            if (current_sub_index == 0):
                current_sub_button = self.ui.tests_page_microcontrollers_button
            elif (current_sub_index == 1):
                current_sub_button = self.ui.tests_page_motors_button
            elif (current_sub_index == 2):
                current_sub_button = self.ui.tests_page_physical_button

        elif (current_main_index == 1):
            current_main_button = self.ui.pushButton_2
            current_sub_index = self.ui.stackedWidget_2.currentIndex()
            if (current_sub_index == 0):
                current_sub_button = self.ui.read_battery
            elif (current_sub_index == 1):
                current_sub_button = self.ui.read_battery_full
            elif (current_sub_index == 2):
                current_sub_button = self.ui.read_versions
            elif (current_sub_index == 3):
                current_sub_button = self.ui.read_buttons
            elif (current_sub_index == 4):
                current_sub_button = self.ui.read_nicla
            elif (current_sub_index == 5):
                current_sub_button = self.ui.read_SRF_temp

        elif (current_main_index == 2):
            current_main_button = self.ui.pushButton_3
            current_sub_index = self.ui.manual_control_stack.currentIndex()
            if (current_sub_index == 0):
                current_sub_button = self.ui.manual_page_leds_select
            elif (current_sub_index == 1):
                current_sub_button = self.ui.manual_page_motors_select
        self.current_main_button = current_main_button
        self.current_sub_button = current_sub_button
        return [current_main_button, current_sub_button]

    def color_selected_menu_buttons(self):
        prev_main_button = self.current_main_button
        prev_sub_button = self.current_sub_button
        current_main_button, current_sub_button = self.get_current_menu_buttons()
        if prev_main_button == current_main_button and prev_sub_button == current_sub_button:
            return
        for button in (self.all_menu_buttons):
            button.setStyleSheet("background-color: rgb(255, 255, 255);")
        current_main_button, current_sub_button = self.get_current_menu_buttons()
        current_main_button.setStyleSheet("background-color: rgb(173, 216, 230);")
        current_sub_button.setStyleSheet("background-color: rgb(173, 216, 230);")


    def change_page(self, widget, index):
        widget.setCurrentIndex(index)
        self.color_selected_menu_buttons()


    def define_buttons(self):
        #main menu buttons
        self.ui.pushButton.clicked.connect(lambda: self.change_page(self.ui.stackedWidget, 0))
        self.ui.pushButton_2.clicked.connect(lambda: self.change_page(self.ui.stackedWidget, 1))
        self.ui.pushButton_3.clicked.connect(lambda: self.change_page(self.ui.stackedWidget, 2))

        #test menu buttons
        self.ui.tests_page_motors_button.clicked.connect(lambda: self.change_page(self.ui.tests_stack_widget, 1))
        self.ui.tests_page_microcontrollers_button.clicked.connect(lambda: self.change_page(self.ui.tests_stack_widget, 0))
        self.ui.tests_page_physical_button.clicked.connect(lambda: self.change_page(self.ui.tests_stack_widget, 2))

        #canbus button
        self.ui.canbus_states_button.clicked.connect(lambda: self.force_retry_can())

        #manual control buttons
        self.ui.manual_page_leds_select.clicked.connect(lambda: self.change_page(self.ui.manual_control_stack, 0))
        self.ui.manual_page_motors_select.clicked.connect(lambda: self.change_page(self.ui.manual_control_stack, 1))



        #test activation buttons
        self.ui.test_nicla_communications.clicked.connect(lambda: self.set_test(1))
        self.ui.test_bottom_uc.clicked.connect(lambda: self.set_test(2))
        self.ui.test_top_uc.clicked.connect(lambda: self.set_test(3))
        self.ui.test_wheels.clicked.connect(lambda: self.set_test(4))
        self.ui.test_left_arm.clicked.connect(lambda: self.set_test(5))
        self.ui.test_right_arm.clicked.connect(lambda: self.set_test(6))
        self.ui.test_relay_button.clicked.connect(lambda: self.set_test(7))
        self.ui.test_fan_button.clicked.connect(lambda: self.set_test(8))
        self.ui.tests_motors_arms_61_on.clicked.connect(lambda: self.send_can(0x103, [0x4D, 0x50, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x00]))
        self.ui.tests_motors_arms_61_off.clicked.connect(lambda: self.send_can(0x103, [0x4D, 0x50, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))
        self.ui.tests_motors_wheels_61_on.clicked.connect(lambda: self.send_can(0x104, [0x4D, 0x50, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x00]))
        self.ui.tests_motors_wheels_61_off.clicked.connect(lambda: self.send_can(0x104, [0x4D, 0x50, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))


        #"read data" sub-menu buttons
        self.ui.read_battery.clicked.connect(lambda: self.change_page(self.ui.stackedWidget_2, 0))
        self.ui.read_battery_full.clicked.connect(lambda: self.change_page(self.ui.stackedWidget_2, 1))
        self.ui.read_versions.clicked.connect(lambda: self.change_page(self.ui.stackedWidget_2, 2))
        self.ui.read_buttons.clicked.connect(lambda: self.change_page(self.ui.stackedWidget_2, 3))
        self.ui.read_nicla.clicked.connect(lambda: self.change_page(self.ui.stackedWidget_2, 4))
        self.ui.read_SRF_temp.clicked.connect(lambda: self.change_page(self.ui.stackedWidget_2, 5))

        #test send button
        self.ui.motor_spin_button_fl.clicked.connect(lambda: self.motor_test_object.move_wheel(0,0))
        self.ui.motor_stop_button_fl.clicked.connect(lambda: self.motor_test_object.move_wheel(0,1))
        self.ui.motor_reverse_button_fl.clicked.connect(lambda: self.motor_test_object.move_wheel(0,2))

        self.ui.motor_spin_button_rl.clicked.connect(lambda: self.motor_test_object.move_wheel(1,0))
        self.ui.motor_stop_button_rl.clicked.connect(lambda: self.motor_test_object.move_wheel(1,1))
        self.ui.motor_reverse_button_rl.clicked.connect(lambda: self.motor_test_object.move_wheel(1,2))

        self.ui.motor_spin_button_fr.clicked.connect(lambda: self.motor_test_object.move_wheel(2,0))
        self.ui.motor_stop_button_fr.clicked.connect(lambda: self.motor_test_object.move_wheel(2,1))
        self.ui.motor_reverse_button_fr.clicked.connect(lambda: self.motor_test_object.move_wheel(2,2))

        self.ui.motor_spin_button_rr.clicked.connect(lambda: self.motor_test_object.move_wheel(3,0))
        self.ui.motor_stop_button_rr.clicked.connect(lambda: self.motor_test_object.move_wheel(3,1))
        self.ui.motor_reverse_button_rr.clicked.connect(lambda: self.motor_test_object.move_wheel(3,2))

        self.ui.motor_right_linear_big_up.clicked.connect(lambda: self.motor_test_object.move_step(0,4))
        self.ui.motor_right_linear_small_up.clicked.connect(lambda: self.motor_test_object.move_step(0,3))
        self.ui.motor_right_linear_stop.clicked.connect(lambda: self.motor_test_object.move_step(0,2))
        self.ui.motor_right_linear_small_down.clicked.connect(lambda: self.motor_test_object.move_step(0,1))
        self.ui.motor_right_linear_big_down.clicked.connect(lambda: self.motor_test_object.move_step(0,0))

        self.ui.motor_left_linear_big_up.clicked.connect(lambda: self.motor_test_object.move_step(1,4))
        self.ui.motor_left_linear_small_up.clicked.connect(lambda: self.motor_test_object.move_step(1,3))
        self.ui.motor_left_linear_stop.clicked.connect(lambda: self.motor_test_object.move_step(1,2))
        self.ui.motor_left_linear_small_down.clicked.connect(lambda: self.motor_test_object.move_step(1,1))
        self.ui.motor_left_linear_big_down.clicked.connect(lambda: self.motor_test_object.move_step(1,0))

        self.ui.motor_cart_big_open.clicked.connect(lambda: self.motor_test_object.move_step(2,0))
        self.ui.motor_cart_small_open.clicked.connect(lambda: self.motor_test_object.move_step(2,1))
        self.ui.motor_cart_stop.clicked.connect(lambda: self.motor_test_object.move_step(2,2))
        self.ui.motor_cart_small_close.clicked.connect(lambda: self.motor_test_object.move_step(2,3))
        self.ui.motor_cart_big_close.clicked.connect(lambda: self.motor_test_object.move_step(2,4))

        # motor_select:  0-right, 1-left, 2-cart.
        # move_direction: 0-up/open big, 1-up/open small, 2-stop, 3-down/close small, 4-down/close big.

        #"read data" state control buttons
        self.ui.states_relay_on.clicked.connect(lambda: self.send_can(0x104, [0x43, 0x52, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x00]))
        self.ui.states_relay_off.clicked.connect(lambda: self.send_can(0x104, [0x43, 0x52, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))
        self.ui.states_arms_61_on.clicked.connect(lambda: self.send_can(0x103, [0x4D, 0x50, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x00]))
        self.ui.states_arms_61_off.clicked.connect(lambda: self.send_can(0x103, [0x4D, 0x50, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))
        self.ui.states_wheels_61_on.clicked.connect(lambda: self.send_can(0x104, [0x4D, 0x50, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x00]))
        self.ui.states_wheels_61_off.clicked.connect(lambda: self.send_can(0x104, [0x4D, 0x50, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]))

    def set_test(self, test_number):
        if not (self.current_test == 0):
            return
        self.test_variables[test_number][0].reset_test()
        self.current_test = test_number

    def fetch_canbus_main(self,device_id,reg_id,timeout, can_selector):
        return self.canbus_worker.fetch_canbus_data_top(device_id, reg_id, timeout, can_selector)

    def send_canbus_main(self,arbitration_id, data, can_selector):
        return self.canbus_worker.send_can_message_top(arbitration_id, data, can_selector)

    def manual_can_fetch_main (self, request_message, reply_id, reply_first_byte, timeout, can_select):
        return self.canbus_worker.manual_can_fetch(request_message, reply_id, reply_first_byte, timeout, can_select)

    def make_tests(self):
        self.nicla_test_object = nicla_test_data( self.ui.test_nicla_communications_passfail, self.ui.test_nicla_communications_data, self.ui.test_nicla_communications, self.general_functions)
        self.bottom_test_object = bottom_test_data(self.all_registers.label_srftemp_srf1, self.all_registers.label_srftemp_srf2, self.all_registers.label_bat_percentage, self.all_registers.label_bat_voltage, self.all_registers.label_bat_error_count, self.ui.test_bottom_uc_data, self.ui.test_bottom_uc_passfail, self.ui.test_bottom_uc, self.general_functions)
        self.top_test_object = top_test_data(self.all_registers.label_srftemp_temp1, self.all_registers.label_srftemp_temp2, self.all_registers.label_srftemp_temp3, self.all_registers.label_srftemp_temp4, self.ui.test_top_uc_data, self.ui.test_top_uc_passfail, self.ui.test_top_uc, self.general_functions)
        self.motor_test_object = motor_test_class(self.all_motors,
                                                  self.ui.test_wheels_data, self.ui.test_wheels,
                                                  self.ui.test_right_arm_data, self.ui.test_right_arm,
                                                  self.ui.test_left_arm_data, self.ui.test_left_arm,
                                                  self.general_functions, self.ui.general_messages_label_2)



    def insert_test_variables(self):
        self.test_variables = {
            0: [],
            1: [self.nicla_test_object, 0],
            2: [self.bottom_test_object, 0],
            3: [self.top_test_object, 0],
            4: [self.motor_test_object, 0],
            5: [self.motor_test_object, 1],
            6: [self.motor_test_object, 2],
            7: [self.physical_tests, 0],
            8: [self.physical_tests, 1]

            # 2: [wheel_test_object]
        }
    def getcolor(self, stylesheet):
        if not "color:" in stylesheet:
            return "black"
        return ((stylesheet.split("color:")[1]).split(";")[0]).strip()

    def update_button_color_running(self, button_object, running_pct):
        offset = 0.01
        running_pct = int(running_pct)
        if (running_pct == 0):
            offset = 0
        if (running_pct == 100):
            button_object.setStyleSheet(f"""
                    QPushButton {{background: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 blue,  stop: 1 blue);
                    color: {self.getcolor(button_object.styleSheet())};
                    border: 1px  solid gray;
                    border-radius: 5px;}}
                """)
        else:
            button_object.setStyleSheet(f"""
                    QPushButton {{background: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 blue,  stop: {running_pct / 100} blue, stop: {(running_pct / 100)+offset} white, stop: 1 white );
                    color: {self.getcolor(button_object.styleSheet())};
                    border: 1px  solid gray;
                    border-radius: 5px;}}
                """)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())




















# End of main.py

