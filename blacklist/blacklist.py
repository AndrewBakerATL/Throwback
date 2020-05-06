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


class Blacklist(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def blacklist(self, ctx, type, member : discord.Member=None):

        if type.capitalize() == 'User':

            if member is not None:

                memid = str(member.id)
                with open('./data/blacklist.json') as blacklist:
                    list = json.load(blacklist)

                    if memid not in list['users']:

                        with open('./data/blacklist.json', 'w') as blacklist:

                            list['users'][f'{memid}'] = {}
                            list['users'][f'{memid}']['name'] = member.name
                            list['users'][f'{memid}']['tag'] = str(member)
                            list['users'][f'{memid}']['id'] = member.id
                            list['users'][f'{memid}']['status'] = 'True'

                            embed = discord.Embed(title='App Blacklist', description=f"{member} was blacklisted", color = 0x00AF20)
                            embed.set_footer(text='M.I.A. Output | Medical Information')
                            await ctx.send(embed=embed)

                            json.dump(list, blacklist, indent=4)

                    if memid in list['users']:

                        with open('./data/blacklist.json', 'w') as blacklist:

                            list['users'][f'{memid}']['status'] = 'True'

                            embed = discord.Embed(title='App Blacklist', description=f"{member} was blacklisted", color=0x00AF20)
                            embed.set_footer(text='M.I.A. Output | Medical Information')
                            await ctx.send(embed=embed)

                            json.dump(list, blacklist, indent=4)

        elif type.capitalize() == 'Server':
            guildid = str(ctx.guild.id)
            with open('./data/blacklist.json') as blacklist:
                list = json.load(blacklist)

                if guildid not in list['servers']:

                    with open('./data/blacklist.json', 'w') as blacklist:

                        list['servers'][f'{guildid}'] = {}
                        list['servers'][f'{guildid}']['name'] = ctx.guild.name
                        list['servers'][f'{guildid}']['id'] = ctx.guild.id
                        list['servers'][f'{guildid}']['status'] = 'True'

                        embed = discord.Embed(title='App Blacklist', description=f"{ctx.guild.name} was blacklisted", color = 0x00AF20)
                        embed.set_footer(text='M.I.A. Output | Medical Information')
                        await ctx.send(embed=embed)

                        json.dump(list, blacklist, indent=4)

                if guildid in list['servers']:

                    with open('./data/blacklist.json', 'w') as blacklist:

                        list['servers'][f'{guildid}']['status'] = 'True'

                        embed = discord.Embed(title='App Blacklist', description=f"{ctx.guild.name} was blacklisted", color=0x00AF20)
                        embed.set_footer(text='M.I.A. Output | Medical Information')
                        await ctx.send(embed=embed)

                        json.dump(list, blacklist, indent=4)

        elif type.capitalize() == 'Remove':

            if member == None:

                guildid = str(ctx.guild.id)
                with open('./data/blacklist.json') as blacklist:
                    list = json.load(blacklist)

                    if guildid in list['servers']:

                        with open('./data/blacklist.json', 'w') as blacklist:

                            list['servers'][f'{guildid}']['status'] = 'False'

                            embed = discord.Embed(title='App Blacklist', description=f"{ctx.guild.name} was removed from blacklist", color = 0x00AF20)
                            embed.set_footer(text='M.I.A. Output | Medical Information')
                            await ctx.send(embed=embed)

                            json.dump(list, blacklist, indent=4)

                    elif guildid not in list['servers']:

                        embed = discord.Embed(title='App Blacklist', description=f"{ctx.guild.name} is not blacklisted.", color = 0x00AF20)
                        embed.set_footer(text='M.I.A. Output | Medical Information')
                        await ctx.send(embed=embed)

            elif member is not None:
                memid = str(member.id)
                with open('./data/blacklist.json') as blacklist:
                    list = json.load(blacklist)

                    if memid in list['users']:

                        with open('./data/blacklist.json', 'w') as blacklist:

                            list['users'][f'{memid}']['status'] = 'False'

                            embed = discord.Embed(title='App Blacklist', description=f"{member} was removed from blacklist", color = 0x00AF20)
                            embed.set_footer(text='M.I.A. Output | Medical Information')
                            await ctx.send(embed=embed)

                            json.dump(list, blacklist, indent=4)

                    elif memid not in list['users']:

                        embed = discord.Embed(title='App Blacklist', description=f"{member} is not blacklisted.", color = 0x00AF20)
                        embed.set_footer(text='M.I.A. Output | Medical Information')
                        await ctx.send(embed=embed)

    @commands.command()
    async def test(self, ctx):
        print('True')


def setup(client):
    client.add_cog(Blacklist(client))
