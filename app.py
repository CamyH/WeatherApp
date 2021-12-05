import json

from flask import Flask, render_template, jsonify, request, g
import requests
import geocoder
import geopy
from geopy.geocoders import Nominatim
import datetime
import sqlite3
import datetime

app = Flask(__name__)

#https://www.digitalocean.com/community/tutorials/how-to-use-an-sqlite-database-in-a-flask-application

db = 'db/database.db'

def get_db():
    db = getattr(g, 'db', None)
    if db is None:
        db = sqlite3.connect(db)
        g.db = db
    return db

def get_db_connection():
    conn = sqlite3.connect(db)
    return conn

@app.teardown_appcontext
def close_db_connection(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('db/schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

# Get server location and set to global variable
# Server location is used as the default location unless user gives permission to use location
location = geocoder.ip('me')

@app.route('/', methods=['GET', 'POST'])
def call_api():
    city = ""
    lat = 0
    lon = 0
    # Server location is used as the default location unless user gives permission to use location
    location = geocoder.ip('me')
    latlng = location.latlng
    # Set lat and lon vars appropriately
    # Lat is always at position 0, lon is always at position 1
    lat = latlng[0]
    lon = latlng[1]
    city = location.city
    if request.method == "POST":
        city = request.form.get("city")
        user_geocoder = Nominatim(user_agent="myGeocoder")
        location = user_geocoder.geocode(city)
        lat = location.latitude
        lon = location.longitude

    # Solution for getting lat and lon from user
    #ip_api = "http://ip-api.com/json/"
    #ip_api_response = requests.get(ip_api).json()
    #lat = ip_api_response['lat']
    #lon = ip_api_response['lon']

    # Get user ip address
    #ip = jsonify({'ip': request.remote_addr})

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
    current_weather_type = ""
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

    # Get today's date and time for use in database
    current_date_time = datetime.datetime.now()
    # Set correct format
    date_time = current_date_time.strftime("%d/%m/%Y %H:%M:%S")

    conn = get_db_connection()
    # Insert weather data into database
    conn.execute("INSERT INTO data (city, temperature, feels_like, wind_speed, current_weather_type, weather_description, sunrise, sunset, uv_index, datetime) VALUES (?,?,?,?,?,?,?,?,?,?)", (str(city), int(temperature), int(feels_like), float(wind_speed), str(current_weather_type), str(weather_description), str(sunrise), str(sunset), float(uv_index), str(date_time)),)
    conn.commit()
    #data = conn.execute('SELECT * FROM data').fetchall()
    conn.close()
    #print(data)

    return render_template('index.html', temp = temperature, feels_like = feels_like, wind = wind_speed, weather = current_weather_type, sunrise = sunrise, sunset = sunset, uvi = uv_index, location = city, weather_description = weather_description)

@app.route('/weather-warnings')
def weather_warnings():
    latlng = location.latlng
    lat = latlng[0]
    lon = latlng[1]

    # Second API call to only get weather alerts for the location
    api = "https://api.openweathermap.org/data/2.5/onecall?lat=%d&lon=%d&units=metric&exclude=current,minutely,hourly,daily&appid=3b1175067ddb84b48f3f5f82fb3e8ecf" % (
        lat, lon)
    response = requests.get(api).json()
    weather_data = ""
    weather_alert_sender = ""
    weather_alert = None
    weather_alert_description = ""

    if 'alerts' in response:
        weather_alert_data_response = response['alerts']
        weather_data = dict(weather_alert_data_response[0])
        for key, value in weather_data.items():
            if key == "sender_name":
                weather_alert_sender = value
            elif key == "event":
                weather_alert = value
            elif key == "description":
                weather_alert_description = value
            else:
                continue

    else:
        print('No weather alerts')

    # Put all weather alerts into a dictionary
    #weather_data = dict(weather_alert_data_response[0])
    # Iterate over dictionary and grab necessary weather alert data to be used on the weather-warnings page


    return render_template('weather-warnings.html', location = location.city, weather_alert_sender = weather_alert_sender, weather_alert = weather_alert, weather_alert_description = weather_alert_description)

@app.route('/weather-map')
def weather_map():
    # Setting lat and lon to be used for the weather map
    latlng = location.latlng
    lat = latlng[0]
    lon = latlng[1]

    return render_template('weather-map.html', lat=lat, lon=lon)

def convert_time(time_epoch):
    # Method to convert time from epoch time to hours & minutes
    time_converted = datetime.datetime.fromtimestamp(time_epoch)
    time = time_converted.time().strftime("%H:%M")
    return time

#def retrieve_city():
#    return json.dumps("Hello")

if __name__ == '__main__':
    app.run()
