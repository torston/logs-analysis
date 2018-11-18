def most_popular_articles():
    return {}


def most_popular_authors():
    return {}


def more_than_percent_error():
    return {}


def find_answer(question_number: int):
    answer = {}

    if question_number == 1:
        answer = most_popular_articles()
    elif question_number == 2:
        answer = most_popular_authors()
    elif question_number == 3:
        answer = more_than_percent_error()

    print(answer)


def print_info():
    print('Hello, this application can give you an answer to following question:')
    print('1: What are the most popular three articles of all time?')
    print('2: Who are the most popular article authors of all time?')
    print('3: On which days did more than 1% of requests lead to errors?')
    print('Put the question number to get answer or anything else to exit application.')


if __name__ == '__main__':

    while True:
        print_info()

        try:
            question_number = int(input())
            is_valid = 1 <= question_number <= 3
            if is_valid:
                find_answer(question_number)
            else:
                break
        except:
            break