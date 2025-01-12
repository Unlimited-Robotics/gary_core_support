
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from data_entries import data_entry


class all_data_entries_class(QObject):

    def __init__(self, update_label, ui):
        super().__init__()
        self.label_bat_percentage = data_entry(ui.bat_percentage, "battery charge percentage [%]", 'decimal', 0x104, 0x22, update_label, 1, 100,ui.bat_percentage_passfail)
        self.label_bat_current = data_entry(ui.bat_current, "current", '2s', 0x104, 0x20, update_label, -8000, 8000, ui.bat_current_passfail)
        self.label_bat_voltage = data_entry(ui.bat_voltage, "voltage", 'decimal', 0x104, 0x1F, update_label, 35000, 50000, ui.bat_voltage_passfail)
        self.label_bat_error_count = data_entry(ui.bat_error_count, "error count (0-128)", 'decimal', 0x104, 0x5B, update_label, 0, 4, ui.bat_error_count_passfail)
        self.label_bat_temp = data_entry(ui.bat_temp, "temperature", 'decimal', 0x104, 0x1E, update_label, 15, 40, ui.bat_temp_passfail)
        self.label_bat_cell1 = data_entry(ui.bat_cell1, "cell1 voltage", 'decimal', 0x104, 0x37, update_label, 3200, 4100, ui.bat_cell1_passfail)
        self.label_bat_cell2 = data_entry(ui.bat_cell2, "cell2 voltage", 'decimal', 0x104, 0x36, update_label, 3200, 4100, ui.bat_cell2_passfail)
        self.label_bat_cell3 = data_entry(ui.bat_cell3, "cell3 voltage", 'decimal', 0x104, 0x35, update_label, 3200, 4100, ui.bat_cell3_passfail)
        self.label_bat_cell4 = data_entry(ui.bat_cell4, "cell4 voltage", 'decimal', 0x104, 0x34, update_label, 3200, 4100, ui.bat_cell4_passfail)
        self.label_bat_cell5 = data_entry(ui.bat_cell5, "cell5 voltage", 'decimal', 0x104, 0x33, update_label, 3200, 4100, ui.bat_cell5_passfail)
        self.label_bat_cell6 = data_entry(ui.bat_cell6, "cell6 voltage", 'decimal', 0x104, 0x32, update_label, 3200, 4100, ui.bat_cell6_passfail)
        self.label_bat_cell7 = data_entry(ui.bat_cell7, "cell7 voltage", 'decimal', 0x104, 0x31, update_label, 3200, 4100, ui.bat_cell7_passfail)
        self.label_bat_cell8 = data_entry(ui.bat_cell8, "cell8 voltage", 'decimal', 0x104, 0x30, update_label, 3200, 4100, ui.bat_cell8_passfail)
        self.label_bat_cell9 = data_entry(ui.bat_cell9, "cell9 voltage", 'decimal', 0x104, 0x2F, update_label, 3200, 4100, ui.bat_cell9_passfail)
        self.label_bat_cell10 = data_entry(ui.bat_cell10, "cell10 voltage", 'decimal', 0x104, 0x2E, update_label, 3200, 4100, ui.bat_cell10_passfail)
        self.label_bat_cell11 = data_entry(ui.bat_cell11, "cell11 voltage", 'decimal', 0x104, 0x2D, update_label, 3200, 4100, ui.bat_cell11_passfail)
        self.label_bat_cell12 = data_entry(ui.bat_cell12, "cell12 voltage", 'decimal', 0x104, 0x2C, update_label, 3200, 4100, ui.bat_cell12_passfail)
        self.label_bat_state_health = data_entry(ui.bat_state_health, "state of health", 'decimal', 0x104, 0x38, update_label, 60, 100,ui.bat_state_health_passfail)
        self.label_ver_top_board = data_entry(ui.ver_top_board, "top board version", 'ascii', 0x103, 0x60, update_label, 0, 0, ui.empty_versions_passfail)
        self.label_ver_top_code = data_entry(ui.ver_top_code, "top code version", 'ascii', 0x103, 0X00, update_label, 0, 0, ui.empty_versions_passfail)
        self.label_ver_bot_board = data_entry(ui.ver_bot_board, "bottom board version", 'ascii', 0x104, 0x61, update_label, 0, 0, ui.empty_versions_passfail)
        self.label_ver_bot_code = data_entry(ui.ver_bot_code, "bottom code version", 'ascii', 0x104, 0X00, update_label, 0, 0, ui.empty_versions_passfail)
        self.label_ver_nic_code = data_entry(ui.ver_nic_code, "nicla sense me code version", 'ascii', 0x102, 0X00, update_label, 0, 0, ui.empty_versions_passfail)
        self.label_ver_nic_board = data_entry(ui.ver_nic_board, "nicla sense me board version", 'ascii', 0x102, 0x62, update_label, 0, 0, ui.empty_versions_passfail)
        self.label_states_buttons = data_entry(ui.states_buttons, "button states", 'binary', 0x104, 0x52, update_label, 0, 0, ui.states_passfail_empty)
        self.label_states_chest = data_entry(ui.states_chest, "chest button pressed time", 'float', 0x103, 0x1B, update_label, 0, 500, ui.states_chest_passfail)
        self.label_states_relay = data_entry(ui.states_relay, "charging relay state (ON = connected)", 'onoff', 0x104, 0x57, update_label, 0, 0, ui.states_passfail_empty)
        self.label_states_arms_61 = data_entry(ui.states_arms_61, "arms 6.1v power", 'onoff', 0x103, 0x59, update_label, 0, 0, ui.states_passfail_empty)
        self.label_states_wheel_61 = data_entry(ui.states_wheel_61, "wheels 6.1v power", 'onoff', 0x104, 0x58, update_label, 0, 0, ui.states_passfail_empty)

        self.label_nicla_pitch = data_entry(ui.nicla_pitch, "pitch", 'float', 0x102, 0x0D, update_label, -3.2, 3.2, ui.nicla_pitch_passfail)
        self.label_nicla_roll = data_entry(ui.nicla_roll, "roll", 'float', 0x102, 0x0E, update_label, -3.2, 3.2, ui.nicla_roll_passfail)
        self.label_nicla_heading = data_entry(ui.nicla_heading, "heading", 'float', 0x102, 0x0F, update_label, 0, 6.2, ui.nicla_heading_passfail)
        self.label_nicla_barometer = data_entry(ui.nicla_barometer, "barometer", 'float', 0x102, 0x5A, update_label, 600, 2000, ui.nicla_barometer_passfail)

        self.label_srftemp_temp1 = data_entry(ui.srftemp_temp1, "temperature sensor 1", 'float', 0x103, 0x10, update_label, 15, 40, ui.srftemp_temp1_passfail)
        self.label_srftemp_temp2 = data_entry(ui.srftemp_temp2, "temperature sensor 2", 'float', 0x103, 0x11, update_label, 15, 40, ui.srftemp_temp2_passfail)
        self.label_srftemp_temp3 = data_entry(ui.srftemp_temp3, "temperature sensor 3", 'float', 0x103, 0x12, update_label, 15, 40, ui.srftemp_temp3_passfail)
        self.label_srftemp_temp4 = data_entry(ui.srftemp_temp4, "temperature sensor 4", 'float', 0x103, 0x13, update_label, 15, 40, ui.srftemp_temp4_passfail)
        self.label_srftemp_srf1 = data_entry(ui.srftemp_srf1, "srf 1", 'float', 0x104, 0x16, update_label, 1, 600, ui.srftemp_srf1_passfail)
        self.label_srftemp_srf2 = data_entry(ui.srftemp_srf2, "srf 2", 'float', 0x104, 0x19, update_label, 1, 600, ui.srftemp_srf2_passfail)

        self.data_entries = {
            0: [[]],
            1: [
                [
                    self.label_bat_percentage,
                    self.label_bat_current,
                    self.label_bat_voltage,
                    self.label_bat_temp,
                    self.label_bat_error_count
                ],
                [
                    self.label_bat_cell1,
                    self.label_bat_cell2,
                    self.label_bat_cell3,
                    self.label_bat_cell4,
                    self.label_bat_cell5,
                    self.label_bat_cell6,
                    self.label_bat_cell7,
                    self.label_bat_cell8,
                    self.label_bat_cell9,
                    self.label_bat_cell10,
                    self.label_bat_cell11,
                    self.label_bat_cell12,
                    self.label_bat_state_health
                ],
                [
                    self.label_ver_top_board,
                    self.label_ver_top_code,
                    self.label_ver_bot_board,
                    self.label_ver_bot_code,
                    self.label_ver_nic_board,
                    self.label_ver_nic_code
                ],
                [
                    self.label_states_buttons,
                    self.label_states_chest,
                    self.label_states_relay,
                    self.label_states_arms_61,
                    self.label_states_wheel_61
                ],
                [
                    self.label_nicla_pitch,
                    self.label_nicla_roll,
                    self.label_nicla_heading,
                    self.label_nicla_barometer
                ],
                [
                    self.label_srftemp_temp1,
                    self.label_srftemp_temp2,
                    self.label_srftemp_temp3,
                    self.label_srftemp_temp4,
                    self.label_srftemp_srf1,
                    self.label_srftemp_srf2
                ]
            ],
            2: [[]],
        }
