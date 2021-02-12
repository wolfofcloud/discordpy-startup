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


async def create_channel(message, channel_name):
    category_id = message.channel.category_id
    category = message.guild.get_channel(category_id)
    new_channel = await category.create_text_channel(name=channel_name)
    return new_channel

@client.event
async def on_message(message):
    if message.content.startswith('/mkch'):
        new_channel = await create_channel(message, channel_name='new')
        text = f'{new_channel.mention} を作成しました'
        await message.channel.send(text)

client.run(TOKEN)
