
from PyQt5.QtCore import QObject, QThread, pyqtSignal
import struct
from data_entries import data_entry
import time

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
                self.test_results += "HAD SOME TIMEOUTS, TRY RUNNING THE TEST AGAIN AND VERIFY THAT THE MICROCONTROLLER CODE IS AT LEAST V_2.69"

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



