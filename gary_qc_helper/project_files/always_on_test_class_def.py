
from PyQt5.QtCore import QObject, QThread, pyqtSignal
import struct
from data_entries import data_entry
import time
import can

class always_on_test_class(QObject):
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
        self.manual_fetch_no_passive = general_functions[9]

        self.test_results = "not run yet"
        self.passfail = "unknown"
        self.update_results()




    def update_results(self):
        """Emit a signal to update the label's text."""
        self.update_label_signal.emit(self.data_label_object, self.test_results)
        self.update_label_signal.emit(self.passfail_label_object, self.passfail)

    def finish_test(self):
        self.finish_signal()

    def reset_test(self):
        self.test_results = ""

    def make_feedback_request(self):
        return can.Message(arbitration_id=0x101, data=[0x47, 0x46, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)

    def make_top_reset_request(self):
        return can.Message(arbitration_id=0x101, data=[0x52, 0x50, 0x01, 0x00, 0x00, 0x00, 0x00, 0x14], is_extended_id=False)

    def make_top_reg_request(self):
        return can.Message(arbitration_id=0x103, data=[0x53, 0x53, 0x02, 0x60, 0x60, 0x03, 0x00, 0x00], is_extended_id=False)

    def make_bot_reset_request(self):
        return can.Message(arbitration_id=0x101, data=[0x52, 0x50, 0x02, 0x00, 0x00, 0x00, 0x00, 0x14], is_extended_id=False)

    def make_bot_reg_request(self):
        return can.Message(arbitration_id=0x104, data=[0x53, 0x53, 0x02, 0x61, 0x61, 0x03, 0x00, 0x00], is_extended_id=False)

    def make_result(self, stage):
        self.passfail = "FAIL"
        if (stage == 0):
            self.test_results = "FAIL: no response from always on board"
        elif (stage == 1):
            self.test_results = "FAIL: top microcontroller not off after request"
        elif (stage == 2):
            self.test_results = "FAIL: bottom microcontroller not off after request"
        elif (stage == 3):
            self.test_results = "FAIL: top microcontroller not on after restart"
        elif (stage == 4):
            self.test_results = "FAIL: bottom microcontroller not on after restart"
        else:
            self.test_results = "PASS"
            self.passfail = "PASS"
        self.update_results()

    def test_always_on_response(self):
        for x in range(3):
            failed, data = self.manual_fetch_no_passive(self.make_feedback_request(), 0x106, 0x47, 0x46, 1, 5000, 0)

            if failed:  # if timed out, return 0
                continue
            else:
                return 1
        return 0

    def test_top_reply(self):
        for x in range(3):
            failed, data = self.manual_fetch_no_passive(self.make_top_reg_request(), 0x105, 0x60, 0x00, 0, 7000, 0)
            if failed:  # if timed out, return 0
                continue
            else:
                return 0
        return 1

    def test_top_reset(self):
        message = self.make_top_reset_request()
        self.send_can_message(message.arbitration_id, message.data, 0)
        time.sleep(0.2)
        return self.test_top_reply()

    def test_bot_reply(self):
        for x in range(3):
            failed, data = self.manual_fetch_no_passive(self.make_bot_reg_request(), 0x105, 0x60, 0x00, 0, 7000, 0)
            if failed:  # if timed out, return 0
                continue
            else:
                return 0
        return 1

    def test_bot_reset(self):
        message = self.make_bot_reset_request()
        self.send_can_message(message.arbitration_id, message.data, 0)
        time.sleep(0.2)
        return self.test_bot_reply()


    def run_test(self,var):  # testing the various functions
        fail_result = 99
        self.update_button_signal.emit(self.button_object, 15)
        if not (self.test_always_on_response()):
            fail_result = 0
        else:
            self.update_button_signal.emit(self.button_object, 30)
            if not (self.test_top_reset()):
                fail_result = 1
            else:
                if not (self.test_bot_reset()):
                    fail_result = 2
                else:
                    self.update_button_signal.emit(self.button_object, 45)
                    time.sleep(1)
                    self.update_button_signal.emit(self.button_object, 60)
                    time.sleep(1)
                    self.update_button_signal.emit(self.button_object, 75)
                    time.sleep(1)
                    if (self.test_top_reply()):
                        fail_result = 3
                    else:
                        self.update_button_signal.emit(self.button_object, 90)
                        if (self.test_bot_reply()):
                            fail_result = 4
        self.update_button_signal.emit(self.button_object, 0)
        self.make_result(fail_result)

        self.finish_test()
        return 0