import sys
import time
import redbus
import configparser
import redbusCommands as mC
import modbus

from InteliHouseUI import Ui_MainWindow
from PyQt5 import QtCore, QtWidgets


class Canvas(FigureCanvas):
    def __init__(self, parent):
        fig, self.ax = plt.subplots(figsize=(5,4), dpi=200)
        super().__init__(fig)
        self.setParent(parent)


class Resources():
    def __init__(self):
        self.output_ports = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.output_currs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.liquids      = [0, 0, 0, 0, 0]
        self.temperature  = [0, 0, 0]
        self.pressure     = [0, 0, 0]
        self.humidity     = [0, 0, 0]
        self.gas          = [0, 0, 0]


class MyWindow(Ui_MainWindow):
# ---------------class init functions---------------
    def __init__(self):
        super(MyWindow, self).__init__()
        self.MainWindow = QtWidgets.QMainWindow()
        self.setupUi(self.MainWindow)
        self.resources = Resources()
        self.redbus = redbus.Redbus(self.resources, dev="/dev/ttySC0")
        self.modbus = modbus.Modbus(self.resources, dev="/dev/ttySC1")
        self.modbus.crc_control = False
        self.modbus.rec_data_len = 6
        self.frame2 = modbus.ModbusFrame(4)
        self.frame = redbus.RedbusFrame(4)
        self.timer = QtCore.QTimer()

        self.progressBars = [self.progressBar1, self.progressBar2, self.progressBar3, self.progressBar4, 
                             self.progressBar5, self.progressBar6, self.progressBar7, self.progressBar8, 
                             self.progressBar9, self.progressBar10, self.progressBarWP, self.progressBarWB,
                             self.progressBarSZ, self.progressBarFU, self.progressBarFU_2,self.progressBarTotalCurr]
        self.pwrLabels = [self.labelPwr1_1, self.labelPwr1_2,  self.labelPwr1_3, self.labelPwr1_4, self.labelPwr1_5,
                           self.labelPwr1_6,  self.labelPwr1_7, self.labelPwr1_8, self.labelPwr1_9, self.labelPwr1_10,]

        self.checkBoxes = [self.checkBox1, self.checkBox2, self.checkBox3, self.checkBox4, self.checkBox5,
                           self.checkBox6, self.checkBox7, self.checkBox8, self.checkBox9, self.checkBox10]

        self.temperatures = [self.label_temp0, self.label_temp1, self.label_temp2]
        self.pressures    = [self.label_press0, self.label_press1, self.label_press2]
        self.humidities   = [self.label_hum0, self.label_hum1, self.label_hum2]
        self.iaqs         = []

        # --------------- config file reading    ---------------
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')

        self.refreshTime            = int(self.config['PARAMETERS']['RefreshFrequency'])
        self.transmissionInterval   = float(self.config['PARAMETERS']['TransmissionInterval'])
        self.infrastructure         = self.config['INFRASTRUCTURE']
        self.addresses              = self.config['ADDRESSES']
        self.mainOutputs            = self.config['MAIN_OUTPUTS']

        print("INFRASTRUCTURE:")

        for key in self.infrastructure:
            print(key, (self.infrastructure[key]))

        print("\nADDRESSES:")
        for key in self.addresses:
            print(key, (self.addresses[key].split(',')))
        
        # --------------- modules initialization ---------------
        self.initiate_modules()


        # --------------- signals - slots config ---------------
        self.timer.timeout.connect(self.refresh_ui)

        self.timer.start(self.refreshTime)

