#06_06_weather_summary
import json
import urllib.parse, urllib.request

url = 'http://api.weatherstack.com/current'
city = urllib.parse.quote('San Francisco')
key = '03121fa790d2f1d5c6a9a32fa968ffeb' # paste_your_key_here'

response = urllib.request.urlopen(url + '?access_key=' + key + '&query=' + city)
j = json.load(response)

print(j['current']['weather_descriptions'][0])