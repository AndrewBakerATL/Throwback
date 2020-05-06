import discord
import asyncio
import json
from discord.ext import commands

class Errors(Exception):

        class FailedInstall(Exception):
            pass
        class ClosedRelease(Exception):
            pass

        class BlacklistError(Exception):

            class User(Exception):
                class NotFound(Exception):
                    pass

            class Server(Exception):
                class NotFound(Exception):
                    pass

class Checks(commands.Cog):

    def __init__(self, client):
        self.client = client

    class Install(commands.Cog):
        async def check_install(ctx):
            with open('./data/servercomp.json') as scomp:
                auth = json.load(scomp)
                guildid = ctx.guild.id

                if auth[f'{guildid}']['status'] == 'active':
                    return True
                else:
                    embed = discord.Embed(title='**App Error**', description="The system is not installed on this server.", color = 0x00AF20)
                    embed.set_footer(text='M.I.A. Output | Medical Information')
                    await ctx.send(embed=embed)
                    raise Errors.FailedInstall

    class Blacklist(commands.Cog):
        async def user(ctx):
            with open("./data/blacklist.json") as blist:
                data = json.load(blist)
                guildid = str(ctx.guild.id)
                authid = str(ctx.author.id)

                if authid in data['users']:
                    if data['users'][authid]['status'] != 'True':
                        return True
                    else:
                        embed = discord.Embed(title='**App Error**', description="You're blacklisted from the service, {}".format(ctx.author.mention), color = 0x00AF20)
                        embed.set_footer(text='M.I.A. Output | Medical Information')
                        await ctx.send(embed=embed)
                        raise Errors.BlacklistError.User
                else:
                    print("User not in database")
                    return True

        async def server(ctx):
            with open("./data/blacklist.json") as blist:
                data = json.load(blist)
                guildid = str(ctx.guild.id)
                authid = str(ctx.author.id)

                if guildid in data['servers']:
                    if data['servers'][guildid]['status'] != 'True':
                        return True
                    else:
                        embed = discord.Embed(title='**App Error**', description="This server is blacklisted from the service.", color = 0x00AF20)
                        embed.set_footer(text='M.I.A. Output | Medical Information')
                        await ctx.send(embed=embed)
                        raise Errors.BlacklistError.Server
                else:
                    print("Server is not in database.")
                    return True

    class Release(commands.Cog):
        async def check_release(ctx):
            with open('./data/config.json') as config:
                state = json.load(config)
                return state['client']['status'] == 'release'

        async def check_prerelease(ctx):
            with open('./data/servercomp.json') as scomp:
                auth = json.load(scomp)
                guildid = ctx.guild.id
                cserver = auth[f'{guildid}']['override'] == 'active' or auth[f'{guildid}']['tester'] == 'True'

                with open('./data/testers.json') as tester:
                    test = json.load(tester)
                    author = ctx.author.id
                    tfile = test['user'][f'{author}']['id']

                    return cserver or tfile

def setup(client):
    client.add_cog(Checks(client))
