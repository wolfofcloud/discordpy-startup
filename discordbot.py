import discord
import os
import traceback

TOKEN = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()
# get_guild



async def create_channel(message, channel_name,):
    guild1 = message.guild
    category_id = 687069139067600897
    category = message.guild1.get_channel(category_id)
    new_channel = await create_text_channel(name=channel_name,category=category)
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
        new_channel = await create_channel(message, channel_name=cot)
        text = f'{new_channel.mention} を作成しました'
        await message.channel.send(text)
        

client.run(TOKEN)
