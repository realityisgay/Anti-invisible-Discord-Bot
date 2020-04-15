import discord
from discord.ext import commands
from discord.utils import find
from discord.utils import get
client = commands.Bot(command_prefix = 'UR CUSTOM PREFIX')



@client.event
async def on_member_update(before, after):

    if str(before.status) == "offline" or str(before.status) == "idle":
        if str(after.status) == "online" or str(after.status) == "dnd":
            role = get(after.guild.roles, id=ADD ROLE ID HERE)
            print("{} has gone {}.".format(after.name,after.status))
            await after.add_roles(role)

    elif str(before.status) == "dnd" or str(before.status) == "online":
        if str(after.status) == "offline" or str(after.status) == "idle":
            role = get(after.guild.roles, id=ADD ROLE ID HERE)
            print("{} has gone {}.".format(after.name,after.status))
            await after.remove_roles(role)


@client.command()
async def role_check(ctx):
    for i in ctx.guild.members:
        if i.bot == False:
            if str(i.status) == 'idle' or str(i.status) == 'offline':
                role = get(ctx.guild.roles, id=ADD ROLE ID HERE)
                await i.remove_roles(role)
            elif str(i.status) == 'dnd' or str(i.status) == 'online':
                role = get(ctx.guild.roles, id=ADD ROLE ID HERE)
                await i.add_roles(role)

client.run('BOTS TOKEN HERE')