# ---------------class usage functions---------------
    """
    cyclic gui refresh with updated parameters from modules
    """
    def refresh_ui(self):    
        ports = 0
        for x, box in enumerate(self.checkBoxes):
            ports += (int(box.isChecked())) << x

        # SensorsBoard query
        addrs = self.addresses['SensorsBoard'].split(',')

        for adr in addrs:
            self.frame.address = int(adr)
            self.frame.command = mC.MODBUS_READ
            self.frame.data[0] = mC.SENSORS_BOARD_READ_DISTANCE
            self.redbus.send_frame(self.frame)

            time.sleep(self.transmissionInterval)

        # MainBoards queries
        addrs = self.addresses['MainBoard'].split(',')
        
        for adr in addrs:
            # set outputs ragardless to checkboxes
            self.frame.address = int(adr)
            self.frame.command = mC.MODBUS_WRITE
            self.frame.data[0] = mC.MAIN_BOARD_OUTPUTS
            self.frame.data[2] = (ports & 0xFF)
            self.frame.data[3] = ((ports >> 8) & 0xFF)

            self.redbus.send_frame(self.frame)
            time.sleep(self.transmissionInterval)

            # read outputs states
            self.frame.address = int(adr)
            self.frame.command = mC.MODBUS_READ
            self.frame.data[0] = mC.MAIN_BOARD_OUTPUTS
            self.redbus.send_frame(self.frame)
            time.sleep(self.transmissionInterval)
            
            # read channels currents
            for x in range(1,6):
                self.frame.address = int(adr)
                self.frame.command = mC.MODBUS_READ
                self.frame.data[0] = x
                self.redbus.send_frame(self.frame)
                time.sleep(self.transmissionInterval)

         # AmbientBoards queries
        addrs = self.addresses['AmbientBoard'].split(',')
        
        for adr in addrs:
            # temperature and pressure
            self.frame.address = int(adr)
            self.frame.command = mC.MODBUS_READ
            self.frame.data[0] = mC.AMBIENT_BOARD_READ_TEMP_PRESS
            self.redbus.send_frame(self.frame)
            time.sleep(self.transmissionInterval)

            # read humidity and IAQ
            self.frame.address = int(adr)
            self.frame.command = mC.MODBUS_READ
            self.frame.data[0] = mC.AMBIENT_BOARD_READ_HUMID_GAS
            self.redbus.send_frame(self.frame)
            time.sleep(self.transmissionInterval)

        self.frame2.address = 0x03
        self.frame2.command = 0x03
        self.frame2.data[0] = 0x00
        self.frame2.data[1] = 0x08
        self.frame2.data[2] = 0x00
        self.frame2.data[3] = 0x02

        self.modbus.send_frame(self.frame2)
        time.sleep(self.transmissionInterval)

        self.refresh_progressBars()

        self.Graph.update()
        #self.refresh_checkBoxes()
    """
    refresh progres bars 
    """
    def refresh_progressBars(self):
        avg_calbration = 0.0
        channels = 0
        for val in self.mainOutputs['Calibration'].split(','):
            avg_calbration += int(val)
            channels += 1
        
        avg_calbration = avg_calbration / channels

        # refresh currents progress bars
        for x, val in enumerate(self.resources.output_currs):
            self.progressBars[x].setValue(val // (int(self.mainOutputs['Calibration'].split(',')[x]) / 5))

        # refresh channel pwr labels
        for x,label in enumerate(self.pwrLabels):
            label.setText("{:.2f} kW" .format((self.resources.output_currs[x] / avg_calbration / 10)))

        # refresh liquids progress bars
        for x, val in enumerate(self.resources.liquids):
            self.progressBars[10 + x].setValue(val)

        # refresh total current progress bar
        self.progressBarTotalCurr.setValue(sum(self.resources.output_currs) / avg_calbration )
        self.label_11.setText("{:.2f} kWh" .format(sum(self.resources.output_currs) / avg_calbration / 10))

        for x, temp in enumerate(self.temperatures):
            temp.setText(f"{self.resources.temperature[x] / 10} *C")
        
        for x, press in enumerate(self.pressures):
            press.setText(f"{self.resources.pressure[x] / 10} hP")
        
        for x, hum in enumerate(self.humidities):
            hum.setText(f"{self.resources.humidity[x] / 10} %")
        

    def refresh_checkBoxes(self):
        for x, val in enumerate(self.resources.output_ports):
            self.checkBoxes[x].setChecked(bool(val))

    def initiate_modules(self):
        print("\n[INFO] Modules initialization....")
        if self.infrastructure['MainBoards'] != '0':
            print("[INFO] MainBoards configured...")

        if self.infrastructure['SensorsBoards'] != '0':
            # ------------- SET RELAY MODE -----------------------
            for x, adr in enumerate(self.addresses['SensorsBoard'].split(',')):
                self.frame.address = int(adr)
                self.frame.command = mC.MODBUS_WRITE
                self.frame.data[0] = mC.SENSORS_BOARD_RELAY_MODE
                self.frame.data[2] = int(self.config['SENSORS_INPUTS']['RelayMode'].split(',')[x])
                self.redbus.send_frame(self.frame)

                time.sleep(self.transmissionInterval)

            # ------------- SET THRESHOLDS -----------------------
            for x, adr in enumerate(self.addresses['SensorsBoard'].split(',')):
                thr_min = int(self.config['SENSORS_INPUTS']['PercentThMin'].split(',')[x])
                thr_max = int(self.config['SENSORS_INPUTS']['PercentThMax'].split(',')[x])
                self.frame.address = int(adr)
                self.frame.command = mC.MODBUS_WRITE
                self.frame.data[0] = mC.SENSORS_BOARD_THRESHOLDS
                self.frame.data[2] = thr_max
                self.frame.data[3] = thr_min
                self.redbus.send_frame(self.frame)

                time.sleep(self.transmissionInterval)

            for x, adr in enumerate(self.addresses['SensorsBoard'].split(',')):
                raw_min = int(self.config['SENSORS_INPUTS']['MinRaw'].split((',')[x]))
                raw_max = int(self.config['SENSORS_INPUTS']['MaxRaw'].split((',')[x]))
                self.frame.address = int(adr)
                self.frame.command = mC.MODBUS_WRITE
                self.frame.data[0] = mC.SENSORS_BOARD_RAW_VALUES
                self.frame.data[2] = raw_min
                self.frame.data[3] = raw_max
                self.redbus.send_frame(self.frame)

                time.sleep(self.transmissionInterval)


            print("[INFO] SensorsBoards configured...")
        
        if self.infrastructure['AmbientBoards'] != '0':
            print("[INFO] AmbientBoards configured...")

        if self.infrastructure['PGMBoards'] != '0':
            print("[INFO] PGMBoards configured...")

        print("[INFO] Initialization done!\n")

        
    def __del__(self):
        addrs = self.addresses['MainBoard'].split(',')

        for adr in addrs:
            # set outputs ragardless to checkboxes
            self.frame.address = int(adr)
            self.frame.command = mC.MODBUS_WRITE
            self.frame.data[0] = mC.MAIN_BOARD_OUTPUTS
            self.frame.data[2] = 0
            self.frame.data[3] = 0

            self.redbus.send_frame(self.frame)
            time.sleep(self.transmissionInterval)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = MyWindow()
    ui.MainWindow.show()
    app.exec_()
    ui.__del__()    # clear all relays outputs in MainBoard
    print("Finish")