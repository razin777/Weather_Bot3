import telebot
import requests
import json
from telebot import types
import utils
from translate import Translator
import platform
import locale

Bot = telebot.TeleBot("6377374644:AAEeQ0-q28_XfJWktHmGiB82l50hJVIFKTo")
API_key = "49188a86d6b41d61700d70ea39266205"
Leng = ''




@Bot.message_handler(commands=['start'])
def start(message):
    Bot.send_message(message.chat.id,utils.get_my_location_country())
    Bot.send_message(message.chat.id, platform.system())
    Bot.send_message(message.chat.id,locale.getlocale(category=locale.LC_CTYPE))
    translator = Translator(to_lang='nl')
    translation = translator.translate("This is a  pen.")
    if translation.find('INVALID TARGET LANGUAGE')==-1:
        Bot.send_message(message.from_user.id, translation)
    else:
        Bot.send_message(message.from_user.id, "xxxxxx")






@Bot.message_handler(commands=['eng'])
def eng(message):
    global Leng
    Leng = 'eng'

@Bot.message_handler(commands=['ru'])
def ru(message):
    global Leng
    Leng = 'ru'

@Bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}&units=metric&lang=ro')
    if res.status_code == 200:
       utils.show_butons(message, Bot, json.loads(res.text)['id'])#show butons and set APP to butons
       Bot.register_next_step_handler(message, get_weather_btn_no_app, res, city) # any next input run function def get_weather_no_app(message,res,city)
    else:
        Bot.send_message(message.chat.id, 'City is incorrect. Input city')

def get_weather_btn_no_app(message,res,city):
    if city != None:
        match message.text:
            case 'current weather':
                utils.show_current_weather(message, Bot, res)
            case 'hourly forecast for 48 hours':
                utils.show_hourly_weather(message, Bot, city, API_key)
            #case 'wether map':
                #utils.show_wether_map (message,Bot,utils.get_location(city),50)
        Bot.send_message(message.chat.id, "Input town")
    else:
        Bot.send_message(message.chat.id, 'Input city')



Bot.polling(none_stop=True, interval=0)










"""
@Bot.message_handler(content_types=['text'])
def get_weather_2(message):

    if res_sity != None :
        btn_caption = message.text.strip()
        match btn_caption:
            case 'Current weather':
                show_weather(message)

           # case 'Hourly forecast for 48 hours':
           #case 'Daily forecast for 8 days':

    else:
        Bot.reply_to(message,'City is incorrect22222')


def get_weather(message,city,btn_caption):
    match btn_caption:
        case 'Current weather':
            show_current_weather(message)
        case 'Hourly forecast for 48 hours':
            show_hourly_forecast_for_48_hours(message)
        case 'Daily forecast for 8 days':
            show_daily_forecast_for_8_days(message)
            
            
            
                #Bot.register_next_step_handler(message,)

"""



















"""

Bot.send_photo(message.chat.id,  icon_url, f"🌡️     {round(data['main']['temp'])}°C \n " \
                   +f"<b>{data['weather'][0]['description']}</b>" + "\n "  \
                   '<b>clouds</b>  '+ str(data['clouds']['all'])+'%\n '\
                   '<b>wind</b>    '+ str(data['wind']['speed'])+' m/c\n',parse_mode= 'html')
                   
"""