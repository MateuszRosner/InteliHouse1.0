import sys
import time
import datetime
import threading

import redbus
import configparser
import redbusCommands as mC
import modbus
import remoteClient

from logger    import Logger
from resources import Resources

from PyQt5 import QtCore, QtWidgets

class App():
    def __init__(self):
        # init objects
        self.resources = Resources()
        self.redbus = redbus.Redbus(resources=self.resources, dev="/dev/ttySC0")
        self.modbus = modbus.Modbus(dev="/dev/ttySC1", dataLen=7)

        self.frame = redbus.RedbusFrame(4)

        # misc variables
        #self.logger = Logger()
        self.prescaller = 1
        self.counter = 0

        # --------------- config file reading    ---------------
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')

        self.refreshTime            = int(self.config['PARAMETERS']['RefreshFrequency'])
        self.mainOutputs            = self.config['MAIN_OUTPUTS']
        self.maxSamples             = int(self.config['CHARTS']['MaxSamples'])
        self.priorities             = self.config['MAIN_OUTPUTS']['Priorities'].split(',')

        self.infrastructure         = self.config['INFRASTRUCTURE']
        self.addresses              = self.config['ADDRESSES']
        
        # run REDBUS and initiate modules
        self.redbus.initiate_modules()
        self.redbus.startUpdates()

        print("[INFO] Application initialized properly")

    def refresh(self): 
        self.modbus.read_ac_params()
        print(self.resources.temperature)

        self.prescaller -= 1
        if self.prescaller == 0:
            #self.logger.logData(self.resources)
            self.prescaller = int(self.config['LOGGER']['Prescaller'])
            
            token = remoteClient.log_to_panel()
            response = remoteClient.send_test_data(token, self.resources)

            try:
                for idx in range(1, 11, 1):
                    self.resources.relays[idx-1] = int(bool(response[f"output{idx}"]))    
            except Exception as err:
                print(f'Other error occurred: {err}')

        if threading.main_thread().is_alive():
            threading.Timer(self.refreshTime/1000, self.refresh).start()

if __name__ == "__main__":
    app = App()
    time.sleep(2)
    app.refresh()
    while True:
        pass
    print("Finish")