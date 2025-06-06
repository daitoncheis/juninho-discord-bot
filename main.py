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

@bot.command(name='ola', aliases=["oi", "Oi", "OI", "oii", "Oii", "OII", "oiii", "Oiii", "OIII", "Olá", "OLÁ", "olá",
                                  "Olá!", "olá!", "Ola", "OLA", "olarr", "Olarr", "OLARR", "eae", "Eae", "EAE", "e aí", 
                                  "E aí", "E AÍ", "e ai", "E ai", "E AI", "opa", "Opa", "OPA", "fala", "Fala", "FALA",
                                  "alô", "Alô", "ALÔ", "alo", "Alo", "ALO", "salve", "Salve", "SALVE", "hello", "Hello", 
                                   "HELLO", "hellos", "Hellos", "HELLOS", "hallo", "Hallo", "HALLO",])  # Comando .ola, .oi ou .olá
async def ola(ctx):
    await ctx.send('Olá! Muito prazer, me chamo Juninho da pika laranja.')

@bot.command(name='ping')
async def ping(ctx):
    latency = round(bot.latency * 1000)  # Latência em milissegundos
    await ctx.send(f'Pong! Latência: {latency}ms')
    
@bot.command(name="eco", help="Repete o que você diz.")
async def echo(ctx, *, message: str):
    await ctx.send(message)

@bot.command(name='help', aliases=['ajuda', 'comandos'])
async def teste(ctx):
    await ctx.send('Lista de comandos!')
bot.run(TOKEN)
