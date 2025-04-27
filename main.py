import telebot 
import requests
from bs4 import BeautifulSoup
import random
import time
# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot = telebot.TeleBot('7907256982:AAHiZ-fsL-1-W-gCpN99U5OmDxfIK0wuN-w')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот-шутник. Напиши /joke, чтобы получить шутку! Напиши /calc, чтобы воспользоваться калькулятором.")

@bot.message_handler(commands=['joke'])
def send_joke(message):
    try:
        # Example: Fetching a joke image from an API
        response = requests.get('https://api.imgflip.com/get_memes')
        data = response.json()
        
        if data['success']:
            # Select a random meme from the list
            memes = data['data']['memes']
            meme = random.choice(memes)
            meme_url = meme['url']
            
            # Send the meme image to the user
            bot.send_photo(message.chat.id, meme_url, caption="Вот шутка на картинке!")
        else:
            bot.reply_to(message, "Не удалось получить картинку с шуткой. Попробуйте позже!")
    except Exception as e:
        bot.reply_to(message, "Произошла ошибка. Попробуйте позже!")

@bot.message_handler(commands=['calc'])
def calculator(message):
    bot.reply_to(message, "Введите выражение для вычисления (например, 2+2):")

    @bot.message_handler(func=lambda msg: True)
    def calculate_expression(msg):
        try:
            # Evaluate the mathematical expression
            result = eval(msg.text)
            bot.reply_to(msg, f"Результат: {result}")
        except Exception as e:
            bot.reply_to(msg, "Ошибка в выражении. Убедитесь, что оно корректно.")

if __name__ == '__main__':
    # Start the bot
    print("Bot is polling...")
    bot.polling()