import nextcord
from nextcord.ext import commands
import requests
import json
from KEYS import *
from EMOJIS import *

class Greetings(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Hello
    @commands.command()
    async def hello(self, ctx):
        embed = nextcord.Embed(title="Dad", url="https://rb.gy/iig8j", description="Now with 69% more dad bod!", color=0x00ff00)
        embed.set_author(name="Dad", url="https://github.com/Dr-CyNiKaL/DadBot", icon_url="https://alekeagle.com/assets/dad.518f1968.png")
        embed.set_thumbnail(url="https://alekeagle.com/assets/dad.518f1968.png")
        embed.add_field(name="Info", value="d!info to see a list of commands!", inline=False)
        embed.set_footer(text="Thanks for reading! (%s)" % version)
        await ctx.send(embed=embed)

    # Info
    @commands.command()
    async def info(self, ctx):
        embed = nextcord.Embed(title="Dad", url="https://rb.gy/iig8j", description="Now with 69% more dad bod!", color=0x00ff00)
        embed.set_author(name="Dad", url="https://github.com/Dr-CyNiKaL/DadBot", icon_url="https://alekeagle.com/assets/dad.518f1968.png")
        embed.set_thumbnail(url="https://alekeagle.com/assets/dad.518f1968.png")
        embed.add_field(name="d!info", value="Displays this message :)", inline=False)
        embed.add_field(name="d!hello", value="See what Dad's up to!", inline=False)
        embed.add_field(name="d!pfp", value="Displays your profile picture", inline=False)
        embed.add_field(name="d!ping", value="Pong!", inline=False)
        embed.add_field(name="d!djoke", value="Get a dad joke!", inline=False)
        embed.add_field(name="d!joke", value="Get oldie but a goodie!", inline=False)
        print("Info command used by %s" % ctx.author.display_name)
        await ctx.send(embed=embed)

    # User Join
    @commands.Cog.listener()
    async def on_member_join(member):
        dadJokeURL = DAD_JOKE_URL
        headers = {
            "X-RapidAPI-Key": DAD_JOKE_API_KEY,
            "X-RapidAPI-Host": "dad-jokes-api1.p.rapidapi.com"
        }
        response = requests.get(dadJokeURL, headers=headers)
        channel = member.guild.system_channel
        await channel.send(f"{member.name} has joined to play catch with Dad!\n**Here's a** ***catch***: *%s*" % json.loads(response.text)["joke"])

    # User Leave
    @commands.Cog.listener()
    async def on_member_remove(member):
        channel = member.guild.system_channel
        await channel.send(f'%s{member.name} has left to get milk. %s%s%s' % (pensive, milk, man_running, dashing))

def setup(client):
    client.add_cog(Greetings(client))