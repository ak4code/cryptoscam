import telebot
import settings
import re

__crypta = ['bts', 'bitcoin', 'eth', 'ethereum', 'usdt', 'xrp', 'ripple', 'ton']
def get_crypto_list(message):
	crypto_list = []
	massage_words = re.findall(r'\w+', message.text.lower())
	specify_currency_message = f'Какая валюта вас интересует?'
	for i in massage_words:
		if i in __crypta:
			crypto_list.append(i)
		if crypto_list == []:
			return bot.reply_to(message, specify_currency_message)
	return crypto_list

bot = telebot.TeleBot(settings.TELEGRAM_BOT_TOKEN, parse_mode='html')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Бабки есть?")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
	if message != 'Есть':
		nice_reply_massage = f'{message.from_user.first_name}, жду бабки на карту, beach!'
		bot.reply_to(message, nice_reply_massage)
		return
	bad_reply_massage = f'Бичам тут не место'
	bot.reply_to(message, bad_reply_massage)


if __name__ == "__main__":
	bot.infinity_polling()

