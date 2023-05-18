import nextcord
from nextcord.ext import commands
import random
from KEYS import *
from EMOJIS import *

class Interactions(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.hungry = ["i'm ", "im ", "i am "]

    # I'm Hungry
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return
        check = message.clean_content.lower().strip()
        check = nextcord.utils.remove_markdown(check)
        for trigger in self.hungry:
            if trigger in check and len(check) > len(trigger):
                if random.randint(1, 100) <= 100:                
                    if 'i\'m' in check:
                        user_message = check.split('i\'m')[1]
                    elif 'im' in check:
                        user_message = check.split('im')[1]
                    elif 'i am' in check:
                        user_message = check.split('i am')[1]
                    await message.channel.send(f"%s Hi{user_message}, I'm Dad!" % (message.author.mention))
                    await message.add_reaction(skull)

def setup(client):
    client.add_cog(Interactions(client))