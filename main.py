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
from management.users.constants import Constants

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
        embed = discord.Embed(title="Welcome to Paraiso!", description="You have joined the game. Hope you'll have fun!", color= discord.Color.random())
        await ctx.respond(embed=embed)

@bot.slash_command(name="balance", description="Check your own balance or another user's balance")
async def balance(ctx, user: discord.Member = None):
    uUser = user
    if uUser is None:
        uUser = ctx.author
    
    if ifexists(uUser.id):
        user = User(uUser.id)
        user.load()
        embed = discord.Embed(title=f"{uUser.display_name}'s balance", description=f"{uUser.mention} has {user.money} coins", color= discord.Color.random())
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
            HGWTDAW = random.randint(1, 100)
            if HGWTDAW < 50:
                # Make the user sadder
                user.remove_mood(round(50 - HGWTDAW) / 2)
            else:
                # Make the user happier
                user.add_mood(round(100 - HGWTDAW) / 2)
            energyToRemove = random.randint(7, 17)
            user.remove_energy(energyToRemove)
            user.save()
            embed = discord.Embed(title="Work complete!", description=f"You have earned {amount} coins, you now have {user.money} coins. You also have lost {energyToRemove} energy, having {user.energy} energy left.", color= discord.Color.random())
            if HGWTDAW < 50:
                embed.description += f"\n\nYour day at work was not so good. You have lost {round(50 - HGWTDAW) / 2} mood points."
            else:
                embed.description += f"\n\nYour day at work was good. You have gained {round(100 - HGWTDAW) / 2} mood points."
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
    embed = discord.Embed(title="Help", description="", color=discord.Color.random())
    embed.description += "**/join** - Join Paraiso and start your journey!\n"
    embed.description += "**/balance** - Check the balance of any user who is a member of Paraiso\n"
    embed.description += "**/work** - Work to earn money. Note that you can only work once per hour, and your energy, mood, and health will affect the amount of money you earn\n"
    embed.description += "**/buy** - Use your money to buy something from the shop\n"
    embed.description += "**/inventory** - Check your inventory, or another user's inventory\n"
    embed.description += "**/stats** - Check your well-being and make sure you're healthy!\n"
    embed.description += "**/sleep** - Sleep to regain energy. Note that you can only sleep once per hour\n"
    embed.description += "**/eat** - Eat food to increase your stats\n"
    await ctx.respond(embed=embed)

@bot.slash_command(name="buy", description="Buy something you need") 
async def Buy(ctx, item: Option(str, "What do you want to buy? ", autocomplete=discord.utils.basic_autocomplete(get_shop_items))):
    if not ifexists(ctx.author.id):
        embed = discord.Embed(title="Join Paraiso first!", description="You aren't a member of Paraiso... yet. Please run `/join` to join the game.", color=discord.Color.red())
        await ctx.respond(embed=embed)
        return
    if item in shop:
        user = User(ctx.author.id)
        user.load()
        if user.money >= shop[item]['price']:
            user.remove_money(shop[item]["price"])

            user.add_item(item)
            user.save()
            embed = discord.Embed(title="Purchase Successful", description=f"You have bought {item} for {shop[item]['price']} coins. You now have {user.money} coins", color= discord.Color.random())
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
        embed = discord.Embed(title="This user is not a member of Paraiso", description="This user is not a member of Paraiso. A user is required to initialize their account by running `/join` before getting a balance.", color=discord.Color.red())
        await ctx.respond(embed=embed)
        return
    user = User(uUser.id)
    user.load()
    if len(user.inventory) == 0:
        embed = discord.Embed(title="Nothing inside...", description=f"The inventory of {uUser.mention}", color=discord.Color.yellow())
        await ctx.respond(embed=embed)
    else:
        embed = discord.Embed(title=f"Inventory of {uUser.name}", description="", color= discord.Color.random())
        scanned_already = []
        for item in user.inventory:
            if item in scanned_already:
                continue
            embed.description += f"**{item}** x{user.inventory.count(item)}\n"
            scanned_already.append(item)
        await ctx.respond(embed=embed)

