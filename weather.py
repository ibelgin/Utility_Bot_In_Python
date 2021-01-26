import requests
from text_converter import main_speak

def weather(city):
    try:
        Api_Key = "2606f769271b8d545fe3458b2b72ed9f" # Paste Your API ID Here
        final_URL = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city,Api_Key)
        result = requests.get(final_URL)
        data = result.json()
        if data["cod"] == 200:
            weather = {
                "Main":data['weather'][0]['main'],
                "city":data['name'],
                "Temprature":str(data['main']['temp'])+" Kelvin"
            }
            return weather
        else:
            return -1
    except:
        return 1



