import rollparse
import discord
import os
from random import randint

ERROR = " Invalid command (Type !help for list of commands)"
client = discord.Client()
is_prod = os.environ.get('IS_PROD', None)
tok = os.environ.get('TOKEN')    



######################################
## Roll specified number of dice
######################################
def roll(dice):
    numDice = int(dice[0])
    numSides = int(dice[1])
    total = 0
    rollStr = ""
    for x in range (0, numDice):
        r = randint(1, numSides)
        if x == 0:
            rollStr = str(r)
        else:
            rollStr = rollStr + "+" + str(r)
        total += r
    return [total, rollStr]



######################################
## Print on ready to console
######################################
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))



######################################
## Handle messages in server/chat
######################################
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/'):
        try:
            # Dice roll command
            if message.content.startswith('/r'):
                #args = message.content.split(" ")
                #dice = (args[1]).split("d")
                #numDice = int(dice[0])
                resStr = parse(message[2:].replace(" ", ""))
                # diceRoll = roll(dice)
                # result = 0
                # if len(args) > 2:
                #     op = args[2]
                #     if op == '+':
                #         result = diceRoll[0] + int(args[3])
                #     elif op == '-':
                #         result = diceRoll[0] - int(args[3])
                #     elif op == '*':
                #         result = diceRoll[0] * int(args[3])
                #     elif op == '/':
                #         result = diceRoll[0] / int(args[3])
                #     else:
                #         error = ("{0.author.mention}" + ERROR).format(message)
                #         await message.channel.send(error)
                #         return
                #     msg = ('{0.author.mention}: ' + str(args[1]) + str(args[2]) + str(args[3]) + ' = (' + diceRoll[1] + ') ' + str(args[2]) + ' ' + str(args[3]) + ' = ' + '**' + str(result) + '**').format(message)
                #     await message.channel.send(msg)
                # else:
                #     msg = ('{0.author.mention}: ' + str(args[1]) + ' = (' + diceRoll[1] + ') = ' + '**' + str(diceRoll[0]) + '**').format(message)
                #     await message.channel.send(msg)

                msg = ('{0.author.mention}: ' + resStr).format(message)
                await message.channel.send(msg)
        except:
            error = ("{0.author.mention}" + ERROR).format(message)
            await message.channel.send(error)

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

        elif message.content == "!defend":
            txt = ("{0.author.mention}: " + "When you defend someone or something from an immediate threat, roll + Savior. For NPC threats: on a hit, you keep them safe and choose one. On a 7-9, it costs you: expose yourself to danger or escalate the situation." + "\n" 
            + "- Add a Team to the pool" + "\n"
            + "- Take influence over someone you protect" + "\n"
            + "- Clear a condition" + "\n"
            + "For PC threats: on a hit, give them -2 to their roll. On a 7-9, you expose yourself to cost, retribution, or judgment.").format(message)
            await message.channel.send(txt)

        elif message.content == "!assess":
            txt = ("{0.author.mention}: " + "When you assess the situation, roll + Superior. On a 10+, ask two. On a 7-9, ask one. Take +1 while acting on the answers:" + "\n" 
            + "- What here can I use to _____?" + "\n"
            + "- What here is the biggest threat?" + "\n"
            + "- What here is the greatest danger?" + "\n"
            + "- Who here is most vulnerable to me?" + "\n"
            + "- How could we best end this quickly?").format(message)
            await message.channel.send(txt)

        elif message.content == "!provoke":
            txt = ("{0.author.mention}: " + "When you provoke someone susceptible to your words, say what you’re trying to get them to do and roll + Superior. For NPCs: on a 10+, they rise to the bait and do what you want. On a 7-9, they can instead choose one:" + "\n" 
            + "- They stumble: You take +1 forward agains them" + "\n"
            + "- They err: You gain a critical opprotunity" + "\n"
            + "- They overreact: You gain influence over them" + "\n"
            + "- Who here is most vulnerable to me?" + "\n"
            + "For PCs: On a 10+, both. On a 7-9, choose one." + "\n"
            + "- If they do it, add a Team to the pool" + "\n"
            + "- If they don't do it, they mark a condition").format(message)
            await message.channel.send(txt)
        
        elif message.content == "!blow":
            txt = ("{0.author.mention}: " + "When you take a powerful blow, roll + conditions marked. On a 10+, choose one:" + "\n" 
            + "- You must remove yourself from the situation: Flee, pass out, etc." + "\n"
            + "- You lose control of yourself or your powers in a terrible way" + "\n"
            + "- Two options from the 7-9 list" + "\n"
            + "On a 7-9, choose one:" + "\n"
            + "- You lash out verbally: Provoke a teammate to foolhardy action or take advantage of your influence to inflict a condition" + "\n"
            + "- You struggle past the pain: Mark two conditions" + "\n"
            + "On a miss, you stand strong. Mark potential as normal, and say how you weather the blow").format(message)
            await message.channel.send(txt)

        elif message.content == "!help":
            desc = "Get description of "
            txt = ("{0.author.mention}: " + "\n" + "Command List:" + "\n" + "\n" 
            + "**/r [#dice]d[#sides] [ + | - | * | / ] [#]**: " + "\t" + "Roll [#dice] [#sides]-sided die, [ + | - | * | / ] [#]." + "\n" + "Example: /r 2d6 + 2" + "\n" + "\n"
            + "**!engage**: " + "\t" + desc + "'Directly Engage a Threat'" + "\n"
            + "**!unleash**: " + "\t" + desc + "'Unleash Your Powers'" + "\n"
            + "**!comfort**: " + "\t" + desc + "'Comfort or Support'" + "\n"
            + "**!pierce**: " + "\t" + desc + "'Pierce the Mask'" + "\n"
            + "**!defend**: " + "\t" + desc + "'Defend'" + "\n"
            + "**!assess**: " + "\t" + desc + "'Assess the Situation'" + "\n"
            + "**!provoke**: " + "\t" + desc + "'Provoke Someone'" + "\n"
            + "**!blow**: " + "\t" + desc + "'Take a Powerful Blow'" + "\n").format(message)
            await message.channel.send(txt)
        
        else:
            error = ("{0.author.mention}" + ERROR).format(message)
            await message.channel.send(error)



######################################
## Connect
######################################
client.run(tok)
