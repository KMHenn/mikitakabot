import discord
import os
from random import randint
#from boto.s3.connection import S3Connection

client = discord.Client()

is_prod = os.environ.get('IS_PROD', None)
tok = os.environ.get('TOKEN')    

def roll(dice):
    numDice = int(dice[0])
    numSides = int(dice[1])
    total = 0
    for x in range (0, numDice):
        r = randint(1, numSides)
        total += r
    return total

def errorHandle():
    return "Invalid command"


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))



@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/'):
        try:
            if message.content.startswith('/r'):
                args = message.content.split(" ")
                dice = (args[1]).split("d")
                diceRoll = roll(dice)
                math = 0

                if len(args) > 2:
                    op = args[2]
                    if op == '+':
                        math = int(args[3])
                    elif op == '-':
                        math = int(args[3]) * -1
                    else:
                        error = errorHandle()
                        await message.channel.send(error + ": Dice roll format is [#dice]d[#sides] [+ | -] [#]")
                        return

                msg = ('{0.author.mention}: ' + str(args[1]) + ' ' + str(args[2]) + ' ' + str(args[3]) + ' = ' + str(diceRoll + math)).format(message)
                await message.channel.send(msg)
        except:
            error = errorHandle()
            await message.channel.send(error + ": Invalid command")

    elif message.content.startswith('!'):
        if message.content == '!engage':
            txt = ("{0.author.mention}: " + "When you directly engage a threat, roll + Danger. On a hit, trade blows. On a 10+, pick two. On a 7-9, pick one: " + "\n" 
            + "- Resist or avoid their blows" + "\n"
            + "- Take something from them" + "\n"
            + "- Create an opprotunity for your allies" + "\n"
            + "- Impress, surprise, or frighten the opposition").format(message)
            await message.channel.send(txt)

        elif message.content == "!unleash":
            txt = ("{0.author.mention}: " + "When you unleash your powers to overcome an obstacle, reshape your environment, or extend your senses, roll + Freak. On a hit, you do it. On a 7-9, mark a condition or the GM will tell you how the effect is unstable or temporary.").format(message)
            await message.channel.send(txt)
        
        elif message.content == "!comfort":
            txt = ("{0.author.mention}: " + "When you comfort or support someone, roll + Mundane. On a hit, they hear you: they mark potential, clear a condition, or shift Labels if they open up to you. On a 10+, you can also add a Team to the pool or clear a condition yourself.").format(message)
            await message.channel.send(txt)

        elif message.content == "!pierce":
            txt = ("{0.author.mention}: " + "When you pierce someone’s mask to see the person beneath, roll + Mundane. On a 10+, ask three. On a 7-9, ask one: " + "\n" 
            + "- What are you really planning?" + "\n"
            + "- What do you want me to do?" + "\n"
            + "- What do you intend to do?" + "\n"
            + "- How could I get your character to ____?" + "\n"
            + "- How could I gain influence over you?").format(message)
            await message.channel.send(txt)


client.run(tok)
