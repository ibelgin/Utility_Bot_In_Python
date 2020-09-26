# Utiliy Bot By Belgin
# 20SH245

from news import get_news
from weather import weather
from responces import welcome,jokes,myhelp
from text_converter import main_speak 
import webbrowser
import random

name=""

def welcome_func():
    global name
    print(welcome["start_bot"])
    main_speak(welcome["start_bot"])
    name = input("-> ")
    print(welcome["Name_reply"].format(name))
    main_speak("Hi {} That's A Really Cute Name . Lets Get Started . ".format(name))
    for i in welcome["All_Commands"]:
        print(i)
    main_speak("These Are The Command's Available. Type \"Help\" For Options")

def Jokes():
    random_num = random.randint(0,len(jokes))
    print("\n","       ",jokes[random_num])
    main_speak(jokes[random_num])
    print("\n","        The Best Joke Is That You Don't Sound Funny : | \n") # Credit's to me : )

#__main__
welcome_func()
while True:
    try:
        user_input = input("\n {} -> ".format(name)).lower()

        if user_input == "weather":
            weather()
            
        elif user_input == "jokes":
            Jokes()

        elif user_input == "news":
            get_news()

        elif user_input == "exit":
            print("\n       Thank You Have A Great Day ! \n")
            main_speak("      Thank You ! Have A Great Day")
            break

        elif user_input == "help":
            print(myhelp)

        elif user_input == "about":
            print(welcome["about"])
        
        elif "open" in user_input.split(" "):
            try :
                temp = ["http://"+i for i in user_input.strip().split(" ")]
                webbrowser.open(temp[1])
            except:
                print("\n Enter A Valid Website Address \n ")
                main_speak("Enter A Valid Website Address")

        else:
            print("Sorry not.programmed")
            main_speak("Sorry Not Programmed for this question")
    
    except:
        continue
