
from PyQt5.QtCore import QObject, QThread, pyqtSignal
import struct
from data_entries import data_entry
import time


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








