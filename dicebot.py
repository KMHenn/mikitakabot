from rollparse import parse
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
            if message.content.startswith('/r'):
                resStr = parse((message.content)[2:].replace(" ", ""))
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

        elif message.content == "!start":
            txt = ("{0.author.mention}: " + "At the start of every session, the GM adds a Team to the pool.").format(message)
            await message.channel.send(txt)

        elif message.content == "!end":
            txt = ("{0.author.mention}: " + "At the end of every session, choose one:" + "\n" 
            + "- **Grow closer to the team**: Explain who made you feel welcome; give influence to that character and clear a condition or mark potential" + "\n"
            + "- **Grow into your own image of yourself**: Explain how you see yourself and why; shift one Label up and another down" + "\n"
            + "- **Grow away from the team**: Explain why you feel detached. Take Inﬂuence over you away from another character" + "\n").format(message)
            await message.channel.send(txt)
        
        elif message.content == "!team":
            txt = ("{0.author.mention}: " + "When you enter battle against a dangerous foe as a team, add two to the Team pool" + "\n"
            + "- If the leader has influence over every teammate, add another Team" + "\n"
            + "- If everyone has the same purpose in the fight, add another Team" + "\n"
            + "- If any team member mistrusts the leader or the team, remove a Team" + "\n"
            + "- If your team is ill-prepared or offbalance, remove a Team" + "\n" + "\n"
            + "The leader of the team can mark a condition to avoid removing a Team from the pool" + "\n" + "\n"
            + "Anyone working with the team can spend Team one for one to help a teammate; give them +1 to their roll" + "\n" + "\n"
            + "Team members can also spend Team to act selfshly. When you act selfshly, say how your actions ignore or insult your teammates, remove one Team from the pool, and shift one Label up and one Label down, your choice. You can use this option after rolling to alter the Label you’re rolling with." + "\n" + "\n"
            + "Whenever time passes, the GM will empty the Team pool and restore it to one Team").format(message)
            await message.channel.send(txt)

        elif message.content == "!conditions":
            txt = ("{0.author.mention}: " + "When a move tells you to mark a condition, mark any condition you choose. Sometimes the GM may tell you a specifc condition to mark, especially after a hard move" + "\n" + "\n"
            + "If you need to mark a condition and have no more conditions to mark, you are taken out. You lose consciousness or ﬂee. The GM will tell you when you come back into another scene. You may clear one condition" + "\n" + "\n"
            + "Once a condition is marked, take -2 to certain moves (max -3)" + "\n" + "\n"
            + "- If you’re Angry, take -2 to comfort or support someone or pierce the mask" + "\n"
            + "- If you’re Afraid, take -2 to directly engage." + "\n"
            + "- If you’re Guilty, take -2 to provoke someone or assess the situation" + "\n"
            + "- If you’re Hopeless, take -2 to unleash your powers" + "\n"
            + "- If you’re Insecure, take -2 to stand in defense or reject what others say about you or the world").format(message)
            await message.channel.send(txt)

        elif message.content == "!clear":
            txt = ("{0.author.mention}: " + "You can always clear a condition by taking a certain action. At the end of any scene in which you take the corresponding action, clear that condition" + "\n"
            + "- To clear Angry, hurt someone or break something important" + "\n"
            + "- To clear Afraid, run from something diffcult" + "\n"
            + "- To clear Guilty, make a sacrifce to absolve your guilt" + "\n"
            + "- To clear Hopeless, ﬂing yourself into easy relief" + "\n"
            + "- To clear Insecure, take foolhardy action without talking to your team" + "\n" + "\n"
            + "You can also clear a condition when someone else comforts or supports you, or when you defend someone").format(message)
            await message.channel.send(txt)

        elif message.content == "!shift":
            txt = ("{0.author.mention}: " + "When you shift a Label, it means that your view of yourself is changing. You see yourself more as the Label you shift up, less as the Label you shift down. If you ever need to shift a Label above +3 or below -2 mark a condition instead, GM’s choice").format(message)
            await message.channel.send(txt)

        elif message.content == "!influence":
            txt = "{0.author.mention}: " + "When someone has Inﬂuence over you, it means you care about what they do, say, or think. At any time you can give Inﬂuence to any character who doesn’t have Inﬂuence over you. All adults have Inﬂuence over you when first introduced" + "\n" + "\n"
            + "When you have Inﬂuence over someone, take +1 to all moves targeting them, including rejecting their Inﬂuence" + "\n" + "\n"
            + "When you take advantage of your Inﬂuence over someone, surrender the Inﬂuence you hold over them to choose one:" + "\n"
            + "- Give them -2 on a move they just made (after the roll)" + "\n"
            + "- Inﬂict a condition on them" + "\n"
            + "- Take an additional +1 on a move targeting them (after the roll)" + "\n" + "\n"
            + "When someone with Inﬂuence over you tells you who you are or how the world works, accept what they say or reject their Inﬂuence. If you accept what they say, the GM will adjust your Labels accordingly; if you want to keep your Labels as they are, you must reject their Inﬂuence" + "\n" + "\n"
            + "When you reject someone's Influence, roll. On a hit, you successfully hold to yourself and tune them out" + "\n" + "\n"
            + "On a 10+, choose two. On a 7-9. choose one:" + "\n"
            + "- Clear a condition or mark potential by immediately acting to prove them wrong" + "\n"
            + "- Shift one Label up and one Label down, your choice" + "\n" 
            + "- Cancel their Inﬂuence and take +1 forward against them" + "\n"
            + "On a miss, their words hit you hard. Mark a condition, and the GM will adjust your Labels" + "\n" + "\n"
            + "If you have Inﬂuence over a teammate and you would gain Inﬂuence over them again, immediately shift one of their Labels up and one of their Labels down, your choice" + "\n" + "\n"
            + "If you have Inﬂuence over an NPC and you would gain Inﬂuence over them again, take +1 forward against them").format(message)
            await message.channel.send(txt)

        elif message.content == "!moment":
            txt = ("{0.author.mention}: " + "When you unlock your Moment of Truth, you can activate it at any time: read your Moment of Truth out loud from the back of your playbook and follow that script. In essence, you (the player) take full control of the narrative in this moment. The GM will let you know what consequences arise..." + "\n" + "\n"
            + "After you use your Moment of Truth, permanently lock one Label. You have changed, and some part of you has become set in stone. You can unlock your Moment of Truth a second time through advancements").format(message)
            await message.channel.send(txt)

        elif message.content == "!advancements":
            txt = ("{0.author.mention}: " + "When someone permanently loses Inﬂuence over you, it means that character can never hold Inﬂuence over you again. This is almost always best used on an NPC, to indicate that you have moved past them and won’t be affected by what you think of them again" + "\n" + "\n"
            + "When you retire from the life, it means you’re not part of the superpowered world anymore, and that character should be considered safe and off-limits to the GM’s moves" + "\n" + "\n"
            + "When you lock a Label, it means that Label can never shift up or down again—that part of yourself is set in stone" + "\n" + "\n"
            + "When you become a paragon of the city, it means you’re no longer a “young” hero—you’re a peer of the biggest heroes in the city, and you aren’t a Masks character anymore. The GM should treat your character as one of the biggest heroes in the city, but play them as an NPC").format(message)
            await message.channel.send(txt)

        elif message.content == "!help":
            desc = "Get description of "
            txt = ("{0.author.mention}: " + "\n" + "Command List:" + "\n" + "\n" 
            + "**/r [#dice]d[#sides] [ + | - | * | / ] [#]**: " + "\t" + "Roll [#dice] [#sides]-sided die, [ + | - | * | / ] [#]." + "\n" + "Example: /r 2d6 + 2" + "\n" + "\n"
            + " BASIC MOVES" + "\n"
            + "**!engage**: " + "\t" + desc + "'Directly Engage a Threat'" + "\n"
            + "**!unleash**: " + "\t" + desc + "'Unleash Your Powers'" + "\n"
            + "**!comfort**: " + "\t" + desc + "'Comfort or Support'" + "\n"
            + "**!pierce**: " + "\t" + desc + "'Pierce the Mask'" + "\n"
            + "**!defend**: " + "\t" + desc + "'Defend'" + "\n"
            + "**!assess**: " + "\t" + desc + "'Assess the Situation'" + "\n"
            + "**!provoke**: " + "\t" + desc + "'Provoke Someone'" + "\n"
            + "**!blow**: " + "\t" + desc + "'Take a Powerful Blow'" + "\n" + "\n"
            + " PERIPHERAL MOVES " + "\n"
            + "**!start**: " + "\t" + desc + "'Start of Session" + "\n"
            + "**!end**: " + "\t" + desc + "'End of Session'" + "\n"
            + "**!team**: " + "\t" + desc + "'Team Mechanics'" + "\n"
            + "**!conditions**: " + "\t" + "'Conditions'" + "\n"
            + "**!clear**: " + "\t" + desc + "'Clearing Conditions'" + "\n"
            + "**!shift**: " + "\t" + desc + "'Shifting Labels'" + "\n"
            + "**!influence**: " + "\t" + desc + "'Influence'" + "\n"
            + "**!moment**: " + "\t" + desc + "'Moment of Truth'" + "\n"
            + "**!advancements**: " + "\t" + desc + "'Advancements'").format(message)
            await message.channel.send(txt)

        else:
            error = ("{0.author.mention}" + ERROR).format(message)
            await message.channel.send(error)



######################################
## Connect
######################################
client.run(tok)
