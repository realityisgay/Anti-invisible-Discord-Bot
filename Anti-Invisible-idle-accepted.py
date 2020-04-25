import discord
from discord.ext import commands
from discord.utils import find
from discord.utils import get
client = commands.Bot(command_prefix = 'YOUR_CUSTOM_PREFIX')
from webserver import keep_alive
import asyncio
import os

roleid = YOUR_ROLE_ID
bottoken = 'YOUR_BOT_TOKEN'

@client.event
async def on_ready():
  print("Anti-Invisible bot is ONLINE!")

@client.event
async def on_member_update(before, after):

  if before.bot == False:
    if str(before.status) == "offline":
      if after.bot == False:
        if str(after.status) == "online" or str(after.status) == "dnd" or str(before.status) == "idle":
            role = get(after.guild.roles, id=(roleid))
            print("{} has gone {}.".format(after.name,after.status))
            await after.add_roles(role)

    elif before.bot == False:
      if str(before.status) == "dnd" or str(before.status) == "online" or str(after.status) == "idle":
        if after.bot == False:
          if str(after.status) == "offline" :
            role = get(after.guild.roles, id=(roleid))
            print("{} has gone {}.".format(after.name,after.status))
            await after.remove_roles(role)


@client.command()
async def check(ctx):
    for i in ctx.guild.members:
        if i.bot == False:
            if str(i.status) == 'offline':
                role = get(ctx.guild.roles, id=(roleid))
                await i.remove_roles(role)
            elif str(i.status) == 'dnd' or str(i.status) == 'online' or str(i.status) == "idle":
                role = get(ctx.guild.roles, id=(roleid))
                await i.add_roles(role)
    

keep_alive()
client.run((bottoken))
