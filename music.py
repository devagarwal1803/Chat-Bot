#-*- coding: utf-8 -*-
import os
import Splash
import random
from tkinter import *
import Instruction
import pygame
import tkinter.messagebox
import tkinter, tkinter.constants, tkinter.filedialog
import sqlite3
root=Tk()
root.title("Login Page")
root.minsize(400,150)
index=0
count=0
v1=IntVar()
listofsongs=[]
happysongs=[]
#=========================================================================================================================================================================================================================================

#===========================================================================================================================================================================================================================================
def type():
    root.destroy()
    if(v1.get()==1):
        rt=Tk()
        rt.title("Music Player")
        rt.configure(background="black")
        d=PhotoImage(file='musiceq.gif')
        Label(rt,image=d).grid(row=1,column=0,columnspan=6)
        def open():
            #directory = tkFileDialog.askdirectory()
            
            directory=("N:\Python Project\Happysongs") 
            os.chdir(directory)
            global count
            for files in os.listdir(directory):
                if files.endswith (".mp3"):
                
                    happysongs.append(files)
                    count+=1
                else:
                    tkinter.messagebox.showerror('Error','Songs Not Found')
            def playlist():
                rtp=Tk()
                rtp.title("Playlist")
                rtp.minsize(200,50)
                listbox=Listbox(rtp,width=40)
                listbox.grid(row=4,column=2,columnspan=2)
                happysongs.reverse()
                for items in happysongs:
                    listbox.insert(0,items)
                happysongs.reverse()
                rtp.mainloop()
                
            Button(rt,text="Playlist",font = 'times 20 bold italic',bd=5,fg='white',bg='black',height=2,width=11,command=playlist).grid(row=3,column=2,columnspan=2)
             
        def play():
            global index
        #global count
            pygame.mixer.init()
            pygame.mixer.music.load(happysongs[0])
            pygame.mixer.music.play()
            '''index=index+1
            pygame.mixer.music.queue(happysongs[index])
            pygame.mixer.music.play() '''  
    #for index in range (0,count):  
         #   pygame.mixer.music.load(listofsongs[index])
          #  pygame.mixer.music.play()
    
        def pause():
            pygame.mixer.music.pause()
        def unpause():
            pygame.mixer.music.unpause()
        def stop():
            pygame.mixer.music.fadeout(1300)
        #pygame.mixer.music.stop()
        def previous():
            global index
            index-=1
            pygame.mixer.music.load(happysongs[index ])
            pygame.mixer.music.play()    
        def next():
            global index
            global count
            index += 1

            index=index%(count)
            
            pygame.mixer.music.load(happysongs[index])
            pygame.mixer.music.play()
        def mute():
            pygame.mixer.music.set_volume(0)
        def vol():
            pygame.mixer.music.set_volume(10)
        def repeat():
            pygame.mixer.music.play(500)
        def suffle():
            global index
            global count
            index = random.randint(0,count)
            pygame.mixer.init()
            pygame.mixer.music.load(happysongs[index])
            pygame.mixer.music.play()
        rt.configure(background="black")
        Button(rt,width=20,bd=5,font='times 20 bold italic',text='MP3 PLAYER',command=open,fg='white',bg='black').grid(row=0,column=0,columnspan=6)
        Button(rt,text="►",height=2,width=5,bd=5,font = 'times 20 bold',command=play,fg='white',bg='black').grid(row=2,column=0)
        Button(rt,text="||",height=2,width=5,bd=5,font = 'times 20 bold',command=pause,fg='white',bg='black').grid(row=2,column=1)
        Button(rt,text="►/||",height=2,width=5,bd=5,font = 'times 20 bold',command=unpause,fg='white',bg='black').grid(row=2,column=2)
        Button(rt,text="◄◄",height=2,width=5,bd=5,font = 'times 20 bold',command=previous,fg='white',bg='black').grid(row=2,column=3)
        Button(rt,text="■",height=2,width=5,bd=5,font = 'times 20 bold',command=stop,fg='white',bg='black').grid(row=2,column=4)
        Button(rt,text="►►",height=2,width=5,bd=5,font = 'times 20 bold',command=next,fg='white',bg='black').grid(row=2,column=5)
        Button(rt,text="\U0001F507",height=2,width=5,bd=5,font='times 20 bold',command=mute,fg='white',bg='black').grid(row=3,column=0)
        Button(rt,text="\U0001F50A",height=2,width=5,bd=5,font='times 20 bold',command=vol,fg='white',bg='black').grid(row=3,column=5)
        Button(rt,text="\U0001F500",height=2,width=5,bd=5,font='times 20 bold',command=suffle,fg='white',bg='black').grid(row=3,column=1)
        Button(rt,text="\U0001F501",height=2,width=5,bd=5,font='times 20 bold',command=repeat,fg='white',bg='black').grid(row=3,column=4)
        rt.mainloop()    
