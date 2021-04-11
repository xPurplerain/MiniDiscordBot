# Ist ein kleiner discord.py Discord Bot
# Version: 1.0
# Funktionen Zurzeit:
# -- ChatClear
# -- Ping (ms)
# -- Status
# -- Aktivität

# Imports

import discord
from discord.ext import commands
import config.token

# Other

client = commands.Bot(command_prefix='.')
client.remove_command("help")

# Events

@client.event
async def on_ready():
    activity = discord.Game(name="mit .help")
    await client.change_presence(status=discord.Status.do_not_disturb, activity=activity)
    print(f'{client.user} hat sich mit Discord verbunden')

# Commands

@client.group(invoke_without_command=True)
async def help(ctx):

@client.command()
async def ping(ctx):
    await ctx.send(f'Dein Ping beträgt {round(client.latency * 1000)}ms')

@client.command()
async def ms(ctx):
    await ctx.send(f'Dein Ping beträgt {round(client.latency * 1000)}ms')

@client.command()
async def clear(ctx, amount=1000):
    await ctx.channel.purge(limit=amount)

@client.command()
async def cc(ctx, amount=1000):
    await ctx.channel.purge(limit=amount)

# Startet den Bot

client.run(config.token.TOKEN)