import os
import logging
import config
from datetime import datetime
import random
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes

#logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

#date time stuff --------------------------------------------------------------
now = datetime.now()

current_time = now.strftime("%H:%M")
print("Current Time =", current_time) #Current Time = 07:41




#bot stuff -------------------------------------------------------------------------------


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_caps = ' '.join(context.args).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

async def time(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=current_time)

async def quote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #reading quotes from text file-------------------------------------------------------------

    my_file = open("src/quotes.txt", "r")
    data = my_file.read()
    data_into_list = data.split("\n")
    the_quote = random.choice(data_into_list)
    print(the_quote)
    

    #post the image
    if 'Marcus' in the_quote:
        print('there is marcus in the quote')
        pic = open('src/1.jpg', 'rb')
        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=pic)
    elif 'Seneca' in the_quote:
        print('there is seneca in the quote')
        pic = open('src/2.jpg', 'rb')
        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=pic)
    elif 'Epictetus' in the_quote:
        print('there is epictetus in the quote')
        pic = open('src/3.jpg', 'rb')
        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=pic)

    await context.bot.send_message(chat_id=update.effective_chat.id, text=the_quote)

    my_file.close()


if __name__ == '__main__':
    application = ApplicationBuilder().token(config.THE_TOKEN).build()
    
    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    caps_handler = CommandHandler('caps', caps)
    time_handler = CommandHandler('time', time)
    quote_handler = CommandHandler('quote', quote)

    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    application.add_handler(caps_handler)
    application.add_handler(time_handler)
    application.add_handler(quote_handler)
    
    application.run_polling()
