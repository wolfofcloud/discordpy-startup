import discord
import os

TOKEN = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()

@client.event
async def on_ready():
    print('ログインしました')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == '/neko':
        await message.channel.send('にゃーん')

client.run(TOKEN)
