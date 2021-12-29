import threading
import serial
import RPi._GPIO as GPIO
import configparser

import redbusCommands as mC
from infrastructure import Infrastructure

TXDEN_1 = 27
TXDEN_2 = 22

BAUD_38400 = 38400

crcTable = [
	0X0000, 0XC0C1, 0XC181, 0X0140, 0XC301, 0X03C0, 0X0280, 0XC241,
	0XC601, 0X06C0, 0X0780, 0XC741, 0X0500, 0XC5C1, 0XC481, 0X0440,
	0XCC01, 0X0CC0, 0X0D80, 0XCD41, 0X0F00, 0XCFC1, 0XCE81, 0X0E40,
	0X0A00, 0XCAC1, 0XCB81, 0X0B40, 0XC901, 0X09C0, 0X0880, 0XC841,
	0XD801, 0X18C0, 0X1980, 0XD941, 0X1B00, 0XDBC1, 0XDA81, 0X1A40,
	0X1E00, 0XDEC1, 0XDF81, 0X1F40, 0XDD01, 0X1DC0, 0X1C80, 0XDC41,
	0X1400, 0XD4C1, 0XD581, 0X1540, 0XD701, 0X17C0, 0X1680, 0XD641,
	0XD201, 0X12C0, 0X1380, 0XD341, 0X1100, 0XD1C1, 0XD081, 0X1040,
	0XF001, 0X30C0, 0X3180, 0XF141, 0X3300, 0XF3C1, 0XF281, 0X3240,
	0X3600, 0XF6C1, 0XF781, 0X3740, 0XF501, 0X35C0, 0X3480, 0XF441,
	0X3C00, 0XFCC1, 0XFD81, 0X3D40, 0XFF01, 0X3FC0, 0X3E80, 0XFE41,
	0XFA01, 0X3AC0, 0X3B80, 0XFB41, 0X3900, 0XF9C1, 0XF881, 0X3840,
	0X2800, 0XE8C1, 0XE981, 0X2940, 0XEB01, 0X2BC0, 0X2A80, 0XEA41,
	0XEE01, 0X2EC0, 0X2F80, 0XEF41, 0X2D00, 0XEDC1, 0XEC81, 0X2C40,
	0XE401, 0X24C0, 0X2580, 0XE541, 0X2700, 0XE7C1, 0XE681, 0X2640,
	0X2200, 0XE2C1, 0XE381, 0X2340, 0XE101, 0X21C0, 0X2080, 0XE041,
	0XA001, 0X60C0, 0X6180, 0XA141, 0X6300, 0XA3C1, 0XA281, 0X6240,
	0X6600, 0XA6C1, 0XA781, 0X6740, 0XA501, 0X65C0, 0X6480, 0XA441,
	0X6C00, 0XACC1, 0XAD81, 0X6D40, 0XAF01, 0X6FC0, 0X6E80, 0XAE41,
	0XAA01, 0X6AC0, 0X6B80, 0XAB41, 0X6900, 0XA9C1, 0XA881, 0X6840,
	0X7800, 0XB8C1, 0XB981, 0X7940, 0XBB01, 0X7BC0, 0X7A80, 0XBA41,
	0XBE01, 0X7EC0, 0X7F80, 0XBF41, 0X7D00, 0XBDC1, 0XBC81, 0X7C40,
	0XB401, 0X74C0, 0X7580, 0XB541, 0X7700, 0XB7C1, 0XB681, 0X7640,
	0X7200, 0XB2C1, 0XB381, 0X7340, 0XB101, 0X71C0, 0X7080, 0XB041,
	0X5000, 0X90C1, 0X9181, 0X5140, 0X9301, 0X53C0, 0X5280, 0X9241,
	0X9601, 0X56C0, 0X5780, 0X9741, 0X5500, 0X95C1, 0X9481, 0X5440,
	0X9C01, 0X5CC0, 0X5D80, 0X9D41, 0X5F00, 0X9FC1, 0X9E81, 0X5E40,
	0X5A00, 0X9AC1, 0X9B81, 0X5B40, 0X9901, 0X59C0, 0X5880, 0X9841,
	0X8801, 0X48C0, 0X4980, 0X8941, 0X4B00, 0X8BC1, 0X8A81, 0X4A40,
	0X4E00, 0X8EC1, 0X8F81, 0X4F40, 0X8D01, 0X4DC0, 0X4C80, 0X8C41,
	0X4400, 0X84C1, 0X8581, 0X4540, 0X8701, 0X47C0, 0X4680, 0X8641,
	0X8201, 0X42C0, 0X4380, 0X8341, 0X4100, 0X81C1, 0X8081, 0X4040
    ]

