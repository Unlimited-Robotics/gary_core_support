
from PyQt5.QtCore import QObject, QThread, pyqtSignal
import struct
import time
import datetime

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
