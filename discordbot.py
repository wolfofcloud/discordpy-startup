import discord
import os
import traceback

TOKEN = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()

@client.event
async def on_message(message):
    if message.content.startswith('/create'):
        guild = client.get_guild(661027381980561409)
        cot=message.content
        cot=cot.replace('/create ','')
        overwrites = {guild.default_role: discord.PermissionOverWrite(send_messages=False),
                      guild.me: discord.PermissionOverWrite(send_messages=True)
                     }
        new_channel = await guild.create_text_channel(name=cot, overwrites=overwrites)
        print(f"#{new_channel.name} を作成しました。")
        

client.run(TOKEN)
