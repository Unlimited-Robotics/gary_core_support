import sys
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow
from qt_design1 import Ui_qt_designer_save1  # Import your generated UI class
import can
import ctypes
import os
import struct
import can.interfaces.pcan
from sys import platform
import datetime
import time





class bad_can_variables_class(QObject):

    def __init__(self, general_messages_label, can0_label, can0_button, can1_label, can1_button, canbus_good_label, continue_button, main_widget):
        super().__init__()
        self.general_messages_label = general_messages_label
        self.can0_label = can0_label
        self.can0_button = can0_button
        self.can1_label = can1_label
        self.can1_button = can1_button
        self.canbus_good_label = canbus_good_label
        self.continue_button = continue_button
        self.main_widget = main_widget



