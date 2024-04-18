from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, filters, Application, ContextTypes
import requests
from bs4 import BeautifulSoup
import pandas as pd
import random

API_KEY = "6856319063:AAHGvZWAiX977g_qEVGCOyMxXjmTEJayePk"
API_BASE_URL = "https://api.tinkoff.ru/invest/some_endpoint"


# -------------------------------------------------Узнаем цену криптовалют---------------------------------------------
async def get_bitcoin_price(update: Update, context: CallbackContext):
    url = 'https://coinmarketcap.com/ru/currencies/bitcoin/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    price = str(soup.find(property="og:description"))
    price = price.split("\"")
    await update.message.reply_text(price[1][:price[1].find("RUB")] + "RUB")


async def get_ethereum_price(update: Update, context: CallbackContext):
    url = 'https://coinmarketcap.com/ru/currencies/ethereum/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    price = str(soup.find(property="og:description"))
    price = price.split("\"")
    await update.message.reply_text(price[1][:price[1].find("RUB")] + "RUB")


async def get_tether_price(update: Update, context: CallbackContext):
    url = 'https://coinmarketcap.com/ru/currencies/tether/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    price = str(soup.find(property="og:description"))
    price = price.split("\"")
    await update.message.reply_text(price[1][:price[1].find("RUB")] + "RUB")


async def get_bnb_price(update: Update, context: CallbackContext):
    url = 'https://coinmarketcap.com/ru/currencies/binance-coin/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    price = str(soup.find(property="og:description"))
    price = price.split("\"")
    await update.message.reply_text(price[1][:price[1].find("RUB")] + "RUB")


async def get_solana_price(update: Update, context: CallbackContext):
    url = 'https://coinmarketcap.com/ru/currencies/solana/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    price = str(soup.find(property="og:description"))
    price = price.split("\"")
    await update.message.reply_text(price[1][:price[1].find("RUB")] + "RUB")


async def get_usdc_price(update: Update, context: CallbackContext):
    url = 'https://coinmarketcap.com/ru/currencies/usd-coin/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    price = str(soup.find(property="og:description"))
    price = price.split("\"")
    await update.message.reply_text(price[1][:price[1].find("RUB")] + "RUB")


async def get_xrp_price(update: Update, context: CallbackContext):
    url = 'https://coinmarketcap.com/ru/currencies/xrp/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    price = str(soup.find(property="og:description"))
    price = price.split("\"")
    await update.message.reply_text(price[1][:price[1].find("RUB")] + "RUB")


async def get_toncoin_price(update: Update, context: CallbackContext):
    url = 'https://coinmarketcap.com/ru/currencies/toncoin/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    price = str(soup.find(property="og:description"))
    price = price.split("\"")
    await update.message.reply_text(price[1][:price[1].find("RUB")] + "RUB")


async def get_dogecoin_price(update: Update, context: CallbackContext):
    url = 'https://coinmarketcap.com/ru/currencies/dogecoin/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    price = str(soup.find(property="og:description"))
    price = price.split("\"")
    await update.message.reply_text(price[1][:price[1].find("RUB")] + "RUB")


async def get_cardano_price(update: Update, context: CallbackContext):
    url = 'https://coinmarketcap.com/ru/currencies/cardano/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    price = str(soup.find(property="og:description"))
    price = price.split("\"")
    await update.message.reply_text(price[1][:price[1].find("RUB")] + "RUB")


# -------------------------------------------Рыночная капитализация----------------------------------------------------
def get_daily_volume(api_key, symbol):
    url = f"https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol={symbol}"
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key,
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        data = response.json()

        daily_volume = data['data'][symbol]['quote']['USD']['volume_24h']

        return f"${daily_volume:,.2f}"
    except Exception as e:
        return f"Произошла ошибка: {str(e)}"


api_key = '0f3fc9c2-0644-4f21-b821-af5ad27f8cf9'


# async def market_cap_bitcoin():
#     bitcoin_volume = get_daily_volume(api_key, 'BTC')
#     print("Цена проданных монет Биткоина за день:", bitcoin_volume)
async def get_bitcoin_daily_volume(update: Update, context: ContextTypes.DEFAULT_TYPE):
    bitcoin_volume = get_daily_volume(api_key, 'BTC')
    await update.message.reply_text("Цена проданных монет Bitcoin за день: " + str(bitcoin_volume))


