import discord
from discord.ext import commands
import json
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

					embed = discord.Embed(title='New Show', description=f"'{ashow}' has been added as a new show in the library.", color = 0x00AF20)
					embed.add_field(name="**USID**", value=list, inline=False)
					embed.set_footer(text='Throwback | Retro Library')
					await ctx.send(embed=embed)

					json.dump(list, wslist, indent=4)

def setup(bot):
    bot.add_cog(Archive(bot))