import discord
import os

TOKEN = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()

# 発言したチャンネルのカテゴリ内にチャンネルを作成する非同期関数
async def create_channel(message, channel_name):
    category_id = 708239634051760179
    category = message.guild.get_channel(category_id)
    new_channel = await category.create_text_channel(name=channel_name)
    return new_channel

@client.event
async def on_ready():
    print('ログインしました')

        
@client.event
async def on_message(message):
    if message.content.startswith('/create'):
        cot=message.content
        cot=cot.replace('/create ','')
        # チャンネルを作成する非同期関数を実行して Channel オブジェクトを取得
        new_channel = await create_channel(message, channel_name=cot)
        # チャンネルのリンクと作成メッセージを送信
        text = f'{new_channel.mention} を作成しました'
        await message.channel.send(text)
        

client.run(TOKEN)
