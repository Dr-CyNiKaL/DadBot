import nextcord
from nextcord.ext import commands
import requests
import json
from KEYS import *
from EMOJIS import *

class Commands(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Custom User Profile
    @commands.command()
    async def pfp(self, ctx):
        embed = nextcord.Embed(title="PLACEHOLDER", color=0x00ff00)
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    # Ping
    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong!")
    
    # Dad Joke
    @commands.command()
    async def djoke(self, ctx):
        dadJokeURL = DAD_JOKE_URL
        headers = {
            "X-RapidAPI-Key": DAD_JOKE_API_KEY,
            "X-RapidAPI-Host": "dad-jokes-api1.p.rapidapi.com"
        }
        response = requests.get(dadJokeURL, headers=headers)
        await ctx.send("Here's a dad joke:\n%s" % json.loads(response.text)["joke"])
    
    # Joke
    @commands.command()
    async def joke(self, ctx):
        JokeURL = JOKE_URL
        querystring = {"format":"json","contains":"C%23","idRange":"0-150","blacklistFlags":"nsfw,racist"}
        headers = {
            "X-RapidAPI-Key": JOKE_API_KEY,
            "X-RapidAPI-Host": "jokeapi-v2.p.rapidapi.com"
        }
        response = requests.get(JokeURL, headers=headers, params=querystring)
        await ctx.send("Here's a joke:")
        await ctx.send("%s %s" % (json.loads(response.text)["setup"], json.loads(response.text)["delivery"]))

def setup(client):
    client.add_cog(Commands(client))