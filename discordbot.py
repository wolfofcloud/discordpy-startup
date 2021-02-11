import os
import discord
import traceback

token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()


client.run(token)
