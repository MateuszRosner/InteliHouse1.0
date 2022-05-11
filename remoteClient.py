from concurrent.futures import thread
import threading
import requests
from datetime import datetime
from requests.exceptions import HTTPError

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

        response = requests.post(url='http://backend-seastead.red-electronics.pl/manager/adddata', 
                                json={  'powtotal': 123, 'powout1' : 28, "powout2" : 16, "powout3" : 5, "powout4" : 33, "powout5" : 8, "powout6" : 8,
                                        "powout7" : 66, "powout8" : 5, "powout9" : 44, "powout10" : 7, "wodapitna1" : 10, "wodapitna2" : 16, "wodabrudna" : 27, "szambo" : 13, "paliwo" : 1,
                                        "temp1"  : resources.temperature[0]/10.0, "temp2"  : resources.temperature[1]/10.0, "temp3"  : resources.temperature[2]/10.0, 
                                        "press1" : resources.pressure[0]/10.0,   "press2" : resources.pressure[1]/10.0,   "press3" : resources.pressure[2]/10.0, 
                                        "humid1" : resources.humidity[0]/10.0,   "humid2" : resources.humidity[1]/10.0,   "humid3" : resources.humidity[2]/10.0, 
                                        "ac_state" : 1, "temp_on" : True, "freeze_protect" : False, "temp_set" : 22.0,
                                        "uq_house_id" : "dnw1", 'valdate' : date_time_parse, "tempdate" : date_time_parse}, 
                                        headers=headers)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        print('Success!')
        print(response.text)

if __name__ == "__main__":
    token = log_to_panel()
    check_log_status(token)
    send_test_data(token)