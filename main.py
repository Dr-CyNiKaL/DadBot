import nextcord
from nextcord.ext import commands
import os
from KEYS import *

#--------------------------------------------------------------------------------#
    ##########################
    #      TO-DO LIST        #
    ##########################
    # 1. Roles for Social Credit System
    # 2. Slash commands
    # 3. Potential stored data for user games (far in the future)

    ##########################
    #      KNOWN BUGS        #
    ##########################
    # 1. I'm hungry feature is still a little jank but it'll do
    # 2. Music will not pause nor play
    # 3. Player volume cannot be changed no matter what

    ###########################
    #      HELPFUL LINKS      #
    ###########################
    # 1. nextcord Documentation: https://docs.nextcord.dev/en/stable/api.html#
    # 2. HTML Color Picker: https://www.w3schools.com/colors/colors_picker.asp
#---------------------------------------------------------------------------------#

version = "DadBot v0.1.0"
intents = nextcord.Intents.all()
intents.members = True
intents.message_content = True
client = commands.Bot(command_prefix="d!", intents=intents)

# SETUP
@client.event
async def on_ready():
    guild_count = 0
    for guild in client.guilds:
        print(f"- {guild.id} (name: {guild.name})")
        guild_count += 1
    
    await client.change_presence(activity=nextcord.Game(name="catch with my sons \U000026BE"))

    print("Dad is in " + str(guild_count) + " guilds.")
    print(f'{client.user} is now up and mowing the lawn! (%s)' % version)
    print('-----------------------------------------------------------')

initial_extensions = []
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        initial_extensions.append(f'cogs.{filename[:-3]}')

if __name__ == '__main__':
    print('-----------------------------------------------------------')
    print("Cogs Loaded: ")
    for extension in initial_extensions:
        client.load_extension(extension)
        print(f'Loaded {extension}')
    print('-----------------------------------------------------------')

#print(initial_extensions)

client.run(DISCORD_TOKEN)
