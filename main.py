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


   







token = os.getenv("DISCORD_TOKEN")
bot.run(token)