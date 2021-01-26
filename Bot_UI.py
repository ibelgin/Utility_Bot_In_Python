import tkinter as tk
import sys, os
from modules.news import get_news
from modules.weather import weather
from modules.responces import welcome,jokes
from modules.text_converter import main_speak 
import webbrowser
import random

root = tk.Tk()
generate_random = lambda x : random.randint(0,x)
sys.path.append(os.path.abspath(os.path.join('..', 'config')))

def Bot_Responce(User_Input):
    if (User_Input.lower() in welcome["BotStart"]):
        BotResponce = welcome["Hi"][generate_random(len(welcome["Hi"])-1)]
        text.insert(tk.END,"\n"+"Bot : "+BotResponce)
        main_speak(BotResponce)
    elif (User_Input.lower() == "clear"):
        text.delete('1.0', tk.END)
    elif (User_Input.lower() in welcome["News"]):
        responce =get_news(5)
        if (responce == -1):
            text.insert(tk.END,"\n"+"Bot : "+"Please Check Your Internet Connection")
            text.insert(tk.END,"\n")
        else:
            text.insert(tk.END,"\n"+"\n Here Are The Top 5 News Headline's \n")
            for i in responce:
                text.insert(tk.END,"\n"+"-> "+i+"\n")
    elif (User_Input.lower() in welcome["Jokes"]):
        no = generate_random(len(jokes)-1)
        text.insert(tk.END,"\n"+"\n {} \n".format(jokes[no]))
    elif( "speak" in User_Input.lower().split(" ")):
        temp = User_Input[6:]
        main_speak(temp)

    elif( "open" in User_Input.lower().split(" ")):
        temp = User_Input[5:]
        webbrowser.open(temp,new=1)
        text.insert(tk.END,"\n"+"Bot : "+"Opened "+temp)
        text.insert(tk.END,"\n")

    elif ( "weather" in User_Input.lower().split(" ")):
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