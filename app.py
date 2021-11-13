from flask import Flask, render_template, jsonify, request
import requests
import geocoder
import datetime
# Using for testing for now

app = Flask(__name__)


@app.route('/', methods=["POST"])
def call_api():
    # Get user ip address
    ip = jsonify({'ip': request.remote_addr})
    location = geocoder.ip('me')
    latlng = location.latlng
    """""
    lat = 55.9533
    lon = 3.1883
    #print("Here is the weather for", location.city)
    # API request
    url = "https://api.openweathermap.org/data/2.5/onecall?lat=%d&lon=%d&units=metric&exclude=minutely,alerts&appid=3b1175067ddb84b48f3f5f82fb3e8ecf" % (
        lat, lon)
    response = requests.get(url).json()
    # Fetching all appropriate data from API response
    weather_type = ""
    weather_description = ""
    timezone = response['timezone']
    temperature = round(response['current']['temp'])
    feels_like = round(response['current']['feels_like'])
    wind_speed = response['current']['wind_speed']
    current_weather = response['current']['weather']
    sunrise_epoch = response['current']['sunrise']
    sunrise = convert_time(sunrise_epoch)
    sunset_epoch = response['current']['sunset']
    sunset = convert_time(sunset_epoch)
    uv_index = response['current']['uvi']
    #precipitation = response['current']['rain']
    rain = ""
    #for item in precipitation:
    #    rain = item["1h"]
    for item in current_weather:
        weather_type = item["main"]
        if weather_type == "Clouds":
            current_weather_type = "Cloudy"
        weather_description = item["description"]
        # Description comes in lower case in most instances, so capitalise first letter of each word
        weather_description = weather_description.title()

    # Daily weather data
    """""
    weather_type_dict = {
        "weather_type": ["thunderstorm", "drizzle", "rain", "snow", "mist", "smoke", "haze", "dust", "fog", "clear", "clouds"]
    }

    #for type, weather_types in weather_type_dict.items():
        #if weather_types == weather_type:


    return render_template('index.html', temp=temperature, feels_like=feels_like, wind=wind_speed, weather=current_weather_type, sunrise=sunrise, sunset=sunset, uvi=uv_index, location=location.city, weather_description=weather_description)



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
    # Method to convert time from epoch time to hours & minutes
    time_converted = datetime.datetime.fromtimestamp(time_epoch)
    time = time_converted.time().strftime("%H:%M")
    return time

#def retrieve_city():
    # https://www.youtube.com/watch?v=6rPxwj1sR5c&ab_channel=SkyAlphaTech
    # https://www.py4u.net/discuss/985565
    # https://www.youtube.com/watch?v=2OYkhatUZmQ&ab_channel=bsaldivar%3ADatascience

if __name__ == '__main__':
    app.run()
