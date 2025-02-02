#!/usr/bin/python3
import time
import serial
import threading
import can
from sys import platform
import ctypes
import os
import struct
import can.interfaces.pcan
import datetime

GOOD_EXIT = 0
DID_COMPOSE = 0

FEEDBACK_ID = 0x106
COMPUTER_ID = 0x105
BOT_ID = 0x104
TOP_ID = 0x103
NICLA_ID = 0x102
ALWAYS_ON_ID = 0x101

if os.environ.get('DISPLAY','') == '':
    os.environ.__setitem__('DISPLAY', ':0.0')
# Setup serial port with ttyTHS0
serial_port = serial.Serial(
    port="/dev/ttyTHS0",  # Using ttyTHS0
    baudrate=115200,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
)
# Wait a second to let the port initialize
time.sleep(1)
def kill_program():
    global DID_COMPOSE
    if not (DID_COMPOSE):
        DID_COMPOSE = 1
        try:
            serial_port.close()
        except:
            pass
        time.sleep(0.5)
        print("restarting status engine\n")
        os.system("cd /opt/ur/gary ; docker compose up status_engine -d")
        print("\n")
        DID_COMPOSE = 1
        time.sleep(0.5)
    try:
        bus.shutdown()
        bus2.shutdown()
    except:
        pass
    exit()

def get_time_delta(time_last_receive):
    time_S = int((datetime.datetime.now()).strftime("%S"))
    time_mS = int((datetime.datetime.now()).strftime("%f"))
    time_M = int((datetime.datetime.now()).strftime("%M"))
    delta = (time_M - time_last_receive[0]) * 60
    delta += time_S - time_last_receive[1]
    delta *= 1000000
    delta += time_mS - time_last_receive[2]
    time_receive = [time_M, time_S, time_mS]

    return [delta,time_receive]


can_running = 0
bus2 = 0
try:
    if platform == "linux" or platform == "linux2" or platform == "unix":
        bustype = 'socketcan'
        channel = 'can0'
        bus = can.Bus(channel=channel, interface=bustype, baudrate=1000000)
        bus = can.Bus(channel=channel, interface=bustype, baudrate=1000000)
        bustype2 = 'socketcan'
        channel2 = 'can1'
        bus2 = can.Bus(channel=channel2, interface=bustype2, baudrate=1000000)

    elif "win" in platform:
        bus = can.interface.Bus(bustype='pcan', channel='PCAN_USBBUS1', bitrate=1000000)
    can_running = 1
except:
    print("can setup failed, exiting")
    kill_program()


Rarm_motor_ids = []
for x in range(0x141, 0x148+1):
    Rarm_motor_ids.append(x)
Larm_motor_ids = []
for x in range(0x14B, 0x152+1):
    Larm_motor_ids.append(x)
wheel_motor_ids = []
for x in range(0x141, 0x144+1):
    wheel_motor_ids.append(x)
# wheel_motor_ids.append(0x141)
# wheel_motor_ids.append(0x142)
# wheel_motor_ids.append(0x144)

linear_motor_ids = []
linear_motor_ids.append(0x153)
linear_motor_ids.append(0x149)
print("\n\n\n\n\n\n-----------------------------------------------------------------------------------------")
print("                                          WELCOME                                        ")
print("-----------------------------------------------------------------------------------------\n\n")


def get_inputs(delta,expected_id): #manual input method used SPECIFICALLY for motor tests
    time_start = get_time_delta([0,0,0])[1]
    while (get_time_delta(time_start)[0] < delta):
        message = bus.recv(1.0)  # Timeout in seconds.
        if message is None:
            continue
        else:
            if (hex(message.arbitration_id) == hex(expected_id)):
                for resultindex in range(len(message.data)-2):
                    if not(message.data[resultindex+1] == 0x00):
                        return 1
    return 0