async def get_ethereum_daily_volume(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ethereum_volume = get_daily_volume(api_key, 'ETH')
    await update.message.reply_text("Цена проданных монет Ethereum за день: " + str(ethereum_volume))


async def get_tether_daily_volume(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tether_volume = get_daily_volume(api_key, 'USDT')
    await update.message.reply_text("Цена проданных монет Tether за день: " + str(tether_volume))


async def get_bnb_daily_volume(update: Update, context: ContextTypes.DEFAULT_TYPE):
    bnb_volume = get_daily_volume(api_key, 'BNB')
    await update.message.reply_text("Цена проданных монет BNB за день: " + str(bnb_volume))


async def get_solana_daily_volume(update: Update, context: ContextTypes.DEFAULT_TYPE):
    sol_volume = get_daily_volume(api_key, 'SOL')
    await update.message.reply_text("Цена проданных монет Solana за день: " + str(sol_volume))


async def get_usdc_daily_volume(update: Update, context: ContextTypes.DEFAULT_TYPE):
    usdc_volume = get_daily_volume(api_key, 'USDC')
    await update.message.reply_text("Цена проданных монет USDC за день: " + str(usdc_volume))


async def get_xrp_daily_volume(update: Update, context: ContextTypes.DEFAULT_TYPE):
    xrp_volume = get_daily_volume(api_key, 'XRP')
    await update.message.reply_text("Цена проданных монет XRP за день: " + str(xrp_volume))


async def get_dogecoin_daily_volume(update: Update, context: ContextTypes.DEFAULT_TYPE):
    doge_volume = get_daily_volume(api_key, 'DOGE')
    await update.message.reply_text("Цена проданных монет Dogecoin за день: " + str(doge_volume))


async def get_toncoin_daily_volume(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ton_volume = get_daily_volume(api_key, 'TON')
    await update.message.reply_text("Цена проданных монет Toncoin за день: " + str(ton_volume))


async def get_cardano_daily_volume(update: Update, context: ContextTypes.DEFAULT_TYPE):
    cardano_volume = get_daily_volume(api_key, 'ADA')
    await update.message.reply_text("Цена проданных монет Cardano(ADA) за день: " + str(cardano_volume))


# -----------------------------------------Рыночная капитализация тут-----------------------------------------------

def get_market_cap(symbol, api_key='0f3fc9c2-0644-4f21-b821-af5ad27f8cf9'):
    url = f"https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol={symbol}"
    headers = {'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': api_key, }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        market_cap = data['data'][symbol]['quote']['USD']['market_cap']
        return f"${market_cap:,.2f}"
    except Exception as e:
        return f"Произошла ошибка: {str(e)}"


async def get_bitcoin_market_cap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    bitcoin_market_cap = get_market_cap('BTC')
    await update.message.reply_text("Рыночная капитализация Bitcoin: " + str(bitcoin_market_cap))


async def get_ethereum_market_cap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ethereum_market_cap = get_market_cap('ETH')
    await update.message.reply_text("Рыночная капитализация Ethereum: " + str(ethereum_market_cap))


async def get_tether_market_cap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tether_market_cap = get_market_cap('USDT')
    await update.message.reply_text("Рыночная капитализация Tether: " + str(tether_market_cap))


async def get_bnb_market_cap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    bnb_market_cap = get_market_cap('BNB')
    await update.message.reply_text("Рыночная капитализация BNB: " + str(bnb_market_cap))


async def get_solana_market_cap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    sol_market_cap = get_market_cap('SOL')
    await update.message.reply_text("Рыночная капитализация Solana: " + str(sol_market_cap))


async def get_usdc_market_cap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    usdc_market_cap = get_market_cap('USDC')
    await update.message.reply_text("Рыночная капитализация USDC: " + str(usdc_market_cap))


async def get_xrp_market_cap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    xrp_market_cap = get_market_cap('XRP')
    await update.message.reply_text("Рыночная капитализация XRP: " + str(xrp_market_cap))


async def get_dogecoin_market_cap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    doge_market_cap = get_market_cap('DOGE')
    await update.message.reply_text("Рыночная капитализация Dogecoin: " + str(doge_market_cap))


async def get_toncoin_market_cap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ton_market_cap = get_market_cap('TON')
    await update.message.reply_text("Рыночная капитализация Toncoin: " + str(ton_market_cap))


async def get_cardano_market_cap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    cardano_market_cap = get_market_cap('ADA')
    await update.message.reply_text("Рыночная капитализация Cardano(ADA): " + str(cardano_market_cap))


# -------------------------------------------Паттерны свечей тут----------------------------------------------------

async def show_random_pattern(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_photo(f"data/{random.randint(1, 10)}.jpg")


# ------------------------------------------Топ крипотовалют тут------------------------------------------------------
def get_top_n_cryptos(n):
    url = 'https://coinmarketcap.com/ru/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    crypto_data = []
    table = soup.find('tbody')
    rows = table.find_all('tr')
    for i, row in enumerate(rows[:n], 1):
        cells = list(row.find_all('td'))
        # print(cells)
        rank = i
        name = cells[2].find('p').get_text().strip()
        price = cells[3].find('a').get_text().replace('\n', '').replace(',', '')
        crypto_data.append({'Rank': rank, 'Name': name, 'Price': price})

    return pd.DataFrame(crypto_data)


async def show_10(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(str(get_top_n_cryptos(10)))


async def show_20(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(str(get_top_n_cryptos(20)))


async def show_40(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(str(get_top_n_cryptos(40)))


# --------------------------------------------------Функции бота------------------------------------------------------
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Выберите действие:",
                                    reply_markup=ReplyKeyboardMarkup(
                                        [['Топ 10 криптовалют'],
                                         ['Узнать суточный объем торгов криптовалюты'],
                                         ['Узнать курс криптовалюты'],
                                         ['Узнать рыночную капитализацию криптовалюты'],
                                         ['Показать случайный паттерн курса'],
                                         ['Скачать лицензию']],
                                        one_time_keyboard=True))


async def actionspanel(update: Update, context: CallbackContext):
    await update.message.reply_text("Выберите действие:",
                                    reply_markup=ReplyKeyboardMarkup(
                                        [['Топ 10 криптовалют'],
                                         ['Узнать суточный объем торгов криптовалюты'],
                                         ['Узнать курс криптовалюты'],
                                         ['Узнать рыночную капитализацию криптовалюты'],
                                         ['Показать случайный паттерн курса'],
                                         ['Скачать лицензию']],
                                        one_time_keyboard=True))


async def pricepanel(update: Update, context: CallbackContext):
    await update.message.reply_text("Выберите криптовалюту, курс которой вы хотите знать:",
                                    reply_markup=ReplyKeyboardMarkup(
                                        [['Bitcoin, курс'], ['Ethereum, курс'], ['Tether, курс'],
                                         ['BNB, курс'], ['Solana, курс'], ['USDC, курс'], ['XRP, курс'],
                                         ['Toncoin, курс'], ['Dogecoin, курс'], ['Cardano, курс'], ['Назад']],
                                        one_time_keyboard=True))


async def dailyvolumepanel(update: Update, context: CallbackContext):
    await update.message.reply_text("Выберите криптовалюту, суточный объем торгов которой вы хотите знать:",
                                    reply_markup=ReplyKeyboardMarkup(
                                        [['Bitcoin, суточный объем торгов'], ['Ethereum, суточный объем торгов']
                                            , ['Tether, суточный объем торгов'], ['BNB, суточный объем торгов'],
                                         ['Solana, суточный объем торгов'], ['USDC, суточный объем торгов'],
                                         ['XRP, суточный объем торгов'], ['Toncoin, суточный объем торгов'],
                                         ['Dogecoin, суточный объем торгов'], ['Cardano, суточный объем торгов'],
                                         ['Назад']],
                                        one_time_keyboard=True))


async def marketcappanel(update: Update, context: CallbackContext):
    await update.message.reply_text("Выберите криптовалюту, рыночную капитализацию которой вы хотите знать:",
                                    reply_markup=ReplyKeyboardMarkup(
                                        [['Bitcoin, рыночная капитализация'], ['Ethereum, рыночная капитализация']
                                            , ['Tether, рыночная капитализация'], ['BNB, рыночная капитализация'],
                                         ['Solana, рыночная капитализация'], ['USDC, рыночная капитализация'],
                                         ['XRP, рыночная капитализация'], ['Toncoin, рыночная капитализация'],
                                         ['Dogecoin, рыночная капитализация'], ['Cardano, рыночная капитализация'],
                                         ['Назад']],
                                        one_time_keyboard=True))

async def changepanel(update: Update, context: CallbackContext):
    await update.message.reply_text("Выберите криптовалюту, изменение цены которой "
                                    "за определенный срок вы хотите знать:",
                                    reply_markup=ReplyKeyboardMarkup(
                                        [['Bitcoin, рыночная капитализация'], ['Ethereum, рыночная капитализация']
                                            , ['Tether, рыночная капитализация'], ['BNB, рыночная капитализация'],
                                         ['Solana, рыночная капитализация'], ['USDC, рыночная капитализация'],
                                         ['XRP, рыночная капитализация'], ['Toncoin, рыночная капитализация'],
                                         ['Dogecoin, рыночная капитализация'], ['Cardano, рыночная капитализация'],
                                         ['Назад']],
                                        one_time_keyboard=True))


async def upload_license(update: Update, context: CallbackContext):
    await update.message.reply_document("LICENSE")


# --------------------------------------------------Тут основа, база--------------------------------------------------
def main(show_crypto_price=None, show_top_cryptocurrencies=None) -> None:
    application = Application.builder().token(API_KEY).build()
    # ----------------------------------------------Системные функции--------------------------------------------
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("actionspanel", actionspanel))
    application.add_handler(MessageHandler(filters.Regex("Назад"), actionspanel))
    application.add_handler(MessageHandler(filters.Regex('Узнать курс криптовалюты'), pricepanel))
    application.add_handler(MessageHandler(filters.Regex('Узнать суточный объем торгов криптовалюты'),
                                           dailyvolumepanel))
    application.add_handler(MessageHandler(filters.Regex('Показать случайный паттерн курса'), show_random_pattern))
    application.add_handler(MessageHandler(filters.Regex('Скачать лицензию'), upload_license))
    application.add_handler(MessageHandler(filters.Regex('Узнать рыночную капитализацию криптовалюты'), marketcappanel))
    # ----------------------------------------------Топы  криптовалют--------------------------------------------
    application.add_handler(MessageHandler(filters.Regex('Топ 10 криптовалют'), show_10))
    application.add_handler(MessageHandler(filters.Regex('Топ 20 криптовалют'), show_20))
    application.add_handler(MessageHandler(filters.Regex('Топ 40 криптовалют'), show_40))
    # -----------------------------------------------Курсы криптовалют-------------------------------------------
    application.add_handler(MessageHandler(filters.Regex('Bitcoin, курс'), get_bitcoin_price))
    application.add_handler(MessageHandler(filters.Regex('Ethereum, курс'), get_ethereum_price))
    application.add_handler(MessageHandler(filters.Regex('Tether, курс'), get_tether_price))
    application.add_handler(MessageHandler(filters.Regex('BNB, курс'), get_bnb_price))
    application.add_handler(MessageHandler(filters.Regex('Solana, курс'), get_solana_price))
    application.add_handler(MessageHandler(filters.Regex('USDC, курс'), get_usdc_price))
    application.add_handler(MessageHandler(filters.Regex('XRP, курс'), get_xrp_price))
    application.add_handler(MessageHandler(filters.Regex('Toncoin, курс'), get_toncoin_price))
    application.add_handler(MessageHandler(filters.Regex('Dogecoin, курс'), get_dogecoin_price))
    application.add_handler(MessageHandler(filters.Regex('Cardano, курс'), get_cardano_price))
    # ----------------------------------------------Суточные объемы торгов---------------------------------------
    application.add_handler(MessageHandler(filters.Regex('Bitcoin, суточный объем торгов'), get_bitcoin_daily_volume))
    application.add_handler(MessageHandler(filters.Regex('Ethereum, суточный объем торгов'), get_ethereum_daily_volume))
    application.add_handler(MessageHandler(filters.Regex('Tether, суточный объем торгов'), get_tether_daily_volume))
    application.add_handler(MessageHandler(filters.Regex('BNB, суточный объем торгов'), get_bnb_daily_volume))
    application.add_handler(MessageHandler(filters.Regex('Solana, суточный объем торгов'), get_solana_daily_volume))
    application.add_handler(MessageHandler(filters.Regex('USDC, суточный объем торгов'), get_usdc_daily_volume))
    application.add_handler(MessageHandler(filters.Regex('XRP, суточный объем торгов'), get_xrp_daily_volume))
    application.add_handler(MessageHandler(filters.Regex('Toncoin, суточный объем торгов'), get_toncoin_daily_volume))
    application.add_handler(MessageHandler(filters.Regex('Dogecoin, суточный объем торгов'), get_dogecoin_daily_volume))
    application.add_handler(MessageHandler(filters.Regex('Cardano, суточный объем торгов'), get_cardano_daily_volume))
    # --------------------------------------------------Рыночная капитализация-----------------------------------------
    application.add_handler(MessageHandler(filters.Regex('Bitcoin, рыночная капитализация'), get_bitcoin_market_cap))
    application.add_handler(MessageHandler(filters.Regex('Ethereum, рыночная капитализация'), get_ethereum_market_cap))
    application.add_handler(MessageHandler(filters.Regex('Tether, рыночная капитализация'), get_tether_market_cap))
    application.add_handler(MessageHandler(filters.Regex('BNB, рыночная капитализация'), get_bnb_market_cap))
    application.add_handler(MessageHandler(filters.Regex('Solana, рыночная капитализация'), get_solana_market_cap))
    application.add_handler(MessageHandler(filters.Regex('USDC, рыночная капитализация'), get_usdc_market_cap))
    application.add_handler(MessageHandler(filters.Regex('XRP, рыночная капитализация'), get_xrp_market_cap))
    application.add_handler(MessageHandler(filters.Regex('Toncoin, рыночная капитализация'), get_toncoin_market_cap))
    application.add_handler(MessageHandler(filters.Regex('Dogecoin, рыночная капитализация'), get_dogecoin_market_cap))
    application.add_handler(MessageHandler(filters.Regex('Cardano, рыночная капитализация'), get_cardano_market_cap))
    # ---------------------------------------Изменение за определенный промежуток времени------------------------------

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()
