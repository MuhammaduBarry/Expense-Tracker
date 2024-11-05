import json
import datetime

json_file_path = "./src/data.json"

def load_json(file_path: str):
    """Load file and read data"""
    with open(file_path, "r") as file:
        return json.load(file)

def dump_json(data: dict, file_path: str):
    """Inserts new data into file"""
    with open(file_path, "w") as file:
        return json.dump(data, file, indent=4)

def increment_number() -> int:
    """Increment number"""
    data = load_json(json_file_path)
    increment = data.get("amount_of_expenses", 0) + 1
    data["amount_of_expenses"] = increment
    dump_json(data, json_file_path)

    return increment

def get_month() -> int:
    """Return Month number"""
    current_month = int(datetime.datetime.now().strftime("%m"))
    month_dict = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    return current_month

