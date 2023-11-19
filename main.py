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
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you"))

@bot.slash_command(name="join", description="Join the game")
async def join(ctx):
    if ifexists(ctx.author.id):
        embed = discord.Embed(title="You are already a member of Paraiso", description="You can't join the game twice. However, you can use an alternative Discord account.", color=discord.Color.red())
        await ctx.respond(embed=embed)
    else:
        user = User(ctx.author.id)
        user.save()
        embed = discord.Embed(title="Welcome to Paraiso!", description="You have joined the game. Hope you'll have fun!", color=discord.Color.green())
        await ctx.respond(embed=embed)

@bot.slash_command(name="balance", description="Check your own balance or another user's balance")
async def balance(ctx, user: discord.Member = None):
    uUser = user
    if uUser is None:
        uUser = ctx.author
    
    if ifexists(uUser.id):
        user = User(uUser.id)
        user.load()
        embed = discord.Embed(title=f"{uUser.display_name}'s balance", description=f"{uUser.mention} has {user.money} coins", color=discord.Color.green())
        await ctx.respond(embed=embed)
    else:
        embed = discord.Embed(title="This user is not a member of Paraiso", description="This user is not a member of Paraiso. A user is required to initialize their account by running `/join` before getting a balance.", color=discord.Color.red())
        await ctx.respond(embed=embed)

@bot.slash_command(name="work", description="Work to earn money")
@commands.cooldown(1, 3600, commands.BucketType.user)
async def work(ctx):
    if ifexists(ctx.author.id):
        user = User(ctx.author.id)
        user.load()
        if user.energy > 0:
            amount = random.randint(30, 70)
            conv_happiness = user.mood / 100
            conv_health = user.health / 100
            conv_energy = user.energy / 100
            amount = amount + (amount * conv_happiness) + (amount * conv_health) + (amount * conv_energy)
            amount = round(amount)
            user.add_money(amount)
            energyToRemove = random.randint(7, 17)
            user.remove_energy(energyToRemove)
            user.save()
            embed = discord.Embed(title="Work complete!", description=f"You have earned {amount} coins, you now have {user.money} coins. You also have lost {energyToRemove} energy, having {user.energy} energy left.", color=discord.Color.green())
            await ctx.respond(embed=embed)
        else:
            embed = discord.Embed(title="Chill out!", description="You are too tired to work. Try again later", color=discord.Color.red())
            await ctx.respond(embed=embed)
    else:
        embed = discord.Embed(title="Join Paraiso first!", description="You aren't a member of Paraiso... yet. Please run `/join` to join the game.", color=discord.Color.red())
        await ctx.respond(embed=embed)

@work.error
async def work_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(title="Easy there!", description=f"You are on cooldown, try again later. Note that you can only work once per hour. Please wait for the cooldown ({round(error.retry_after)} seconds)", color=discord.Color.red())
        await ctx.respond(embed=embed)

@bot.slash_command(name="help", description="To help users with learning new commands")
async def Help(ctx):
    embed = discord.Embed(title="Help", description="Here are all commands of the bot: \n\n 1. `/balance` - Check your own balance or another user's balance \n\n 2. `/help` - This! \n\n 3. `/join` - Join the game \n\n 4. `/work` - Work to earn money", color=discord.Color.purple())
    await ctx.respond(embed=embed)

@bot.slash_command(name="buy", description="Buy something you need") 
async def Buy(ctx, item: Option(str, "What do you want to buy? ", autocomplete=discord.utils.basic_autocomplete(get_shop_items))):
    if not ifexists(ctx.author.id):
        embed = discord.Embed(title="Join Paraiso first!", description="You aren't a member of Paraiso... yet. Please run `/join` to join the game.", color=discord.Color.red())
        return
    if item in shop:
        user = User(ctx.author.id)
        user.load()
        if user.money >= shop[item]:
            user.remove_money(shop[item])
            user.add_item(item)
            user.save()
            embed = discord.Embed(title="Purchase Successful", description=f"You have bought {item} for {shop[item]} coins. You now have {user.money} coins", color=discord.Color.green())
            await ctx.respond(embed=embed)
        else:
            embed = discord.Embed(title="Insufficient Funds", description=f"You do not have enough coins to buy {item}. You have {user.money} coins", color=discord.Color.red())
            await ctx.respond(embed=embed)
    else:
        embed = discord.Embed(title="Invalid Item", description=f"{item} is not available in the shop.", color=discord.Color.red())
        await ctx.respond(embed=embed)

@bot.slash_command(name="inventory", description="Check your inventory")
async def Inventory(ctx, user: discord.Member = None):
    uUser = user
    if uUser is None:
        uUser = ctx.author
    if not ifexists(uUser.id):
        await ctx.respond("You are not a member of Paraiso. Please run `/join` to join the game.")
        return
    user = User(uUser.id)
    user.load()
    if len(user.inventory) == 0:
        embed = discord.Embed(title="Nothing inside...", description=f"The inventory of {uUser.mention}", color=discord.Color.yellow())
        await ctx.respond(embed=embed)
    else:
        embed = discord.Embed(title=f"Inventory of {uUser.name}", description="", color=discord.Color.green())
        scanned_already = []
        for item in user.inventory:
            if item in scanned_already:
                continue
            embed.description += f"**{item}** x{user.inventory.count(item)}\n"
            scanned_already.append(item)
        await ctx.respond(embed=embed)

token = os.getenv("DISCORD_TOKEN")
bot.run(token)