def get_inputs2(delta,expected_id): #manual input method used SPECIFICALLY for motor tests
    time_start = get_time_delta([0,0,0])[1]
    while (get_time_delta(time_start)[0] < delta):
        message = bus2.recv(0.01)  # Timeout in seconds.
        if message is None:
            continue
        else:
            if (hex(message.arbitration_id) == hex(expected_id)):
                for resultindex in range(len(message.data)-2):
                    if not(message.data[resultindex+1] == 0x00):
                        return 1
    return 0
def empty_canbus():
    rcv = 1
    cnt = 0
    while not rcv is None:
        cnt += 1
        rcv = bus.recv(0.1)
        if (cnt > 10):
            break


def await_reg(delta,expected_id,register_id): #manual input method used SPECIFICALLY for motor tests
    time_start = get_time_delta([0,0,0])[1]
    while (get_time_delta(time_start)[0] < delta):
        # print(get_time_delta(time_start)[0])
        message = bus.recv(0.5)  # Timeout in seconds.
        if message is None:
            continue
        else:
            # print("expecting: "+str(hex(register_id)),end='     ')
            # print(message)
            if (hex(message.arbitration_id) == hex(expected_id) and hex(message.data[0]) == hex(register_id)):
                return 1
    return 0


def check_reg(register_id,device_id):
    for ii in range(3):
        msg = can.Message(arbitration_id=device_id, data=[0x53, 0x53, 0x02, register_id, register_id, 0x02, 0, 0], is_extended_id=False)
        bus.send(msg)
        if (await_reg(20000, COMPUTER_ID, register_id)):
            time.sleep(0.2)
            empty_canbus()
            return 1
    time.sleep(0.1)
    empty_canbus()
    return 0

def request_restart(restart_vector, time_to_reset):
    for ii in range(4):
        msg = can.Message(arbitration_id=ALWAYS_ON_ID, data=[0x52, 0x50, restart_vector, 0, 0, 0, 0, time_to_reset], is_extended_id=False)
        bus.send(msg)
        time_start = get_time_delta([0, 0, 0])[1]
        time_send = get_time_delta([0, 0, 0])[1]
        while (get_time_delta(time_start)[0] < 100000):
            if (get_time_delta(time_send)[0] > 1000):
                time_send = get_time_delta([0, 0, 0])[1]
                bus.send(msg)
            message = bus.recv(0.3)  # Timeout in seconds.
            if message is None:
                continue

            else:
                if (message.arbitration_id == 0x106):
                    good_response = 1
                    for x in range(len(msg.data)):
                        if not msg.data[x] == message.data[x]:
                            good_response = 0
                            break
                    if (good_response):
                        return 1
                    continue
    time.sleep(0.1)
    empty_canbus()
    return 0

def check_always_on_feedback(device_id):
    for ii in range(3):
        msg = can.Message(arbitration_id=device_id, data=[0x47, 0x46, 0, 0, 0, 0, 0, 0], is_extended_id=False)
        bus.send(msg)
        if (await_reg(20000, FEEDBACK_ID, 0x47)):
            time.sleep(0.1)
            empty_canbus()
            return 1
    time.sleep(0.1)
    empty_canbus()
    return 0



def check_motor(motor_ids,motor_results):
    for motor_id in range(len(motor_ids)):
        got_reply = 0
        for ii in range(3):
            msg = can.Message(arbitration_id=motor_ids[motor_id], data=[0x9A, 0, 0, 0, 0, 0, 0, 0], is_extended_id=False)
            bus.send(msg)
            if (get_inputs(10000, (motor_ids[motor_id]))):
                got_reply = 1
                motor_results[motor_id] = 1
                break
        if not got_reply:
            motor_results[motor_id] = 0


