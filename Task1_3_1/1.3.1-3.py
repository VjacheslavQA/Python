import datetime
from collections import namedtuple

def define_age_and_zodiac():
    date_of_birthday = datetime.datetime.strptime(input("Enter your Birthday in the format d-m-y: "), "%d-%m-%Y")
    today = datetime.date.today()
    day = date_of_birthday.day
    month = date_of_birthday.month
    year = date_of_birthday.year
    age = today.year - year - ((today.month, today.day) < (month, day))
    zodiac = ''
    if (date_of_birthday.month == 3 and 21 <= date_of_birthday.day <= 31) or (
            date_of_birthday.month == 4 and 1 <= date_of_birthday.day <= 20):
        zodiac = 'Овен'
    elif (date_of_birthday.month == 4 and 21 <= date_of_birthday.day <= 31) or (
            date_of_birthday.month == 5 and 1 <= date_of_birthday.day <= 20):
        zodiac = 'Телец'
    elif (date_of_birthday.month == 5 and 21 <= date_of_birthday.day <= 31) or (
            date_of_birthday.month == 6 and 1 <= date_of_birthday.day <= 21):
        zodiac = 'Близнецы'
    elif (date_of_birthday.month == 6 and 22 <= date_of_birthday.day <= 31) or (
            date_of_birthday.month == 7 and 1 <= date_of_birthday.day <= 22):
        zodiac = 'Рак'
    elif (date_of_birthday.month == 7 and 23 <= date_of_birthday.day <= 31) or (
            date_of_birthday.month == 8 and 1 <= date_of_birthday.day <= 23):
        zodiac = 'Лев'
    elif (date_of_birthday.month == 8 and 24 <= date_of_birthday.day <= 31) or (
            date_of_birthday.month == 9 and 1 <= date_of_birthday.day <= 23):
        zodiac = 'Дева'
    elif (date_of_birthday.month == 9 and 24 <= date_of_birthday.day <= 31) or (
            date_of_birthday.month == 10 and 1 <= date_of_birthday.day <= 23):
        zodiac = 'Весы'
    elif (date_of_birthday.month == 10 and 24 <= date_of_birthday.day <= 31) or (
            date_of_birthday.month == 11 and 1 <= date_of_birthday.day <= 22):
        zodiac = 'Скорпион'
    elif (date_of_birthday.month == 11 and 23 <= date_of_birthday.day <= 31) or (
            date_of_birthday.month == 12 and 1 <= date_of_birthday.day <= 21):
        zodiac = 'Стрелец'
    elif (date_of_birthday.month == 12 and 22 <= date_of_birthday.day <= 31) or (
            date_of_birthday.month == 1 and 1 <= date_of_birthday.day <= 20):
        zodiac = 'Козерог'
    elif (date_of_birthday.month == 1 and 21 <= date_of_birthday.day <= 31) or (
            date_of_birthday.month == 2 and 1 <= date_of_birthday.day <= 20):
        zodiac = 'Водолей'
    elif (date_of_birthday.month == 2 and 21 <= date_of_birthday.day <= 31) or (
            date_of_birthday.month == 3 and 1 <= date_of_birthday.day <= 20):
        zodiac = 'Рыбы'
    Result = namedtuple('Result', 'Age Zodiac')
    dict = Result(age, zodiac)

    return dict


if __name__ == '__main__':
    print(define_age_and_zodiac())
