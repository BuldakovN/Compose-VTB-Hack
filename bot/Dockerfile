FROM python:3.7

RUN python -m pip install pyTelegramBotAPI

WORKDIR /app

ADD telegram_bot.py telegram_bot.py

CMD [ "python3", "telegram_bot.py"]
