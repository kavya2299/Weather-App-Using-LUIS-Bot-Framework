
import pyowm
from config.config_reader import ConfigReader

class WeatherInformation():
    def __init__(self):
        self.config_reader = ConfigReader()
        self.configuration = self.config_reader.read_config()
        self.owmapikey = self.configuration['WEATHER_API_KEY']
        self.owm = pyowm.OWM(self.owmapikey)

    def get_weather_info(self,city):
        self.city=city
        weather_mgr = self.owm.weather_manager()
        observation = weather_mgr.weather_at_place(self.city)
        weather = observation.weather
        status = str(weather.detailed_status)
        
        # dict in Celsius units
        temp_dict_celsius = weather.temperature('celsius')
        temp_min_celsius = str(temp_dict_celsius['temp_min'])
        temp_max_celsius = str(temp_dict_celsius['temp_max'])
        #observation = self.owm.weather_at_place(city)
        #w = observation.get_weather()

        #observation = self.owm.weather_at_place(city)
        #w = observation.weather
        #latlon_res = observation.get_location()
        #lat = str(latlon_res.get_lat())
        #lon = str(latlon_res.get_lon())

        # wind_res = w.get_wind()
        # wind_speed = str(wind_res.get('speed'))

        # humidity = str(w.get_humidity())

        # celsius_result = w.get_temperature('celsius')
        # temp_min_celsius = str(celsius_result.get('temp_min'))
        # temp_max_celsius = str(celsius_result.get('temp_max'))

        # fahrenheit_result = w.get_temperature('fahrenheit')
        # temp_min_fahrenheit = str(fahrenheit_result.get('temp_min'))
        # temp_max_fahrenheit = str(fahrenheit_result.get('temp_max'))
        # print(temp_max_celsius, temp_min_celsius)
        # self.bot_says = "Today the weather in " + self.city +" is : \n Maximum Temperature :"+temp_max_celsius+ " degree celsius"+"& \n Minimum Temperature :"+temp_min_celsius+ " degree celsius" 
        self.bot_says = "Today the weather in " + self.city +" is " + status
        return self.bot_says