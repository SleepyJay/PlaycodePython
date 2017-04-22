# CronParser

import re

class CronParser(object):

    #
    def __init__(self):
        #self.re_cron_line = re.compile('\s*([^\s])\s+([^\s])\s+([^\s])\s+([^\s])\s+([^\s])\s+.+')
        self.re_cron_line = re.compile('\s*(([^\s])\s+){5}.+')
        
    #
    def loadFile(self, file_path):
        f = open(file_path, 'r')

        if not f:
            # Exception?
            pass

        line_num = 0

        for line in f:
            line_num += 1

            if line.startswith('#'):
                continue


    #
    def parse(self, crontab_text):
        text_list = split('\n', crontab_text)
        
        for i in range(len(text_list)):
            line = text_list[i]
            parsed = self.parseLine(line, i)

        
    #
    def parseLine(self, line, lno):
        print "{}: {}".format(lno, line)
        if self.re_cron_line.match(line):
            return True
        else:
            return False

    
