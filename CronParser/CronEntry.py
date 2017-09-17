# CronEntry

import collections

class CronEntry(object):
#   0       1       2        3          4         5       6
    Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday = range(7)

    #
    def __init__(self, sched, cmd):
        self.minutes     = self.parseMinutes(sched.minutes)
        self.hours       = self.parseHours(sched.hours)
        self.month_days  = self.parseMonthDays(sched.month_days)
        self.months      = self.parseMonths(sched.months)
        self.weekdays    = self.parseWeekDays(sched.weekdays)

        self.command    = cmd
        self.sched      = sched

    #
    def parseMinutes(self, min_str):
        if min_str == '*':
            return min_str
        return [int(x) for x in min_str.split(',')]

    #
    def parseHours(self, hour_str):
        if hour_str == '*':
            return hour_str
        return [int(x) for x in hour_str.split(',')]

    #
    def parseMonthDays(self, day_str):
        if day_str == '*':
            return day_str
        return [int(x) for x in day_str.split(',')]

    #
    def parseMonths(self, month_str):
        if month_str == '*':
            return month_str
        return [int(x) for x in month_str.split(',')]

    #
    def parseWeekDays(self, day_str):
        if day_str == '*':
            return day_str
        return [int(x) for x in day_str.split(',')]










