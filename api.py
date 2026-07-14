import requests

class F1ApiClient:
    def __init__(self):
        self.url = "https://api.openf1.org/v1/drivers"

    def get_live_drivers(self, session_key=9158):
        try:
            params = {"session_key": session_key}
            response = requests.get(self.url, params=params, timeout=10)
            if response.status_code != 200:
                print(f"error from the server [{response.status_code}]")
                return []

            data = response.json()
            if isinstance(data,list):
                return data
            
            print("the api data is not a list")
            return []
        
        except requests.exceptions.RequestException as e:
            print(f"error connection {e}")
            return []