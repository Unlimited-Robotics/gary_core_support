
from PyQt5.QtCore import QObject, QThread, pyqtSignal
import time


class leds_class(QObject):

    def __init__(self, red_slider, green_slider, blue_slider,
                 current_color_plate, button_white, button_green, button_blue, button_red, button_purple, button_turquoise,
                 head_off_button, head_wave_button, head_eyes_button, head_full_button,
                 chest_off_button, chest_blink_button, chest_loading_button, chest_full_button,
                 general_functions):
        super().__init__()
        # self.general_functions = general_functions
        self.send_can_message = general_functions[2]
        self.red_slider = red_slider
        self.green_slider = green_slider
        self.blue_slider = blue_slider
        self.current_color_plate  = current_color_plate
        self.button_white         = button_white
        self.button_green         = button_green
        self.button_blue          = button_blue
        self.button_red           = button_red
        self.button_purple        = button_purple
        self.button_turquoise     = button_turquoise

        self.head_off_button      = head_off_button
        self.head_wave_button     = head_wave_button
        self.head_eyes_button     = head_eyes_button
        self.head_full_button     = head_full_button
        self.chest_off_button     = chest_off_button
        self.chest_blink_button   = chest_blink_button
        self.chest_loading_button = chest_loading_button
        self.chest_full_button    = chest_full_button


        self.red_val = 0
        self.green_val = 0
        self.blue_val = 0

        self.red_slider.valueChanged.connect(lambda: self.update_color_from_slider(self.red_slider.value(), 0))
        self.green_slider.valueChanged.connect(lambda: self.update_color_from_slider(self.green_slider.value(), 1))
        self.blue_slider.valueChanged.connect(lambda: self.update_color_from_slider(self.blue_slider.value(), 2))

        self.set_color(255, 0, 255) #set initial color

        self.button_white.clicked.connect(lambda: self.set_color(255,255,255))
        self.button_green.clicked.connect(lambda: self.set_color(0,255,0))
        self.button_blue.clicked.connect(lambda: self.set_color(0,0,255))
        self.button_red.clicked.connect(lambda: self.set_color(255,0,0))
        self.button_purple.clicked.connect(lambda: self.set_color(255,0,255))
        self.button_turquoise.clicked.connect(lambda: self.set_color(0,255,128))

        self.head_off_button     .clicked.connect(lambda: self.send_leds(0, 0x00, 0x00, 0x00))
        self.head_wave_button    .clicked.connect(lambda: self.send_leds(0, 0x03, 0x00, 0x07))
        self.head_eyes_button    .clicked.connect(lambda: self.send_leds(0, 0xFF, 0x04, 0x02))
        self.head_full_button    .clicked.connect(lambda: self.send_leds(0, 0x01, 0x05, 0xFF))
        self.chest_off_button    .clicked.connect(lambda: self.send_leds(1, 0x00, 0x00, 0xFF))
        self.chest_blink_button  .clicked.connect(lambda: self.send_leds(1, 0x03, 0x00, 0x04))
        self.chest_loading_button.clicked.connect(lambda: self.send_leds(1, 0x0C, 0x00, 0x04))
        self.chest_full_button   .clicked.connect(lambda: self.send_leds(1, 0x0D, 0x00, 0xFF))



    def send_leds(self, head_chest_sel, motion_sel, reps, speed):
        if (head_chest_sel):
            head_chest_byte = 0x43
        else:
            head_chest_byte = 0x48
        self.send_can_message(0x103, [head_chest_byte, 0x4C, motion_sel, speed, reps*2, self.red_val, self.green_val, int((self.blue_val*4)/5)], 0)
        time.sleep(0.01)


    def update_shown_color(self):
        self.current_color_plate.setStyleSheet(f"background-color: rgb({self.red_val}, {self.green_val}, {self.blue_val}); color: black;")

    def update_color_from_slider(self, slider_value, color_select):
        if (color_select == 0):
            self.red_val = slider_value
        elif (color_select == 1):
            self.green_val = slider_value
        elif (color_select == 2):
            self.blue_val = slider_value
        self.update_shown_color()

    def set_color(self, red, green, blue):
        self.red_val = red
        self.green_val = green
        self.blue_val = blue

        self.red_slider.setValue(self.red_val)
        self.green_slider.setValue(self.green_val)
        self.blue_slider.setValue(self.blue_val)
        self.update_shown_color()



