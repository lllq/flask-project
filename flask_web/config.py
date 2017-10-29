# _*_ coding:utf-8 _*_
# __author__ = 'll'
import os

SECRET_KEY = os.urandom(24)
DEBUG = True

DIALECT = 'mysql'
DRIVER = 'mysqldb'
USERNAME = 'root'
PASSWORD = 'mysql'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE ='zhihu'

SQLALCHEMY_DATABASE_URI="{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)