from .common import *
import pymysql

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jssww*6b_kyyax3=sc+!#&f*&j3&ph9@a7zpiitb^w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

pymysql.install_as_MySQLdb()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',   # 数据库引擎
        'NAME': 'blog',         # 你要存储数据的库名，事先要创建之
        'USER': 'root',         # 数据库用户名
        'PASSWORD': 'yuzongxian199824',     # 密码
        'HOST': 'localhost',    # 主机
        'PORT': '3306',         # 数据库使用的端口
        'TIME_ZONE': 'Asia/Shanghai',       # 数据库时区
        'USE_TZ': False,        # 数据库时区启用
    }
}