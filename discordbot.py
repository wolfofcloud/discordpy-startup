from discord.ext import commands
import os
import traceback


bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

async def create_channel(massage,channel_name):
    category_id=708239634051760179
    new_channel=awate category.create_text_channel(neme=channel_name)
    return new_channnel
    

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
@client.event
async def on_message(message):
    if messege.content.startswich('/create'):
        new_channel=await create_channel(massege,channel_name='new')
       


bot.run(token)
