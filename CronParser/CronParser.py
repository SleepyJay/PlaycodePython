# CronParser

import re

class CronParser(object):

    #
    def __init__(self):
        self.re_cron_line = re.compile('\s*(([^\s])\s+){5}.+')
        self.re_comment_line = re.compile('^\s*#')
        self.re_empty_line = re.compile('^\s*$')
        
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
            parsed = self.lexLine(line, i)

        
    #
    def lexLine(self, line, lno):
        print "{}: {}".format(lno, line)
        if self.re_cron_line.match(line):
            return "cron"
        elif self.re_comment_line.match(line):
            return "comment"
        elif self.re_empty_line.match(line):
            return "empty"
        else:
            return None

    
