import os
import sqlite3
import requests
from datetime import datetime, timezone

# cursor.execute("SELECT city FROM users")
# db_city = cursor.fetchone()[0]
data_base = sqlite3.connect("data_base.db")
cursor = data_base.cursor() 
cursor.execute("CREATE TABLE IF NOT EXISTS users(country TEXT, city TEXT, name TEXT, surname TEXT)")
data_base.commit()
#r_window.start_registration()


city_list = [
    "Момбаса", "Канберра", "Амстердам", "Гавана", "Париж", "Парамарибо", "Астана"
]



# def geo_coder(city):
#     api_key2 = "697e1945f42a75b33e37791d0a456aab"
#     url3 = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={api_key2}" # geo_coder
   
#     response3 = requests.get(url3) # geocoder
#     if response3.status_code == 200:
#         data3 = response3.json() # geocoder

#         lat = round(data3[0]['lat'], 2)
#         # lat = [lat]
#         # lat.sort()

#         lon = round(data3[0]['lon'], 2)
#         # lon = [lon]
#         # lon.sort()

#         print(lat)
#         print(lon)
        
#         return lat, lon
#     else:
#         print("квейлыв")

    
# lat, lon = geo_coder("Dnipro")

def hour_weather(city, i):
    api_key2 = "5c3c27af2a8a49bb923164323231512"
    url2 = f'http://api.weatherapi.com/v1/forecast.json?key={api_key2}&q={city}&days=1&aqi=no&alerts=yes'
    response2 = requests.get(url2)
    # print(response2)
    if response2.status_code == 200:
        data2 = response2.json()
        # print(data2)
        # forecast = data2["forecast"]["forecastday"][0]["hour"]
        
        # temp_c = round(forecast[i]["temp_c"])
        # time = forecast[i]["time"].split()[1]
            # i += 1
        sunrise = data2["forecast"]["forecastday"][0]["astro"]["sunrise"]
        sunset = data2["forecast"]["forecastday"][0]["astro"]["sunset"]
        print(sunrise)
        return sunrise, sunset, response2   
        #print(forecast)
    else:
        print("zagranpasport ")


# hour_weather("Кольцо")



def get_weather(city):
    import modules.registration_window as reg
    import modules.main_window as main_w
    api_key = "a9b71ebb3501fa3f660ec085a14b6444"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&lang=uk&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        main_data = data["main"]
        temperature = round(main_data["temp"])
        weather = data["weather"][0]['description']
        maxtemp = round(data["main"]["temp_max"])
        mintemp = round(data["main"]["temp_min"])
        time_zone = data['timezone']
        main_wezer = data["weather"][0]["main"]
        main_id = data['weather'][0]['id']
        # sunset = data['sys']['sunset']
        # sunset_utc = datetime.fromtimestamp(sunset, timezone.utc)
        # sunset_t = sunset_utc.strftime("%H:%M")
        # sunrise = data['sys']['sunrise']
        # sunrise_utc = datetime.fromtimestamp(sunrise, timezone.utc)
        # sunrise_t = sunrise_utc.strftime("%H:%M") 
        # print(f"{main_wezer}")

        # print(data)


        # print(sunrise_utc)
        # print(sunset_utc)
        
        return temperature, weather, maxtemp, mintemp, time_zone, main_wezer, main_id, response # добіл штоб не мучался
        
    else:
        # reg.error_label1.configure(text = 'НЕВІРНО ВКАЗАНЕ МІСТО!' )
        # main_w.error_label.configure(text = "НЕВІРНО ВКАЗАНЕ МІСТО!")
        print("астралопитек")
# a = get_weather("Dnipro")
# print(a)



