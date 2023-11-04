import json
import os

# A class for managing users. It consists of health, energy, mood, money, inventory
class User:

    """
    A class for managing users. It consists of health, energy, mood, money, inventory.
    """
    
    def __init__(self, id):
        self.id = id
        self.health = 100
        self.energy = 100
        self.mood = 50
        self.money = 10
        self.inventory = []

    def save(self):
        with open("users.json", "r") as f:
            users = json.load(f)
        users[str(self.id)] = {
            "health": self.health,
            "energy": self.energy,
            "mood": self.mood,
            "money": self.money,
            "inventory": self.inventory
        }
        with open("users.json", "w") as f:
            json.dump(users, f, indent = 4)

    def load(self):
        with open("users.json", "r") as f:
            users = json.load(f)
        self.health = users[str(self.id)]["health"]
        self.energy = users[str(self.id)]["energy"]
        self.mood = users[str(self.id)]["mood"]
        self.money = users[str(self.id)]["money"]
        self.inventory = users[str(self.id)]["inventory"]
    
    def delete(self):
        with open("users.json", "r") as f:
            users = json.load(f)
        del users[str(self.id)]
        with open("users.json", "w") as f:
            json.dump(users, f, indent = 4)
    
    def add_item(self, item):
        self.inventory.append(item)
        self.save()
    
    def remove_item(self, item):
        self.inventory.remove(item)
        self.save()
    
    def add_money(self, amount):
        self.money += amount
        self.save()
    
    def remove_money(self, amount):
        self.money -= amount
        self.save()
    
    def add_health(self, amount):
        self.health += amount
        self.save()
    
    def remove_health(self, amount):
        self.health -= amount
        self.save()

    def add_energy(self, amount):
        self.energy += amount
        self.save()
    
    def remove_energy(self, amount):
        self.energy -= amount
        self.save()

    def add_mood(self, amount):
        self.mood += amount
        self.save()
    
    def remove_mood(self, amount):
        self.mood -= amount
        self.save()

    def get_health(self):
        return self.health

    def get_energy(self):
        return self.energy
    
    def get_mood(self):
        return self.mood

    def get_money(self):
        return self.money
    
    def get_inventory(self):
        return self.inventory
    
    def get_id(self):
        return self.id
    