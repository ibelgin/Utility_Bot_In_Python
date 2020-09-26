import json
import requests
from text_converter import main_speak
def get_news():
    try:
        api_key = "a6b3d91efefd417f831ad57610d1aed5"
        url = "https://newsapi.org/v2/top-headlines?country=us&apiKey={}".format(api_key)

        responce = requests.get(url)
        news_json = json.loads(responce.text)
        print('''
            Enter The Number of News To Read
            Please Enter A Number Less Than 15.
        ''')
        main_speak("Enter The Number Of Headlines You Want To Read . Only 15 News Are Possible Please Enter A Number less than 15")
        count = int(input("-> ")) # Number Of News To Read
        temp = 1
        print()
        if count <=15 and count >=1 :
            for news in news_json['articles']:
                if temp<=count:
                    headline = str(news['title'])
                    print("        ",temp,".",headline,"\n")
                    main_speak(headline)
                    temp+=1
        else:
            print("\n Please Enter A Number Less Then 15  But Not Less Than 0 \n")

    except:
        print("Please Check Your Internet Connection : (")
        main_speak("Please Check Your Internet Connection : (")
