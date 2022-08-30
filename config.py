import os
from dotenv import load_dotenv

load_dotenv()

FLASK_ENV = ENV = os.getenv('ENVIRONMENT')

if FLASK_ENV == "development":
    DEBUG = True

SCHEDULER_API_ENABLED = True

MAIL_SERVER = "smtp.gmail.com"
MAIL_PORT = 465
MAIL_USERNAME = MAIL_DEFAULT_SENDER = os.getenv('MAIL_USERNAME')
MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
MAIL_USE_TLS = False
MAIL_USE_SSL = True
