import secrets

class Config:
    DEBUG = True
    HOST = "0.0.0.0"
    SECRET_KEY = secrets.token_hex(16)
    MONGO_URI = "mongodb://localhost:27017/monitoring_db"
