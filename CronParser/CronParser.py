# CronParser

import re

class CronParser(object):

    #
    def __init__(self):
        self.re_cron_line = re.compile('\s*(([^\s])\s+){5}.+')
        self.re_comment_line = re.compile('^\s*#')
        self.re_empty_line = re.compile('^\s*$')

        self.parsed_lines = []

    #
    def parseLines(self, lines):
        for i in range(len(lines)):
            line = lines[i]
            parsed_line = self.lexLine(line, i)
            #print "{} ==> {}".format(line, parsed_line)

            if parsed_line == 'cron':
                self.parsed_lines.append(parsed_line)

        return self.parsed_lines


    #
    def lexLine(self, line, lno):
        #print "{}: {}".format(lno, line)
        line = line.rstrip()
        if self.re_cron_line.match(line):
            return "cron"
        elif self.re_comment_line.match(line):
            return "comment"
        elif self.re_empty_line.match(line):
            return "empty"
        else:
            return None

    #
    def parseFile(self, file_path):
        f = open(file_path, 'r')

        if not f:
            # Exception?
            pass
        
        lines = map( (lambda x: x.rstrip()), f.readlines())
        return self.parseLines(lines)


