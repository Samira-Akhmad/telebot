import telebot
TOKEN = "8677462371:AAEbJWyWdvSaxAddZIsZZ2FZu1GzGNKMgd4"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello! I am your bot, ready to assist you!")

@bot.message_handler(commands=['about'])
def about(message):
    bot.send_message(message.chat.id, "What are you going to ask about?")

bot.polling()