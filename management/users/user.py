import json
import os
from .constants import Constants

constants = Constants()

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
        if self.inventory.count(item) > constants.max_item_amount:
            # Remove all items that are over the limit
            for i in range(self.inventory.count(item) - constants.max_item_amount):
                self.inventory.remove(item)
        self.save()
    
    def remove_item(self, item):
        self.inventory.remove(item)
        self.save()
    
    def add_money(self, amount):
        self.money += amount
        if self.money > constants.max_money:
            self.money = constants.max_money
        self.save()
    
    def remove_money(self, amount):
        self.money -= amount
        self.save()
    
    def add_health(self, amount):
        self.health += int(amount)
        if self.health > constants.max_health:
            self.health = constants.max_health
        self.save()
    
    def remove_health(self, amount):
        self.health -= int(amount)
        if self.health < constants.min_health:
            self.health = constants.min_health
        self.save()

    def add_energy(self, amount):
        self.energy += int(amount)
        if self.energy > constants.max_energy:
            self.energy = constants.max_energy
        self.save()
    
    def remove_energy(self, amount):
        self.energy -= int(amount)
        if self.energy < constants.min_energy:
            self.energy = constants.min_energy
        self.save()

    def add_mood(self, amount):
        self.mood += int(amount)
        if self.mood > constants.max_mood:
            self.mood = constants.max_mood
        self.save()
    
    def remove_mood(self, amount):
        self.mood -= int(amount)
        if self.mood < constants.min_mood:
            self.mood = constants.min_mood
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
    