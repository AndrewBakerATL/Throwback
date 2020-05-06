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
import uuid

class Archive(commands.Cog):
	
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def add(self, ctx, *args):
		usid = str(uuid.uuid4())
		ashow = " ".join(word for word in args)
		sidshow = "-".join(word for word in args)
		with open('./data/shows/series.json', 'r') as slist:
			list = json.load(slist)
			if ashow in list:
				await ctx.send("Entry already exists.")
			else:
				with open('./data/shows/series.json', 'w') as wslist:
					list[ashow] = {}
					list[ashow]['SID'] = sidshow
					list[ashow]['USID'] = usid
					list[ashow]['TN'] = None
					list[ashow]['Description'] = None
					list[ashow]['Featured Image'] = None
					list[ashow]['Episodes'] = None
					list[ashow]['Seasons'] = None

					embed = discord.Embed(title='App Notification (New Entry)', description=f"'{ashow}' has been added as a new show in the library.", color = 0x00AF20)
					embed.add_field(name="**SID**", value=list[ashow]['SID'], inline=False)
					embed.set_footer(text='Throwback | Retro Library')
					await ctx.send(embed=embed)

					json.dump(list, wslist, indent=4)

	@commands.command()
	async def update (self, ctx, SID=None, field=None, *source):
		src = " ".join(word for word in source)
		types = ('SID', 'USID', 'TN', 'Description', 'Featured Image', 'Episodes', 'Seasons')
		with open('./data/shows/series.json', 'r') as slist:
			list = json.load(slist)
			if field.capitalize() in types:
				for item in list:
					if list[item]['SID'] == SID:
						with open('./data/shows/series.json', 'w') as write:
							list[item][field.capitalize()] = src
							json.dump(list, write, indent=4)
			else:
				await ctx.send('That field is not supported.')

def setup(bot):
    bot.add_cog(Archive(bot))