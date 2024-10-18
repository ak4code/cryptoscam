from environs import Env

env = Env()
env.read_env()

# SECRET_KEY tg_bot
secret_token = env("secret_token")
