from database import DatabaseManager
from models import Driver
from api import F1ApiClient

def main():
    api_client = F1ApiClient()
    print("loading connection ...")
    row_drivers = api_client.get_live_drivers()

    if not row_drivers:
        print("faild to take the data drivers !")
        return 
    
    db = DatabaseManager()

    print(f"loading {len(row_drivers)} ... ")

    for driver_data in row_drivers:
        obj_driver = Driver(driver_data)
        db.insert_driver(obj_driver)

    db.close_connection()
    print('done')

if __name__ == "__main__":
    main()