def check_motor2(motor_ids,motor_results):
    for motor_id in range(len(motor_ids)):
        got_reply = 0
        for ii in range(3):
            msg = can.Message(arbitration_id=motor_ids[motor_id], data=[0x9A, 0, 0, 0, 0, 0, 0, 0], is_extended_id=False)
            bus2.send(msg)
            if (get_inputs2(10000, (motor_ids[motor_id]))):
                got_reply = 1
                motor_results[motor_id] = 1
                break
        if not got_reply:
            motor_results[motor_id] = 0

can1_enable = 1
def motor_test(id_list,result_list,can1_sel):
    global Rarm_motor_ids
    global Larm_motor_ids
    global wheel_motor_ids
    global current_list_length
    global can1_enable
    current_list_length = 1

    if (can1_sel == 0):
        time.sleep(0.02)
        get_inputs(100000, 0x100)
        time.sleep(0.02)
        check_motor(id_list, result_list)
    else:
        if (type(bus2) == int):
            print("")
            print("no can1 detected, assuming no arms from now on")
            print("")
        else:
            try:
                get_inputs2(100000, 0x100)
                time.sleep(0.02)
                check_motor2(id_list, result_list)
            except:
                print("")
                print("failed can1, please check can1 connection (or termination) , assuming no arms or linears from now on")
                can1_enable = 0
                print("")
    time.sleep(0.02)





# Default message to send (4 bytes in hex)
message = b'\x00\x00\x00\x00'
enable = 0


 # 0 =      PC DEAD
 # 1 =  STARTED PRESSED
 # 2 =   WAIT RESPONSE
 # 3 =   YES EMERGENCY
 # 4 =   SAFE PRESSED
 # 5 = EMERGENCY REQUEST
 # 6 =   NO EMERGENCY
incoming_emergency_state = 666


# Function to handle UART reading
def read_from_uart():
    global DID_COMPOSE
    global message
    global incoming_emergency_state
    try:
        while True:
            if serial_port.inWaiting() > 0:
                data = serial_port.read()

                if ("00" in str(data.hex())):
                    incoming_emergency_state = 0

                elif ("01" in str(data.hex())):
                    incoming_emergency_state = 1

                elif ("03" in str(data.hex())):
                    incoming_emergency_state = 2

                elif ("05" in str(data.hex())):
                    incoming_emergency_state = 3

                elif ("07" in str(data.hex())):
                    incoming_emergency_state = 4

                elif ("0f" in str(data.hex())):
                    incoming_emergency_state = 5

                elif ("5f" in str(data.hex())):
                    incoming_emergency_state = 6

    except Exception as exception_error:
       print("")
    finally:
        try:
            kill_program()
        except:
            if not (DID_COMPOSE):
                DID_COMPOSE = 1
                try:
                    serial_port.close()
                except:
                    pass
                time.sleep(0.5)
                print("restarting status engine\n")
                os.system("cd /opt/ur/gary ; docker compose up status_engine -d")
                print("\n")
                DID_COMPOSE = 1
                time.sleep(0.5)
            exit()

# Function to send data every 200ms
def send_data():
    global message
    global enable
    global DID_COMPOSE
    try:
        while True:
            if (enable):
                serial_port.write(message)
            time.sleep(0.1)  # 200ms delay
    except Exception as exception_error:
        if (GOOD_EXIT):
            print("\n\n NO ISSUES FOUND!!! \n\n\n\n")
            print("note that without an active serial monitor the emergency might disconnect the motor powers,")
            print("restart the gary if this is an issue")
            print("closing program...")
        else:
            print("\n\nissues found, program exiting...")

    finally:
        try:
            kill_program()
        except:
            if not (DID_COMPOSE):
                DID_COMPOSE = 1
                try:
                    serial_port.close()
                except:
                    pass
                time.sleep(0.5)
                print("restarting status engine\n")
                os.system("cd /opt/ur/gary ; docker compose up status_engine -d")
                print("\n")
                DID_COMPOSE = 1
                time.sleep(0.5)
            exit()
