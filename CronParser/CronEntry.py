# CronEntry

class CronEntry(object):

    #
    def __init__(self, sched, cmd):
        min, hr, dmo, mon, dow = sched.split()

        self.minute     = min  # 1
        self.hour       = hr   # 2
        self.day_month  = dmo  # 3
        self.month      = mon  # 4
        self.day_week   = dow  # 5
        self.command    = cmd  # 6
        
        self.sched            = sched


        









