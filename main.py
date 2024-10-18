from environs import Env
import telebot


env = Env()
env.read_env()
env.str("SECRET_TOKEN") # => SOMETHING
bot = telebot.TeleBot("secret_token", parse_mode='html')

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

