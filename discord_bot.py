# deviousAI discord bot
import discord
import random
import praw
import datetime
from chatterbot import ChatBot
from chatterbot.response_selection import get_random_response

# reddit credentials:
reddit = praw.Reddit(client_id=' ',
                     client_secret=' ',
                     user_agent=' ',
                     username=' ',
                     password=' ')

# chatterbot setup:
chatbot = ChatBot(
    'deviousAI',
    response_selection_method=get_random_response,
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'statement_comparison_function': 'chatterbot.comparisons.levenshtein_distance'
        },
        {
            'import_path': 'chatterbot.logic.MathematicalEvaluation'
        }
    ],
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)
chatbot.trainer.export_for_training('./data/my_corpus/export.json')


# need some variables:   
Rando = True
subreddit2 = 'python'
howmany = 1
toint = 1               
newtophot = 'top'
links = 'links'
client = discord.Client()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
@client.event
async def on_message(message):
    # ^ we do not want the bot to reply to itself

    # global all the things, why not...
    global Rando
    global subreddit2
    global howmany
    global toint          
    global newtophot
    global links
    
    if message.author == client.user:
        return

    if message.content.startswith('!help'):
        await client.send_message(message.channel, '`!help !hello !time !reddit !reddithelp`')
        await client.send_message(message.channel, '`!D4 !D6 !D8 !D12 !D16 !D20`')
        await client.send_message(message.channel, '`!loot !spellbook !random !tableflip`')
        await client.send_message(message.channel, 'If you want to chat with me put `~` in front.')

    if message.content.startswith('~'):
        response = str(message.content)
        response = str.replace(response, "~", '')
        reply = str(chatbot.get_response(response))
        reply = str.replace(reply, "~", '')
        await client.send_message(message.channel, reply, tts=True)

    elif message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)         

    elif message.content.startswith('!reddithelp'):
        await client.send_message(message.channel, 'Example: `!reddit dogs top 5`')
        await client.send_message(message.channel, 'Example: `!reddit cats top 3 links`')
        await client.send_message(message.channel, "Tip: replace 'top' with 'hot' or 'new'")
        
    elif message.content.startswith('!reddit'):
        try:
            subreddit2 = message.content.split(' ')[1]
            howmany = message.content.split(' ')[3]
            toint = int(howmany)                
            newtophot = message.content.split(' ')[2]
            try:
                links = message.content.split(' ')[4]
            except Exception as e:
                links = 'nolink'
            if links == 'links' and toint < 10:
                if newtophot == 'hot': 
                    submissions = reddit.subreddit(subreddit2).hot(limit=toint)
                    for item in submissions:
                        await client.send_message(message.channel, item.url)
                            
                if newtophot == 'top': 
                    submissions = reddit.subreddit(subreddit2).top(limit=toint)
                    for item in submissions:
                        await client.send_message(message.channel, item.url)
                            
                if newtophot == 'new': 
                    submissions = reddit.subreddit(subreddit2).new(limit=toint)
                    for item in submissions:
                        await client.send_message(message.channel, item.url)
                          
            elif links != 'links' and toint < 10:      
                if newtophot == 'hot':        
                    for submission in reddit.subreddit(subreddit2).hot(limit=toint):
                        subreply = submission.title
                        await client.send_message(message.channel, subreply)                       
                if newtophot == 'top':
                    for submission in reddit.subreddit(subreddit2).top(limit=toint):
                        subreply = submission.title
                        await client.send_message(message.channel, subreply)
                if newtophot == 'new':
                    for submission in reddit.subreddit(subreddit2).new(limit=toint):
                        subreply = submission.title
                        await client.send_message(message.channel, subreply)
            elif toint >= 10:
                await client.send_message(message.channel, "That's too many...")           
        except Exception as e:
             await client.send_message(message.channel, "Try: `!reddithelp` for proper syntax")


