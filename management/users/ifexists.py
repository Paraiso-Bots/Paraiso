import os
import json

def ifexists(user_id):
    # Docstring
    """
    Checks if a user exists in the database
    """
    with open("users.json", "r") as f:
        users = json.load(f)
    if str(user_id) in users:
        return True
    else:
        return False
