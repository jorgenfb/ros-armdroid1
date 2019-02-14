from gpiozero import DigitalOutputDevice, DigitalInputDevice


class IOAdapter(object):
    def __init__(self):
        self.__motor_code_output0 = DigitalOutputDevice(10)
        self.__motor_code_output1 = DigitalOutputDevice(9)
        self.__motor_code_output2 = DigitalOutputDevice(8)
        self.__motor_code_output3 = DigitalOutputDevice(7)
        self.__motor_select_output0 = DigitalOutputDevice(6)
        self.__motor_select_output1 = DigitalOutputDevice(5)
        self.__motor_select_output2 = DigitalOutputDevice(3)
        self.__sync_output = DigitalOutputDevice(4)

        self.connected = DigitalInputDevice(1, pull_up=False)

    def write_output(self, syncBit, motorId, motorCode):
        b0 = (motorCode >> 0) & 1
        b1 = (motorCode >> 1) & 1
        b2 = (motorCode >> 2) & 1
        b3 = (motorCode >> 3) & 1

        m0 = (motorId >> 0) & 1
        m1 = (motorId >> 1) & 1
        m2 = (motorId >> 2) & 1

        # Write motor output value
        self.__motor_code_output0.value = True if b0 else False
        self.__motor_code_output1.value = True if b1 else False
        self.__motor_code_output2.value = True if b2 else False
        self.__motor_code_output3.value = True if b3 else False

        self.__motor_select_output0.value = True if m0 else False
        self.__motor_select_output1.value = True if m1 else False
        self.__motor_select_output2.value = True if m2 else False

        self.__sync_output.value = syncBit
