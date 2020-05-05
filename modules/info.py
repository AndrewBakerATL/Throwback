import discord
from discord.ext import commands

class Information(commands.Cog):
	
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def info(self, ctx):
		embed = discord.Embed(title='Information', description="Throwback is a retro streaming platform. For more information on the subject, please see the open-source docs at the link below.", color = 0x00AF20)
		embed.add_field(name="**Disclaimer**", value="Throwback doesn't inherently host any of the content streamed ourselves; we're only a libary for pre-existing content.", inline=False)
		embed.add_field(name="**Development Team**", value="Creator: Soujiro#4999 \nDeveloper: Kaz#1634 \nTester: Open \nTester: Open", inline=False)
		embed.add_field(name="**Documentation Links**", value="[Invite Link](https://discord.com/api/oauth2/authorize?client_id=705656833305477162&permissions=8&scope=bot) | [Terms of Use](https://google.com) | [Features](https://github.com/CSAndrew/Throwback) | [Commands](https://github.com/CSAndrew/Throwback)", inline=False)
		# embed.set_author(name="Throwback", icon_url="https://github.com/CSAndrew/Throwback/blob/develop/assets/Scooby.jpg?raw=true")
		embed.set_footer(text='Throwback | Retro Library')
		await ctx.send(embed=embed)

	@commands.command()
	async def invite(self, ctx):
		embed = discord.Embed(title='Invite Link', description="https://discord.com/api/oauth2/authorize?client_id=705656833305477162&permissions=8&scope=bot", color = 0x00AF20)
		embed.set_footer(text='Throwback | Retro Library')
		await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Information(bot))