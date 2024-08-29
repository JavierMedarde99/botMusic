from urllib import request
import discord
from discord.ext import commands
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import os

load_dotenv()

token = os.getenv('DISCORD_TOKEN')
client_spotify = os.getenv('SPOTIFY_CLIENT')
secret_spotify = os.getenv('SPOTIFY_SECRET')

intents = discord.Intents.all()
intents.messages = True
intents.members = True

bot = commands.Bot(command_prefix="!",intents=intents)

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_spotify, client_secret=secret_spotify))

@bot.command()
async def info(ctx):
    await ctx.send("hola mundo")

@bot.command()
async def test(ctx):
    track = sp.playlist('37i9dQZF1DX1HCSfq0nSal')
    print(track["tracks"]["items"][0]["track"]["external_urls"]["spotify"])

@bot.command()
async def play(ctx):
    channel = ctx.message.author.voice.channel
    connect = await channel.connect()
    url = "spotify:track:0zpIdU4Q65JlzyueQQnx7Q"
    audio = discord.FFmpegPCMAudio(url,executable="ffmpeg")
    await connect.play(audio)

@bot.event 
async def on_message(message):
    if message.author == bot.user:
        return
    
    if 'hola' in message.content.lower():
        await message.channel.send("hola bro")
    
    await bot.process_commands(message)

bot.run(token)