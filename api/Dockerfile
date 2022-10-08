FROM python:3.7

RUN python -m pip install flask flask_restful gunicorn psycopg2-binary

WORKDIR /app

ADD main_api.py main_api.py
ADD api_db.py api_db.py

EXPOSE 1707

CMD [ "gunicorn", "--bind", "0.0.0.0:1707", "main_api:app" ]
