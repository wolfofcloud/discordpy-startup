import discord
import os

TOKEN = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()
# get_guild
guild2 = messege.guild.get_guild(661027381980561409)

# 発言したチャンネルのカテゴリ内にチャンネルを作成する非同期関数
async def create_channel(message, channel_name,overwrites):
    category_id = 687069139067600897
    category = message.guild.get_channel(category_id)
    new_channel = await guild2.category.create_text_channel(name=channel_name,overwrites=overwrites)
    return new_channel

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
