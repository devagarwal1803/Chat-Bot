from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import os


bot=ChatBot('My Bot',preprocessors=[
        'chatterbot.preprocessors.clean_whitespace'
    ])
#bot.set_trainer(ListTrainer)
trainer = ChatterBotCorpusTrainer(bot)
trainer.train(
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations"
)

trainer = ListTrainer(bot)
'''for files in os.listdir('C:/Users/Hacker/Desktop/Chatbot/chatterbot-corpus-master/chatterbot_corpus/data/english/'):
	data=open('C:/Users/Hacker/Desktop/Chatbot/chatterbot-corpus-master/chatterbot_corpus/data/english/'+files,'r').readlines()
	trainer.train(data)
'''
while True:
	message=input('You:')
	if message.strip()!='Bye' or message.strip()=='bye':
		reply=bot.get_response(message)
		print('Chatbot: ',reply)
	if message.strip()=='Bye' or message.strip()=='bye':
		printf('Bye')
		break
