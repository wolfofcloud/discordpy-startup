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
    
@bot.command()
async def create(ctx,arg):
    category = '708239634051760179'
    new_channel = await categoty.create_text_channl(name=arg)
    return new_channel
    
bot.run(token)
