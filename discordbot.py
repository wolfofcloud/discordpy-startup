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
async def test(ctx,arg):
    await ctx.send(arg)
    
@bot.event
async def create_channel(channel_neme):
    category = '708239634051760179'
    new_channel = await category.create_text_channl(name=channel_name)
    return new_channel

@bot.command()
async def create(ctx,arg):
    new_channnel = await create_channel(channel_name=arg)
    
bot.run(token)
