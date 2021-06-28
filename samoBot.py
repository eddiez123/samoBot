import discord
import os
from discord.ext import commands
from discord.utils import find

TOKEN = 'ODUyMzkyNzI1MDM0MzAzNTM5.YMGKlg.Gftv_Bq_0dqSXd89MME7hMT6t_Y'

# Prefix to be entered before the command. (for example, .ping)
client = commands.Bot(command_prefix='.')

# Global counter for the amount of times "mha fans" is used
global counter 
counter = 0


# Exclusive for Patrick birthday pog
@client.event
async def on_guild_join(guild):
    general = find(lambda x: x.name == 'bamboozled-again', guild.text_channels)
    if general and general.permissions_for(guild.me).send_messages:
        await general.send('HAPPY BIRTHDAY PATRICK CAN I GET A POGGERS IN CHAT ALSO EDDIE IS VERY COOL AND GOOD AT LEAGUE OF LEGENDS AHAHA AMIRITE')


# On ready function; using it to test multiple different things that will occur when the bot turns on
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd,activity=discord.Game("Ur bootyhole"))

    # Exclusive print statement for Timmy's discord 
    # general = client.get_guild(145653809954291712)
    # channel = client.get_channel(145653809954291712)
    # if channel and channel.permissions_for(general.me).send_messages:
    #     await channel.send("mha fans")

    print("Bot is ready.")


# Updating the global counter for mha fans
@client.event
async def on_message(message):
    general = client.get_guild(145653809954291712)
    channel = client.get_channel(145653809954291712)

    # if message.content.strip() == "mha fans" and message.channel == channel:
    global counter
    counter += 1
    print(counter)


# Test function to display the global counter 
@client.command()
async def mhacounter(ctx):
    await ctx.send(f"mha fans has been said {counter} times")


# Practice functions
@client.command()
async def test(ctx):
    await ctx.send(f"This is a test reply {round(client.latency * 1000)} ms")

@client.command(aliases=['CUM'])
async def cum(ctx):
    await ctx.send(file=discord.File('.\daeddie.jpg'))


client.run(TOKEN)
