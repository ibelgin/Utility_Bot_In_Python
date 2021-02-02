import requests
import random
import string

def passwordGenerator(pass_len):
    password = ''
    password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits) + random.choice(string.punctuation)
    for y in range(int(pass_len)- 4):
        password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    return password

def ip_address(ipadd):
    try:
        res=requests.get('http://ipinfo.io/'+ipadd+'?token=cf6c6c0ce2d37e')
        data=res.json()
        data_returned = '''
            Ip Address : {} 
            City : {}
            Region : {}
            country : {}
            Location : {}
            Org : {}
            postal : {}
            Time Zone : {}
        '''.format(data["ip"],data["city"],data["region"],data["country"],data["loc"],data["org"],data["postal"],data["timezone"])
        return data_returned
    except:
        return "Check Your Internet Connection Or Enter a Valid IP"

# {
#  "ip": "139.130.4.5",
#  "city": "Brisbane",
#  "region": "Queensland",
#  "country": "AU",
#  "loc": "-27.4679,153.0281",
#  "org": "AS1221 Telstra Corporation Ltd",
#  "postal": "4000",
#  "timezone": "Australia/Brisbane"
# }

