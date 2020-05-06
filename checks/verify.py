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


class Verify(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def status(self, ctx, type):

        with open('./data/config.json') as status_file:
            data = json.load(status_file)

        if type == 'release':
            data['client']['status'] = 'release'
            with open('./data/config.json', 'w') as write:
                json.dump(data, write, indent=2)

            print("status = {}".format(data['client']['status']))

        elif type == 'prerelease':
            data['client']['status'] = 'prerelease'
            with open('./data/config.json', 'w') as write:
                json.dump(data, write, indent=2)

            print("status = {}".format(data['client']['status']))

        elif type == 'inactive':
            data['client']['status'] = 'inactive'
            with open('./data/config.json', 'w') as write:
                json.dump(data, write, indent=2)

            print("status = {}".format(data['client']['status']))


def setup(client):
    client.add_cog(Verify(client))
