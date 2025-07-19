import telebot
import os

TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Bem-vindo ao Mercado Cripto 100x! Use /carteira para baixar a carteira atualizada.")

@bot.message_handler(commands=['carteira'])
def send_carteira(message):
    with open("Carteira_Cripto_100x_Simulada.pdf", "rb") as pdf:
        bot.send_document(message.chat.id, pdf)

bot.polling()
