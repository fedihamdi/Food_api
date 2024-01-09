import os
from dotenv import load_dotenv


PROPAGATE_EXCEPTIONS = True
# ENVIRONNEMENT CONFIGURATION

## Load .env file
load_dotenv(verbose=True)

## Get these value from .env or from environnement

OPEN_FOOD_FACT_URL = os.getenv("OPEN_FOOD_FACT_URL", default="https://world.openfoodfacts.org")
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", default="secret-key-123")

## Database config

DEVELOPMENT = True
DEBUG = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", default="postgresql://postgres:mysecretpassword@localhost:5432/postgres")