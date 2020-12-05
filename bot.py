import os
import telebot
import dotenv

from nutcracker import ParserBolshoi


dotenv.load_dotenv('.env')

# init
bot = telebot.TeleBot(os.getenv('TOKEN'))

chat_id_with_me = os.getenv('CHAT_ID_WITH_ME')

# ping
@bot.message_handler(commands=['ping'])
def ping(message):
    bot.send_message(message.chat.id,
                     '<b>PONG</b>\n' +
                     f'Chat id: {message.chat.id}',
                     parse_mode='HTML')


# send notify about new Nutcracker schedule in Bolshoi
parser = ParserBolshoi('https://www.bolshoi.ru/visit/buyingnew/')
nutcracker_msg = parser.run()

bot.send_message(chat_id_with_me, nutcracker_msg, parse_mode='HTML')

# polling
bot.polling()
