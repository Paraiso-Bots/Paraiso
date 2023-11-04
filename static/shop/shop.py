import discord

shop = {
    "apple": 3,
    "banana": 7,
    "tomato": 5,
    "potato": 6,
    "mystery box": 25,
    "gift box": 50,
}

async def get_shop_items(ctx: discord.AutocompleteContext):
    return shop.keys()