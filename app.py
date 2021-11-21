from flask import Flask, render_template, jsonify, request
import requests
import geocoder
import datetime

app = Flask(__name__)

# Get users location and set to global variable
location = geocoder.ip('me')

@app.route('/', methods=['GET', 'POST'])
def call_api():
    # Get city from search bar if used
    if request.data != None:
        user_city = request.data
        print(user_city)

    # Get user ip address
    ip = jsonify({'ip': request.remote_addr})
    location = geocoder.ip('me')
    latlng = location.latlng
    city = request.data
    lat = 55.9533
    lon = 3.1883
    #print("Here is the weather for", location.city)
    # API request
    api = "https://api.openweathermap.org/data/2.5/onecall?lat=%d&lon=%d&units=metric&exclude=minutely,alerts&appid=3b1175067ddb84b48f3f5f82fb3e8ecf" % (
        lat, lon)
    response = requests.get(api).json()
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

    weather_type_dict = {
        "weather_type": ["thunderstorm", "drizzle", "rain", "snow", "mist", "smoke", "haze", "dust", "fog", "clear", "clouds"]
    }

    #for type, weather_types in weather_type_dict.items():
        #if weather_types == weather_type:


    # ADD IN UV INDEX SCALE


    return render_template('index.html', temp = temperature, feels_like = feels_like, wind = wind_speed, weather = current_weather_type, sunrise = sunrise, sunset = sunset, uvi = uv_index, location = location.city, weather_description = weather_description)

@app.route('/weather-warnings')
def weather_warnings():
    latlng = location.latlng
    # Hardcoded lat and lon for now
    lat = 55.9533
    lon = 3.1883

    # Second API call to only get weather alerts for the location
    api = "https://api.openweathermap.org/data/2.5/onecall?lat=%d&lon=%d&units=metric&exclude=current,minutely,hourly,daily&appid=3b1175067ddb84b48f3f5f82fb3e8ecf" % (
        lat, lon)
    response = requests.get(api).json()
    weather_alert = "empty"
    # Check if there are any weather alerts for the user's location
    for item in response:
        if item == "alerts":
            weather_alert = response['alerts']['event']
    # Guard clause to check if there are any weather alerts
    if weather_alert == None:
        return render_template('weather-warnings.html', location = location.cit, weather_alert = weather_alert)
    return render_template('weather-warnings.html', location = location.city, weather_alert = weather_alert)

@app.route('/weather-map')
def weather_map():
    latlng = location.latlng
    # Hardcoded lat and lon for now
    lat = 55.9533
    lon = 3.1883

    api = "http://maps.openweathermap.org/maps/2.0/weather/PAC0/2/2/2?appid=3b1175067ddb84b48f3f5f82fb3e8ecf"
    #response = requests.get(api).json()
    return render_template('weather-map.html')

def convert_time(time_epoch):
    # Method to convert time from epoch time to hours & minutes
    time_converted = datetime.datetime.fromtimestamp(time_epoch)
    time = time_converted.time().strftime("%H:%M")
    return time

#def retrieve_city():
#    return json.dumps("Hello")

if __name__ == '__main__':
    app.run()
