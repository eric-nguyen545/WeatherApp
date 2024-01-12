from tkinter import *
import requests
import json
from datetime import datetime
 
#Initialize Window
 
window =Tk()
window.geometry("400x400") #size of the window by default
window.resizable(0,0) #to make the window size fixed
#title of our window
window.title("Weather")
 
#Fetch and display weather info
city_value = StringVar()
 
 
def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()
 
 
city_value = StringVar()
 
def showWeather():
    #Enter you api key, copies from the OpenWeatherMap dashboard
    api_key = '24d168c141cb2ed4344aaad5e0ec98d9'  #sample API
 
    # Get city name from user from the input field (later in the code)
    location = city_value.get()

    # API url
    weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid={api_key}'
 
    # Get the response from fetched url
    response = requests.get(weather_url)
 
    # changing response from json to python readable 
    weather_info = response.json()
 
    tfield.delete("1.0", "end")   #to clear the text field for every new output
 
#Storing the fetched values of weather of a city
    if weather_info['cod'] == 200:

        temp = int(weather_info['main']['temp'])
        feels_like = int(weather_info['main']['feels_like'])
        pressure = weather_info['main']['pressure']
        humidity = weather_info['main']['humidity']
        wind_spd = weather_info['wind']['speed'] * 3.6
        sunrise = weather_info['sys']['sunrise']
        sunset = weather_info['sys']['sunset']
        timezone = weather_info['timezone']
        cloudy = weather_info['clouds']['all']
        descp = weather_info['weather'][0]['description']
        sunrise = time_format_for_location(sunrise + timezone)
        sunset = time_format_for_location(sunset + timezone)

        weather = f"Weather of: {location}\nTemperature: {temp}° C\nFeels like : {feels_like}° C \nThe wind speed is {wind_spd} meters per second \nPressure: {pressure} hPa\nHumidity: {humidity}%\nSunrise at {sunrise} and Sunset at {sunset}\nCloud: {cloudy}%\nInfo: {descp}"
    else:
        weather = f"\n\tWeather for '{location}' not found!\n\tKindly Enter valid City Name !!"
 
    tfield.insert(INSERT, weather)   #to insert or send value in our Text Field to display output

#Interface
city_head= Label(window, text = 'Enter City Name', font = 'Arial 12 bold').pack(pady=10) #to generate label heading
inp_city = Entry(window, textvariable = city_value,  width = 24, font='Arial 14 bold').pack()
Button(window, command = showWeather, text = "Check Weather", font="Arial 10", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5 ).pack(pady= 20)
 
#Output
weather_now = Label(window, text = "The Weather is:", font = 'arial 12 bold').pack(pady=10)

tfield = Text(window, width=46, height=10)
tfield.pack()
window.mainloop()