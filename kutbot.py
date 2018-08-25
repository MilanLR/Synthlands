from check import Check
import random
import discord
from discord.ext import commands
import re
import json



client = commands.Bot(command_prefix = '.')


messages = 0



@client.command()
async def ping():
    await client.say('Ik ben er hoor!')

@client.command()
async def echo(*args):
    output = ' '.join(args)
    await client.say(output)
    


@client.event
async def on_ready():
    print("client is ready!")


@client.event
async def on_member_join(member):
    print ("someone joined")
    

@client.event
async def on_message(message):
    author = message.author
    content = message.content
    channel = message.channel


# so it won't reply to itself
    if message.author == client.user:
        return


    global messages


    messages += 1
    if messages == 5:
        messages = 0
        send_messages = ["~The world is just so big.", "~Can I play a game with you?", "~Shall we go on adventure?", "~I would love that.", "~We must hurry, don't you think?", "~How about tomorrow?", "~Seems fine to me.", "~Just another day."]
        reply = send_messages[random.randint(0, (len(send_messages))-1)]
        await client.send_message(client.get_channel('483045683889438723'), reply)
    


    elif message.content.startswith('.sendid'):
        await client.send_message(channel, channel.id)



    if content.startswith('.damage'):

        with open('health.json', 'r') as healthfile:
            data = json.load(healthfile)

        
        data[message.mentions[0].name]['health'] -= int(content.split(' ')[2])

        with open('health.json', 'w') as healthfile:
            json.dump(data, healthfile, indent=2)
        


#the dice

    if content.startswith('.dice'):
        max = int(content.split(' ')[1])
        number = random.randint(1,max)
        await client.send_message(channel, "You rolled {}".format(number))


    if content.startswith('.zegmaarna'):
        msg = content.split()[1:]
        output = ' '.join(msg)
        await client.send_message(channel, output)
    if content.startswith('ping'):
        await client.send_message(channel, "pong")


client.run(TOKEN)


