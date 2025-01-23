
from PyQt5.QtCore import QObject, QThread, pyqtSignal
import struct
from data_entries import data_entry
import time
import can
import serial
import datetime

class emergency_test_class(QObject):
    update_label_signal = pyqtSignal(object, str)  # Signal to send label and text
    update_button_signal = pyqtSignal(object, int)  # Signal to send label and text

    def __init__(self, button_object, data_label, passfail_label, general_functions):
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
        self.manual_fetch = general_functions[5]
        self.manual_fetch_no_passive = general_functions[9]

        self.get_serial_msg = general_functions[13]
        self.set_serial_send = general_functions[10]

        self.test_results = "not run yet"
        self.passfail = "unknown"
        self.update_results()


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

    def update_results(self):
        """Emit a signal to update the label's text."""
        self.update_label_signal.emit(self.data_label_object, self.test_results)
        self.update_label_signal.emit(self.passfail_label_object, self.passfail)

    def finish_test(self):
        self.finish_signal()

    def reset_test(self):
        self.test_results = ""

    def make_result(self, stage):
        self.passfail = "FAIL"
        self.test_results = "FAIL: no response from always on board"
        self.test_results = "PASS"
        self.passfail = "PASS"
        self.update_results()



    def send_while_waiting(self,time_to_wait):
        self.serial_port.write(self.message_types[self.currently_sending])
        start_time = self.get_time_delta([0, 0, 0])[1]
        time_send = self.get_time_delta(start_time)[1]
        while (self.get_time_delta(start_time)[0] < time_to_wait):
            if (self.get_time_delta(time_send)[0] > 1000):

                self.serial_port.write(self.message_types[self.currently_sending])
                time_send = self.get_time_delta(time_send)[1]

    def test_motor_reply(self, motor_object):
        for x in range(3):
            failed, data = self.manual_fetch(motor_object.make_request(), motor_object.motor_id,
                                             motor_object.request_type, 50000,
                                             motor_object.can_selector)  # request the register
            if failed:  # if timed out, return 0
                continue
            else:
                for data_idx in range(1, len(data)):
                    if not data[data_idx] == 0:
                        return 1
        return 0

    def test_wheels(self):
        #turn off wheel 6.1v
        self.send_can_message(0x104, [0x4D, 0x50, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], 0)
        self.send_while_waiting(100)
        self.send_can_message(0x104, [0x4D, 0x50, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], 0)
        self.send_while_waiting(1000)






    def run_test(self,var):  # testing the various functions
        self.currently_sending = 0

        self.setup_serial_interface()
        start_time = self.get_time_delta([0, 0, 0])[1]
        self.send_while_waiting(1000)
        incoming_message = self.get_incoming_message()
        if not (incoming_message == 6):
            if (incoming_message < 10):
                self.test_results = "EMERGENCY NOT RELEASED OR ANOTHER COMPONENT IS CAUSING ISSUES"
            else:
                self.test_results = "ERROR, NO MESSAGE RECEIVED FROM EMERGENCY BOARD VIA SERIAL"
            self.stop_test()
            return 1





        self.update_button_signal.emit(self.button_object, 0)
        self.make_result()

        self.finish_test()
        return 0