#===========================================================================================================================================================================================================================================
    if(v1.get()==2):
        st=Tk()
        st.title("Music Player")
        st.configure(background="black")
        d=PhotoImage(file='musiceq.gif')
        Label(st,image=d).grid(row=1,column=0,columnspan=6)
        def open():
            #directory = tkFileDialog.askdirectory()
            #os.chdir(directory)
            directory=("N:\Python Project\Sadsongs")
            os.chdir(directory)
            global count
            for files in os.listdir(directory):
                if files.endswith (".mp3"):
                
                    happysongs.append(files)
                    count+=1
                else:
                    tkinter.messagebox.showerror('Error','Songs Not Found')
            def playlist():
                stp=Tk()
                stp.title("Playlist")
                stp.minsize(200,50)
                listbox=Listbox(stp,width=40)
                listbox.grid(row=4,column=2,columnspan=2)
                happysongs.reverse()
                for items in happysongs:
                    listbox.insert(0,items)
                happysongs.reverse()
                stp.mainloop()
                
            Button(st,text="Playlist",font = 'times 20 bold italic',bd=5,fg='white',bg='black',height=2,width=11,command=playlist).grid(row=3,column=2,columnspan=2)
             
        def play():
            global index
        #global count
            pygame.mixer.init()
            pygame.mixer.music.load(happysongs[0])
            pygame.mixer.music.play()
            '''index=index+1
            pygame.mixer.music.queue(happysongs[index])
            pygame.mixer.music.play()'''   
    #for index in range (0,count):  
         #   pygame.mixer.music.load(listofsongs[index])
          #  pygame.mixer.music.play()
    
        def pause():
            pygame.mixer.music.pause()
        def unpause():
            pygame.mixer.music.unpause()
        def stop():
            pygame.mixer.music.fadeout(1300)
        #pygame.mixer.music.stop()
        def previous():
            global index
            index-=1
            pygame.mixer.music.load(happysongs[index ])
            pygame.mixer.music.play()    
        def next():
            global index
            global count
            index += 1

            index=index%(count)
            
            pygame.mixer.music.load(happysongs[index])
            pygame.mixer.music.play()
        def mute():
            pygame.mixer.music.set_volume(0)
        def vol():
            pygame.mixer.music.set_volume(10)
        def repeat():
            pygame.mixer.music.play(500)
        def suffle():
            global index
            global count
            index = random.randint(0,count)
            pygame.mixer.init()
            pygame.mixer.music.load(happysongs[index])
            pygame.mixer.music.play()
        st.configure(background="black")
        Button(st,width=20,bd=5,font='times 20 bold italic',text='MP3 PLAYER',command=open,fg='white',bg='black').grid(row=0,column=0,columnspan=6)
        Button(st,text="►",height=2,width=5,bd=5,font = 'times 20 bold',command=play,fg='white',bg='black').grid(row=2,column=0)
        Button(st,text="||",height=2,width=5,bd=5,font = 'times 20 bold',command=pause,fg='white',bg='black').grid(row=2,column=1)
        Button(st,text="►/||",height=2,width=5,bd=5,font = 'times 20 bold',command=unpause,fg='white',bg='black').grid(row=2,column=2)
        Button(st,text="◄◄",height=2,width=5,bd=5,font = 'times 20 bold',command=previous,fg='white',bg='black').grid(row=2,column=3)
        Button(st,text="■",height=2,width=5,bd=5,font = 'times 20 bold',command=stop,fg='white',bg='black').grid(row=2,column=4)
        Button(st,text="►►",height=2,width=5,bd=5,font = 'times 20 bold',command=next,fg='white',bg='black').grid(row=2,column=5)
        Button(st,text="\U0001F507",height=2,width=5,bd=5,font='times 20 bold',command=mute,fg='white',bg='black').grid(row=3,column=0)
        Button(st,text="\U0001F50A",height=2,width=5,bd=5,font='times 20 bold',command=vol,fg='white',bg='black').grid(row=3,column=5)
        Button(st,text="\U0001F500",height=2,width=5,bd=5,font='times 20 bold',command=suffle,fg='white',bg='black').grid(row=3,column=1)
        Button(st,text="\U0001F501",height=2,width=5,bd=5,font='times 20 bold',command=repeat,fg='white',bg='black').grid(row=3,column=4)
        st.mainloop()        
