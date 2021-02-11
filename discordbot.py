import os
import discord
import traceback

token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()

@client.event
async def on_ready():
  print('ログインしました')
  
@client.event
async def on_message(message):
  if message.content == '/neko':
    await messege.channel.send('猫')

client.run(token)
