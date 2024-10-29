import os
import discord
import asyncio
from discord.ext import commands
import webserver

DISCORD_TOKEN = os.environ["discordkey"]
MENTIONED_USER_ID = 253893397037842432  # ID do usuário atualizado

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_message(message):
    # Verifica se o autor da mensagem não é o bot e se o usuário mencionado é o ID desejado
    if message.author.id != bot.user.id and MENTIONED_USER_ID in [user.id for user in message.mentions]:
        try:
            for _ in range(58):
                await message.author.send("GET SPAMMED")
                await asyncio.sleep(1)  # Adiciona um atraso de 1 segundo entre as mensagens
        except discord.Forbidden:
            await message.channel.send(f"{message.author.mention}, tentei te enviar uma DM, mas não consegui. Por favor, habilite DMs.")

# Inicia o bot
bot.run(DISCORD_TOKEN)

webserver.keep_alive()