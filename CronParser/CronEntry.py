# CronEntry

class CronEntry(object):

    #
    def __init__(self, sched, cmd):
        min, hr, dmo, mon, dow = sched.split()

        self.min_part         = min  # 1
        self.hour_part        = hr   # 2
        self.day_month_part   = dmo  # 3
        self.month_part       = mon  # 4
        self.day_of_week_part = dow  # 5
        self.command          = cmd  # 6

        









