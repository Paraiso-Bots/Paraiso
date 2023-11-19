import discord

shop = {
    "Apple": {"price": 3, "type": "food", "health": 10, "energy": 5, "mood": 5},
    "Banana": {"price": 7, "type": "food", "health": 15, "energy": 10, "mood": 5},
    "Cheese": {"price": 10, "type": "food", "health": 20, "energy": 15, "mood": 10},
    "Tomato": {"price": 5, "type": "food", "health": 10, "energy": 5, "mood": 5},
    "Meat": {"price": 12, "type": "food", "health": 25, "energy": 20, "mood": 15},
    "Flour": {"price": 15, "type": "food", "health": 5, "energy": 5, "mood": 5},
    "Sugar": {"price": 12, "type": "food", "health": 5, "energy": 10, "mood": 5},
    "Milk": {"price": 10, "type": "food", "health": 10, "energy": 10, "mood": 5},
    "Egg": {"price": 6, "type": "food", "health": 10, "energy": 5, "mood": 10},
    "Potato": {"price": 7, "type": "food", "health": 15, "energy": 10, "mood": 5},
    "Butter": {"price": 14, "type": "food", "health": 10, "energy": 10, "mood": 10},
    "Cola": {"price": 14, "type": "food", "health": 5, "energy": 20, "mood": 10},
    "House": {"price": 500, "type": "passive"},
    "Car": {"price": 300, "type": "passive"},
    "Diamond":{"price": 1000, "type": "collectable"}
}

async def get_shop_items(ctx: discord.AutocompleteContext):
    return shop.keys()