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
    

def send_test_data(token):
    headers = {"Authorization": token}

    print("[INFO] Test data sending...")
    try:
        date_time = datetime.now()
        date_time_parse = date_time.strftime("%Y-%m-%d %H:%M:%S")

        response = requests.post(url='http://backend-seastead.red-electronics.pl/manager/adddata', 
                                json={  'valdate' : date_time_parse, 'powtotal': 123, 'powout1' : 1, "powout2" : 1, "powout3" : 1, "powout4" : 1,	"powout5" : 1, "powout6" : 1,
                                        "powout7" : 1, "powout8" : 1, "powout9" : 1, "powout10" : 1, "wodapitna1" : 15, "wodapitna2" : 21, "wodabrudna" : 16, "szambo" : 5, "paliwo" : 1,
                                        "temp1" : 21.7, "temp2" : 22.9, "temp3" : 20.0, "press1" : 1012, "press2" : 1012, "press3" : 1004, "humid1" : 24, "humid2" : 56, "humid3" : 34, "uq_house_id" : "dnw1", "ac_state" : 1,
                                        "tempdate" : date_time_parse, "temp_on" : True, "freeze_protect" : False, "temp_set" : 22.0}, 
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