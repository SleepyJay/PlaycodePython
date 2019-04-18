
from datetime import timedelta, datetime, date

'''This is a bunch of sugar around date time stuff.'''
# Without this sugar, though, I kept mixing stuff up everywhere. This helped greatly to clarify.


#
def string_to_date(dt_str):
    return datetime.strptime(dt_str, '%m/%d/%Y')


#
def date_to_string(dt_obj):
    return "{}/{}/{}".format(dt_obj.month, dt_obj.day, dt_obj.year)


#
def yyyymmdd_to_date(yy, mm, dd):
    return datetime(year=int(yy), month=int(mm), day=int(dd))


#
def now_date():
    return datetime.now()


#
def now_string():
    return date_to_string(datetime.now())


#
def add_days(dt_obj, d):
    return ( dt_obj + timedelta(days=d) )

