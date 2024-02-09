#----------------------------------- https://github.com/m4mallu/clonebot --------------------------------------------#
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("6759047715:AAFh1u9cSjnwBguLASEaZveCqcrOlmu08no", "")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("16494736", ""))

    # Get from my.telegram.org
    API_HASH = os.environ.get("2cb7fa5859e2de684e3e10d9c049621a", "")

    # Generate a user session string
    TG_USER_SESSION = os.environ.get("BQD7sJAAk6CywfJvQ90OhQbFwvP_LU4xZVSsmtNr1GSs3kHk_ebEPWFRO5B5x-dRaqsXr8dj0Qg30HbCdf0QwLsgx5b_xJbkUb-NZGqOt_7B4MH3fMs3W7h8ZcwQdm0KJHkhAp5ewZq7ltAXHeQTmu9MNloC8Q_2WuDEn8nlclKJxMDdfiaImr4pPp3hBghAFJR-W06AFgAPU-spJCj1BcbZe4JIFI0PVhfv-sHH9sb4y291boAe0cw4HLEzyLH6ti_j8swiX8wJHmfOezx-I0i-5DbWPhLCoKavrLcmec_scyq4MVoD5mhMnYPhNlMeIFXwZZSwXCQPBmoHuhnQQ2yncDqQ2wAAAAEuQunIAA", "")

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
