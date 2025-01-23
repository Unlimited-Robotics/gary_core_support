
from PyQt5.QtCore import QObject, QThread, pyqtSignal
import can


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


