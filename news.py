import json
import requests
from text_converter import main_speak
def get_news():
    try:
        api_key = "a6b3d91efefd417f831ad57610d1aed5"
        url = "https://newsapi.org/v2/top-headlines?country=us&apiKey={}".format(api_key)

        responce = requests.get(url)
        news_json = json.loads(responce.text)

        count = 1 # Number Of News To Read
        print()
        for news in news_json['articles']:
            if count<=5:
                headline = str(news['title'])
                print("        ",count,".",headline,"\n")
                main_speak(headline)
                count+=1
    except:
        print("Please Check Your Internet Connection : (")
        main_speak("Please Check Your Internet Connection : (")