# except Exception as e:
        
    elif message.content.startswith('!time'):
        t = datetime.datetime.now()
        await client.send_message(message.channel, 'The {} is {:%H:%M}.'.format("time",t))
    elif message.content.startswith('!D4'):
        await client.send_message(message.channel, 'You roll a four-sided die:')
        await client.send_message(message.channel, random.randint (1, 4))
    elif message.content.startswith('!D6'):
        await client.send_message(message.channel, 'You roll a six-sided die:')
        await client.send_message(message.channel, random.randint (1, 6))
    elif message.content.startswith('!D8'):
        await client.send_message(message.channel, 'You roll an eight-sided die:')
        await client.send_message(message.channel, random.randint (1, 8))
    elif message.content.startswith('!D12'):
        await client.send_message(message.channel, 'You roll a twelve-sided die:')
        await client.send_message(message.channel, random.randint (1, 12))
    elif message.content.startswith('!D16'):
        await client.send_message(message.channel, 'You roll a sixteen-sided die:')
        await client.send_message(message.channel, random.randint (1, 16))
    elif message.content.startswith('!D20'):
        await client.send_message(message.channel, 'You roll a twenty-sided die:')
        await client.send_message(message.channel, random.randint (1, 20))
    elif message.content.startswith('!heart'):
        await client.send_message(message.channel, 'Awww, I <3 you too!')

        # start a random thing:
    elif message.content.startswith('!random'):
        await client.send_message(message.channel, 'Starting... use `!stop` to stop.')
        Rando = True
        x = 0
        y = 1
        while x != y and Rando == True:
            x = random.randint(0,5)
            y = random.randint(0,5)
            if x == y:
                xy2 = ('%s equals %s, all done.' % (x,y))
                await client.send_message(message.channel, xy2)
            else:
                xy = ('%s does not equal %s' % (x,y))
                await client.send_message(message.channel, xy)
        # end that random thing with:
    elif message.content.startswith("!stop"):
        Rando = False
                
    elif message.content.startswith('!loot'):
        swords = ['Knife', 'Dagger', 'Sword', 'Scimitar', 'Claymore']
        sword = swords[random.randint(0,4)]        
        prefix = ['Godly', 'Silver', 'Steel', 'Rusty', 'Demonic']
        pre = prefix[random.randint(0,4)]        
        suffix = ['Flames', 'Dousing', 'Icebite', 'Lightning', 'Slaying']
        ix = suffix [random.randint(0,4)]        
        await client.send_message(message.channel, "You found a %s %s of %s!" % (pre, sword, ix))

    elif message.content.startswith('ping'):
        for user in message.mentions:
            msg = 'PONG {}'.format(user.mention)
            await client.send_message(message.channel, msg)
        
    elif message.content.startswith('!spellbook'):
        await client.send_message(message.channel, "`--fireball --iceshard --leafwhip`")
        await client.send_message(message.channel, "`--lightray --darkbullet --rockthrow`")

#spells here:

    elif message.content.startswith('--@fireball'):
                # using 'try' if !fireball someone
        for user in message.mentions:
            msg = 'You cast fireball at {}!'.format(user.mention)
            await client.send_message(message.channel, msg)
            roll = random.randint (1, 4)
            if roll == 1:
                msg = "{0.author.mention}\'s fireball explodes in their face!".format(message)
            elif roll == 2:
                msg = "{0.author.mention}\'s fireball is awkwardly small, it disappears instantly...".format(message)
            elif roll == 3:
                msg = "{0.author.mention}\'s fireball hits their target for %s damage!".format(message) % random.randint(1,10)
            elif roll == 4:
                msg = "Critical! {0.author.mention}\'s fireball hits their target for %s damage!".format(message) % random.randint(2,20)
            await client.send_message(message.channel, msg)
                        # except if nothing written after !fireball
                        
    elif message.content.startswith('--fireball'):
        msg = '{0.author.mention} casts fireball!'.format(message)
        await client.send_message(message.channel, msg)
        roll = random.randint (1, 4)
        if roll == 1:
            msg = "{0.author.mention}\'s fireball explodes in their face!".format(message)
        elif roll == 2:
            msg = "{0.author.mention}\'s fireball is awkwardly small, it disappears instantly...".format(message)
        elif roll == 3:
            msg = "{0.author.mention}\'s fireball hits their target for %s damage!".format(message) % random.randint(1,10)
        elif roll == 4:
            msg = "Critical! {0.author.mention}\'s fireball hits their target for %s damage!".format(message) % random.randint(2,20)
        await client.send_message(message.channel, msg)
