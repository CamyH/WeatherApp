from flask import Flask, render_template
import requests
# Using for testing for now

app = Flask(__name__)


@app.route('/')
def call_api():
    """""
    #location = geocoder.ip('me')
    #latlng = location.latlng
    lat = 55.9533
    lon = 3.1883
    #print("Here is the weather for", location.city)
    url = "https://api.openweathermap.org/data/2.5/onecall?lat=%d&lon=%d&units=metric&exclude=minutely,hourly,alerts,daily&appid=3b1175067ddb84b48f3f5f82fb3e8ecf" % (
        lat, lon)
    response = requests.get(url).json()
    weather_type = ""
    timezone = response['timezone']
    temperature = round(response['current']['temp'])
    feels_like = round(response['current']['feels_like'])
    wind_speed = response['current']['wind_speed']
    weather = response['current']['weather']
    for item in weather:
        weather_type = item["main"]
"""""
    return render_template('index.html')
#def index_page():
#    return render_template('index.html', temperature=temperature)
"""""
@app.route('/city')
def call_api():
    #location = geocoder.ip('me')
    #latlng = location.latlng
    lat = 55.9533
    lon = 3.1883
    #print("Here is the weather for", location.city)
    url = "https://api.openweathermap.org/data/2.5/onecall?lat=%d&lon=%d&units=metric&exclude=minutely,hourly,alerts,daily&appid=3b1175067ddb84b48f3f5f82fb3e8ecf" % (
        lat, lon)
    response = requests.get(url).json()
    weather_type = ""
    timezone = response['timezone']
    temperature = round(response['current']['temp'])
    feels_like = round(response['current']['feels_like'])
    wind_speed = response['current']['wind_speed']
    weather = response['current']['weather']
    for item in weather:
        weather_type = item["main"]

    print(timezone)
    return "Current weather is %s" % temperature

"""""
if __name__ == '__main__':
    app.run()
