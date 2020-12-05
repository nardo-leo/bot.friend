import os
from threading import Thread
from time import sleep

import schedule
import telebot
import dotenv

from nutcracker import ParserBolshoi


dotenv.load_dotenv('.env')

# init
bot = telebot.TeleBot(os.getenv('TOKEN'))

chat_id_with_me = os.getenv('CHAT_ID_WITH_ME')


def schedule_checker():
    while True:
        schedule.run_pending()
        sleep(1)

# ping
@bot.message_handler(commands=['ping'])
def ping(message):
    bot.send_message(message.chat.id,
                     '<b>PONG</b>\n' +
                     f'Chat id: {message.chat.id}',
                     parse_mode='HTML')


# send notify about new Nutcracker schedule in Bolshoi
def main():
    parser = ParserBolshoi('https://www.bolshoi.ru/visit/buyingnew/')
    nutcracker_msg = parser.run()

    bot.send_message(chat_id_with_me, nutcracker_msg, parse_mode='HTML')


if __name__ == '__main__':
    schedule.every().day.at('14:00').do(main)

    Thread(target=schedule_checker).start()

    # polling
    bot.polling()
