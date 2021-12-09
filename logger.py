import sys
import os

from datetime import datetime

LABELS = {"Date" : " ", "Time" : " ", "PowTotal" : 0.0, "WodaPitna1" : 0, "WodaPitna2" : 0, "WodaBrudna" : 0,  "Szambo" : 0, "Paliwo" : 0, 
          "TempSalon" : 0.0, "TempKuchnia" : 0.0, "TempTaras" : 0.0, "PressSalon" : 0.0, "PressTaras" : 0.0,
          "HumidSalon" : 0.0, "HumidKuchnia" : 0.0, "HumidTaras" : 0.0}

class Logger():
    def __init__(self):
        path = os.getcwd()
        path = os.path.join(path, "logs")

        # check if path exists
        if not os.path.exists(path=path):
            try:
                os.makedirs(path)
                print("[INFO] Logger directory created")
            except Exception as msg:
                print(f"Error {msg} occured....")

        else:
            print("[INFO] Logger directory already exists")

    def logData(self, resources):
        date = datetime.now().strftime("%Y_%m_%d")
        time = datetime.now().strftime("%H:%M:%S")

        # check if log file exists 
        path = os.getcwd()
        path = os.path.join(path, "logs", date)

        if not os.path.exists(path=path):
            try:
                os.makedirs(path)
            except Exception as msg:
                print(f"Error {msg} occured....")
            finally:
                with open(path, 'w') as f:
                    f.write(",".join(list(LABELS.keys())) + '\n')

        
        with open(path, 'a') as f:
            f.write(s)
