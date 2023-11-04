import discord

shop = {
    "apple": 3,
    "banana": 7,
    "cheese": 10,
    "tomato": 5,
    "meat": 12,
    "flour": 15,
    "sugar": 12,
    "milk": 10,
    "egg": 6,
    "potato": 7,
    "butter": 14,
    "cola": 14
    
    
}

async def get_shop_items(ctx: discord.AutocompleteContext):
    return shop.keys()