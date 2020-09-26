import requests
from text_converter import main_speak

def weather():
    try:
        main_speak("Enter The City Name ")
        city = input("\n Enter The City Name -> ")
        print()
        
        Api_Key = "2606f769271b8d545fe3458b2b72ed9f" # Paste Your API ID Here
        final_URL = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city,Api_Key)
        result = requests.get(final_URL)
        data = result.json()
        if data["cod"] == 200:
            doc = ('''
        The Weather At {} is {}.
        Description - {}.

        Temprature is {} Degree Kelvin
                '''.format(
                    data['name'],
                    data['weather'][0]['main'],
                    data['weather'][0]['description'],
                    data['main']['temp']
                ))
            print(doc)
            main_speak(doc)
        else:
            print("\n Sorry The Entered City Does Not Exist Or Check Your Internet Connection\n")
            main_speak("Sorry The Entered City Does Not Exist Or Check Your Internet Connection")
    except:
        print("\n Please Check Your Internet Connection : ( \n")



