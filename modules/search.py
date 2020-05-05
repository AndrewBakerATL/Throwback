import discord
from discord.ext import commands
from apiclient.discovery import build


class Search(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def google(self, ctx, *, term):
        apikey = ''
        resource = build("customsearch", 'v1', developerKey=apikey).cse()
        result = resource.list(q='{}'.format(term), cx='003797154308276670266:zw8o82b3drt').execute()
        results = result['items'][0]
        image = results['pagemap']['cse_thumbnail'][0]['src']
        embed = discord.Embed(color = 0x00AF20)
        embed.set_footer(text='Google Search')
        embed.add_field(name="**Top Result: {}**".format(results['title']), value=results['link'])
        embed.set_thumbnail(url="{}".format(image))
        await ctx.send(embed=embed)

    @commands.command()
    async def glist(self, ctx, *, term):
        apikey = ''
        resource = build("customsearch", 'v1', developerKey=apikey).cse()
        result = resource.list(q='{}'.format(term), cx='003797154308276670266:zw8o82b3drt').execute()
        results = result['items']
        embed = discord.Embed(color = 0x00AF20)
        embed.set_footer(text='Google Search')
        for item in results:
            embed.add_field(name="**Search Entry: {}**".format(item['title']), value="{}\n{}\n \n ".format(item['link'], item['snippet']), inline=False)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Search(client))
