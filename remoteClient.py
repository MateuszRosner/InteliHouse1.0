import requests
from datetime import datetime
from requests.exceptions import HTTPError

for url in ['http://192.168.0.29:6013/addData']:
    try:
        #response = requests.get(url)
        date_time = datetime.now()
        date_time_parse = date_time.strftime("%Y-%m-%d %H:%M:%S")

        response = requests.post(url, json={'valdate' : date_time_parse, 'powtotal': 123, 'powout1' : 1, "powout2" : 1, "powout3" : 1, "powout4" : 1,	"powout5" : 1, "powout6" : 1,
                                        	"powout7" : 1, "powout8" : 1, "powout9" : 1, "powout10" : 1, "wodapitna1" : 1, "wodapitna2" : 1, "wodabrudna" : 1, "szambo" : 1, "paliwo" : 1,
                                            "temp1" : 1, "temp2" : 1, "temp3" : 1, "press1" : 1, "press2" : 1, "press3" : 1, "humid1" : 1, "humid2" : 1, "humid3" : 2, "uq_house_id" : "domek1", "ac_state" : 1,
                                            "ac_temp" : 21.5})

        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('Success!')
        print(response.text)

def startUpdates(self):
        self.updateThread = threading.Thread(target=self.updateData)
        self.updateThread.daemon = True
        self.updateThread.start()
        print("[INFO] Modbus data update thread started....")
