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
    return ""


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))



@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/'):
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
                    errorHandle()
                    return

            msg = ('{0.author.mention}: ' + str(args[1]) + ' ' + str(args[2]) + ' ' + str(args[3]) + ' = ' + str(diceRoll + math)).format(message)
            await message.channel.send(msg)



client.run(tok)
