# CronEntry

class CronEntry(object):

    #  0      1        2        3          4         5       6
    Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday = range(7)

    #
    def __init__(self, schedule, cmd):
        self.minutes = self.parse_minutes(schedule.minutes)
        self.hours = self.parse_hours(schedule.hours)
        self.month_days = self.parse_month_days(schedule.month_days)
        self.months = self.parse_months(schedule.months)
        self.weekdays = self.parse_week_days(schedule.weekdays)

        self.command = cmd
        self.schedule = schedule

    #
    def parse_minutes(self, min_str):
        if min_str == '*':
            return min_str
        return [int(x) for x in min_str.split(',')]

    #
    def parse_hours(self, hour_str):
        if hour_str == '*':
            return hour_str
        return [int(x) for x in hour_str.split(',')]

    #
    def parse_month_days(self, day_str):
        if day_str == '*':
            return day_str
        return [int(x) for x in day_str.split(',')]

    #
    def parse_months(self, month_str):
        if month_str == '*':
            return month_str
        return [int(x) for x in month_str.split(',')]

    #
    def parse_week_days(self, day_str):
        if day_str == '*':
            return day_str
        return [int(x) for x in day_str.split(',')]