class RedbusFrame():
    def __init__(self, data_length):
        self.address = 0
        self.command = 0
        self.data_length = data_length
        self.data = [0 for _ in range(data_length)]
        self.CRC = 0

    def calcCRC(self):
        length = len(self) - 2                          # length of header and payload
        temp = 0
        crcWord = 0xFFFF
        self.__iter__()

        while(length):
            temp = (self.__next__() ^ crcWord) & 0xFF   # reduce value to 8-bit length
            crcWord = crcWord >> 8
            crcWord ^= crcTable[temp]
            length -= 1

        self.CRC = crcWord

    def clear(self):
        self.address = 0
        self.command = 0
        self.data.clear()
        self.CRC = 0

    def __repr__(self):
        return (f"Address: {self.address}, Command: {self.command}, Data: {self.data}, CRC: {self.CRC}")

    def __len__(self):
        len = 0
        for _ in self:
            len += 1

        return len

    def __iter__(self):
        self.index = 0
        return(self)

    def __next__(self):
        if self.index < 8:
            if self.index == 0:
                data = self.address
            elif self.index == 1:
                data = self.command
            elif self.index == 2:
                data = self.data[0]
            elif self.index == 3:
                data = self.data[1]
            elif self.index == 4:
                data = self.data[2]
            elif self.index == 5:
                data = self.data[3]
            elif self.index == 6:
                data = self.CRC & 0xFF
            elif self.index == 7:
                data = ((self.CRC >> 8) & 0xFF)

            self.index += 1

            return data
        else:
            raise StopIteration            

    
