import telebot
import requests
import json
from telebot import types


def show_greetings (message,bot):
    bot.send_message(message.from_user.id, "👋 Welcome to the weather forecast bot".translate())
    image = '782349389.gif'
    file = open('./' + image, 'rb')
    bot.send_photo(message.chat.id, file)

def show_butons (message,bot,id_city):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(text ='current weather')
    btn2 = types.KeyboardButton(text ='hourly forecast for 48 hours')
    #webApp = types.WebAppInfo(f'https://openweathermap.org/weathermap?basemap=map&cities=true&layer=pressure&lat={location.latitude}&lon={location.longitude}&zoom={10}')
    #webApp = types.WebAppInfo(f'https://openweathermap.org/city/2643743')
    webApp = types.WebAppInfo(f"https://openweathermap.org/city/{id_city}")
    btn3 = types.KeyboardButton(text="weather map", web_app=webApp)
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.from_user.id,'Push buton below', reply_markup=markup)


def show_current_weather (message,bot,res):
    data = json.loads(res.text)
    icon = data['weather'][0]['icon']
    icon_url = f"https://openweathermap.org/img/wn/{icon}@2x.png"
    bot.send_message(message.chat.id, f"Weather now: \n ")
    bot.send_photo(message.chat.id, icon_url)
    bot.send_message(message.chat.id, f"🌡️     {round(data['main']['temp'])}°C \n " \
                     + f"<b>{data['weather'][0]['description']}</b>" + '\n ' \
                     '<b>clouds</b>  \n' + str(data['clouds']['all']) + '%\n ' \
                      '<b>wind</b>    ' + str(data['wind']['speed']) + 'm/c\n '
                      '<b>city</b>    ' + str(data['name']), parse_mode='html')


def show_hourly_weather (message,bot,city_name,API_key):
    res = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={API_key}&units=metric&lang=ru')
    data_dict = json.loads(res.text)
    bot.send_message(message.chat.id, f"{data_dict['city']['name']}: \n ", parse_mode='html')
    for data_dict_list_dict in data_dict['list']:
        #print(data_dict_list_dict)
        #print(data_dict_list_dict['main']['temp'])
        #print(data_dict_list_dict['weather'][0]['description'])
        bot.send_message(message.chat.id, f"{data_dict_list_dict['dt_txt']}: \n ")
        bot.send_message(message.chat.id, f"🌡️     {round(data_dict_list_dict['main']['temp'])}°C \n " \
                     + f"<b>{data_dict_list_dict['weather'][0]['description']}</b>" + '\n ' \
                     '<b>clouds</b>  ' + str(data_dict_list_dict['clouds']['all']) + '%\n ' \
                      '<b>wind</b>    ' + str(data_dict_list_dict['wind']['speed']) + 'm/c\n', parse_mode='html')

"""

def show_current_weather (message,bot,city,API_key):
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}&units=metric')
    data = json.loads(res.text)
    icon = data['weather'][0]['icon']'
    icon_url = f"https://openweathermap.org/img/wn/{icon}@2x.png"
    bot.reply_to(message, f"Weather now: \n ")
    bot.send_photo(message.chat.id, icon_url)
    bot.send_message(message.chat.id, f"🌡️     {round(data['main']['temp'])}°C \n " \
                     + f"<b>{data['weather'][0]['description']}</b>" + '\n ' \
                     '<b>clouds</b>  ' + str(data['clouds']['all']) + '%\n ' \
                      '<b>wind</b>    ' + str(data['wind']['speed']) + 'm/c\n '
                      '<b>city</b>    ' + str(data['name']), parse_mode='html')




def show_hourly_weather (message,bot,city,API_key):
    res = requests.get(f'https://pro.openweathermap.org/data/2.5/forecast/hourly?q={city}&appid={API_key}')
    data = json.loads(res.text)
    icon = data['weather'][0]['icon']
    icon_url = f"https://openweathermap.org/img/wn/{icon}@2x.png"
    bot.reply_to(message, f"Weather now: \n ")
    bot.send_photo(message.chat.id, icon_url)
    bot.send_message(message.chat.id, f"🌡️     {round(data['main']['temp'])}°C \n " \
                     + f"<b>{data['weather'][0]['description']}</b>" + '\n ' \
                     '<b>clouds</b>  ' + str(data['clouds']['all']) + '%\n ' \
                      '<b>wind</b>    ' + str(data['wind']['speed']) + 'm/c\n '
                      '<b>city</b>    ' + str(data['name']), parse_mode='html')

"""