#===========================================================================================================================================================================================================================================
    if(v1.get()==3):
        lt=Tk()
        lt.title("Music Player")
        lt.configure(background="black")
        d=PhotoImage(file='musiceq.gif')
        Label(lt,image=d).grid(row=1,column=0,columnspan=6)
        def open():
            #directory = tkFileDialog.askdirectory()
            #os.chdir(directory)
            directory=("N:\Python Project\Lovesongs")
            os.chdir(directory)
            global count
            for files in os.listdir(directory):
                if files.endswith (".mp3"):
                
                    happysongs.append(files)
                    count+=1
                else:
                    tkinter.messagebox.showerror('Error','Songs Not Found')
            def playlist():
                ltp=Tk()
                ltp.title("Playlilt")
                ltp.minsize(200,50)
                listbox=Listbox(ltp,width=40)
                listbox.grid(row=4,column=2,columnspan=2)
                happysongs.reverse()
                for items in happysongs:
                    listbox.insert(0,items)
                happysongs.reverse()
                ltp.mainloop()
                
            Button(lt,text="Playlist",font = 'times 20 bold italic',bd=5,fg='white',bg='black',height=2,width=11,command=playlist).grid(row=3,column=2,columnspan=2)
             
        def play():
            global index
        #global count
            pygame.mixer.init()
            pygame.mixer.music.load(happysongs[0])
            pygame.mixer.music.play()
            '''index=index+1
            pygame.mixer.music.queue(happysongs[index])
            pygame.mixer.music.play()'''   
    #for index in range (0,count):  
         #   pygame.mixer.music.load(listofsongs[index])
          #  pygame.mixer.music.play()
    
        def pause():
            pygame.mixer.music.pause()
        def unpause():
            pygame.mixer.music.unpause()
        def stop():
            pygame.mixer.music.fadeout(1300)
        #pygame.mixer.music.stop()
        def previous():
            global index
            index-=1
            pygame.mixer.music.load(happysongs[index ])
            pygame.mixer.music.play()    
        def next():
            global index
            global count
            index += 1

            index=index%(count)
            
            pygame.mixer.music.load(happysongs[index])
            pygame.mixer.music.play()
        def mute():
            pygame.mixer.music.set_volume(0)
        def vol():
            pygame.mixer.music.set_volume(10)
        def repeat():
            pygame.mixer.music.play(500)
        def suffle():
            global index
            global count
            index = random.randint(0,count)
            pygame.mixer.init()
            pygame.mixer.music.load(happysongs[index])
            pygame.mixer.music.play()
        lt.configure(background="black")
        Button(lt,width=20,bd=5,font='times 20 bold italic',text='MP3 PLAYER',command=open,fg='white',bg='black').grid(row=0,column=0,columnspan=6)
        Button(lt,text="►",height=2,width=5,bd=5,font = 'times 20 bold',command=play,fg='white',bg='black').grid(row=2,column=0)
        Button(lt,text="||",height=2,width=5,bd=5,font = 'times 20 bold',command=pause,fg='white',bg='black').grid(row=2,column=1)
        Button(lt,text="►/||",height=2,width=5,bd=5,font = 'times 20 bold',command=unpause,fg='white',bg='black').grid(row=2,column=2)
        Button(lt,text="◄◄",height=2,width=5,bd=5,font = 'times 20 bold',command=previous,fg='white',bg='black').grid(row=2,column=3)
        Button(lt,text="■",height=2,width=5,bd=5,font = 'times 20 bold',command=stop,fg='white',bg='black').grid(row=2,column=4)
        Button(lt,text="►►",height=2,width=5,bd=5,font = 'times 20 bold',command=next,fg='white',bg='black').grid(row=2,column=5)
        Button(lt,text="\U0001F507",height=2,width=5,bd=5,font='times 20 bold',command=mute,fg='white',bg='black').grid(row=3,column=0)
        Button(lt,text="\U0001F50A",height=2,width=5,bd=5,font='times 20 bold',command=vol,fg='white',bg='black').grid(row=3,column=5)
        Button(lt,text="\U0001F500",height=2,width=5,bd=5,font='times 20 bold',command=suffle,fg='white',bg='black').grid(row=3,column=1)
        Button(lt,text="\U0001F501",height=2,width=5,bd=5,font='times 20 bold',command=repeat,fg='white',bg='black').grid(row=3,column=4)
        lt.mainloop()
