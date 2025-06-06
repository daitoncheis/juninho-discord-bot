import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True  
bot = commands.Bot(command_prefix=".", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot conectado com sucesso como :{bot.user}')

@bot.command(name='oi') #!hello 
async def oi(ctx):
    await ctx.send('Olá! Muito prazer, me chamo Juninho da pika laranja.')

@bot.command(name='ping')
async def ping(ctx):
    latency = round(bot.latency * 1000)  # Latência em milissegundos
    await ctx.send(f'Pong! Latência: {latency}ms')

@bot.command(name='comandos')
async def teste(ctx):
    await ctx.send('Lista de comandos!')
bot.run(TOKEN)
