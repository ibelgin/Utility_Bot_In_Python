# Text To Speech Converter Module
from gtts import gTTS # Converting Text To Speech
import playsound  # To Play The Music
import os # To Remove The File Once It is Played

file = "speech.mp3"

# This is To Play The Saved Audio
def play_saved_speech(file):
    try :
        playsound.playsound(file,True)
    except:
        print("\n Some Error While Playing \n")

def main_speak(text):
    # These Two Lines WillConvert The Given TEXT To
    # Speech and then Save The File In The Project Directory
    try:
        tts = gTTS(text=text, lang="en")
        tts.save(file)
        #This Will Play The Speech File
        play_saved_speech(file)
        os.remove(file)
    except:
        print("\n Some error Occured . Please Check Your Internet Connection : ( \n")

