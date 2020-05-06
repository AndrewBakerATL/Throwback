import requests
import discord
from discord.ext import commands
import random
import asyncio
import os
from itertools import cycle
import json
import subprocess
from time import sleep
from errors import errors

with open('./data/config.json') as json_file:
    data = json.load(json_file)
    bot = commands.Bot(command_prefix = data['client']['prefix'])

#   Load Extensions

for filename in os.listdir('./streaming'):
    if filename.endswith('.py'):
        bot.load_extension(f'streaming.{filename[:-3]}')

for filename in os.listdir('./modules'):
    if filename.endswith('.py'):
        bot.load_extension(f'modules.{filename[:-3]}')

@bot.event
async def on_ready():
    print('Bot Online')
    print("Bot Name: {}".format(bot.user.name))
    print("Bot running under user: {}".format(bot.user))
    game = discord.Game("Indexing Shows...")
    await bot.change_presence(status=discord.Status.dnd, activity=game)

Token = data['client']['token']
bot.run(Token)