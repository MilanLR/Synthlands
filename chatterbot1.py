from chatterbot import ChatBot
from chatterbot.response_selection import get_random_response
import datetime
import random
import praw

reddit = praw.Reddit(client_id=' ',
                     client_secret=' ',
                     user_agent=' ',
                     username=' ',
                     password=' ')
if reddit.read_only == True:
    print ('Reddit Read-Only Mode Active')
else:
    print ('Reddit Read-Write Mode Active')

chatbot = ChatBot(
    'Scottie',
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
#Train based on the english corpus
chatbot.train("chatterbot.corpus.english")
# Train custom data
chatbot.train('data.my_corpus.dicerolls')
# chatbot.train('data.my_corpus.exp')
# Get a response to an input statement
# Export current training data

def CHAT():
    subreply = None
    CHAT = True    
    while CHAT == True:        
        talk_to = input('chat: ')
        to_str = str(talk_to)        
        if talk_to == ('bye'):
            CHAT = False
            print ('Exiting conversation.')
            quit()
        if talk_to == ('reddit'):
            do_what = input('What about it? ')
            if do_what == ('upload banner'):
                sub_reddit = reddit.subreddit('fived')
                sub_reddit.stylesheet.upload('eyes', 'eyes.jpg')
            elif do_what == ('read sub'):
                subx = input('Which one? ')
                tointhowx = input('How many? ')
                howx = int(tointhowx)
                for submission in reddit.subreddit(subx).hot(limit=howx):
                    subreply = submission.title
                    print(subreply)
                    line = subreply
                    for char in "()":
                        line = line.replace(char,' ')                    
                    response = chatbot.get_response(line)
                    print(response)
        elif talk_to ==('What time is it?'):
            datetime.datetime.time(datetime.datetime.now())
            print('The current time is:', datetime.datetime.time(datetime.datetime.now()))            
        else:            
            reply = chatbot.get_response(to_str)            
            if reply == 'D4' or reply =='d4':
                print ('Scottie rolls a', random.randint(1, 4))
            elif reply == 'D6' or reply =='d6':
                print ('Scottie rolls a', random.randint(1, 6))
            elif reply == 'D8' or reply =='d8':
                print ('Scottie rolls a', random.randint(1, 8))
            else:
                print (reply)




# START THE PROGRAM                        
CHAT()     
        

