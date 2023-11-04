import discord
from discord.ext import commands
from discord.commands import Option
import discord.ui
import os
import random
import asyncio
import json
from dotenv import load_dotenv


from management.users.user import User
from management.users.ifexists import ifexists

from static.shop.shop import shop, get_shop_items


load_dotenv()

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

bot.remove_command("help")

@bot.event
async def on_ready():
    print("Bot is ready")
    print("Logged in as: " + bot.user.name + "\n")
    # Status of the bot must be set to "Watching users"
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you"))


@bot.slash_command(name="join", description="Join the game")
async def join(ctx):
    if ifexists(ctx.author.id):
        await ctx.respond("You are already in the game")
    else:
        user = User(ctx.author.id)
        user.save()
        await ctx.respond("You have joined the game")

@bot.slash_command(name = "balance", descriprion = "Check your own balance or another user's balance")
async def balance(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author
    
    if ifexists(user.id):
        user = User(user.id)
        user.load()
        await ctx.respond(f"{user.money} coins")
    else:
        await ctx.respond("This user is not in the game")

@bot.slash_command(name="work", description="Work to earn money")
@commands.cooldown(1, 3600, commands.BucketType.user)
async def work(ctx):
    if ifexists(ctx.author.id):
        user = User(ctx.author.id)
        user.load()
        if user.energy > 0:
            amount = random.randint(30, 70)
            # Modifiers
            conv_happiness = user.mood / 100
            conv_health = user.health / 100
            conv_energy = user.energy / 100
            amount = amount + (amount * conv_happiness) + (amount * conv_health) + (amount * conv_energy)
            amount = round(amount)
            user.add_money(amount)
            energyToRemove = random.randint(7, 17)
            user.remove_energy(energyToRemove)
            user.save()
            await ctx.respond(f"You have earned {amount} coins, you now have {user.money} coins. You also have lost {energyToRemove} energy, you now have {user.energy} energy.")
        else:
            await ctx.respond("You are too tired to work")
    else:
        await ctx.respond("You are not in the game")

@work.error
async def work_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.respond(f"You are on cooldown, try again in {round(error.retry_after)} seconds. Note that you can only work once per hour")


   

@bot.slash_command(name="help", descriptiom="to help users with learning new commands")
async def Help(ctx):
    await ctx.respond("Here are all commands of the bot: \n\n 1)/balance \n\n 2)/help \n\n 3)/join \n\n 4)work")

@bot.slash_command(name = "buy", description = "Buy something you need") 
async def Buy(ctx, item: Option(str, "What do you want to buy? ", autocomplete=discord.utils.basic_autocomplete(get_shop_items))):
    if item in shop:
        user = User(ctx.author.id)
        user.load()
        if user.money >= shop[item]:
            user.remove_money(shop[item])
            user.add_item(item)
            user.save()
            await ctx.respond(f"You have bought {item} for {shop[item]} coins. You now have {user.money} coins")


token = os.getenv("DISCORD_TOKEN")
bot.run(token)