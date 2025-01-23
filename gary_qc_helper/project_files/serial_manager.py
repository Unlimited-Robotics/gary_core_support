
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow
from qt_design1 import Ui_qt_designer_save1  # Import your generated UI class
import serial
import datetime





class Serial_Worker(QObject):

    update_button_signal = pyqtSignal(object, int)  # Signal to send label and text
    update_canstate_labels_signal = pyqtSignal()  # Signal to send label and text

    def __init__(self, general_functions):
        super().__init__()
        self.running = True
        self.get_current_send = general_functions[11]
        self.set_current_received = general_functions[12]
        self.serial_port = 0
        self.message_types = [
             b'\x11\x11\x11\x11',
             b'\x33\x33\x33\x33',
             b'\x55\x55\x55\x55',
             b'\x77\x77\x77\x77',
             b'\xFF\xFF\xFF\xFF']
        self.serial_running = 0

    def setup_serial_interface(self):
        try:
            self.serial_port = serial.Serial(
                port="/dev/ttyTHS0",  # Using ttyTHS0
                baudrate=115200,
                bytesize=serial.EIGHTBITS,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
            )
            self.serial_running = 1
        except:
            self.serial_running = 0



    def run(self):
        self.setup_serial_interface()
        if (self.serial_running):
            self.send_time = self.get_time_delta([0,0,0])[1]
            self.serial_port.write(self.message_types[self.get_current_send])
        received = 999
        while self.running:
            if not (self.serial_running):
                continue
            received = self.get_incoming_message()
            if not received > 20:
                self.set_current_received(received)
            if (self.get_time_delta(self.send_time)[0] > 100000):
                self.send_time = self.get_time_delta([0,0,0])[1]
                print("thing")
                # self.serial_port.write(self.message_types[self.get_current_send])
        self.serial_port.close()



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

    # 0 =      PC DEAD
    # 1 =  STARTED PRESSED
    # 2 =   WAIT RESPONSE
    # 3 =   YES EMERGENCY
    # 4 =   SAFE PRESSED
    # 5 = EMERGENCY REQUEST
    # 6 =   NO EMERGENCY
    def get_incoming_message(self):
        incoming_emergency_state = 999
        if (self.serial_port == 0):
            return incoming_emergency_state
        if self.serial_port.inWaiting() > 0:
            data = self.serial_port.read()
            if ("00" in str(data.hex())):
                return 0
            elif ("01" in str(data.hex())):
                return 1
            elif ("03" in str(data.hex())):
                return 2
            elif ("05" in str(data.hex())):
                return 3
            elif ("07" in str(data.hex())):
                return 4
            elif ("0f" in str(data.hex())):
                return 5
            elif ("5f" in str(data.hex())):
                return 6
        return incoming_emergency_state