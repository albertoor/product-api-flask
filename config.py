import os

class Configuration:
    MYSQL_HOST = "127.0.0.1"
    MYSQL_USER = "root"
    MYSQL_PASSWORD = "Bull87621."
    MYSQL_DB = "inventory_flask_db"
    MSYQL_PORT = 3306

class DevConfig():
    DEBUG = True

config = {
    'development':DevConfig
}