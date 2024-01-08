# CODING: UTF8
# CIC PORTAL
from dotenv import load_dotenv
import json
import os


load_dotenv()

DB_CIC = json.loads(os.getenv("CIC_SETTINGS"))
DB_ERP = json.loads(os.getenv("ERP_SETTINGS"))
DB_VENDA = json.loads(os.getenv("VENDA_SETTINGS"))


class Config(object):
    SECRET_KEY = "c219d4e3-3ea8-4dbb-8641-C1C-P0RT4L-3ea8-4dbb-8641-8bbfc644aa18"
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///development.sqlite"
    SQLALCHEMY_BINDS = { # Optional
        "QAS": "sqlite:///quality_assurance.sqlite",
        "UAT": "sqlite:///user_acceptance.sqlite"
    }
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_ADMIN_SWATCH = 'Darkly' # https://bootswatch.com/3/

class DevelopmentConfig(Config):
    # SQLALCHEMY_DATABASE_URI = "postgresql://{user}:{password}@{host}:{port}/{database}?{options}".format(**DB_CIC) # Default
    DEVELOPMENT = True
    DEBUG = True

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql://{user}:{password}@{host}:{port}/{database}?{options}".format(**DB_CIC) # Default
    DEBUG = False

