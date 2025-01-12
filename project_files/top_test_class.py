
from PyQt5.QtCore import QObject, QThread, pyqtSignal
import struct
from data_entries import data_entry
import time

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
