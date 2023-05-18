from nextcord.ext import commands
import random
from KEYS import *
from EMOJIS import *

class Interactions(commands.Cog):
    def __init__(self, client):
        self.client = client

    # I'm Hungry
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return
        if 'i\'m' in message.content.lower() or 'im' in message.content.lower() or 'i am' in message.content.lower():
            if random.randint(1, 100) <= 69:
                user_message = message.content.lower()
                if 'i\'m' in user_message:
                    user_message = user_message.split('i\'m')[1]
                elif 'im' in user_message:
                    user_message = user_message.split('im')[1]
                elif 'i am' in user_message:
                    user_message = user_message.split('i am')[1]
                await message.channel.send(f'Hi{user_message}, I\'m Dad!')

def setup(client):
    client.add_cog(Interactions(client))