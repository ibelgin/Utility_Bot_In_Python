import tkinter as tk
import sys, os

import modules.generalfun
from modules.news import get_news
from modules.weather import weather
from modules.responces import welcome,jokes
from modules.text_converter import main_speak 
import webbrowser
import random

root = tk.Tk()
generate_random = lambda x : random.randint(0,x)
sys.path.append(os.path.abspath(os.path.join('..', 'config')))

def copy_to_clipboard(str):
    root.clipboard_clear()
    root.clipboard_append(str)
    root.update()
def Bot_Responce(User_Input):
    
    # Starting The Bot

    if (User_Input.lower() in welcome["BotStart"]):
        BotResponce = welcome["Hi"][generate_random(len(welcome["Hi"])-1)]
        text.insert(tk.END,"\n"+"Bot : "+BotResponce)
        main_speak(BotResponce)

    # Clear The Screen

    elif (User_Input.lower() == "clear"):
        text.delete('1.0', tk.END)

    # Printing The News

    elif (User_Input.lower() in welcome["News"]):
        responce =get_news(5)
        if (responce == -1):
            text.insert(tk.END,"\n"+"Bot : "+"Please Check Your Internet Connection")
            text.insert(tk.END,"\n")
        else:
            text.insert(tk.END,"\n"+"\n Here Are The Top 5 News Headline's \n")
            for i in responce:
                text.insert(tk.END,"\n"+"-> "+i+"\n")

    # Generate a Random Joke

    elif (User_Input.lower() in welcome["Jokes"]):
        no = generate_random(len(jokes)-1)
        text.insert(tk.END,"\n"+"\n {} \n".format(jokes[no]))

    # Make The Bot Speak Somthing 

    elif( "speak" in User_Input.lower().split(" ")):
        temp = User_Input[6:]
        main_speak(temp)

    # Open The Web Browser With A Link

    elif( "open" in User_Input.lower().split(" ")):
        temp = User_Input[5:]
        webbrowser.open(temp,new=1)
        text.insert(tk.END,"\n"+"Bot : "+"Opened "+temp)
        text.insert(tk.END,"\n")

    # Find Weather of A City 

    elif ( "weather in" == User_Input.lower()[0:10]):
        temp = User_Input[10:]
        responce = weather(temp)
        if (responce == -1):
            text.insert(tk.END,"\n"+"Bot : Enter A Valid City Name or Check Your Internet Connection"+"\n")
        elif (responce == 1):
            text.insert(tk.END,"\n"+"Please Check Your Internet Connection"+"\n")
        else:
            for i in responce.values():
                text.insert(tk.END,"\n"+i)
            text.insert(tk.END,"\n")
    
    # Open Google With A Search Keyword

    elif ( "search for" == User_Input.lower()[0:10]):
        webbrowser.open("https://www.google.com/search?q="+User_Input[10:])
        text.insert(tk.END,"\n"+"Opened Google With The Search Query - "+User_Input[10:]+"\n")

    elif ("password" in User_Input.lower()):
        for i in User_Input.split(' '):
            if (i.isdigit()):
                responce = modules.generalfun.passwordGenerator(i)
                text.insert(tk.END,"\n"+"Password Saved To Clipboard - "+responce+"\n")
                copy_to_clipboard(str(responce))
                break
            else:
                continue 
        else:
            responce = modules.generalfun.passwordGenerator(8)
            text.insert(tk.END,"\n"+"Password Saved To Clipboard - "+responce+"\n")
            copy_to_clipboard(responce)
        text.insert(tk.END,"\n"+"")
    
    elif ("ipaddress" in User_Input.lower()):
        temp = User_Input.split(' ')
        result = modules.generalfun.ip_address(temp[1])
        print(result)
        text.insert(tk.END,"\n"+result+"\n")
            
def send():
    text.config(state='normal')
    text.insert(tk.END,"\n"+"You : "+e.get())
    text.insert(tk.END,"\n")
    Bot_Responce(e.get())
    text.config(state='disabled')

text =tk.Text(root,bg="#FFF",width=50)
text.grid(row=0,column=0,columnspan=2)
e=tk.Entry(root,width=50)
send=tk.Button(root,text="Send",bg="#FFF",width=15,command=send).grid(row=1,column=1)
e.grid(row=1,column=0)
root.title("Utility Bot")
tk.mainloop()
