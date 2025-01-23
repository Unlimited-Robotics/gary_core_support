

import sys
from sys import platform
from qt_design1 import Ui_qt_designer_save1
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from canbus import CANBusWorker
from nicla_test_class import nicla_test_data
from bottom_test_class import bottom_test_data
from top_test_class import top_test_data
from all_motors_class_def import all_motor_class
from motor_test_class import motor_test_class
from leds_class_def import leds_class
from physical_test_class_def import physical_test_class
from always_on_test_class_def import always_on_test_class

from all_data_entries import all_data_entries_class
from bad_can_page_variables import bad_can_variables_class

from PyQt5.QtCore import QObject, QThread, pyqtSignal
from PyQt5 import QtWidgets




class MainWindow(QMainWindow):
    data1 = 0
    def __init__(self):
        super().__init__()
        self.ui = Ui_qt_designer_save1()
        self.ui.setupUi(self)
        self.current_test = 0

        # Signal from CANBusWorker

        self.serial_message_to_send = 0


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
                                  self.color_selected_menu_buttons,
                                  self.manual_can_fetch_no_passive_main]


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
        self.worker_thread1 = QThread()
        self.worker_thread2 = QThread()

        self.canbus_worker = CANBusWorker(
            self.get_current_page,
            self.get_current_subpage,
            self.get_current_test,
            self.all_registers.data_entries,
            self.test_variables,
            self.update_button_color_running,
            self.bad_can_vars,
            self.update_canstate_labels
        )


        # Move each worker to its own thread
        self.canbus_worker.moveToThread(self.worker_thread1)

        # Connect signals for the first worker
        self.worker_thread1.started.connect(self.canbus_worker.run)
        self.destroyed.connect(self.worker_thread1.quit)
        self.destroyed.connect(self.worker_thread1.wait)


        # Start the threads
        self.worker_thread1.start()

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

        #extra buttons
        self.ui.canbus_states_button.clicked.connect(lambda: self.force_retry_can())
        self.ui.exit_button.clicked.connect(lambda: self.exit())

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
        self.ui.test_always.clicked.connect(lambda: self.set_test(9))

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

    def manual_can_fetch_no_passive_main (self, request_message, reply_id, reply_first_byte, reply_second_byte, second_byte_enable, timeout, can_select):
        return self.canbus_worker.manual_can_fetch_no_passive(request_message, reply_id, reply_first_byte, reply_second_byte, second_byte_enable, timeout, can_select)


    def make_tests(self):
        self.nicla_test_object = nicla_test_data( self.ui.test_nicla_communications_passfail, self.ui.test_nicla_communications_data, self.ui.test_nicla_communications, self.general_functions)
        self.bottom_test_object = bottom_test_data(self.all_registers.label_srftemp_srf1, self.all_registers.label_srftemp_srf2, self.all_registers.label_bat_percentage, self.all_registers.label_bat_voltage, self.all_registers.label_bat_error_count, self.ui.test_bottom_uc_data, self.ui.test_bottom_uc_passfail, self.ui.test_bottom_uc, self.general_functions)
        self.top_test_object = top_test_data(self.all_registers.label_srftemp_temp1, self.all_registers.label_srftemp_temp2, self.all_registers.label_srftemp_temp3, self.all_registers.label_srftemp_temp4, self.ui.test_top_uc_data, self.ui.test_top_uc_passfail, self.ui.test_top_uc, self.general_functions)
        self.motor_test_object = motor_test_class(self.all_motors,
                                                  self.ui.test_wheels_data, self.ui.test_wheels,
                                                  self.ui.test_right_arm_data, self.ui.test_right_arm,
                                                  self.ui.test_left_arm_data, self.ui.test_left_arm,
                                                  self.general_functions, self.ui.general_messages_label_2)
        self.always_on_test_object = always_on_test_class(self.ui.test_always, self.ui.test_always_data, self.ui.test_always_passfail, self.general_functions)



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
            8: [self.physical_tests, 1],
            9: [self.always_on_test_object,0]

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
    def exit(self):
        try:
            self.canbus_worker.bus0.shutdown()
            self.canbus_worker.bus1.shutdown()
        except:
            pass
        self.canbus_worker.stop()
        exit()
        self.destroyed.connect(self.cleanup)
        sys.exit(self.exec_())





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


















