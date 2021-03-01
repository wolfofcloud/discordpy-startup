import discord
import os
import traceback

TOKEN = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()
guild = client.get_guild(661027381980561409)

async def create_channel(message, channel_name ,overwrites):
    category = message.guild.get_channel(687069139067600897)
    new_channel = await message.guild.create_text_channel(name=channel_name, overwrites=overwrites, category=category)
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
        overwrites1 = {
            message.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            message.guild.me: discord.PermissionOverwrite(read_messages=True)
            }
        new_channel = await create_channel(message, channel_name=cot, overwrites=overwrites1)
        overwrite = discord.PermissionOverwrite()
        overwrite.read_messages = True
        await new_channel.set_permissions(new_role, overwrite=overwrite)
        text = f'{new_channel.mention} を作成しました'
        await message.channel.send(text)
    if message.content.startswith("/join"):
        cot=message.content
        cot=cot.replace('/join ','')
        member=message.author
        role=discord.utils.get(message.guild.roles, name=cot)
        await member.add_roles(role)
         text = '権限を付与しました'
        await message.channel.end(text)
    

client.run(TOKEN)
