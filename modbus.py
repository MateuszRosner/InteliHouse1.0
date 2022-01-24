import threading
import serial
import RPi._GPIO as GPIO
import configparser
import time
import minimalmodbus

import modbusCommands as mC

TXDEN_1 = 27
TXDEN_2 = 22

BAUD_38400 = 38400

         

    
class Modbus():
    def __init__(self, baudrate=9600, dev="/dev/ttySC1", crcControl=True, slaveAdr=1):
         # --------------- config file reading    ---------------
        config = configparser.ConfigParser()
        config.read('config.ini')

        self.rtd_net = minimalmodbus.Instrument(dev, slaveAdr)
        self.rtd_net.serial.baudrate = baudrate
        self.rtd_net.serial.bytesize = 8
        self.rtd_net.serial.parity   = serial.PARITY_NONE
        self.rtd_net.serial.stopbits = 1
        self.rtd_net.serial.timeout  = 0.1

        self.rtd_net.clear_buffers_before_each_transaction = True

        """self.ser=serial.Serial(
            baudrate=Baudrate,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=0.1)
        self.dev = dev
        self.ser.port = self.dev"""

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(TXDEN_2, GPIO.OUT)
        GPIO.output(TXDEN_2, GPIO.HIGH)

        """try:
            self.ser.open() 
        except serial.SerialException:
            print("[ERROR] Can't open serial port")"""

        """self.frame = ModbusFrame(4)
        self.rec_data_len = dataLen
        self.crc_control = crcControl
        self.thread = threading.Thread(target=self.read_data, args=(data_bank,))
        self.thread.daemon = True
        self.thread.start()
        print("[INFO] Modbus thread started....")"""
    
    def send_frame(self, frame):
        
        if self.ser.isOpen():
            """frame.calcCRC()
            GPIO.output(TXDEN_1, GPIO.LOW)     # transmitter
            time.sleep(0.0008)
            frame = bytearray(frame)
            self.ser.write(frame)
            time.sleep(0.0008)
            GPIO.output(TXDEN_1, GPIO.HIGH)    # reciver"""

    def read_data(self, data_bank):
            
        """while self.ser.isOpen():
            try:
                data = self.ser.read(self.rec_data_len)
                data = bytearray(data)

            except serial.SerialTimeoutException:
                print("[WARNING] Timeout exception...")
                return
            
            if len(data) < self.rec_data_len:
                self.frame.data.clear()
            else:
                self.frame.address = (data[0])
                self.frame.command = (data[1])
                self.frame.data.append((data[2]))
                self.frame.data.append((data[3]))
                self.frame.data.append((data[4]))
                self.frame.data.append((data[5]))
                if self.rec_data_len > 6:
                    self.frame.CRC = (data[6] & 0xFF) | (data[7] << 8)

                print(self.frame)

                # check CRC
                if self.crc_control == True:
                    CRC = self.frame.CRC
                    self.frame.calcCRC()

                    if CRC != self.frame.CRC:
                        print("[WARNING] CRC error")
                        self.frame.data.clear()
                        continue"""

        """if self.frame.address == 1:                            # decode data from MainBoard
            if self.frame.command > mC.MAIN_BOARD_OUTPUTS:     # current values of 2 ports (ports number determined by command value)
                current_val1 =   self.frame.data[1] << 8
                current_val1 +=  self.frame.data[0]
                
                current_val2 =   self.frame.data[3] << 8
                current_val2 +=  self.frame.data[2]

                data_bank.output_currs[(self.frame.command * 2)-2] = current_val1# // int(self.mainOutputs['Calibration'].split(',')[(self.frame.command * 2)-2])
                data_bank.output_currs[(self.frame.command * 2)-1] = current_val2# // int(self.mainOutputs['Calibration'].split(',')[(self.frame.command * 2)-1])

                print(f"Current {(self.frame.command*2)-1}: {current_val1}  Current {self.frame.command*2}: {current_val2}")

            elif self.frame.command == mC.MAIN_BOARD_READ_DIGITAL_IN:
                pass

            else:                                           # outputs currents
                ports =     self.frame.data[1] << 8
                ports +=    self.frame.data[0]
                
                for x in range(len(data_bank.output_ports)):
                    data_bank.output_ports[x] = bool (ports & (1 << x))
            
                print(f"Inputs: {self.frame.data[0]}")
            
        elif self.frame.address == 14:
            if self.frame.command == mC.SENSORS_BOARD_READ_DISTANCE:
                data_bank.liquids[0] = self.frame.data[3]"""
                
        self.frame.data.clear()

    def Test(self):
        GPIO.output(TXDEN_2, GPIO.LOW)     # transmitter
        print(self.rtd_net.read_register(1))
        GPIO.output(TXDEN_2, GPIO.HIGH)    # reciver
    
    def FlushBuffer(self):
        self.ser.flush()

    

if __name__ == "__main__":
    pass


