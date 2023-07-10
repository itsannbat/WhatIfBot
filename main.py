# Import discord package
import discord
from discord.ext import commands
import random

# The bot
bot = commands.Bot(command_prefix = '8! ', case_insensitive = True)
genChannel = 852997471314509884

# when the bot starts
@bot.event
async def on_ready(): # async allows the function to run even though there is a delay
    general_channel = bot.get_channel(genChannel)

    await general_channel.send('Hello, I am What-If Bot. I am an absolute meme. write "8! commands" to get started')

# help
@bot.command(name = 'commands')
async def commands(context):
    infoEmbed = discord.Embed(title = "List of Functions", color = 0xA977F1)
    infoEmbed.add_field(name = "what if ...", value = "answers your what if question", inline = False)
    infoEmbed.add_field(name = "8! joke", value = "gives a funny dad joke", inline = False)
    infoEmbed.add_field(name = "8! version", value = "states the version", inline = False)
    infoEmbed.set_footer(text = "Ann B and Huy M")

    await context.message.channel.send(embed = infoEmbed)

# version
@bot.command(name = 'version')
async def version(context):
    verEmbed = discord.Embed(title = "Current Version:", color = 0xA977F1)
    verEmbed.add_field(name = "Version Code", value = "v1.0.2", inline = False)
    verEmbed.add_field(name = "Release Date", value = "June 12, 2021", inline = False)
    verEmbed.set_author(name = "What-If Bot")
    verEmbed.set_footer(text = "Ann B and Huy M")

    await context.message.channel.send(embed = verEmbed)

# jokes
@bot.command(name = 'joke')
async def joke(context):
    
    file = open('dadjokes.txt')
    content = file.readlines()
    r1 = random.randint(0,len(content) - 1)

    await context.message.channel.send(content[r1])

# what if
@bot.event
async def on_message(message):
    if "what if" in message.content.lower():
        file = open('what-ifs.txt')
        content = file.readlines()
        r2 = random.randint(0,len(content) - 1)

        await message.channel.send(content[r2])

    await bot.process_commands(message)

# When the bot disconnects from the server
@bot.event
async def on_disconnect():
    general_channel = bot.get_channel(genChannel)
    await general_channel.send('Goodbye, and have a nice day!')


# Run the bot on server
bot.run('token')