from fastapi import FastAPI, HTTPException
from database import DatabaseManager
from pydantic import BaseModel

app = FastAPI(title="F1 Driver Live Directory 🏎️")

class DriverCreateSchema(BaseModel):
    driver_number:str
    full_name:str
    team_name:str
    country_code:str

@app.get("/")
def home():
    return {"message": "Welcome to the F1 Modular API! Go to /drivers to see the database."}

@app.get("/drivers")
def get_drivers():
    db = DatabaseManager()
    data = db.get_all_drivers()
    db.close_connection()

    return {
        "status" : "success",
        "total_results": len(data),
        "drivers": data
    }
@app.get("/drivers/{driver_number}")
def get_driver(driver_number: str):
    db = DatabaseManager()
    data1 = db.get_driver_by_num(driver_number)
    db.close_connection()

    if data1 == None:
        raise HTTPException(status_code=404,detail="Driver not found")
    else:
        return {
            "status" : "success",
            "drivers": data1
        }
    
@app.post("/drivers")
def add_new_driver(driver_data: DriverCreateSchema):
    db = DatabaseManager()
    from models import Driver
    driver_obj = Driver(driver_data.model_dump())

    db.insert_driver(driver_obj)
    db.close_connection()

    return {
            "status" : "success",
            "message": f"driver{driver_obj._driver_number} processed."
        }

@app.put("/drivers/{driver_number}")
def update_driver(driver_number:str, new_team_name:str):
    db = DatabaseManager()
    success = db.update_driver_team(driver_number, new_team_name)
    db.close_connection()

    if not success:
        raise HTTPException(status_code=404, detail="Driver to update was not found")

    return {"status": "success",
            "message": f"Driver {driver_number} team updated to {new_team_name}."
        }

@app.delete("/drivers/{driver_number}")
def delete_driver(driver_number: str):
    db = DatabaseManager()
    success = db.delete_driver(driver_number)
    db.close_connection()

    if not success:
        raise HTTPException(status_code=404, detail="Driver to delete was not found")
    return {"status": "success",
            "message": f"Driver {driver_number} deleted successfully."
        }