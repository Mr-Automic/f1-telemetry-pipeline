# F1 Practice: Modular Architecture 🏎️

A clean-slate, decoupled implementation of a Formula 1 database tracking system using Object-Oriented Programming (OOP) principles.

## 🧱 Layer 1: Data Modeling & Encapsulated Core
In this initial phase, the core data models were isolated to ensure zero-dependency data handling before introducing database logic.

### Key Technical Achievements:
* **Environment Isolation:** Configured a clean virtual environment (`.venv`) and robust `.gitignore` setup to prevent environment pollution.
* **Data Encapsulation:** Implemented the `Driver` model to safely parse raw incoming JSON/dictionary data using defensive programming.
* **Architectural Decoupling:** Added the `to_tuple()` adapter method to eliminate tight coupling, shielding the database manager from internal model changes.
* **Rigorous Verification:** Created `test_models.py` to independently verify data instantiation and formatting consistency.

### How to Run Verification
```bash
source .venv/bin/activate
python3 test_models.py