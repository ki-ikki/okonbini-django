from .base import *
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# GEMINI API KEY
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # PostgreSQL 用のバックエンドを指定
        'NAME': 'okonbini_db',  # データベース名
        'USER': 'administrator',  # ユーザー名
        'PASSWORD': 'administrator',  # パスワード
        'HOST': 'okonbini-postgre',  # PostgreSQL サービス名（docker-compose.yml のサービス名と一致）
        'PORT': '5432',  # ポート番号
    }
}