def check_existances():
    if check_reg(0x60, TOP_ID):
        print("top uC found...")
    else:
        print("\n\ntop uC NOT found, exiting...\n\n")
        kill_program()
    if check_reg(0x61, BOT_ID):
        print("bottom uC found...")
    else:
        print("\n\nbottom uC NOT found, exiting...\n\n")
        kill_program()
    if check_reg(0x62, NICLA_ID):
        print("nicla found...")
    else:
        print("\n\nnicla NOT found, exiting...\n\n")
        kill_program()
    if check_always_on_feedback(ALWAYS_ON_ID):
        print("always on found...")
    else:
        print("\n\nalways on NOT found, exiting...\n\n")
        kill_program()

def check_always_on_restarts():
    if not request_restart(0x01, 0x14):
        print("\n\ntop restart request failed, exiting...\n\n")
        kill_program()
    if check_reg(0x60, TOP_ID):
        print("\n\ntop uC NOT RESTARTED BY ALWAYS ON AS REQUESTED, exiting...\n\n")
        kill_program()
    if not check_reg(0x61, BOT_ID):
        print("\n\ntop uC restart shut down bottom uC, exiting...\n\n")
        kill_program()
    if not check_reg(0x62, NICLA_ID):
        print("\n\ntop uC restart shut down nicla uC, exiting...\n\n")
        kill_program()
    time.sleep(3)
    if not check_reg(0x60, TOP_ID):
        print("\n\ntop uC did NOT turn back on in the expected timeframe, exiting...\n\n")
        kill_program()
    print("top uC restarted successfully...")

    if not request_restart(0x02, 0x14):
        print("\n\nbottom restart request failed, exiting...\n\n")
        kill_program()
    if not check_reg(0x60, TOP_ID):
        print("\n\nbottom uC restart shut down top uC, exiting...\n\n")
        kill_program()
    # time.sleep(3)
    if check_reg(0x61, BOT_ID):
        print("\n\nbottom uC NOT RESTARTED BY ALWAYS ON AS REQUESTED, exiting...\n\n")
        kill_program()
    time.sleep(3)
    if not check_reg(0x61, BOT_ID):
        print("\n\nbottom uC did NOT turn back on in the expected timeframe, exiting...\n\n")
        kill_program()
    print("bottom uC restarted successfully...")



    if not request_restart(0x02, 0x14):
        print("\n\nbottom (second time) restart request failed, exiting...\n\n")
        kill_program()
    if not check_reg(0x60, TOP_ID):
        print("\n\nnicla uC restart shut down top uC, exiting...\n\n")
        kill_program()
    if check_reg(0x62, NICLA_ID):
        print("\n\nnicla NOT RESTARTED BY ALWAYS ON AS REQUESTED, exiting...\n\n")
        kill_program()
    time.sleep(3)
    if not check_reg(0x62, NICLA_ID):
        print("\n\nnicla did NOT turn back on in the expected timeframe, exiting...\n\n")
        kill_program()
    print("nicla restarted successfully...")


arm_enables = [0,0]




