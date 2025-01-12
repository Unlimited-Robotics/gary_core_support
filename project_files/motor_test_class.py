
from PyQt5.QtCore import QObject, QThread, pyqtSignal
import struct
import time
from sys import platform


class motor_test_class(QObject):
    update_label_signal = pyqtSignal(object, str)  # Signal to send label and text
    finish_signal = pyqtSignal()  # Signal to send label and text
    update_button_signal = pyqtSignal(object, int)  # Signal to send label and text

    def __init__(self, all_motors,
                 wheels_data_label, wheels_button_object,
                 right_data_label, right_button_object,
                 left_data_label, left_button_object,
                 general_functions, general_messages_label_2):
        super().__init__()
        self.all_motors_object = all_motors
        self.update_button_signal.connect(general_functions[0])
        self.wheels_data_label     = wheels_data_label
        self.wheels_button_object  = wheels_button_object
        self.right_data_label      = right_data_label
        self.right_button_object   = right_button_object
        self.left_data_label       = left_data_label
        self.left_button_object    = left_button_object
        self.general_messages_label_2 = general_messages_label_2

        self.general_messages_label_2.setWordWrap(True)
        self.wheels_data_label.setWordWrap(True)
        self.right_data_label.setWordWrap(True)
        self.left_data_label.setWordWrap(True)

        self.fetch_canbus_data = general_functions[1]
        self.send_can_message = general_functions[2]
        self.update_label_signal.connect(general_functions[3])
        self.finish_signal = general_functions[4]
        self.manual_fetch = general_functions[5]
        self.get_can_state = general_functions[6];
        self.test_results = "not run yet"
        self.passfail = "unknown"
        self.update_results()





    def update_results(self):
        """Emit a signal to update the label's text."""
        pass
        # self.update_label_signal.emit(self.data_label_object, self.test_results)
        # self.update_label_signal.emit(self.passfail_label_object, self.passfail)

    def finish_test(self):
        self.finish_signal()

    #return 1 if passed, 0 if failed
    def test_motor_reply(self, motor_object):
        for x in range(3):
            failed, data = self.manual_fetch(motor_object.make_request(), motor_object.motor_id, motor_object.request_type, 50000, motor_object.can_selector)  # request the register
            if failed:  # if timed out, return 0
                continue
            else:
                for data_idx in range(1, len(data)):
                    if not data[data_idx] == 0:
                        return 1
        return 0

    def test_list(self, motor_list, data_label, button):
        result_text = ""
        cnt = 0
        for motor_object in motor_list:
            cnt += 1
            result_text += motor_object.name
            if (self.test_motor_reply(motor_object)):
                result_text += ": PASSED (id:" + str(motor_object.motor_id) + ")\n\n"
            else:
                result_text += ": FAILED (id:" + str(motor_object.motor_id) + ")\n\n"
            self.update_label_signal.emit(data_label, result_text)
            self.update_button_signal.emit(button, int((cnt*100)/len(motor_list)))
        self.update_button_signal.emit(button, 0)
        self.update_label_signal.emit(data_label, result_text)


    def run_test(self, var):
        if (var == 0):
            self.test_list(self.all_motors_object.wheels_list, self.wheels_data_label, self.wheels_button_object)

        elif (var == 1):
            self.test_list(self.all_motors_object.Left_arm_list, self.left_data_label, self.left_button_object)

        elif (var == 2):
            self.test_list(self.all_motors_object.Right_arm_list, self.right_data_label, self.right_button_object)

        self.finish_test()
        return 1

    def reset_test(self):
        self.test_results = ""

    #motor_select:  0-FL, 1-RL, 2-FR, 3-RR.
    #move_direction: 0-forwards, 1-stop, 2-reverse.
    def move_wheel(self, motor_select, move_direction):
        motor_to_move = self.all_motors_object.wheels_list[motor_select]
        if (motor_select <= 1):
            if move_direction == 0:
                message_to_send = motor_to_move.make_spin()
            elif move_direction == 2:
                message_to_send = motor_to_move.make_reverse()
            else:
                message_to_send = motor_to_move.make_stop()
        else:
            if move_direction == 0:
                message_to_send = motor_to_move.make_reverse()
            elif move_direction == 2:
                message_to_send = motor_to_move.make_spin()
            else:
                message_to_send = motor_to_move.make_stop()
        self.send_can_message(message_to_send.arbitration_id, message_to_send.data, motor_to_move.can_selector)

    #motor_select:  0-right, 1-left, 2-cart.
    #move_direction: 0-down/open big, 1-down/open small, 2-stop, 3-up/close small, 4-up/close big.
    def move_step(self, motor_select, move_direction):
        motor_to_move = self.all_motors_object.step_motors_list[motor_select]
        if ( "win" in platform):
            motor_to_move.can_selector = 0

        if move_direction == 0:
            message_to_send = motor_to_move.make_big_move_right()
        elif move_direction == 1:
            message_to_send = motor_to_move.make_small_move_right()
        elif move_direction == 3:
            message_to_send = motor_to_move.make_small_move_left()
        elif move_direction == 4:
            message_to_send = motor_to_move.make_big_move_left()
        else:
            message_to_send = motor_to_move.make_stop()
            self.send_can_message(message_to_send.arbitration_id, message_to_send.data, motor_to_move.can_selector)
            time.sleep(0.05)
            self.send_can_message(message_to_send.arbitration_id, message_to_send.data,  motor_to_move.can_selector)
            time.sleep(0.05)
            failed = 1
            for x in range(10):
                failed, data = self.manual_fetch(motor_to_move.make_read_pos_req(), motor_to_move.motor_id, motor_to_move.make_read_pos_req().data[0], 50000, motor_to_move.can_selector)  # request the register
                if failed:  # if timed out, return 0
                    continue
                else:
                    for data_idx in range(1, len(data)):
                        if not data[data_idx] == 0:
                            failed = 0
                            break
                    if not failed:
                        break
            if failed == 0:
                movepos_message = motor_to_move.make_write_pos_req(data)
                self.send_can_message(movepos_message.arbitration_id, movepos_message.data, motor_to_move.can_selector)
                time.sleep(0.05)
                self.send_can_message(movepos_message.arbitration_id, movepos_message.data, motor_to_move.can_selector)
                time.sleep(0.05)
                self.general_messages_label_2.setText("")

            else:
                self.general_messages_label_2.setText("BAD LOCATION ON \""+motor_to_move.name+"\", PLEASE PRESS STOP AGAIN UNTIL THIS IS GONE OR RESET THE ROBOT")
                self.general_messages_label_2.setStyleSheet("color: red;")



        # def make_read_pos_req(self):
        #     return can.Message(arbitration_id=self.motor_id, data=[0x92, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
        #                        is_extended_id=False)
        #
        # def make_write_pos_req(self, response):

        self.send_can_message(message_to_send.arbitration_id, message_to_send.data, 0)#motor_to_move.can_selector)






