import sqlite3

class DatabaseManager:
    def __init__(self, db_name='f1_modular.db'):
        self.con = sqlite3.connect(db_name)
        self.cur = self.con.cursor()
        self._create_table()

    def _create_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS drivers(
                    driver_number TEXT PRIMARY KEY,
                    full_name TEXT,
                    team_name TEXT,
                    country_code TEXT)""")
        
        self.con.commit()
        print("-- Database Infrastructure Initialized Successfully --")

    def insert_driver(self, driver_obj):
        driver_tuple = driver_obj.to_tuple()
        self.cur.execute("INSERT OR IGNORE INTO drivers(driver_number, full_name, team_name, country_code) VALUES (?,?,?,?)",driver_tuple)
        self.con.commit()

        if self.cur.rowcount > 0:
            print(f"Driver [{driver_obj._driver_number}] Inserted Successfully.")
        else:
            print(f"Driver [{driver_obj._driver_number}] Already exists. Skipped (Ignored).")
        
    def update_driver_team(self, driver_number, new_team_name):
        self.cur.execute("UPDATE drivers SET team_name = ? WHERE driver_num = ?",(new_team_name, driver_number))
        self.con.commit()
        print(f"-- Database [{driver_number}] updated Successfully --")

    def delete_driver(self, driver_number):
        self.cur.execute("DELETE FROM drivers WHERE driver_num = ?",(driver_number,))
        self.con.commit()
        print(f"-- Database [{driver_number}] deleted Successfully --")

    def get_all_drivers(self):
        self.cur.execute("SELECT driver_number, full_name, team_name, country_code FROM drivers")
        rows = self.cur.fetchall()

        driver_list = []
        for row in rows:
            driver_list.append({
                "driver_num": row[0],
                "full_name": row[1],
                "team_name": row[2],
                "country_code": row[3]
            })
        return driver_list
    
    def close_connection(self):
        self.cur.close()
        self.con.close()
        print("-- Database Connection Safeguarded & Closed --")

