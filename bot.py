import discord
from discord.ext import commands
import os
import asyncio
import random
from datetime import datetime, time, timedelta
import pytz
from dotenv import load_dotenv

print("1. Iniciando carregamento do .env...")
load_dotenv()
print("2. .env carregado.")

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
IA_API_KEY = os.getenv('IA_API_KEY')

print(f"3. Discord Token obtido: {'SIM' if DISCORD_TOKEN else 'NÃO'}")
print(f"4. IA API Key obtida: {'SIM' if IA_API_KEY else 'NÃO'}")

# --- Escolha da API de IA ---
USE_GEMINI = False # Mude para False para usar OpenAI

if USE_GEMINI:
    if not IA_API_KEY:
        print("Erro FATAL: A chave de API do Gemini (IA_API_KEY) não foi encontrada ou está vazia.")
        exit()
    import google.generativeai as genai
    genai.configure(api_key=IA_API_KEY)
    model = genai.GenerativeModel('gemini-pro')
    print("5. Usando Google Gemini Pro como modelo de IA.")
else:
    if not IA_API_KEY:
        print("Erro FATAL: A chave de API da OpenAI (IA_API_KEY) não foi encontrada ou está vazia.")
        exit()
    import openai
    openai.api_key = IA_API_KEY
    print("5. Usando OpenAI como modelo de IA.")

# --- Configuração do Bot Discord ---
print("6. Configurando intents do Discord...")
intents = discord.Intents.default()
intents.message_content = True
intents.members = True # Manter este aqui também
print("7. Intents configuradas. Inicializando cliente Discord...")
client = discord.Client(intents=intents)
print("8. Cliente Discord inicializado.")

# ... (o restante do seu código)

@client.event
async def on_ready():
    print(f'{client.user} está online! (Mensagem do on_ready)')
    # Esta forma pode remover o aviso visual no editor,
    # mas o resultado é o mesmo na prática para este caso.
    

# ... (o restante do seu código)

if DISCORD_TOKEN:
    print("9. Tentando rodar o bot com o token fornecido...")
    try:
        client.run(DISCORD_TOKEN)
    except discord.LoginFailure:
        print("Erro GRAVE: O token do Discord é inválido. Por favor, verifique seu DISCORD_BOT_TOKEN no arquivo .env e no Discord Developer Portal.")
    except Exception as e:
        print(f"Um erro inesperado ocorreu ao tentar rodar o bot: {e}")
else:
    print("Erro FATAL: O TOKEN DO DISCORD não foi encontrado. Por favor, defina-o nas variáveis de ambiente no seu .env.")

print("Fim do script principal (se chegou aqui, algo pode ter travado ou finalizado sem erro explícito).")