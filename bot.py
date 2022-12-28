import discord
import os
from dotenv import load_dotenv
import responses

#Grabbing API TOKEN
load_dotenv()
TOKEN = os.getenv("TOKEN")

async def send_message(message, user_message, is_private):
    #decides if response should be sent to channel or private message
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

#Linking bot to discord
def run_discord_bot():
    client = discord.Client()

    #Confirm bot is indeed up and running
    @client.event
    async def on_ready():
        guild_count = 0
        for guild in client.guilds:
            print(f"- {guild.id} (name: {guild.name})")
            guild_count += 1
        print("Dad is in " + str(guild_count) + " guilds.")
        print(f'{client.user} is now up and mowing the lawn!')

    client.run(TOKEN)

    #Prevent endless loop (only respond to user messages)
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        if user_message[0] == '?': #? indicates private message
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)
