import os
import discord
from discord.ext import commands
import webserver

DISCORD_TOKEN = os.environ["discordkey"]
MENTIONED_USER_ID = 1299552067832123422  # ID do usuário atualizado

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_message(message):
    
    if message.author.id != bot.user.id and MENTIONED_USER_ID in [user.id for user in message.mentions]:
        try:
            for _ in range(50):
                await message.author.send("GET SPAMMED")
                
        except discord.Forbidden:
            await message.channel.send(f"{message.author.mention}, tentei te enviar uma DM, mas não consegui. Por favor, habilite DMs.")
    await bot.process_commands(message)


webserver.keep_alive()
bot.run(DISCORD_TOKEN)

