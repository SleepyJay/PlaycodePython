# CronParser

import re
import collections
from CronEntry import CronEntry

class LineType:
    cron, comment, empty = range(3)

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

            if parsed_line == LineType.cron:
                self.parsed_lines.append(parsed_line)

        return self.parsed_lines


    #
    def lexLine(self, line, lno):
        #print "{}: {}".format(lno, line)
        line = line.rstrip()
        return self.matchLine(line, lno)

    
    #
    def matchLine(self, line, lno):
        if self.re_cron_line.match(line):
            return LineType.cron
        elif self.re_comment_line.match(line):
            return LineType.comment
        elif self.re_empty_line.match(line):
            return LineType.empty
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


