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
        #embed.add_field(name="d!pfp", value="Displays your profile picture", inline=False)
        embed.add_field(name="d!ping", value="Pong!", inline=False)
        embed.add_field(name="d!djoke", value="Get a dad joke!", inline=False)
        embed.add_field(name="d!joke", value="An oldie but a goodie!", inline=False)
        await ctx.send(embed=embed)

    # User Join
    @commands.Cog.listener()
    async def on_member_join(self, member):
        dadJokeURL = DAD_JOKE_URL
        headers = {
            "X-RapidAPI-Key": DAD_JOKE_API_KEY,
            "X-RapidAPI-Host": "dad-jokes-api1.p.rapidapi.com"
        }
        response = requests.get(dadJokeURL, headers=headers)
        channel = member.guild.system_channel
        message = await channel.send(f"%s {member.mention} has joined to play catch with Dad! %s\n**Here's a** ***catch***: *%s*" % (partying, baseball, json.loads(response.text)["joke"]))
        for emoji in [party_popper,party_popper,sparkles,confetti_ball,cricket]:
            await message.add_reaction(emoji)

    # User Leave
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = member.guild.system_channel
        message = await channel.send(f'%s {member.mention} has left to get milk. %s' % (pensive, store))
        for emoji in [milk,man_running,dashing]:
            await message.add_reaction(emoji)

def setup(client):
    client.add_cog(Greetings(client))