#===========================================================================================================================================================================================================================================
    if(v1.get()==4):
        edmt=Tk()
        edmt.title("Music Player")
        edmt.configure(background="black")
        d=PhotoImage(file='musiceq.gif')
        Label(edmt,image=d).grid(row=1,column=0,columnspan=6)
        def open():
            #directory = tkFileDialog.askdirectory()
            #os.chdir(directory)
            directory=("N:\Python Project\EDM")
            os.chdir(directory)
            global count
            for files in os.listdir(directory):
                if files.endswith (".mp3"):
                
                    happysongs.append(files)
                    count+=1
                else:
                    tkinter.messagebox.showerror('Error','Songs Not Found')
            def playlist():
                edmtp=Tk()
                edmtp.title("Playlist")
                edmtp.minsize(200,50)
                listbox=Listbox(edmtp,width=40)
                listbox.grid(row=4,column=2,columnspan=2)
                happysongs.reverse()
                for items in happysongs:
                    listbox.insert(0,items)
                happysongs.reverse()
                edmtp.mainloop()
                
            Button(edmt,text="Playlist",font = 'times 20 bold italic',bd=5,fg='white',bg='black',height=2,width=11,command=playlist).grid(row=3,column=2,columnspan=2)
             
        def play():
            global index
            index=0
        #global count
            pygame.mixer.init()
            pygame.mixer.music.load(happysongs[0])
            pygame.mixer.music.play()
            '''index+=1
            pygame.mixer.music.queue(happysongs[index])
            pygame.mixer.music.play()'''   
    #for index in range (0,count):  
         #   pygame.mixer.music.load(listofsongs[index])
          #  pygame.mixer.music.play()
    
        def pause():
            pygame.mixer.music.pause()
        def unpause():
            pygame.mixer.music.unpause()
        def stop():
            pygame.mixer.music.fadeout(1300)
        #pygame.mixer.music.stop()
        def previous():
            global index
            index-=1
            pygame.mixer.music.load(happysongs[index ])
            pygame.mixer.music.play()    
        def next():
            global index
            global count
            index += 1

            index=index%(count)
            
            pygame.mixer.music.load(happysongs[index])
            pygame.mixer.music.play()
        def mute():
            pygame.mixer.music.set_volume(0)
        def vol():
            pygame.mixer.music.set_volume(10)
        def repeat():
            pygame.mixer.music.play(500)
        def suffle():
            global index
            global count
            index = random.randint(0,count)
            pygame.mixer.init()
            pygame.mixer.music.load(happysongs[index])
            pygame.mixer.music.play()
        edmt.configure(background="black")
        Button(edmt,width=20,bd=5,font='times 20 bold italic',text='MP3 PLAYER',command=open,fg='white',bg='black').grid(row=0,column=0,columnspan=6)
        Button(edmt,text="►",height=2,width=5,bd=5,font = 'times 20 bold',command=play,fg='white',bg='black').grid(row=2,column=0)
        Button(edmt,text="||",height=2,width=5,bd=5,font = 'times 20 bold',command=pause,fg='white',bg='black').grid(row=2,column=1)
        Button(edmt,text="►/||",height=2,width=5,bd=5,font = 'times 20 bold',command=unpause,fg='white',bg='black').grid(row=2,column=2)
        Button(edmt,text="◄◄",height=2,width=5,bd=5,font = 'times 20 bold',command=previous,fg='white',bg='black').grid(row=2,column=3)
        Button(edmt,text="■",height=2,width=5,bd=5,font = 'times 20 bold',command=stop,fg='white',bg='black').grid(row=2,column=4)
        Button(edmt,text="►►",height=2,width=5,bd=5,font = 'times 20 bold',command=next,fg='white',bg='black').grid(row=2,column=5)
        Button(edmt,text="\U0001F507",height=2,width=5,bd=5,font='times 20 bold',command=mute,fg='white',bg='black').grid(row=3,column=0)
        Button(edmt,text="\U0001F50A",height=2,width=5,bd=5,font='times 20 bold',command=vol,fg='white',bg='black').grid(row=3,column=5)
        Button(edmt,text="\U0001F500",height=2,width=5,bd=5,font='times 20 bold',command=suffle,fg='white',bg='black').grid(row=3,column=1)
        Button(edmt,text="\U0001F501",height=2,width=5,bd=5,font='times 20 bold',command=repeat,fg='white',bg='black').grid(row=3,column=4)
        edmt.mainloop()
        
