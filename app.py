import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
intents.messages = True
intents.members = True

bot = commands.Bot(command_prefix="!",intents=intents)

@bot.command()
async def info(ctx):
    await ctx.send("hola mundo")

@bot.command()
async def play(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()

@bot.event 
async def on_message(message):
    if message.author == bot.user:
        return
    
    if 'hola' in message.content.lower():
        await message.channel.send("hola bro")
    
    await bot.process_commands(message)

bot.run(token)