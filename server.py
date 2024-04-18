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


# -----------------------------------------Рыночная капитализация тут--------------------------------------------------

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


# ----------------------------------Изменение цены за определенный период тут-------------------------------------------
# ---------------------------------------------------1 час--------------------------------------------------------------
def get_1h_percent_change(symbol, api_key='0f3fc9c2-0644-4f21-b821-af5ad27f8cf9'):
    url = f"https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol={symbol}"
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key,
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        data = response.json()

        percent_change_1h = data['data'][symbol]['quote']['USD']['percent_change_1h']

        if percent_change_1h < 0:
            return f"уменьшилось на {abs(percent_change_1h):.2f}%"
        else:
            return f"увеличилось на {percent_change_1h:.2f}%"
    except Exception as e:
        return f"Произошла ошибка: {str(e)}"


async def get_bitcoin_1h_change(update: Update, context: ContextTypes.DEFAULT_TYPE):
    bitcoin_1h_percent_change = get_1h_percent_change('BTC')
    await update.message.reply_text("1-часовое изменение цены Bitcoin: " + str(bitcoin_1h_percent_change))


async def get_ethereum_1h_change(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ethereum_1h_percent_change = get_1h_percent_change('ETH')
    await update.message.reply_text("1-часовое изменение цены Эфириума: " + str(ethereum_1h_percent_change))


async def get_tether_1h_change(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tether_1h_percent_change = get_1h_percent_change('USDT')
    await update.message.reply_text("1-часовое изменение цены Тезера: " + str(tether_1h_percent_change))


async def get_bnb_1h_change(update: Update, context: ContextTypes.DEFAULT_TYPE):
    bnb_1h_percent_change = get_1h_percent_change('BNB')
    await update.message.reply_text("1-часовое изменение цены BNB: " + str(bnb_1h_percent_change))


async def get_solana_1h_change(update: Update, context: ContextTypes.DEFAULT_TYPE):
    sol_1h_percent_change = get_1h_percent_change('SOL')
    await update.message.reply_text("1-часовое изменение цены Соланы: " + str(sol_1h_percent_change))


async def get_usdc_1h_change(update: Update, context: ContextTypes.DEFAULT_TYPE):
    usdc_1h_percent_change = get_1h_percent_change('USDC')
    await update.message.reply_text("1-часовое изменение цены USDC: " + str(usdc_1h_percent_change))


async def get_xrp_1h_change(update: Update, context: ContextTypes.DEFAULT_TYPE):
    xrp_1h_percent_change = get_1h_percent_change('XRP')
    await update.message.reply_text("1-часовое изменение цены XRP: " + str(xrp_1h_percent_change))


async def get_dogecoin_1h_change(update: Update, context: ContextTypes.DEFAULT_TYPE):
    doge_1h_percent_change = get_1h_percent_change('DOGE')
    await update.message.reply_text("1-часовое изменение цены Dogecoin: " + str(doge_1h_percent_change))


async def get_toncoin_1h_change(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ton_1h_percent_change = get_1h_percent_change('TON')
    await update.message.reply_text("1-часовое изменение цены Toncoin: " + str(ton_1h_percent_change))


async def get_cardano_1h_change(update: Update, context: ContextTypes.DEFAULT_TYPE):
    cardano_1h_percent_change = get_1h_percent_change('ADA')
    await update.message.reply_text("1-часовое изменение цены Cardano: " + str(cardano_1h_percent_change))


# ------------------------------------------------2 часа---------------------------------------------------------------
def get_24h_percent_change(symbol, api_key='0f3fc9c2-0644-4f21-b821-af5ad27f8cf9'):
    url = f"https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol={symbol}"
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key,
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        data = response.json()

        percent_change_24h = data['data'][symbol]['quote']['USD']['percent_change_24h']

        if percent_change_24h < 0:
            return f"уменьшилось на {abs(percent_change_24h):.2f}%"
        else:
            return f"увеличилось на {percent_change_24h:.2f}%"
    except Exception as e:
        return f"Произошла ошибка: {str(e)}"


async def get_bitcoin_24h_change(update: Update, context: ContextTypes.DEFAULT_TYPE):
    bitcoin_24h_percent_change = get_24h_percent_change('BTC')
    await update.message.reply_text("24-часовое изменение цены Bitcoin: " + str(bitcoin_24h_percent_change))


async def get_ethereum_24h_change(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ethereum_24h_percent_change = get_24h_percent_change('ETH')
    await update.message.reply_text("24-часовое изменение цены Эфириума: " + str(ethereum_24h_percent_change))


async def get_tether_24h_change(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tether_24h_percent_change = get_24h_percent_change('USDT')
    await update.message.reply_text("24-часовое изменение цены Тезера: " + str(tether_24h_percent_change))


async def get_bnb_24h_change(update: Update, context: ContextTypes.DEFAULT_TYPE):
    bnb_24h_percent_change = get_24h_percent_change('BNB')
    await update.message.reply_text("24-часовое изменение цены BNB: " + str(bnb_24h_percent_change))


async def get_solana_24h_change(update: Update, context: ContextTypes.DEFAULT_TYPE):
    sol_24h_percent_change = get_24h_percent_change('SOL')
    await update.message.reply_text("24-часовое изменение цены Соланы: " + str(sol_24h_percent_change))


async def get_usdc_24h_change(update: Update, context: ContextTypes.DEFAULT_TYPE):
    usdc_24h_percent_change = get_24h_percent_change('USDC')
    await update.message.reply_text("24-часовое изменение цены USDC: " + str(usdc_24h_percent_change))


async def get_xrp_24h_change(update: Update, context: ContextTypes.DEFAULT_TYPE):
    xrp_24h_percent_change = get_24h_percent_change('XRP')
    await update.message.reply_text("24-часовое изменение цены XRP: " + str(xrp_24h_percent_change))


async def get_dogecoin_24h_change(update: Update, context: ContextTypes.DEFAULT_TYPE):
    doge_24h_percent_change = get_24h_percent_change('DOGE')
    await update.message.reply_text("24-часовое изменение цены Dogecoin: " + str(doge_24h_percent_change))


async def get_toncoin_24h_change(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ton_24h_percent_change = get_24h_percent_change('TON')
    await update.message.reply_text("24-часовое изменение цены Toncoin: " + str(ton_24h_percent_change))


async def get_cardano_24h_change(update: Update, context: ContextTypes.DEFAULT_TYPE):
    cardano_24h_percent_change = get_24h_percent_change('ADA')
    await update.message.reply_text("24-часовое изменение цены Cardano: " + str(cardano_24h_percent_change))


# ------------------------------------------------1 неделя-------------------------------------------------------------

def get_7d_percent_change(symbol, api_key='0f3fc9c2-0644-4f21-b821-af5ad27f8cf9'):
    url = f"https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol={symbol}"
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key,
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        data = response.json()

        percent_change_7d = data['data'][symbol]['quote']['USD']['percent_change_7d']

        if percent_change_7d < 0:
            return f"уменьшилось на {abs(percent_change_7d):.2f}%"
        else:
            return f"увеличилось на {percent_change_7d:.2f}%"
    except Exception as e:
        return f"Произошла ошибка: {str(e)}"

async def get_bitcoin_7d_change(update: Update, context: ContextTypes.DEFAULT_TYPE):
    bitcoin_7d_percent_change = get_7d_percent_change('BTC')
    await update.message.reply_text("24-часовое изменение цены Bitcoin: " + str(bitcoin_7d_percent_change))


async def get_ethereum_7d_change(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ethereum_7d_percent_change = get_7d_percent_change('ETH')
    await update.message.reply_text("24-часовое изменение цены Эфириума: " + str(ethereum_7d_percent_change))


async def get_tether_7d_change(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tether_7d_percent_change = get_7d_percent_change('USDT')
    await update.message.reply_text("24-часовое изменение цены Тезера: " + str(tether_7d_percent_change))


async def get_bnb_7d_change(update: Update, context: ContextTypes.DEFAULT_TYPE):
    bnb_7d_percent_change = get_7d_percent_change('BNB')
    await update.message.reply_text("24-часовое изменение цены BNB: " + str(bnb_7d_percent_change))


async def get_solana_7d_change(update: Update, context: ContextTypes.DEFAULT_TYPE):
    sol_7d_percent_change = get_7d_percent_change('SOL')
    await update.message.reply_text("24-часовое изменение цены Соланы: " + str(sol_7d_percent_change))


async def get_usdc_7d_change(update: Update, context: ContextTypes.DEFAULT_TYPE):
    usdc_7d_percent_change = get_7d_percent_change('USDC')
    await update.message.reply_text("24-часовое изменение цены USDC: " + str(usdc_7d_percent_change))


async def get_xrp_7d_change(update: Update, context: ContextTypes.DEFAULT_TYPE):
    xrp_7d_percent_change = get_7d_percent_change('XRP')
    await update.message.reply_text("24-часовое изменение цены XRP: " + str(xrp_7d_percent_change))


async def get_dogecoin_7d_change(update: Update, context: ContextTypes.DEFAULT_TYPE):
    doge_7d_percent_change = get_7d_percent_change('DOGE')
    await update.message.reply_text("24-часовое изменение цены Dogecoin: " + str(doge_7d_percent_change))


async def get_toncoin_7d_change(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ton_7d_percent_change = get_7d_percent_change('TON')
    await update.message.reply_text("24-часовое изменение цены Toncoin: " + str(ton_7d_percent_change))


async def get_cardano_7d_change(update: Update, context: ContextTypes.DEFAULT_TYPE):
    cardano_7d_percent_change = get_7d_percent_change('ADA')
    await update.message.reply_text("24-часовое изменение цены Cardano: " + str(cardano_7d_percent_change))


# -------------------------------------------Паттерны свечей тут-------------------------------------------------------

async def show_random_pattern(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_photo(f"data/{random.randint(1, 10)}.jpg")


# ------------------------------------------Топ криптовалют тут-------------------------------------------------------
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


# --------------------------------------------------Функции бота-------------------------------------------------------
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Выберите действие:",
                                    reply_markup=ReplyKeyboardMarkup(
                                        [['Топ 10 криптовалют'],
                                         ['Узнать суточный объем торгов криптовалюты'],
                                         ['Узнать курс криптовалюты'],
                                         ['Узнать рыночную капитализацию криптовалюты'],
                                         ['Узнать изменение цены криптовалюты за определенный период'],
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
                                         ['Узнать изменение цены криптовалюты за определенный период'],
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
                                        [['Bitcoin, суточный объем торгов'], ['Ethereum, суточный объем торгов'],
                                         ['Tether, суточный объем торгов'], ['BNB, суточный объем торгов'],
                                         ['Solana, суточный объем торгов'], ['USDC, суточный объем торгов'],
                                         ['XRP, суточный объем торгов'], ['Toncoin, суточный объем торгов'],
                                         ['Dogecoin, суточный объем торгов'], ['Cardano, суточный объем торгов'],
                                         ['Назад']],
                                        one_time_keyboard=True))


async def marketcappanel(update: Update, context: CallbackContext):
    await update.message.reply_text("Выберите криптовалюту, рыночную капитализацию которой вы хотите знать:",
                                    reply_markup=ReplyKeyboardMarkup(
                                        [['Bitcoin, рыночная капитализация'], ['Ethereum, рыночная капитализация'],
                                         ['Tether, рыночная капитализация'], ['BNB, рыночная капитализация'],
                                         ['Solana, рыночная капитализация'], ['USDC, рыночная капитализация'],
                                         ['XRP, рыночная капитализация'], ['Toncoin, рыночная капитализация'],
                                         ['Dogecoin, рыночная капитализация'], ['Cardano, рыночная капитализация'],
                                         ['Назад']],
                                        one_time_keyboard=True))


async def changepanel(update: Update, context: CallbackContext):
    await update.message.reply_text("Выберите криптовалюту, изменение цены которой "
                                    "за определенный срок вы хотите знать:",
                                    reply_markup=ReplyKeyboardMarkup(
                                        [['Bitcoin, изменение цены'], ['Ethereum, изменение цены'],
                                         ['Tether, изменение цены'], ['BNB, изменение цены'],
                                         ['Solana, изменение цены'], ['USDC, изменение цены'],
                                         ['XRP, изменение цены'], ['Toncoin, изменение цены'],
                                         ['Dogecoin, изменение цены'], ['Cardano, изменение цены'],
                                         ['Назад']],
                                        one_time_keyboard=True))


async def bitcoinchangepanel(update: Update, context: CallbackContext):
    await update.message.reply_text("Выберите период, за который вы хотите знать изменение цены Bitcoin:",
                                    reply_markup=ReplyKeyboardMarkup(
                                        [['Bitcoin, 1 час'],
                                         ['Bitcoin, 24 часа'],
                                         ['Bitcoin, 1 неделя'],
                                         ['Hазад']],
                                        one_time_keyboard=True))


async def ethereumchangepanel(update: Update, context: CallbackContext):
    await update.message.reply_text("Выберите период, за который вы хотите знать изменение цены Ethereum:",
                                    reply_markup=ReplyKeyboardMarkup(
                                        [['Ethereum, 1 час'],
                                         ['Ethereum, 24 часа'],
                                         ['Ethereum, 1 неделя'],
                                         ['Hазад']],
                                        one_time_keyboard=True))


async def tetherchangepanel(update: Update, context: CallbackContext):
    await update.message.reply_text("Выберите период, за который вы хотите знать изменение цены Tether:",
                                    reply_markup=ReplyKeyboardMarkup(
                                        [['Tether, 1 час'],
                                         ['Tether, 24 часа'],
                                         ['Tether, 1 неделя'],
                                         ['Hазад']],
                                        one_time_keyboard=True))


async def bnbchangepanel(update: Update, context: CallbackContext):
    await update.message.reply_text("Выберите период, за который вы хотите знать изменение цены BNB:",
                                    reply_markup=ReplyKeyboardMarkup(
                                        [['BNB, 1 час'],
                                         ['BNB, 24 часа'],
                                         ['BNB, 1 неделя'],
                                         ['Hазад']],
                                        one_time_keyboard=True))


async def solanachangepanel(update: Update, context: CallbackContext):
    await update.message.reply_text("Выберите период, за который вы хотите знать изменение цены Solana:",
                                    reply_markup=ReplyKeyboardMarkup(
                                        [['Solana, 1 час'],
                                         ['Solana, 24 часа'],
                                         ['Solana, 1 неделя'],
                                         ['Hазад']],
                                        one_time_keyboard=True))


async def usdcchangepanel(update: Update, context: CallbackContext):
    await update.message.reply_text("Выберите период, за который вы хотите знать изменение цены USDC:",
                                    reply_markup=ReplyKeyboardMarkup(
                                        [['USDC, 1 час'],
                                         ['USDC, 24 часа'],
                                         ['USDC, 1 неделя'],
                                         ['Hазад']],
                                        one_time_keyboard=True))


async def xrpchangepanel(update: Update, context: CallbackContext):
    await update.message.reply_text("Выберите период, за который вы хотите знать изменение цены XRP:",
                                    reply_markup=ReplyKeyboardMarkup(
                                        [['XRP, 1 час'],
                                         ['XRP, 24 часа'],
                                         ['XRP, 1 неделя'],
                                         ['Hазад']],
                                        one_time_keyboard=True))


async def toncoinchangepanel(update: Update, context: CallbackContext):
    await update.message.reply_text("Выберите период, за который вы хотите знать изменение цены Toncoin:",
                                    reply_markup=ReplyKeyboardMarkup(
                                        [['Toncoin, 1 час'],
                                         ['Toncoin, 24 часа'],
                                         ['Toncoin, 1 неделя'],
                                         ['Hазад']],
                                        one_time_keyboard=True))


async def dogecoinchangepanel(update: Update, context: CallbackContext):
    await update.message.reply_text("Выберите период, за который вы хотите знать изменение цены Dogecoin:",
                                    reply_markup=ReplyKeyboardMarkup(
                                        [['Dogecoin, 1 час'],
                                         ['Dogecoin, 24 часа'],
                                         ['Dogecoin, 1 неделя'],
                                         ['Hазад']],
                                        one_time_keyboard=True))


async def cardanochangepanel(update: Update, context: CallbackContext):
    await update.message.reply_text("Выберите период, за который вы хотите знать изменение цены Cardano:",
                                    reply_markup=ReplyKeyboardMarkup(
                                        [['Cardano, 1 час'],
                                         ['Cardano, 24 часа'],
                                         ['Cardano, 1 неделя'],
                                         ['Hазад']],
                                        one_time_keyboard=True))


async def upload_license(update: Update, context: CallbackContext):
    await update.message.reply_document("LICENSE.txt")


# --------------------------------------------------Тут основа, база---------------------------------------------------
def main(show_crypto_price=None, show_top_cryptocurrencies=None) -> None:
    application = Application.builder().token(API_KEY).build()
    # ----------------------------------------------Системные функции--------------------------------------------------
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("actionspanel", actionspanel))
    application.add_handler(MessageHandler(filters.Regex("Назад"), actionspanel))
    application.add_handler(MessageHandler(filters.Regex("Hазад"), changepanel))
    application.add_handler(MessageHandler(filters.Regex('Узнать курс криптовалюты'), pricepanel))
    application.add_handler(MessageHandler(filters.Regex('Узнать суточный объем торгов криптовалюты'),
                                           dailyvolumepanel))
    application.add_handler(MessageHandler(filters.Regex('Показать случайный паттерн курса'), show_random_pattern))
    application.add_handler(MessageHandler(filters.Regex('Скачать лицензию'), upload_license))
    application.add_handler(MessageHandler(filters.Regex('Узнать рыночную капитализацию криптовалюты'), marketcappanel))
    application.add_handler(MessageHandler(filters.Regex('Узнать изменение цены криптовалюты за определенный период'),
                                           changepanel))
    # ----------------------------------------------Топы  криптовалют--------------------------------------------------
    application.add_handler(MessageHandler(filters.Regex('Топ 10 криптовалют'), show_10))
    application.add_handler(MessageHandler(filters.Regex('Топ 20 криптовалют'), show_20))
    application.add_handler(MessageHandler(filters.Regex('Топ 40 криптовалют'), show_40))
    # -----------------------------------------------Курсы криптовалют-------------------------------------------------
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
    # ----------------------------------------------Суточные объемы торгов---------------------------------------------
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
    application.add_handler(MessageHandler(filters.Regex('Bitcoin, изменение цены'), bitcoinchangepanel))
    application.add_handler(MessageHandler(filters.Regex('Ethereum, изменение цены'), ethereumchangepanel))
    application.add_handler(MessageHandler(filters.Regex('Tether, изменение цены'), tetherchangepanel))
    application.add_handler(MessageHandler(filters.Regex('BNB, изменение цены'), bnbchangepanel))
    application.add_handler(MessageHandler(filters.Regex('Solana, изменение цены'), solanachangepanel))
    application.add_handler(MessageHandler(filters.Regex('USDC, изменение цены'), usdcchangepanel))
    application.add_handler(MessageHandler(filters.Regex('XRP, изменение цены'), xrpchangepanel))
    application.add_handler(MessageHandler(filters.Regex('Toncoin, изменение цены'), toncoinchangepanel))
    application.add_handler(MessageHandler(filters.Regex('Dogecoin, изменение цены'), dogecoinchangepanel))
    application.add_handler(MessageHandler(filters.Regex('Cardano, изменение цены'), cardanochangepanel))
    # ------------------------------------------------1 час------------------------------------------------------------
    application.add_handler(MessageHandler(filters.Regex('Bitcoin, 1 час'), get_bitcoin_1h_change))
    application.add_handler(MessageHandler(filters.Regex('Ethereum, 1 час'), get_ethereum_1h_change))
    application.add_handler(MessageHandler(filters.Regex('Tether, 1 час'), get_tether_1h_change))
    application.add_handler(MessageHandler(filters.Regex('BNB, 1 час'), get_bnb_1h_change))
    application.add_handler(MessageHandler(filters.Regex('Solana, 1 час'), get_solana_1h_change))
    application.add_handler(MessageHandler(filters.Regex('USDC, 1 час'), get_usdc_1h_change))
    application.add_handler(MessageHandler(filters.Regex('XRP, 1 час'), get_xrp_1h_change))
    application.add_handler(MessageHandler(filters.Regex('Toncoin, 1 час'), get_toncoin_1h_change))
    application.add_handler(MessageHandler(filters.Regex('Dogecoin, 1 час'), get_dogecoin_1h_change))
    application.add_handler(MessageHandler(filters.Regex('Cardano, 1 час'), get_cardano_1h_change))
    # -----------------------------------------------24 часа-----------------------------------------------------------
    application.add_handler(MessageHandler(filters.Regex('Bitcoin, 24 часа'), get_bitcoin_24h_change))
    application.add_handler(MessageHandler(filters.Regex('Ethereum, 24 часа'), get_ethereum_24h_change))
    application.add_handler(MessageHandler(filters.Regex('Tether, 24 часа'), get_tether_24h_change))
    application.add_handler(MessageHandler(filters.Regex('BNB, 24 часа'), get_bnb_24h_change))
    application.add_handler(MessageHandler(filters.Regex('Solana, 24 часа'), get_solana_24h_change))
    application.add_handler(MessageHandler(filters.Regex('USDC, 24 часа'), get_usdc_24h_change))
    application.add_handler(MessageHandler(filters.Regex('XRP, 24 часа'), get_xrp_24h_change))
    application.add_handler(MessageHandler(filters.Regex('Toncoin, 24 часа'), get_toncoin_24h_change))
    application.add_handler(MessageHandler(filters.Regex('Dogecoin, 24 часа'), get_dogecoin_24h_change))
    application.add_handler(MessageHandler(filters.Regex('Cardano, 24 часа'), get_cardano_24h_change))
    # ------------------------------------------------1 неделя--------------------------------------------------------
    application.add_handler(MessageHandler(filters.Regex('Bitcoin, 1 неделя'), get_bitcoin_7d_change))
    application.add_handler(MessageHandler(filters.Regex('Ethereum, 1 неделя'), get_ethereum_7d_change))
    application.add_handler(MessageHandler(filters.Regex('Tether, 1 неделя'), get_tether_7d_change))
    application.add_handler(MessageHandler(filters.Regex('BNB, 1 неделя'), get_bnb_7d_change))
    application.add_handler(MessageHandler(filters.Regex('Solana, 1 неделя'), get_solana_7d_change))
    application.add_handler(MessageHandler(filters.Regex('USDC, 1 неделя'), get_usdc_7d_change))
    application.add_handler(MessageHandler(filters.Regex('XRP, 1 неделя'), get_xrp_7d_change))
    application.add_handler(MessageHandler(filters.Regex('Toncoin, 1 неделя'), get_toncoin_7d_change))
    application.add_handler(MessageHandler(filters.Regex('Dogecoin, 1 неделя'), get_dogecoin_7d_change))
    application.add_handler(MessageHandler(filters.Regex('Cardano, 1 неделя'), get_cardano_7d_change))
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()
