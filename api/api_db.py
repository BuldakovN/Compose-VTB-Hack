import psycopg2
from psycopg2 import Error
from psycopg2 import sql

#connection = psycopg2.connect("host=89.208.231.41 dbname=VTB-Hack user=user password=262}ym2C0A79vdFw")

# Самые подходящие новости для этой роли
# мексимально 5 новостей
def main_news(type_person):
    # соединение с БД
    connection = psycopg2.connect(
        user="user",
        password="262}ym2C0A79vdFw",
        host="89.208.231.41",
        database="VTB-Hack"
    )
    try:
        # запрос к БД
        cursor = connection.cursor()
        cursor.execute(sql.SQL("SELECT id, title, link, source_name, publish_date, subjects_category, description, full_text, " + type_person + " FROM {} ORDER BY " + type_person + " DESC LIMIT 3").format(sql.Identifier('NewsTable')))
        # считываем данные
        news_records = cursor.fetchall()

        # хранение результата
        mas_news = []


        for row in news_records:
            mas_news.append(row)
        return mas_news


    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")




print(main_news("score_role_1"))