@bot.slash_command(name="stats", description="Check your stats, or another user's stats")
async def Stats(ctx, user: discord.Member = None):
    uUser = user
    if uUser is None:
        uUser = ctx.author
    if not ifexists(uUser.id):
        embed = discord.Embed(title="This user is not a member of Paraiso", description="This user is not a member of Paraiso. A user is required to initialize their account by running `/join` before getting a balance.", color=discord.Color.red())
        await ctx.respond(embed=embed)
        return
    user = User(uUser.id)
    user.load()
    embed = discord.Embed(title=f"Stats of {uUser.name}", description=f"**♥️ Health:** {user.health} / {Constants().max_health}\n**⚡ Energy:** {user.energy} / {Constants().max_energy}\n**😀 Mood:** {user.mood} / {Constants().max_mood}\n**💰 Money:** {user.money}")
    # Find the average of all stats. If it's low, add a red square to the title and a red color to the embed.
    average = (user.health + user.energy + user.mood) / 3
    if average < 25:
        embed.title += " 🔴"
        embed.color = discord.Color.red()
    elif average < 50:
        embed.title += " 🟠"
        embed.color = discord.Color.orange()
    elif average < 75:
        embed.title += " 🟡"
        embed.color = discord.Color.gold()
    else:
        embed.title += " 🟢"
        embed.color = discord.Color.green()
    # Add an overall description field to the embed.
    embed.description += f"\n\n**Overall Well-Being: {round(average)}%**"
    await ctx.respond(embed=embed)


@bot.slash_command(name="sleep", description="Sleep to regain energy")
@commands.cooldown(1, 3600, commands.BucketType.user)
async def Sleep(ctx):
    if not ifexists(ctx.author.id):
        embed = discord.Embed(title="Join Paraiso first!", description="You aren't a member of Paraiso... yet. Please run `/join` to join the game.", color=discord.Color.red())
        await ctx.respond(embed=embed)
        return
    user = User(ctx.author.id)
    user.load()
    if user.energy == Constants().max_energy:
        embed = discord.Embed(title="You are already fully rested!", description="You are already fully rested. You don't need to sleep.", color=discord.Color.red())
        await ctx.respond(embed=embed)
        return
    random_energy = random.randint(20, 70)
    if random_energy < 30:
        status = "Unfortunately, you didn't sleep well."
    elif random_energy < 50:
        status = "You slept well enough."
    elif random_energy < 70:
        status = "The dream was so satisfactory you didn't want to wake up, and managed to rest well."
    user.add_energy(random_energy)
    user.save()
    embed = discord.Embed(title="Wake up!", description="You have woken up from your sleep. " + status + f" You have gained {random_energy} energy, and now have {user.energy} energy.", color= discord.Color.random())
    await ctx.respond(embed=embed)

@Sleep.error
async def Sleep_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(title="You are already fully rested!", description=f"You are on cooldown, try again later. Note that you can only sleep once per hour. Please wait for the cooldown ({round(error.retry_after)} seconds)", color=discord.Color.red())
        await ctx.respond(embed=embed)
@bot.slash_command(name = "eat", description = "Eat the food to increase the stats.")
async def eat(ctx, food: Option(str, "What do you want to eat?", autocomplete=discord.utils.basic_autocomplete(get_shop_items))):
    if not ifexists(ctx.author.id):
        embed = discord.Embed(title="Join Paraiso first!", description="You aren't a member of Paraiso... yet. Please run `/join` to join the game.", color=discord.Color.red())
        await ctx.respond(embed=embed)
        return
    if food in shop:
        user = User(ctx.author.id)
        user.load()
        if food in user.inventory:
            if shop[food]["type"] == "food":
                user.remove_item(food)
                random_health_from_food = random.randint(shop[food]["health"] - 5, shop[food]["health"] + 5)
                random_energy_from_food = random.randint(shop[food]["energy"] - 5, shop[food]["energy"] + 5)
                random_mood_from_food = random.randint(shop[food]["mood"] - 5, shop[food]["mood"] + 5)
                user.add_health(random_health_from_food)
                user.add_energy(random_energy_from_food)
                user.add_mood(random_mood_from_food)
                user.save()
                embed = discord.Embed(title="Eat Successful", description=f"You have eaten {food}. You have gained {random_health_from_food} health, {random_energy_from_food} energy, and {random_mood_from_food} mood. In total, you have {user.health} health, {user.energy} energy, and {user.mood} mood. Hope you enjoyed your meal", color= discord.Color.random())
                await ctx.respond(embed=embed)
            else:
                embed = discord.Embed(title="Invalid Item", description=f"{food} is not food.", color=discord.Color.red())
                await ctx.respond(embed=embed)
        else:
            embed = discord.Embed(title="Invalid Item", description=f"You do not have {food}.", color=discord.Color.red())
            await ctx.respond(embed=embed)
    else:
        embed = discord.Embed(title="Invalid Item", description=f"{food} is not available in the shop.", color=discord.Color.red())
        await ctx.respond(embed=embed)

