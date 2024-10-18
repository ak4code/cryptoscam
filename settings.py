from environs import Env

env = Env()
env.read_env()

# SECRET_KEY tg_bot
TELEGRAM_BOT_TOKEN = env("TELEGRAM_BOT_TOKEN")
CRYPTO_API_KEY = env("CRYPTO_API_KEY")
