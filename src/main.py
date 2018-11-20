#!/usr/bin/env python

import psycopg2

DB_NAME = 'news'


def most_popular_articles():
    articles = query_db("""
        SELECT articles.title, count(*) as views 
        FROM log INNER JOIN articles 
        ON log.path = CONCAT('/article/', articles.slug) 
        GROUP BY articles.title 
        ORDER BY views DESC 
        LIMIT 3
        """
    )

    return articles, '"{0}" - {1} views'


def most_popular_authors():
    authors = query_db("""
        SELECT name, count(*) as views 
        FROM log INNER JOIN 
        (SELECT articles.slug, articles.title, authors.name 
        FROM articles JOIN authors 
        ON articles.author = authors.id) as authors_articles 
        ON log.path = CONCAT('/article/', authors_articles.slug) 
        GROUP BY name 
        ORDER BY views DESC
        """
    )

    return authors, '{0} - {1} views'


def more_than_percent_error():
    errors = query_db("""
        SELECT TO_CHAR(time::date,'FMMonth DD, YYYY'),
        round((count(CASE WHEN status !=  '200 OK' THEN 1 END) * 100 
        / count(status)::numeric), 1) as percent 
        FROM log 
        GROUP BY time::date 
        having count(CASE WHEN status !=  '200 OK' THEN 1 END) * 100 
        / count(status)::numeric >= 1
        """
    )

    return errors, '{0} - {1}% errors'


def query_db(query):
    db = psycopg2.connect(database=DB_NAME)
    c = db.cursor()
    c.execute(query)
    result = c.fetchall()
    db.close()
    return result


def print_answer(result):
    print('')
    print('Answer:')
    for element in result[0]:
        print(result[1].format(element[0], element[1]))

    print('')


def find_answer(number):
    answer = []

    if number == 1:
        answer = most_popular_articles()
    elif number == 2:
        answer = most_popular_authors()
    elif number == 3:
        answer = more_than_percent_error()

    print_answer(answer)


def print_info():
    print('1: What are the most popular three articles of all time?')
    print('2: Who are the most popular article authors of all time?')
    print('3: On which days did more than 1% of requests lead to errors?')
    print('')
    print('Put the question number or anything else to exit application.')


if __name__ == '__main__':
    print('This application can give you an answer to following question:')
    while True:
        print_info()

        try:
            question_number = int(input("Enter question number:"))
            is_valid = 1 <= question_number <= 3
            if is_valid:
                find_answer(question_number)
            else:
                break
        except Exception as e:
            print(e)
            break