#===========================================================================================================================================================================================================================================
def login():
    if(str(y.get())=="1228" and str(z.get())=="Divyam"):
        tkinter.messagebox.showinfo("Success","Login Successful")
        
        type()
        
    else:
        tkinter.messagebox.showinfo("Failed","Try Again")

#===========================================================================================================================================================================================================================================
def fun():
    if(v1.get()==0):
       tkinter.messagebox.showinfo("Wrong Choice","Please Select type of Song and Login Again")
    else:
        login()

#===========================================================================================================================================================================================================================================

root.configure(background="black")
p=PhotoImage(file="music1.gif")
Label(root,image=p).grid(row=0,column=0,columnspan=4)
Label(root,text='Select Your Mood',font = 'times 15 bold italic',bd=5,fg='white',bg='black').grid(row=3,column=0,columnspan=4)
Radiobutton(root,text='HaPpY',font = 'times 15 bold italic',fg='Yellow',bg='black',variable=v1,value=1).grid(row=4,column=0)
Radiobutton(root,text='SaD',font = 'times 15 bold italic',fg='green',bg='black',variable=v1,value=2).grid(row=4,column=1)
Radiobutton(root,text='LoVe',font = 'times 15 bold italic',fg='red',bg='black',variable=v1,value=3).grid(row=4,column=2)
Radiobutton(root,text='EDM',font = 'times 15 bold italic',fg='blue',bg='black',variable=v1,value=4).grid(row=4,column=3)

Label(root,text="UserName",font = 'times 15 bold italic',fg='white',bg='black').grid(row=1,column=0)
z=Entry(root)
z.grid(row=1,column=1)
Label(root,text="Password",font = 'times 15 bold italic',fg='white',bg='black').grid(row=2,column=0)
y=Entry(root,show="*")
y.grid(row=2,column=1)
Button(root,text='Login',font = 'times 15 bold italic',fg='white',bg='black',bd=5,height=1,command=fun).grid(row=5,column=0,columnspan=4)




root.mainloop()
#===========================================================================================================================================================================================================================================
