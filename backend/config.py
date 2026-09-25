import os 
from datetime import timedelta
from dotenv import load_dotenv
BASE = os.path.abspath(os.path.dirname(__file__))

load_dotenv()

class Config:
    
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE,'instance','PPA_V2.db')}"

    SECRET_KEY = "Placement_Portal_V2_26F2"

    SQLALCHEMY_TRACK_NOTIFICATIONS = False

    JWT_SECRET_KEY = "jwt_PPA_V2"

    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=15)

    CACHE_TYPE = "RedisCache"

    CACHE_REDIS_URL = "redis://localhost:6379/1"

    CACHE_DEFAULT_TIMEOUT = 300

    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True

    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")

    MAIL_DEFAULT_SENDER = os.getenv("MAIL_USERNAME")
