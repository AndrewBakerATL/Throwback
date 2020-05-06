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
from apiclient.discovery import build

class Events(commands.Cog):


    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        guildid = guild.id
        system = guild.system_channel

        with open('./data/servercomp.json', 'r') as read:
            scomp = json.load(read)

            if str(guildid) not in scomp:

                with open('./data/servercomp.json', 'w') as write:

                    scomp[f'{guildid}'] = {}
                    scomp[f'{guildid}']['name'] = guild.name
                    scomp[f'{guildid}']['owner'] = str(guild.owner)
                    scomp[f'{guildid}']['id'] = guild.id
                    scomp[f'{guildid}']['ownerid'] = guild.owner_id
                    scomp[f'{guildid}']['members'] = guild.member_count
                    scomp[f'{guildid}']['override'] = 'False'
                    scomp[f'{guildid}']['tester'] = 'False'
                    scomp[f'{guildid}']['status'] = 'inactive'

                    json.dump(scomp, write, indent=4)

                    await system.send("Testing Install")

            elif str(guildid) in scomp:
                await system.send("Already Installed")

def setup(client):
    client.add_cog(Events(client))
