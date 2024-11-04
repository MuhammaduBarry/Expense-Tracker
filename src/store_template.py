def information_dict(id: int, date: str, description: str, amount: int) -> dict:
    """Create a dictionary for task info"""
    new_task = dict()
    new_task["id"], new_task["date"], new_task["description"], new_task["amount"] = id, date, description, amount
    return new_task