def test_arms(expect_answer,first_test):
    global arm_enables
    Rarm_motor_results = []
    Larm_motor_results = []
    for x in Rarm_motor_ids:
        Rarm_motor_results.append(0)
    for x in Larm_motor_ids:
        Larm_motor_results.append(0)
    bad_motor_ids = []
    bad_motor_indexes = []

    # check arms
    if (first_test):
        if (type(bus2) == int):
            print("no can1 detected, assuming no arms from now on")
            arm_enables = [0, 0]
        else:  # if can2 exists
            print("\n\ntesting arms...")
            motor_test(Rarm_motor_ids, Rarm_motor_results, 1)
            for x in Rarm_motor_results:
                if x:
                    arm_enables[0] = 1  # arm exists if any motor exists
                    break
            motor_test(Larm_motor_ids, Larm_motor_results, 1)
            for x in Larm_motor_results:
                if x:
                    arm_enables[1] = 1  # arm exists if any motor exists
                    break
    if (arm_enables[0] == 0 and arm_enables[1] == 0):
        if (first_test):
            print("\n\nNO ARMS FOUND, CONTINUING WITHOUT ARM TESTS\n\n")
        else:
            print("ARMS SKIPPED\n\n")
    else:
        if (arm_enables[0] == 1):  # if right arm exists, find any bad responses
            rarm_good = 1
            for mot_idx in range(len(Rarm_motor_results)):
                if Rarm_motor_results[mot_idx] != expect_answer:
                    rarm_good = 0
                    bad_motor_ids.append(Rarm_motor_ids[mot_idx])
                    bad_motor_indexes.append(mot_idx)
            if not rarm_good:
                print("\n\nright arm found issues in the following motors", end='')
                if (expect_answer):
                    print(": ")
                else:
                    print(" (these motors should be off but they are on): ")
                for badmotoridx in range(len(bad_motor_ids)):
                    print("motor number: " + str(bad_motor_indexes[badmotoridx]) + "  with ID: " + str(hex(bad_motor_ids[badmotoridx])))
                kill_program()
            else:
                if (expect_answer):
                    print("right arm good, all motors responded...")
                else:
                    print("right arm good, no motors responded...")

        if (arm_enables[0] == 1):  # if left arm exists, find any bad responses
            larm_good = 1
            for mot_idx in range(len(Rarm_motor_results)):
                if Rarm_motor_results[mot_idx] != expect_answer:
                    larm_good = 0
                    bad_motor_ids.append(Rarm_motor_ids[mot_idx])
                    bad_motor_indexes.append(mot_idx)
            if not larm_good:
                print("\n\nleft arm found issues in the following motors", end='')
                if (expect_answer):
                    print(": ")
                else:
                    print(" (these motors should be off but they are on): ")
                for badmotoridx in range(len(bad_motor_ids)):
                    print("motor number: " + str(bad_motor_indexes[badmotoridx]) + "  with ID: " + str(hex(bad_motor_ids[badmotoridx])))
                kill_program()
            else:
                if (expect_answer):
                    print("left arm good, all motors responded...")
                else:
                    print("left arm good, no motors responded...")

def test_wheels(expect_answer):
    wheel_motor_results = []
    for x in wheel_motor_ids:
        wheel_motor_results.append(0)
    bad_motor_ids = []
    bad_motor_indexes = []
    print("testing wheels...")
    motor_test(wheel_motor_ids, wheel_motor_results, 0)
    wheels_good = 1
    for mot_idx in range(len(wheel_motor_results)):
        if wheel_motor_results[mot_idx] != expect_answer:
            wheels_good = 0
            bad_motor_ids.append(wheel_motor_ids[mot_idx])
            bad_motor_indexes.append(mot_idx)
    if not wheels_good:
        print("\n\nfound issues in the following wheel motors",end='')
        if (expect_answer):
            print(": ")
        else:
            print(" (these motors should be off but they are on): ")
        for badmotoridx in range(len(bad_motor_ids)):
            print("motor number: " + str(bad_motor_indexes[badmotoridx]) + "  with ID: " + str(hex(bad_motor_ids[badmotoridx])))
        kill_program()
    else:
        if (expect_answer):
            print("wheels good, all motors responded...")
        else:
            print("wheels good, no motors responded...")


