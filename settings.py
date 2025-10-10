from dotenv import load_dotenv
from typing import Union,Tuple
import os

load_dotenv()


class Settings():
    def __init__(self):
        self.bot_prefix: str = os.getenv('BOT_PREFIX','!')
        self.bot_token: str = os.getenv('BOT_TOKEN','notatoken')
        self.host: str = os.getenv('NODE_HOST','localhost')
        self.port: int = os.getenv('NODE_PORT',2333)
        self.password: str = os.getenv('NODE_PASSWORD','youshallnotpass')
        self.secure: bool = os.getenv('NODE_SECURE',False)


bot_config = Settings()
try:
    # Bot prefix
    bot_prefix: str = bot_config.bot_prefix if bot_config.bot_prefix != '' else '!'

    # Token ve host
    bot_token: str = bot_config.bot_token if bot_config.bot_token != '' else 'notatoken'
    host: str = bot_config.host if bot_config.host != '' else 'localhost'
    port: int = bot_config.port if bot_config.port != '' else 2333

    # Şifre kontrolü
    password: str = bot_config.password if bot_config.password != '' else 'youshallnotpass'
    secure: bool = bot_config.secure if bot_config.secure != '' else False
except ValueError as ve:
    print(f'{ve}')
except Exception as e:
    print(f'Exception: {e}')
