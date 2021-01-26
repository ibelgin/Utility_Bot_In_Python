import json
import requests

def get_news(count):
    try:
        headlines=[]
        api_key = "a6b3d91efefd417f831ad57610d1aed5"
        url = "https://newsapi.org/v2/top-headlines?country=in&apiKey={}".format(api_key)
        responce = requests.get(url)
        news_json = json.loads(responce.text)
        temp = 1
        if count <=15 and count >=1 :
            for news in news_json['articles']:
                if temp<=count:
                    headlines.append(str(news['title']))
                    temp+=1
        else:
            headlines=[]
        return headlines
    except:
        return -1