def test_linears(expect_answer):
    global can1_enable
    linear_motor_results = []
    for x in linear_motor_ids:
        linear_motor_results.append(0)
    bad_motor_ids = []
    bad_motor_indexes = []
    if not can1_enable:
        print("no can1, cant test linears\n")
        return
    print("testing linears...")
    motor_test(linear_motor_ids, linear_motor_results, 1)
    linears_good = 1
    for mot_idx in range(len(linear_motor_results)):
        if linear_motor_results[mot_idx] != expect_answer:
            linears_good = 0
            bad_motor_ids.append(linear_motor_ids[mot_idx])
            bad_motor_indexes.append(mot_idx)
    if not linears_good:
        print("\n\nlinears found issues in the following motors",end='')
        if (expect_answer):
            print(": ")
        else:
            print(" (these motors should be off but they are on): ")
        for badmotoridx in range(len(bad_motor_ids)):
            print("motor number: " + str(hex(bad_motor_indexes[badmotoridx])) + "  with ID: " + str(hex(bad_motor_ids[badmotoridx])))
        kill_program()
    else:
        if (expect_answer):
            print("linears good, both motors responded...")
        else:
            print("linears good, neither motor responded...")


def set_61(on_off):
    onoff = 0xFF if on_off else 0x00
    msg = can.Message(arbitration_id=BOT_ID, data=[0x4D, 0x50, onoff, 0, 0, 0, 0, 0], is_extended_id=False)
    bus.send(msg)
    time.sleep(0.1)
    bus.send(msg)
    time.sleep(0.1)
    msg = can.Message(arbitration_id=TOP_ID, data=[0x4D, 0x50, onoff, 0, 0, 0, 0, 0], is_extended_id=False)
    bus.send(msg)
    time.sleep(0.1)
    bus.send(msg)
    time.sleep(0.1)


