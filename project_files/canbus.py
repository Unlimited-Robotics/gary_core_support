
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow
from qt_design1 import Ui_qt_designer_save1  # Import your generated UI class
import can
import ctypes
import os
import struct
import can.interfaces.pcan
from sys import platform
import datetime
import time
from bad_can_page_variables import bad_can_variables_class






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
                    self.can_running1 = 1
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