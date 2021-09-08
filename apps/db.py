import pymysql
from apps import config

_connection = pymysql.connect(host=config.HOST, port=config.PORT, user=config.user, password=config.password,
                              db='health')


def cursor():
    cursor = _connection.cursor()
    return cursor
