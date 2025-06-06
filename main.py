import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} está online!")