
from PyQt5.QtCore import QObject, QThread, pyqtSignal
typelist = ["float","decimal","2s", "binary", "ascii","onoff"]
import struct

class data_entry(QObject):
    update_label_signal = pyqtSignal(object, str)  # Signal to send label and text
    def __init__(self, label_object, name, datatype, device_id, reg_id, update_label_func, starndard_min, standard_max, passfail_label):
        super().__init__()
        self.label_object = label_object  # QLabel object
        self.passfail_label_object = passfail_label  # QLabel object
        self.name = name                  # Name associated with the label
        self.datatype = datatype          # Name associated with the label
        self.valid_data = 0
        self.starndard_min = starndard_min
        self.standard_max = standard_max
        self.device_id = device_id
        self.reg_id = reg_id
        self.passfail = ""

        if not datatype in typelist:
            print("type \""+ datatype+"\" is unsupported for label \""+name+"\"")
        self.data = "Not received yet"    # Initial data
        #self.update_label_signal = update_label_signal  # Signal to emit updates
        self.update_label_signal.connect(update_label_func)
        self.update_label()


    def udate(self, text):
        """Update the data and emit a signal to refresh the label."""
        self.data = text
        self.update_label()


    def update_label(self):
        """Emit a signal to update the label's text."""
        self.make_passfail()
        self.update_label_signal.emit(self.label_object, self.make_text())
        self.update_label_signal.emit(self.passfail_label_object, self.passfail)

    def makedatafloat(self):
        # Pack it into a byte format
        last_4_bytes = eval(self.data)[-4:]
        # Unpack the last 4 bytes as a float (using big-endian byte order '>' and 'f' for float)
        float_value = struct.unpack('<f', last_4_bytes)[0]
        return (float_value)

    def makedatadec(self):
        resultdec = 0
        for byte_idx in range(len(eval(self.data)[2:])):
            resultdec += int(eval(self.data)[2 + byte_idx]) * (256 ** ((6 - byte_idx) - 1))
        return resultdec

    def makedata2s(self):
        resultdec = 0
        for byte_idx in range(len(eval(self.data)[6:])):
            resultdec += int(eval(self.data)[6 + byte_idx]) * (256 ** ((2 - byte_idx) - 1))
        if resultdec > 32767:
            return "-"+str(65535-resultdec-1)
        return resultdec

    def makedatabinary(self):
        datastring = ""
        actual_data = eval(self.data)[2:]
        for databyte in actual_data:
            if databyte == 0:
                datastring+= "0 "
            else:
                datastring+= "1 "
        return (datastring)

    def makedataascii(self):
        datastring = ""
        actual_data = eval(self.data)[2:]
        for byte in actual_data:
            if not (byte == 0x00):
                datastring += chr(byte)
        return datastring

    def makedataonoff(self):
        actual_data = eval(self.data)[-1]
        if not (actual_data == 0x00):
            return "ON"
        return "OFF"

    def make_data_not_text(self, data_parse):
        self.data = data_parse
        if "received" in self.data:
            return "not yet received"
        if self.datatype == "float":
            return f"{self.makedatafloat()}"
        elif self.datatype == "decimal":
            return f"{self.makedatadec()}"
        elif self.datatype == "2s":
            return f"{self.makedata2s()}"
        elif self.datatype == "binary":
            return f"{self.makedatabinary()}"
        elif self.datatype == "ascii":
            return f"{self.makedataascii()}"
        elif self.datatype == "onoff":
            return f"{self.makedataonoff()}"
        return "parsing failed"

    def make_text(self):
        """Format the label text."""
        if not(self.valid_data):
            return f"{self.name}: {self.data}"
        if self.datatype == "float":
            return f"{self.name}: {self.makedatafloat()}"
        elif self.datatype == "decimal":
            return f"{self.name}: {self.makedatadec()}"
        elif self.datatype == "2s":
            return f"{self.name}: {self.makedata2s()}"
        elif self.datatype == "binary":
            return f"{self.name}: {self.makedatabinary()}"
        elif self.datatype == "ascii":
            return f"{self.name}: {self.makedataascii()}"
        elif self.datatype == "onoff":
            return f"{self.name}: {self.makedataonoff()}"
        return f"{self.name}: {self.data}"

    def make_passfail(self):
        if "received" in self.data:
            return ""
        if "chest button" in self.name:
            if float(self.make_data_not_text(self.data)) == 0:
                self.passfail = "UNKNOWN (likely due to never having been pressed) , press button to see if value changed"
                return "FAIL, press button to see if value changed"
        if (self.starndard_min == 0 and self.standard_max == 0):
            self.passfail = ""
            return ""
        data_numeral = float(self.make_data_not_text(self.data))
        if (data_numeral >= self.starndard_min and data_numeral <= self.standard_max):
            self.passfail = "PASS"
            return "PASS"
        self.passfail = "FAIL"
        return "FAIL"