#def show_wether_map (message,bot,location,zoom):
    #webApp = types.WebAppInfo( f'https://openweathermap.org/weathermap?basemap=map&cities=true&layer=pressure&lat={location.latitude}&lon={location.longitude}&zoom={zoom}')
    #bot.send_message(message.chat.id,src,parse_mode='html')
    #show_butons(message, bot)
# webApp2 = types.WebAppInfo("https://services.metservice.com/weather-widget/widget?params=blue|large|landscape|days-3|classic&loc=oslo&type=urban")
    #btn9 = types.KeyboardButton(text="btn9", web_app=webApp2)
#btn3 = types.KeyboardButton('daily forecast for 8 days')
    #webApp = types.WebAppInfo("https://weather101.free.nf/index3.html") #создаем webappinfo - формат хранения url
    #webApp = types.WebAppInfo("https://weather101.free.nf/index4tomorrow_io.html")  # создаем webappinfo - формат хранения url
    #wA = types.WebAppInfo("https://weather101.free.nf/index4tomorrow_io.html")
    #btn3 = types.KeyboardButton(text="www", web_app=webApp) #создаем кнопку типа webap


"""    
    data = json.loads(res.text)
    icon = data['weather'][0]['icon']
    icon_url = f"https://openweathermap.org/img/wn/{icon}@2x.png"
    bot.reply_to(message, f"Weather now: \n ")
    bot.send_photo(message.chat.id, icon_url)
    bot.send_message(message.chat.id, f"🌡️     {round(data['main']['temp'])}°C \n " \
                     + f"<b>{data['weather'][0]['description']}</b>" + '\n ' \
                         '<b>clouds</b>  ' + str(data['clouds']['all']) + '%\n ' \
                      '<b>wind</b>    ' + str(data['wind']['speed']) + 'm/c\n '
                      '<b>city</b>    ' + str(data['name']), parse_mode='html')


def show_daily_weather (message,bot,city,API_key):
    res = requests.get(f'https://pro.openweathermap.org/data/2.5/forecast/hourly?q={city}&appid={API_key}')
    data = json.loads(res.text)
    icon = data['weather'][0]['icon']
    icon_url = f"https://openweathermap.org/img/wn/{icon}@2x.png"
    bot.reply_to(message, f"Weather now: \n ")
    bot.send_photo(message.chat.id, icon_url)
    bot.send_message(message.chat.id, f"🌡️     {round(data['main']['temp'])}°C \n " \
                     + f"<b>{data['weather'][0]['description']}</b>" + '\n ' \
                     '<b>clouds</b>  ' + str(data['clouds']['all']) + '%\n ' \
                      '<b>wind</b>    ' + str(data['wind']['speed']) + 'm/c\n '
                      '<b>city</b>    ' + str(data['name']), parse_mode='html')



#bot.reply_to(message, f"{res.json()}")
    bot.send_message(message.chat.id,'html 7777')
    m = "<div id=\"openweathermap-widget-1\"></div><script src='//openweathermap.org/themes/openweathermap/assets/vendor/owm/js/d3.min.js'></script><script>window.myWidgetParam ? window.myWidgetParam : window.myWidgetParam = [];  window.myWidgetParam.push({id: 1,cityid: '704617',appid: '17e09f822f4957ac64ee0ce13bb114b2',units: 'metric',containerid: 'openweathermap-widget-1',  });  (function() {var script = document.createElement('script');script.async = true;script.charset = \"utf-8\";script.src = \"//openweathermap.org/themes/openweathermap/assets/vendor/owm/js/weather-widget-generator.js\";var s = document.getElementsByTagName('script')[0];s.parentNode.insertBefore(script, s);  })();</script>"
    bot.send_message(message.chat.id, m)
    bot.send_message(message.chat.id,m,parse_mode='html')

    
"""

from geopy.geocoders import Nominatim  # Подключаем библиотеку
import geocoder

def get_my_location_country():
    g = geocoder.ip('me')
    return g.country




def get_data(city,API):
    res = requests.get(API)
    if res.status_code == 200:
        return json.loads(res.text)
    else:
        return None

def get_location(city):
    geolocator = Nominatim(user_agent="Tester")  # Указываем название приложения (так нужно, да)
    adress = city  # Получаем интересующий нас адрес
    location = geolocator.geocode(adress)  # Создаем переменную, которая состоит из нужного нам адреса
    return location  # Выводим результат: адрес в полном виде
    #print(location.latitude, location.longitude)  # И теперь выводим GPS-координаты нужного нам адреса