# Ice D8,Leaf D6,light and dark D10,rock D4
    elif message.content.startswith('--@iceshard'):
                # using 'try' if !fireball someone
        for user in message.mentions:
            msg = 'You cast iceshard at {}!'.format(user.mention)
            await client.send_message(message.channel, msg)
            roll = random.randint (1, 8)
            if roll == 1:
                msg = "{0.author.mention}\'s iceshard explodes in their face!".format(message)
            elif roll == 2:
                msg = "{0.author.mention}\'s iceshard is awkwardly small, it disappears instantly...".format(message)
            elif roll == 3:
                msg = "{0.author.mention}\'s iceshard hits their target for %s damage!".format(message) % random.randint(1,10)
            elif roll == 4:
                msg = "Critical! {0.author.mention}\'s iceshard hits their target for %s damage!".format(message) % random.randint(2,20)
            elif roll == 5:
                msg = "Critical! {0.author.mention}\'s iceshard hits their target for %s damage!".format(message) % random.randint(2,20)
            elif roll == 6:
                msg = "Critical! {0.author.mention}\'s iceshard hits their target for %s damage!".format(message) % random.randint(4,20)
            elif roll == 7:
                msg = "Critical! {0.author.mention}\'s iceshard hits their target for %s damage!".format(message) % random.randint(6,20)
            elif roll == 8:
                msg = "Critical! {0.author.mention}\'s iceshard hits their target for %s damage! You froze them solid!".format(message) % random.randint(10,20)
            await client.send_message(message.channel, msg)

                        
    elif message.content.startswith('--iceshard'):
        msg = '{0.author.mention} casts iceshard!'.format(message)
        await client.send_message(message.channel, msg)
        roll = random.randint (1, 8)
        if roll == 1:
            msg = "{0.author.mention}\'s iceshard explodes in their face!".format(message)
        elif roll == 2:
            msg = "{0.author.mention}\'s iceshard is awkwardly small, it disappears instantly...".format(message)
        elif roll == 3:
            msg = "{0.author.mention}\'s iceshard hits their target for %s damage!".format(message) % random.randint(1,10)
        elif roll == 4:
            msg = "{0.author.mention}\'s iceshard hits their target for %s damage!".format(message) % random.randint(2,16)
        elif roll == 5:
            msg = "{0.author.mention}\'s iceshard hits their target for %s damage!".format(message) % random.randint(2,16)
        elif roll == 6:
            msg = "{0.author.mention}\'s iceshard hits their target for %s damage!".format(message) % random.randint(4,16)
        elif roll == 7:
            msg = "Critical! {0.author.mention}\'s iceshard hits their target for %s damage!".format(message) % random.randint(6,16)
        elif roll == 8:
            msg = "Critical! {0.author.mention}\'s iceshard hits their target for %s damage! You froze them solid!".format(message) % random.randint(10,16)
        await client.send_message(message.channel, msg)

    elif message.content.startswith('--@leafwhip'):
                # using 'try' if !fireball someone
        for user in message.mentions:
            msg = 'You cast leafwhip at {}!'.format(user.mention)
            await client.send_message(message.channel, msg)
            roll = random.randint (1, 6)
            if roll == 1:
                msg = "{0.author.mention}\'s leafwhip causes them to trip and fall flat on their face!".format(message)
            elif roll == 2:
                msg = "{0.author.mention}\'s leafwhip is is more like a leaf tickle than anything...".format(message)
            elif roll == 3:
                msg = "{0.author.mention}\'s leafwhip hits their target for %s damage!".format(message) % random.randint(1,10)
            elif roll == 4:
                msg = "{0.author.mention}\'s leafwhip hits their target for %s damage!".format(message) % random.randint(4,20)
            elif roll == 5:
                msg = "Critical! {0.author.mention}\'s leafwhip hits their target for %s damage!".format(message) % random.randint(6,20)
            elif roll == 6:
                msg = "Critical! {0.author.mention}\'s leafwhip hits their target for %s damage!".format(message) % random.randint(8,20)                
            await client.send_message(message.channel, msg)
                        
    elif message.content.startswith('--leafwhip'):
        msg = '{0.author.mention} casts leafwhip!'.format(message)
        await client.send_message(message.channel, msg)
        roll = random.randint (1, 6)
        if roll == 1:
            msg = "{0.author.mention}\'s leafwhip causes them to trip and fall flat on their face!".format(message)
        elif roll == 2:
            msg = "{0.author.mention}\'s leafwhip is is more like a leaf tickle than anything...".format(message)
        elif roll == 3:
            msg = "{0.author.mention}\'s leafwhip hits their target for %s damage!".format(message) % random.randint(1,10)
        elif roll == 4:
            msg = "{0.author.mention}\'s leafwhip hits their target for %s damage!".format(message) % random.randint(4,20)
        elif roll == 5:
            msg = "Critical! {0.author.mention}\'s leafwhip hits their target for %s damage!".format(message) % random.randint(6,20)
        elif roll == 6:
            msg = "Critical! {0.author.mention}\'s leafwhip hits their target for %s damage!".format(message) % random.randint(8,20)     
        await client.send_message(message.channel, msg)
    
    elif message.content.startswith('--@lightray'):
                # using 'try' if !fireball someone
        for user in message.mentions:
            msg = 'You cast lightray at {}!'.format(user.mention)
            await client.send_message(message.channel, msg)
            roll = random.randint (1, 10)
            if roll == 1:
                msg = "{0.author.mention}\'s lightray sparkles briefly.".format(message)
            elif roll == 2:
                msg = "{0.author.mention}\'s lightray makes a small flash and vanishes.".format(message)
            elif roll == 3:
                msg = "{0.author.mention}\'s lightray hits their target for %s damage!".format(message) % random.randint(1,10)
            elif roll == 4:
                msg = "{0.author.mention}\'s lightray hits their target for %s damage!".format(message) % random.randint(2,10)
            elif roll == 5:
                msg = "{0.author.mention}\'s lightray hits their target for %s damage!".format(message) % random.randint(2,12)
            elif roll == 6:
                msg = "{0.author.mention}\'s lightray hits their target for %s damage!".format(message) % random.randint(2,15)
            elif roll == 7:
                msg = "{0.author.mention}\'s lightray hits their target for %s damage!".format(message) % random.randint(2,18)
            elif roll == 8:
                msg = "Critical! {0.author.mention}\'s lightray hits their target for %s damage!".format(message) % random.randint(4,20)
            elif roll == 9:
                msg = "Critical! {0.author.mention}\'s lightray hits their target for %s damage!".format(message) % random.randint(6,20)
            elif roll == 10:
                msg = "Critical! {0.author.mention}\'s lightray hits their target for %s damage!".format(message) % random.randint(8,20)





                
            await client.send_message(message.channel, msg)
                        # except if nothing written after !fireball
                        
    elif message.content.startswith('--lightray'):
        msg = '{0.author.mention} casts lightray!'.format(message)
        await client.send_message(message.channel, msg)
        roll = random.randint (1, 10)
        if roll == 1:
            msg = "{0.author.mention}\'s lightray sparkles briefly.".format(message)
        elif roll == 2:
            msg = "{0.author.mention}\'s lightray makes a small flash and vanishes.".format(message)
        elif roll == 3:
            msg = "{0.author.mention}\'s lightray hits their target for %s damage!".format(message) % random.randint(1,10)
        elif roll == 4:
            msg = "{0.author.mention}\'s lightray hits their target for %s damage!".format(message) % random.randint(2,10)
        elif roll == 5:
            msg = "{0.author.mention}\'s lightray hits their target for %s damage!".format(message) % random.randint(2,12)
        elif roll == 6:
            msg = "{0.author.mention}\'s lightray hits their target for %s damage!".format(message) % random.randint(2,15)
        elif roll == 7:
            msg = "{0.author.mention}\'s lightray hits their target for %s damage!".format(message) % random.randint(2,18)
        elif roll == 8:
            msg = "Critical! {0.author.mention}\'s lightray hits their target for %s damage!".format(message) % random.randint(4,20)
        elif roll == 9:
            msg = "Critical! {0.author.mention}\'s lightray hits their target for %s damage!".format(message) % random.randint(6,20)
        elif roll == 10:
            msg = "Critical! {0.author.mention}\'s lightray hits their target for %s damage!".format(message) % random.randint(8,20)
        await client.send_message(message.channel, msg)

    elif message.content.startswith('--@darkbullet'):
                # using 'try' if !fireball someone
        for user in message.mentions:
            msg = 'You cast darkbullet at {}!'.format(user.mention)
            await client.send_message(message.channel, msg)
            roll = random.randint (1, 10)
            if roll == 1:
                msg = "{0.author.mention}\'s darkbullet sparkles briefly.".format(message)
            elif roll == 2:
                msg = "{0.author.mention}\'s darkbullet makes a small flash and vanishes.".format(message)
            elif roll == 3:
                msg = "{0.author.mention}\'s darkbullet hits their target for %s damage!".format(message) % random.randint(1,10)
            elif roll == 4:
                msg = "{0.author.mention}\'s darkbullet hits their target for %s damage!".format(message) % random.randint(2,10)
            elif roll == 5:
                msg = "{0.author.mention}\'s darkbullet hits their target for %s damage!".format(message) % random.randint(2,12)
            elif roll == 6:
                msg = "{0.author.mention}\'s darkbullet hits their target for %s damage!".format(message) % random.randint(2,15)
            elif roll == 7:
                msg = "{0.author.mention}\'s darkbullet hits their target for %s damage!".format(message) % random.randint(2,18)
            elif roll == 8:
                msg = "Critical! {0.author.mention}\'s darkbullet hits their target for %s damage!".format(message) % random.randint(4,20)
            elif roll == 9:
                msg = "Critical! {0.author.mention}\'s darkbullet hits their target for %s damage!".format(message) % random.randint(6,20)
            elif roll == 10:
                msg = "Critical! {0.author.mention}\'s darkbullet hits their target for %s damage!".format(message) % random.randint(8,20)





                
            await client.send_message(message.channel, msg)
                        # except if nothing written after !fireball
                        
    elif message.content.startswith('--darkbullet'):
        msg = '{0.author.mention} casts darkbullet!'.format(message)
        await client.send_message(message.channel, msg)
        roll = random.randint (1, 10)
        if roll == 1:
            msg = "{0.author.mention}\'s darkbullet sparkles briefly.".format(message)
        elif roll == 2:
            msg = "{0.author.mention}\'s darkbullet makes a small flash and vanishes.".format(message)
        elif roll == 3:
            msg = "{0.author.mention}\'s darkbullet hits their target for %s damage!".format(message) % random.randint(1,10)
        elif roll == 4:
            msg = "{0.author.mention}\'s darkbullet hits their target for %s damage!".format(message) % random.randint(2,10)
        elif roll == 5:
            msg = "{0.author.mention}\'s darkbullet hits their target for %s damage!".format(message) % random.randint(2,12)
        elif roll == 6:
            msg = "{0.author.mention}\'s darkbullet hits their target for %s damage!".format(message) % random.randint(2,15)
        elif roll == 7:
            msg = "{0.author.mention}\'s darkbullet hits their target for %s damage!".format(message) % random.randint(2,18)
        elif roll == 8:
            msg = "Critical! {0.author.mention}\'s darkbullet hits their target for %s damage!".format(message) % random.randint(4,20)
        elif roll == 9:
            msg = "Critical! {0.author.mention}\'s darkbullet hits their target for %s damage!".format(message) % random.randint(6,20)
        elif roll == 10:
            msg = "Critical! {0.author.mention}\'s darkbullet hits their target for %s damage!".format(message) % random.randint(8,20)
        await client.send_message(message.channel, msg)


    elif message.content.startswith('--@rockthrow'):
                # using 'try' if !fireball someone
        for user in message.mentions:
            msg = 'You cast rockthrow at {}!'.format(user.mention)
            await client.send_message(message.channel, msg)
            roll = random.randint (1, 4)
            if roll == 1:
                msg = "{0.author.mention}\'s rockthrow breaks into several small pebbles and skitters across the floor harmlessly...".format(message)
            elif roll == 2:
                msg = "{0.author.mention}\'s rockthrow is awkwardly small and crumbles into dust...".format(message)
            elif roll == 3:
                msg = "{0.author.mention}\'s rockthrow hits their target for %s damage!".format(message) % random.randint(1,10)
            elif roll == 4:
                msg = "Critical! {0.author.mention}\'s rockthrow hits their target for %s damage!".format(message) % random.randint(2,20)
                await client.send_message(message.channel, msg)
                        # except if nothing written after !fireball
                        
    elif message.content.startswith('--rockthrow'):
        msg = '{0.author.mention} casts rockthrow!'.format(message)
        await client.send_message(message.channel, msg)
        roll = random.randint (1, 4)
        if roll == 1:
            msg = "{0.author.mention}\'s rockthrow breaks into several small pebbles and skitters across the floor harmlessly...".format(message)
        elif roll == 2:
            msg = "{0.author.mention}\'s rockthrow is awkwardly small and crumbles into dust...".format(message)
        elif roll == 3:
            msg = "{0.author.mention}\'s rockthrow hits their target for %s damage!".format(message) % random.randint(1,10)
        elif roll == 4:
            msg = "Critical! {0.author.mention}\'s rockthrow hits their target for %s damage!".format(message) % random.randint(2,20)
        await client.send_message(message.channel, msg)

    elif message.content.startswith('!tableflip'):
        await client.send_message(message.channel, "(╯°□°）╯︵ ┻━┻") 
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(' ')
