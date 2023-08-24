# pip install pytelegrambotapi

import telebot

TOKEN = "5830833659:AAFXua8GjDj2ZzdPTIdbofaWn19CE6Z4Y8M"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=["text" ])
def echo(message):
    print(message.text)
    msg = message.text.split()
    for word in msg:
        if word.startswith(("https", "http")) or word.isdigit() or word.startswith("+") or word.startswith("@") :
            print("link topildi")
            bot.delete_message(message.chat.id, message.message_id)
            bot.send_message(message.chat.id, text=f"@{message.from_user.username} \n Reklama tarqatmang!")

bot.polling()