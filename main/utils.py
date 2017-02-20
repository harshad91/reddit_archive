import datetime


def init_timestamp(year):
    return datetime.datetime(int(year), 1, 1)


def add_days(dtm, days=365):
    return dtm + datetime.timedelta(days=days)

if __name__ == "__main__":
    print add_days(datetime.datetime.now())
