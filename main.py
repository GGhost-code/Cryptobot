from telegram import Update
from telegram.ext import CallbackContext, CommandHandler, Updater, MessageHandler, Application

API_KEY = "6856319063:AAHGvZWAiX977g_qEVGCOyMxXjmTEJayePk"

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Здравствуйте, выберите действие на появившейся у вас клавиатуре."
                              " Если клавиатура не появилась, напишите команду /actionspanel")

def main() -> None:
    """Run bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(API_KEY).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()




