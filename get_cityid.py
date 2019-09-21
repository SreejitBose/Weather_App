import json
import urllib.request
from pyfiglet import Figlet

def get_weather(location):
    try:
        url=urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+location+'&APPID=70f65be1d0175e5e660966edcffab3e9')
    except Exception as e:
        if (str(e)=='<urlopen error [Errno 11001] getaddrinfo failed>'):
            print('[-] Cannot reach openweathermap.org.....please check your connection')  
        elif (str(e)=='HTTP Error 404: Not Found'):
            print('[-] Ivalid city name')  
        elif (str(e)=='HTTP Error 401: Unauthorized'):
            print('[-] Unauthorized ..... API key mismatch')        
        exit()
    json_data=json.loads(url.read())
    print('Name of city - '+json_data['name'])
    current_temp=json_data['main']['temp']-273.15
    max_temp=json_data['main']['temp_max']-273.15
    min_temp=json_data['main']['temp_min']-273.15
    pressure=json_data['main']['pressure']
    wind_speed=json_data['wind']['speed']*3.6
    humidity=json_data['main']['humidity']
    description=json_data['weather'][0]['description']
    print('Current Temperature - '+str(int(current_temp))+"°C")
    print(description)
    print('Maximum Temperature - '+str(int(max_temp))+"°C")
    print('Minimum Temperature - '+str(int(min_temp))+"°C")
    print('humidity - '+str(int(humidity))+"%")
    print('Pressure - '+str(int(pressure))+"mBar")
    print('Wind speed - '+str(int(wind_speed))+"Km/h")

def main():
    print('')
    # print('*************************       ****************************')
    f=Figlet(font='slant')
    print(f.renderText('Weather App'))
    print('                  Powered by openweathermap.org             ')

    city=input('Enter City Name\n')
    get_weather(city)

if __name__ == "__main__":
    main()    