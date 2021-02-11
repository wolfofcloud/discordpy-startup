  
from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.event
async def create_channel(message, channel_name):
    category = message.guild.708239634051760179
    new_channel = await category.create_text_channel(name=channel_name)
    return new_channel

# 発言時に実行されるイベントハンドラを定義
@bot.command()
async def on_message(message):
    if message.content.startswith('/mkch'):
        new_channel = await create_channel(message, channel_name='new')
        text = f'{new_channel.mention} を作成しました'
        await message.channel.send(text)


bot.run(token)
