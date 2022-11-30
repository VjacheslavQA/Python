import datetime


def friday13():

    today = datetime.date.today()
    friday13th = []

    future = datetime.timedelta(days=1)

    while len(friday13th) < 10:
        if today.day == 13 and today.isoweekday() == 5:
            friday13th.append(today.strftime("%a %d %B %Y"))

        today += future

    return friday13th

if __name__ == "__main__":
    print(friday13())

