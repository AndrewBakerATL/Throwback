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

class Fetch(commands.Cog):
	
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def index(self, ctx, show):
		with open('./data/series.json') as slist:
			list = json.load(slist)
			embed = discord.Embed(title='Archived Show', description="", color = 0x00AF20)
			embed.set_footer(text='Throwback | Retro Library')
			await ctx.send(embed=embed)

	@commands.command()
	async def profile(self, ctx, show):
		embed = discord.Embed(title='Invite Link', description="https://discordapp.com/api/oauth2/authorize?client_id=692633365182021632&permissions=8&scope=bot", color = 0x00AF20)
		embed.set_footer(text='Throwback | Retro Library')
		await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Fetch(bot))