# Function to handle keyboard input for changing the message
def handle_keyboard_input():
    global message
    global enable
    global incoming_emergency_state
    global GOOD_EXIT
    global DID_COMPOSE

    time.sleep(1)

    try:
        while True:
            message = b'\x11\x11\x11\x11'
            enable = 1
            # 0 =      PC DEAD
            # 1 =  STARTED PRESSED
            # 2 =   WAIT RESPONSE
            # 3 =   YES EMERGENCY
            # 4 =   SAFE PRESSED
            # 5 = EMERGENCY REQUEST
            # 6 =   NO EMERGENCY

            time.sleep(1)

            while (incoming_emergency_state == 666):
                print("NO SERIAL DATA RECEIVED FROM THE EMERGENCY...\n")
                time.sleep(1)

            while (incoming_emergency_state != 6):
                if (incoming_emergency_state == 0):
                    print("serial send appears to be malfunctioning, please check connection or permissions...\n")
                else:
                    print("please release the emergency button to start...\n")
                time.sleep(1)

            print("emergency state good...\n")

            # print("\n\n-----------------------------------------------------------------------------------------")
            # print("TESTING microCONTROLLER CANBUS COMMUNICATION                         ")
            # print("-----------------------------------------------------------------------------------------\n\n")
            # check_existances()




            # print("\n\n-----------------------------------------------------------------------------------------")
            # print("TESTING ALWAYS ON POWER RESET FUNCTIONS                            ")
            # print("-----------------------------------------------------------------------------------------\n\n")
            # check_always_on_restarts()

            test_arms(1,1)
            test_linears(1)
            test_wheels(1)

            print("\n\n----------------------------------------------------------------------------------")
            print("TURNING OFF THE LOW VOLTAGE POWER TO THE MOTORS AND TESTING MAIN POWER CONNECTION!")
            print("----------------------------------------------------------------------------------\n\n")
            set_61(0)
            time.sleep(3)

            test_arms(1,0)
            test_linears(1)
            test_wheels(1)
            if not (arm_enables[0] == 0 and arm_enables[1] == 0):

                print("\n\n-----------------------------------------------------------------------------")
                print("TURNING OFF THE HIGH VOLTAGE POWER TO THE WHEELS ONLY, MAKING SURE THEY ALL TURN OFF!")
                print("------------------------------------------------------------------------------\n\n")
                message = b'\x55\x55\x55\x55'
                time.sleep(1)
                while (incoming_emergency_state != 5):
                    print("emergency state not updating, waiting for state change (this could be an issue in the serial connection)...\n")
                    time.sleep(1)
                time.sleep(1)

                test_arms(1, 0)
                test_linears(0)
                test_wheels(0)


                print("\n\n-----------------------------------------------------------------------------")
                print("TURNING OFF THE HIGH VOLTAGE POWER TO THE ARMS ONLY, MAKING SURE THEY ALL TURN OFF!")
                print("------------------------------------------------------------------------------\n\n")
                message = b'\x77\x77\x77\x77'
                time.sleep(3)

                test_arms(0, 0)
                test_linears(1)
                test_wheels(1)



            print("\n\n----------------------------------------------------------------------------------")
            print("TURNING OFF THE HIGH VOLTAGE POWER TO ALL MOTORS, MAKING SURE THEY ALL TURN OFF!")
            print("----------------------------------------------------------------------------------\n\n")
            message = b'\xFF\xFF\xFF\xFF'
            time.sleep(3)

            test_arms(0, 0)
            test_linears(0)
            test_wheels(0)


            print("\n\n-----------------------------------------------------------------------------------")
            print("TURNING ON ONLY THE LOW VOLTAGE POWER TO THE WHEELS MAKING SURE THEY ALL TURN ON!")
            print("------------------------------------------------------------------------------------\n\n")

            set_61(1)
            time.sleep(3)

            test_arms(1,0)
            test_linears(1)
            test_wheels(1)

            print("\n\n----------------------------------------------------------------------------")
            print("ALL POWER CONNECTIONS ARE GOOD, TURNING THE POWER BACK ON FOR FINAL CHECK!")
            print("----------------------------------------------------------------------------\n\n")


            message = b'\x11\x11\x11\x11'
            time.sleep(1)
            while (incoming_emergency_state != 6):
                print("emergency state not updating, waiting for state change...\n")
                time.sleep(1)
            time.sleep(3)
            test_arms(1,0)
            test_linears(1)
            test_wheels(1)

            print("\n\n\n\n\n\n-------------------------------------------------------------------------------")
            print("                                TEST COMPLETE                                 ")
            print("-------------------------------------------------------------------------------\n\n")

            GOOD_EXIT = 1
            kill_program()
            exit()

    except KeyboardInterrupt:
        print("Exiting keyboard input handler.")
    finally:
        try:
            if not (DID_COMPOSE):
                DID_COMPOSE = 1
                try:
                    serial_port.close()
                except:
                    pass
                time.sleep(0.5)
                print("restarting status engine\n")
                os.system("cd /opt/ur/gary ; docker compose up status_engine -d")
                print("\n")
                DID_COMPOSE = 1
                time.sleep(0.5)
            try:
                bus.shutdown()
                bus2.shutdown()
            except:
                pass
        except:
            kill_program()

# Run both reading, sending, and keyboard input handling in parallel
try:
    # Create and start threads
    print("stopping status engine\n")
    os.system("cd /opt/ur/gary ; docker stop gary-status_engine-1")
    print("\n")
    time.sleep(1)
    read_thread = threading.Thread(target=read_from_uart)
    send_thread = threading.Thread(target=send_data)
    input_thread = threading.Thread(target=handle_keyboard_input)

    read_thread.start()
    send_thread.start()
    input_thread.start()

    # Wait for both threads to finish
    read_thread.join()
    send_thread.join()
    input_thread.join()

except KeyboardInterrupt:
    print("Exiting Program")
    kill_program()

finally:
    try:
        if not (DID_COMPOSE):
            DID_COMPOSE = 1
            try:
                serial_port.close()
            except:
                pass
            time.sleep(0.5)
            print("restarting status engine\n")
            os.system("cd /opt/ur/gary ; docker compose up status_engine -d")
            print("\n")
            DID_COMPOSE = 1
            time.sleep(0.5)
        try:
            bus.shutdown()
            bus2.shutdown()
        except:
            pass
    except:
        kill_program()
