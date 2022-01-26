import threading
import serial
import RPi._GPIO as GPIO
import configparser
import time

import modbusCommands as mC

from modbusFrame import ModbusFrame

TXDEN_1 = 27
TXDEN_2 = 22

BAUD_38400 = 38400
BAUD_9600  = 9600

    
class Modbus():
    def __init__(self, baudrate=9600, dev="/dev/ttySC1", crcControl=True, dataLen=8):
         # --------------- config file reading    ---------------
        config = configparser.ConfigParser()
        config.read('config.ini')

        self.ser=serial.Serial(
            baudrate=baudrate,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=0.1)

        self.dev = dev
        self.ser.port = self.dev

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(TXDEN_2, GPIO.OUT)
        GPIO.output(TXDEN_2, GPIO.HIGH)

        try:
            self.ser.open() 
        except serial.SerialException:
            print("[ERROR] Can't open serial port")

        self.frame = ModbusFrame(4)
        self.rec_data_len = dataLen
        self.crc_control = crcControl
    
    def send_frame(self, frame):
        
        if self.ser.isOpen():
            frame.calcCRC()
            GPIO.output(TXDEN_2, GPIO.LOW)     # transmitter
            time.sleep(0.006)
            frame = bytearray(frame)
            self.ser.write(frame)
            time.sleep(0.004)
            GPIO.output(TXDEN_2, GPIO.HIGH)    # reciver

    def read_data(self):
        if self.ser.isOpen() == True:
            data = self.ser.read(self.rec_data_len)
            data = bytearray(data)

            if len(data) < self.rec_data_len:
                self.frame.clear()
                self.ser.flush()
                return False
            else:
                self.frame.address = (data[0])
                self.frame.command = (data[1])
                self.frame.data.append((data[2]))
                self.frame.data.append((data[3]))
                self.frame.data.append((data[4]))
                self.frame.data.append((data[5]))
                self.frame.data.append((data[6]))
                #self.frame.data.append((data[7]))

                self.frame.CRC = (data[7] & 0xFF) | (data[8] << 8)

                print(self.frame)

                # check CRC
                """if self.crc_control == True:
                    CRC = self.frame.CRC
                    self.frame.calcCRC()

                    if CRC != self.frame.CRC:
                        print("[WARNING] CRC error")
                        self.frame.clear()
                        self.ser.flush()
                        return False  """
        
                
        self.frame.data.clear()
        return True

    def Test(self):
        frame = ModbusFrame(4)
        frame.address = 0x01
        frame.command = 0x03
        frame.data[0] = 0x00
        frame.data[1] = 0x01
        frame.data[2] = 0x00
        frame.data[3] = 0x01
        
        self.send_frame(frame)

        if self.read_data() == True:
            print("Modbus alive")
        else:
            print("Modbus is dead")
    
    def FlushBuffer(self):
        self.ser.flush()

    

if __name__ == "__main__":
    pass


