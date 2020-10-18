import logging

from telegram.ext import Updater

import config

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

updater = Updater(token=config.bot_token)

updater.start_polling(config.polling_interval)

updater.idle()
