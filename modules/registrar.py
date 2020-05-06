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
import time
import datetime

class Register(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def register(self, ctx):
        authid = str(ctx.author.id)
        with open('./data/users/users.json', 'r') as read:
            list = json.load(read)
            if authid not in list:
                with open('./data/users/users.json', 'w') as write:
                    embed = discord.Embed(title='App Notification (New User)', description=f"{ctx.author.name} has signed up.", color = 0x00AF20)
                    list[authid] = {}
                    list[authid]['Username'] = str(ctx.author)
                    list[authid]['Name'] = ctx.author.name
                    list[authid]['Favorite Show'] = None
                    # Monthly Watch Time
                    list[authid]['MWT'] = 0
                    # Overall Watch Time
                    list[authid]['OWT'] = 0
                    # Show Completion Rate
                    list[authid]['SCR'] = 0
                    # Queue Completion Rate
                    list[authid]['QCR'] = 0
                    # Show Queue
                    list[authid]['Queue'] = {}
                    timestamp = ctx.message.created_at
                    time = timestamp.replace(microsecond=0)
                    embed.add_field(name="**Timestamp**", value=f'{time}', inline=False)
                    embed.set_footer(text='Throwback | Retro Library')
                    await ctx.send(embed=embed)

                    json.dump(list, write, indent=4)

def setup(client):
    client.add_cog(Register(client))
