     from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

     def start(update, context):
         update.message.reply_text('Йо, бро! Я твой новый бот!')

     def echo(update, context):
         update.message.reply_text(update.message.text)

     def main():
         updater = Updater("8093243052:AAEEbVzfHHmIpJzb52UzxJSVt4bR2fM9gjc", use_context=True)
         dp = updater.dispatcher
         dp.add_handler(CommandHandler("start", start))
         dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
         updater.start_polling()
         updater.idle()

     if __name__ == '__main__':
         main()
     
