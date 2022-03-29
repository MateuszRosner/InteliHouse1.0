from concurrent.futures import thread
import threading
import requests
import threading
from requests.exceptions import HTTPError

def test_run():
    for url in ['http://localhost:8080/']:
        try:
            #response = requests.get(url)
            response = requests.post(url, json={'current_user_url': 'https://api.github.com/user', 'u_id' : '123-987'})
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

if __name__ == "__main__":
    test_run()
