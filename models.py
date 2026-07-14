class Driver:
    def __init__(self,data):
        self._driver_number = data.get('driver_number')
        self._full_name = data.get('full_name')
        self._team_name = data.get('team_name')
        self._country_code = data.get('country_code')

    def to_tuple(self):
        return (self._driver_number, self._full_name, self._team_name, self._country_code )
    
    def display_drivers(self):
        print(f'[{self._driver_number}] {self._full_name} {self._team_name}-{self._country_code}')
