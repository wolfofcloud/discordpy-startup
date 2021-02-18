import discord
import os
import traceback

TOKEN = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()
# get_guild



async def create_channel(message, channel_name,overwrites):
    guild1 = message.guild
    guild2 = client.get_guild(661027381980561409)
    category_id = 687069139067600897
    category = message.guild1.get_channel(category_id)
    new_channel = await guild2.create_text_channel(name=channel_name,overwrites=overwrites,category=category)
    return new_channel

@client.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@client.event
async def on_ready():
    print('ログインしました')

        
@client.event
async def on_message(message):
    if message.content.startswith('/create'):
        cot=message.content
        cot=cot.replace('/create ','')
        guild1 = message.guild
        new_role = await guild1.create_role(name=cot)
        guild2 = client.get_guild(661027381980561409)
        overwrites = {
            guild2.default_role: discord.PermissionOverwrite(read_messages=False),
            guild2.me: discord.PermissionOverwrite(read_messages=True)
        }
        
        # チャンネルを作成する非同期関数を実行して Channel オブジェクトを取得
        new_channel = await create_channel(message, channel_name=cot,overwrites=overwrites)
        # チャンネルのリンクと作成メッセージを送信
        text = f'{new_channel.mention} を作成しました'
        await message.channel.send(text)
        

client.run(TOKEN)
