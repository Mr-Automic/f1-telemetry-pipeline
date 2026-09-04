import psycopg2
from psycopg2 import OperationalError, DatabaseError
import os
from dotenv import load_dotenv

load_dotenv()

class DatabaseManager:
    def __init__(self):
        self.con = psycopg2.connect(
            host=os.getenv("DB_HOST", "localhost"),
            port=os.getenv("DB_PORT", "5432"),
            database=os.getenv("DB_NAME", "f1_db"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        self.cur = self.con.cursor()
        self._create_table()

    def _create_table(self):
        query ="""CREATE TABLE IF NOT EXISTS drivers(
                    driver_number VARCHAR(10) PRIMARY KEY,
                    full_name VARCHAR(100),
                    team_name VARCHAR(100),
                    country_code VARCHAR(10));"""
        
        self.cur.execute(query)
        self.con.commit()
        print("-- Database Infrastructure Initialized Successfully --")

    def insert_driver(self, driver_obj):
        driver_tuple = driver_obj.to_tuple()

        query = """INSERT INTO drivers(driver_number, full_name, team_name, country_code)
                VALUES (%s,%s,%s,%s) ON CONFLICT (driver_number) DO NOTHING;"""
        
        self.cur.execute(query, driver_tuple)
        self.con.commit()

        if self.cur.rowcount > 0:
            print(f"Driver [{driver_obj._driver_number}] Inserted Successfully.")
        else:
            print(f"Driver [{driver_obj._driver_number}] Already exists. Skipped (Ignored).")
        
    def update_driver_team(self, driver_number, new_team_name):
        
        query = """UPDATE drivers SET team_name = %s WHERE driver_number = %s"""

        self.cur.execute(query,(new_team_name, driver_number))
        self.con.commit()
        print(f"-- Database [{driver_number}] updated Successfully --")
        return self.cur.rowcount > 0

    def delete_driver(self, driver_number):
        query = "DELETE FROM drivers WHERE driver_number = %s"

        self.cur.execute(query,(driver_number,))
        self.con.commit()
        print(f"-- Database [{driver_number}] deleted Successfully --")
        return self.cur.rowcount > 0

    def get_all_drivers(self):
        query = "SELECT driver_number, full_name, team_name, country_code FROM drivers"

        self.cur.execute(query)
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
    
    def get_driver_by_num(self, driver_num):
        query = "SELECT driver_number, full_name, team_name, country_code FROM drivers WHERE driver_number = %s"

        self.cur.execute(query,(driver_num,))
        row = self.cur.fetchone()

        if row is not None:
            return{
                "driver_num": row[0],
                "full_name": row[1],
                "team_name": row[2],
                "country_code": row[3]
            }
        return None

    def close_connection(self):
        self.cur.close()
        self.con.close()
        print("-- Database Connection Safeguarded & Closed --")

