import discord
from discord.ext import commands
from itertools import cycle
from discord.ext import tasks
from errors import errors

class Echeck(commands.Cog):

    def __init__(self, client):
        self.client = client

# Error Checking

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            author = ctx.message.author
            embed = discord.Embed(title='**App Error**', description="Command was not found.", color = 0x00AF20)
            embed.set_footer(text='M.I.A. Output | Medical Information')
            await ctx.send(embed=embed)

        if isinstance(error, commands.MissingPermissions):
            author = ctx.message.author
            embed = discord.Embed(title='**App Error**', description=f"{author.mention}, you don't have the required permissions for that.", color = 0x00AF20)
            embed.set_footer(text='M.I.A. Output | Medical Information')
            await ctx.send(embed=embed)

        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title='**App Error**', description="You're missing a required argument.", color = 0x00AF20)
            embed.set_footer(text='M.I.A. Output | Medical Information')
            await ctx.send(embed=embed)

        if isinstance(error, commands.CheckFailure):
            embed = discord.Embed(title='**App Error**', description="One or more of the system checks have failed.", color = 0x00AF20)
            embed.set_footer(text='M.I.A. Output | Medical Information')
            await ctx.send(embed=embed)

        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(title='**App Error**', description="**M.I.A.** was given a bad argument.", color = 0x00AF20)
            embed.set_footer(text='M.I.A. Output | Medical Information')
            await ctx.send(embed=embed)

        if isinstance(error, commands.CommandInvokeError):
            if isinstance(error.original, errors.Errors.BlacklistError):
                await ctx.send('Blacklisted')

            if isinstance(error.original, errors.Errors.FailedInstall):
                await ctx.send("Failed Install")


        print(error)

def setup(client):
    client.add_cog(Echeck(client))
