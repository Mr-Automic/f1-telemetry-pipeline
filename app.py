from fastapi import FastAPI
from database import DatabaseManager

app = FastAPI(title="F1 Driver Live Directory 🏎️")

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
