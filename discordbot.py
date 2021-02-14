import discord
import os

TOKEN = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()

# 発言したチャンネルのカテゴリ内にチャンネルを作成する非同期関数
async def create_channel(message, channel_name,overwrites):
    category_id = 708239634051760179
    guild = client.get_guild(GUIILD_ID)
    category = message.guild.get_channel(category_id)
    new_channel = await guild.category.create_text_channel(name=channel_name,overwrites=overwrites)
    return new_channel

@client.event
async def on_ready():
    print('ログインしました')

        
@client.event
async def on_message(message):
    if message.content.startswith('/create'):
        cot=message.content
        cot=cot.replace('/create ','')
        guild = message.guild
        new_role = await guild.create_role(name=cot)
        guild = client.get_guild(GUIILD_ID)
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            gulid.new_role:discord.PermissionOverwrite(read_messages=False),
            guild.me: discord.PermissionOverwrite(read_messages=True)
        }
        
        # チャンネルを作成する非同期関数を実行して Channel オブジェクトを取得
        new_channel = await create_channel(message, channel_name=cot,overwrites=overwrites)
        # チャンネルのリンクと作成メッセージを送信
        text = f'{new_channel.mention} を作成しました'
        await message.channel.send(text)
        

client.run(TOKEN)
