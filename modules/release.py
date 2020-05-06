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

class NoServer(commands.CommandError):
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

class NoUser(commands.CommandError):
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

class Release(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def set(self, ctx, type, member : discord.Member=None):
        guildid = ctx.guild.id
        author = ctx.author.id

        if type == 'grant':

            if member == None:

                with open('./data/servercomp.json', 'r') as read:
                    scomp = json.load(read)

                    if str(guildid) not in scomp:
                        raise NoServer(ctx.message.server)

                    elif str(guildid) in scomp:

                        with open('./data/servercomp.json', 'w') as write:

                            scomp[f'{guildid}']['tester'] = 'True'
                            embed = discord.Embed(title='**Tester Added**', description=f"{ctx.guild.name} was added as a tester.", color = 0x00AF20)
                            embed.set_footer(text='M.I.A. Output | Medical Information')
                            await ctx.send(embed=embed)

                            json.dump(scomp, write, indent=4)

            elif member is not None:

                memid = member.id
                memname = member.name

                with open('./data/testers.json', 'r') as test:
                    tfile = json.load(test)

                    if str(memid) not in tfile['users']:

                        with open('./data/testers.json', 'w') as write:
                            tfile['users'][f'{memid}'] = {}
                            tfile['users'][f'{memid}']['name'] = member.name
                            tfile['users'][f'{memid}']['tag'] = str(member)
                            tfile['users'][f'{memid}']['id'] = member.id
                            tfile['users'][f'{memid}']['status'] = 'Active'

                            embed = discord.Embed(title='**Tester Added**', description=f"{member} was added as a tester.", color = 0x00AF20)
                            embed.set_footer(text='M.I.A. Output | Medical Information')
                            await ctx.send(embed=embed)

                            json.dump(tfile, write, indent=4)


                    elif str(memid) in tfile['users']:

                        with open('./data/testers.json', 'w') as write:
                            tfile['users'][f'{memid}']['status'] = 'Active'

                            embed = discord.Embed(title='**Tester Added**', description=f"{member} was re-added as a tester.", color = 0x00AF20)
                            embed.set_footer(text='M.I.A. Output | Medical Information')
                            await ctx.send(embed=embed)

                            json.dump(tfile, write, indent=4)

        elif type == 'revoke':

            if member == None:

                with open('./data/servercomp.json', 'r') as read:
                    scomp = json.load(read)

                    if str(guildid) not in scomp:
                        raise NoServer(ctx.message.server)

                    elif str(guildid) in scomp:

                        with open('./data/servercomp.json', 'w') as write:

                            scomp[f'{guildid}']['tester'] = 'False'
                            embed = discord.Embed(title='**Tester Revoked**', description=f"{ctx.guild.name} was revoked as a tester.", color = 0x00AF20)
                            embed.set_footer(text='M.I.A. Output | Medical Information')
                            await ctx.send(embed=embed)

                            json.dump(scomp, write, indent=4)

            elif member is not None:

                memid = member.id
                memname = member.name

                with open('./data/testers.json', 'r') as test:
                    tfile = json.load(test)

                    if str(memid) not in tfile['users']:

                        with open('./data/testers.json', 'w') as write:
                            tfile['users'][f'{memid}'] = {}
                            tfile['users'][f'{memid}']['name'] = member.name
                            tfile['users'][f'{memid}']['tag'] = str(member)
                            tfile['users'][f'{memid}']['id'] = member.id
                            tfile['users'][f'{memid}']['status'] = 'Revoked'

                            embed = discord.Embed(title='**Tester Added**', description=f"{member} was revoked as a tester.", color = 0x00AF20)
                            embed.set_footer(text='M.I.A. Output | Medical Information')
                            await ctx.send(embed=embed)

                            json.dump(tfile, write, indent=4)


                    elif str(memid) in tfile['users']:

                        with open('./data/testers.json', 'w') as write:
                            tfile['users'][f'{memid}']['status'] = 'Revoked'

                            embed = discord.Embed(title='**Tester Added**', description=f"{member} was revoked as a tester.", color = 0x00AF20)
                            embed.set_footer(text='M.I.A. Output | Medical Information')
                            await ctx.send(embed=embed)

                            json.dump(tfile, write, indent=4)

def setup(client):
    client.add_cog(Release(client))
