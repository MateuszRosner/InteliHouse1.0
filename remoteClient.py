from concurrent.futures import thread
import threading
import requests
from datetime import datetime
from requests.exceptions import HTTPError
import resources

login = 'DNW1'
password = 'A8NE77?_33'

def log_to_panel():
    print("[INFO] Token aquisition started...")
    payload = dict(username=login, password=password)
    try:
        token = requests.post(url='http://backend-seastead.red-electronics.pl/manager/login', json={'username' : login, 'password' : password})
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        print('[INFO] Success, token aquired!')
        token = token.json()
        print(token['token'])
        return token['token']

def check_log_status(token):
    headers = {"Authorization": token}
    
    print("[INFO] Check logging status...")
    try:
        response = requests.get(url='http://backend-seastead.red-electronics.pl/manager/protected', headers=headers)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        print('Success, user logged!')
        print(response.text)
    

def send_test_data(token, resources):
    headers = {"Authorization": token}

    print("[INFO] Test data sending...")
    try:
        date_time = datetime.now()
        date_time_parse = date_time.strftime("%Y-%m-%d %H:%M:%S")

        if resources.tempdate == 0:
            resources.tempdate = date_time_parse

        response = requests.post(url='http://backend-seastead.red-electronics.pl/manager/adddata', 
                                json={  'powtotal': 0, 'powout1' : 0, "powout2" : 0, "powout3" : 0, "powout4" : 0, "powout5" : 0, 
                                        "powout6" : 0, "powout7" : 0, "powout8" : 0, "powout9" : 0, "powout10" : 0, 
                                        "wodapitna1" : resources.liquids[0],      "wodapitna2" : resources.liquids[1],      "wodabrudna" : resources.liquids[2], "szambo" : resources.liquids[3], "paliwo" : resources.liquids[4],
                                        "temp1"  : resources.temperature[0]/10.0, "temp2"  : resources.temperature[1]/10.0, "temp3"  : resources.temperature[2]/10.0, 
                                        "press1" : resources.pressure[0]/10.0,    "press2" : resources.pressure[1]/10.0,    "press3" : resources.pressure[2]/10.0, 
                                        "humid1" : resources.humidity[0]/10.0,    "humid2" : resources.humidity[1]/10.0,    "humid3" : resources.humidity[2]/10.0, 
                                        "ac_state" : resources.ac_state,          "temp_on" : resources.temp_on ,           "freeze_protect" : resources.anti_freez,        "temp_set" : resources.ac_temp,
                                        "uq_house_id" : "dnw1",                   'valdate' : date_time_parse,              "tempdate" : resources.tempdate}, 
                                        headers=headers)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        print('Success!')
        print(response.text)
        return response.json()

if __name__ == "__main__":
    res = resources.Resources()
    token = log_to_panel()
    check_log_status(token)
    send_test_data(token, res)