@bot.slash_command(name="sell", description="Sell something you don't need")
async def Sell(ctx, item: Option(str, "What do you want to sell?", autocomplete=discord.utils.basic_autocomplete(get_shop_items))):
    if not ifexists(ctx.author.id):
        embed = discord.Embed(title="Join Paraiso first!", description="You aren't a member of Paraiso... yet. Please run `/join` to join the game.", color=discord.Color.red())
        await ctx.respond(embed=embed)
        return
    if item in shop:
        user = User(ctx.author.id)
        user.load()
        if item in user.inventory:
            user.remove_item(item)
            # Sold for the price + random between -50% and +50% of the price
            price = shop[item]["price"] + random.randint(-shop[item]["price"] / 2, shop[item]["price"] / 2)
            user.add_money(price)
            user.save()
            embed = discord.Embed(title="Sell Successful", description=f"You have sold {item} for {price} coins. You now have {user.money} coins", color= discord.Color.random())
            await ctx.respond(embed=embed)
        else:
            embed = discord.Embed(title="Invalid Item", description=f"You do not have {item}.", color=discord.Color.red())
            await ctx.respond(embed=embed)
    else:
        embed = discord.Embed(title="Invalid Item", description=f"{item} is not available in the shop.", color=discord.Color.red())
        await ctx.respond(embed=embed)
    
leaderboard_com = bot.create_group(name="leaderboard", description="Check the leaderboard")

@leaderboard_com.command(name="server", description="Check the leaderboard among all members of the server that are members of Paraiso")
async def leaderboard_server(ctx):
    with open("users.json", "r") as f:
        users = json.load(f)
        ids_int = []
        for id in users.keys():
            ids_int.append(int(id))
        
        sort = {}
        for id in ids_int:
            user = User(id)
            user.load()
            sort[user.id] = user.money
        
        # remove members that are not in the server
        members = ctx.guild.members
        for id in sort.keys():
            if id not in [member.id for member in members]:
                del sort[id]
            
        sort = dict(sorted(sort.items(), key=lambda item: item[1], reverse=True))
        embed = discord.Embed(title="Top 10 Paraiso Members in this Server", description="", color=discord.Color.random())
        i = 1
        # Top 10
        for id in sort.keys():
            if i > 10:
                break
            user = User(id)
            user.load()
            embed.description += f"**{i}.** {bot.get_user(user.id).mention} - {sort[id]} coins\n"
            i += 1
        
        await ctx.respond(embed=embed)

@leaderboard_com.command(name="global", description="Check the leaderboard among all members of Paraiso")
async def leaderboard_global(ctx):
    with open("users.json", "r") as f:
        users = json.load(f)
        ids_int = []
        for id in users.keys():
            ids_int.append(int(id))
        
        sort = {}
        for id in ids_int:
            user = User(id)
            user.load()
            sort[user.id] = user.money
        
        sort = dict(sorted(sort.items(), key=lambda item: item[1], reverse=True))
        embed = discord.Embed(title="Top 10 Paraiso Members", description="", color=discord.Color.random())
        i = 1
        # Top 10
        for id in sort.keys():
            if i > 10:
                break
            user = User(id)
            user.load()
            embed.description += f"**{i}.** {bot.get_user(user.id).name} - {sort[id]} coins\n"
            i += 1
        
        await ctx.respond(embed=embed)



        

token = os.getenv("DISCORD_TOKEN")
bot.run(token)