class Redbus():
    def __init__(self, resources, Baudrate = 38400, dev = "/dev/ttyS0", crcControl=True, dataLen=8):
        self.mainOutputs = config['MAIN_OUTPUTS']

        self.ser=serial.Serial(
            baudrate=Baudrate,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=0.1)
        self.dev = dev
        self.ser.port = self.dev

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(TXDEN_1, GPIO.OUT)
        GPIO.setup(TXDEN_2, GPIO.OUT)

        GPIO.output(TXDEN_1, GPIO.HIGH)
        GPIO.output(TXDEN_2, GPIO.HIGH)

        try:
            self.ser.open() 
        except serial.SerialException:
            print("[ERROR] Can't open serial port")

        self.resources = resources
        self.infrastructure = Infrastructure('config.ini')
        self.frame = RedbusFrame(dataLen)
        self.rec_data_len = dataLen
        self.crc_control = crcControl
        self.thread = threading.Thread(target=self.read_data)
        self.thread.daemon = True
        self.thread.start()
        print("[INFO] Modbus thread started....")
    
    def send_frame(self, frame):
        if self.ser.isOpen():
            frame.calcCRC()
            GPIO.output(TXDEN_1, GPIO.LOW)     # transmitter
            frame = bytearray(frame)
            self.ser.write(frame)
            GPIO.output(TXDEN_1, GPIO.HIGH)    # recive


    def read_data(self):
            
        while self.ser.isOpen():
            try:
                data = self.ser.read(self.rec_data_len)
                data = bytearray(data)

            except serial.SerialTimeoutException:
                print("[WARNING] Timeout exception...")
                return
            
            if len(data) < self.rec_data_len:
                self.frame.clear()
                self.ser.flush()
            else:
                self.frame.address = (data[0])
                self.frame.command = (data[1])
                self.frame.data.append((data[2]))
                self.frame.data.append((data[3]))
                self.frame.data.append((data[4]))
                self.frame.data.append((data[5]))
                self.frame.CRC = (data[6] & 0xFF) | (data[7] << 8)

                # check CRC
                if self.crc_control == True:
                    CRC = self.frame.CRC
                    self.frame.calcCRC()

                    if CRC != self.frame.CRC:
                        print("[WARNING] CRC error")
                        self.frame.clear()
                        self.ser.flush()
                        continue
                
                # decode data from MainBoard 
                if self.frame.address == 1:
                    # current values of 2 ports (ports number determined by command value)                                             
                    if (self.frame.command >= mC.MAIN_BOARD_READ_CURR_1_2) and (self.frame.command <= mC.MAIN_BOARD_READ_CURR_9_10):        
                        current_val1 =   self.frame.data[1] << 8
                        current_val1 +=  self.frame.data[0]
                        
                        current_val2 =   self.frame.data[3] << 8
                        current_val2 +=  self.frame.data[2]

                        self.resources.output_currs[(self.frame.command * 2)-2] = current_val1
                        data_bank.output_currs[(self.frame.command * 2)-1] = current_val2

                    elif self.frame.command == mC.MAIN_BOARD_READ_DIGITAL_IN:
                        pass

                    # outputs
                    elif self.frame.command == mC.MAIN_BOARD_OUTPUTS:                                                               
                        ports =     self.frame.data[1] << 8
                        ports +=    self.frame.data[0]
                        
                        for x in range(len(data_bank.output_ports)):
                            self.resources.output_ports[x] = bool (ports & (1 << x))

                # decode data from SensorsBoards
                elif self.frame.address == 15:
                    if self.frame.command == mC.SENSORS_BOARD_READ_DISTANCE:
                        self.resources.liquids[0] = self.frame.data[0]
                        self.resources.liquids[1] = self.frame.data[1]
                        self.resources.liquids[2] = self.frame.data[2]
                        self.resources.liquids[3] = self.frame.data[3]

                elif self.frame.address == 14:
                    if self.frame.command == mC.SENSORS_BOARD_READ_DISTANCE:
                        self.resources.liquids[0] = self.frame.data[0]
                        self.resources.liquids[1] = self.frame.data[1]
                        self.resources.liquids[2] = self.frame.data[2]
                        self.resources.liquids[3] = self.frame.data[3]
                
                # decode data from AmbientBoards
                elif self.frame.address == 13:
                    if self.frame.command == mC.AMBIENT_BOARD_READ_TEMP_PRESS:
                        self.resources.temperature[2]   = self.frame.data[1] << 8 | self.frame.data[0]
                        self.resources.pressure[2]      = self.frame.data[3] << 8 | self.frame.data[2]

                    elif self.frame.command == mC.AMBIENT_BOARD_READ_HUMID_GAS:
                        self.resources.humidity[2]      = self.frame.data[1] << 8 | self.frame.data[0]

                elif self.frame.address == 12:
                    if self.frame.command == mC.AMBIENT_BOARD_READ_TEMP_PRESS:
                        self.resources.temperature[1]   = self.frame.data[1] << 8 | self.frame.data[0]
                        self.resources.pressure[1]      = self.frame.data[3] << 8 | self.frame.data[2]

                    elif self.frame.command == mC.AMBIENT_BOARD_READ_HUMID_GAS:
                        self.resources.humidity[1]      = self.frame.data[1] << 8 | self.frame.data[0]

                elif self.frame.address == 11:
                    if self.frame.command == mC.AMBIENT_BOARD_READ_TEMP_PRESS:
                        self.resources.temperature[0]   = self.frame.data[1] << 8 | self.frame.data[0]
                        self.resources.pressure[0]      = self.frame.data[3] << 8 | self.frame.data[2]

                    elif self.frame.command == mC.AMBIENT_BOARD_READ_HUMID_GAS:
                        self.resources.humidity[0]      = self.frame.data[1] << 8 | self.frame.data[0]

                self.frame.data.clear()
    
    def FlushBuffer(self):
        self.ser.flush()

    

if __name__ == "__main__":
    f = RedbusFrame(4)

    length = len(f) -2 
    
    f.address = 1
    f.command = 3

    f.__iter__()

    while(length):
        print(f.__next__())
        length -= 1

    f.calcCRC()
    print(f.CRC)


