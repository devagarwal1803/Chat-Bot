from tkinter import *
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import os
global bot

def reply():
    message=str(you.get())
    #print(bot)
    if message.strip()!='Bye' or message.strip()=='bye':
        reply=str(bot.get_response(message))
        bot2=Label(text=reply,width=50,justify=LEFT,compound = LEFT,padx = 10)
        bot2.place(x=60,y=100)
        bot2.update()
        #print('Chatbot: ',reply)
    if message.strip()=='Bye' or message.strip()=='bye':
        print('Bye')
        exit
    #you_entry.delete(0,END)

bot=ChatBot('My Bot')
trainer = ChatterBotCorpusTrainer(bot)

'''trainer.train(
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations"
)'''

trainer = ListTrainer(bot)
for files in os.listdir('C:/Users/Hacker/Desktop/Chatbot/chatterbot/chatterbot_corpus/data/english/'):
	data=open('C:/Users/Hacker/Desktop/Chatbot/chatterbot/chatterbot_corpus/data/english/'+files,'r').readlines()
	trainer.train(data)

root=Tk()
root.geometry('500x200')
root.title("Talk2Me")
you_text=Label(text="You:",)
you_text.place(x=15 , y = 70)
you=StringVar()
you_entry=Entry(textvariable=you , width="70")
you_entry.place(x=60,y=70)
bot_text=Label(text="Bot:",)
bot_text.place(x=15 , y = 100)
#bot1=Text(root,width="53",height="2")
#bot1.place(x=60,y=100)
btn = Button(root, text ='Reply' ,width="15",height="1",command=lambda:reply())
btn.place(x=200,y=150)
root.mainloop()
