from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, filters, Application, ContextTypes
import requests

API_KEY = "6856319063:AAHGvZWAiX977g_qEVGCOyMxXjmTEJayePk"
API_BASE_URL = "https://api.tinkoff.ru/invest/some_endpoint"


async def get_top_cryptocurrencies(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(1)
    global API_BASE_URL
    url = f"{API_BASE_URL}/top_cryptocurrencies"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.get(url, headers=headers)
    data = response.json()
    await update.message.reply_text("Данная функция на данный момент на стадии разработки, но в ближайшее время "
                                    "функционал появится. На данный момент топ - 1 криптовалюта - Bitcoin")
    # top_cryptos = data
    # for crypto in top_cryptos:
    #     print(f"Криптовалюта: {crypto['name']}, Цена: {crypto['price']}")


async def get_cryptocurrency_price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Данная функция на данный момент на стадии разработки, но в ближайшее время "
                                    "функционал появится")
    # url = f"{API_BASE_URL}/cryptocurrency/{cryptocurrency}/price"
    # headers = {"Authorization": f"Bearer {API_KEY}"}
    # response = requests.get(url, headers=headers)
    # data = response.json()
    # return data
#
# # типо показываем курс выбранной криптовалют
# chosen_crypto = "BTC"
# crypto_price = get_cryptocurrency_price(chosen_crypto)
# print(f"Курс криптовалюты {chosen_crypto}: {crypto_price['price']}")


async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Привет! Выберите действие:",
                              reply_markup=ReplyKeyboardMarkup(
                                  [['Топ 10 криптовалют'], ['Узнать курс криптовалюты']],
                                  one_time_keyboard=True))

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    await update.message.reply_text(update.message.text)



def main(show_crypto_price=None, show_top_cryptocurrencies=None) -> None:
    application = Application.builder().token(API_KEY).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.Regex('Топ 10 криптовалют'), get_top_cryptocurrencies))
    # application.add_handler(MessageHandler(filters.Regex('Топ 20 криптовалют'), show_top_cryptocurrencies))
    application.add_handler(MessageHandler(filters.Regex('Узнать курс криптовалюты'), get_cryptocurrency_price))

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()
