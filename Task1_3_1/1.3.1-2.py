import datetime
import pytz
from pytz import timezone


def time_between_cities(first_city, second_city):
    server_time = datetime.datetime.utcnow()
    first = timezone(first_city).fromutc(server_time)
 #   dt_kiev = datetime.datetime.now(first)

    second = timezone(second_city).fromutc(server_time)
 #   dt_berlin = datetime.datetime.now(second)


    delta = first.hour - second.hour
    return f' First city {first}\n Second city {second}\n Difference between cities {delta}'


if __name__ == "__main__":
    print(time_between_cities('Europe/Kiev', 'America/New_York'))
 #   print(pytz.all_timezones)






