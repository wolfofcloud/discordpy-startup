import os
import discord
import traceback

token = os.environ['DISCORD_BOT_TOKEN']

@client.event
async def on_massege(messege):
  if messege.content=="/neko":
    await messege.channel.send("ねこ

client.run(token)
