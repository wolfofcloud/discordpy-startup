import discord
import os
import traceback

TOKEN = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()

@client.event
async def on_message(message):
    if message.content.startswith('/create'):
        # discord.Guild.create_text_channelを使用する
        guild = client.get_guild(GUILD_ID)
        # @everyoneは発言できないが、自分はできる
        overwrites = {guild.default_role: discord.PermissionOverWrite(send_messages=False),
                      guild.me: discord.PermissionOverWrite(send_messages=True)
                     }
        new_channel = await guild.create_text_channel(name="お知らせ", overwrites=overwrites, topic="お知らせを表示します。")
        print(f"#{new_channel.name} を作成しました。")
        

client.run(TOKEN)
