from flask import Flask, render_template, jsonify, request
import requests
import geocoder
import datetime
# Using for testing for now

app = Flask(__name__)


@app.route('/', methods=["GET"])
def call_api():
    # Get user ip address
    ip = jsonify({'ip': request.remote_addr})
    location = geocoder.ip('me')
    latlng = location.latlng
    """""
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
    sunrise_epoch = response['current']['sunrise']
    sunrise = convert_time(sunrise_epoch)
    sunset_epoch = response['current']['sunset']
    sunset = convert_time(sunset_epoch)
    uv_index = response['current']['uvi']
    #precipitation = response['current']['rain']
    rain = ""
    #for item in precipitation:
    #    rain = item["1h"]
    for item in weather:
        weather_type = item["main"]

    # Daily weather data
    , temp=temperature, feels_like=feels_like, wind=wind_speed, weather=weather_type, sunrise=sunrise, sunset=sunset, uvi=uv_index
    """""

    return render_template('index.html', location=location.city, temp=23)
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

def convert_time(time_epoch):
    time_converted = datetime.datetime.fromtimestamp(time_epoch)
    time = time_converted.time().strftime("%H:%M")
    return time

if __name__ == '__main__':
    app.run()
