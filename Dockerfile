# ベースイメージの設定
FROM python:3.13

# Pythonの標準出力のバッファリングを解除して、出力を即座に表示できるよう設定
ENV PYTHONUNBUFFERED=1

# 作業ディレクトリの設定
WORKDIR /app

# pipの最新バージョンにアップグレード
RUN pip install --upgrade pip
RUN pip install --no-cache-dir psycopg
RUN pip install python-dotenv
RUN pip install icecream
RUN pip install beautifulsoup4
RUN pip install requests
RUN pip install -q -U google-generativeai
RUN apt-get update
RUN apt-get install -y postgresql-client

# 依存関係のインストール
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# ソースコードをコンテナ内にコピー
COPY . /app/