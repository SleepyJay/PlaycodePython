#!/usr/bin/python
import fileinput
import json
import re

class SQLParser:
    
    def __init__(self):
        self.state = ['']
        self.result = []
        self.baseSpace = "  "
        self.level = 0
        self.phrase = ''
        self.debug = 0
    
    def parse(self, doc):
        keywords = set(['select', 'from', 'where', 'insert', 'order']);
        regexSplit = re.compile('([^a-zA-Z.0-9_])')
        
        for line in doc:
            words = regexSplit.split(line)
            
            for word in words:
                cur = self.peek()
                
                if(word == "\n"):
                    if(self.debug):
                        print "---"
                    continue
                
                if(self.debug):
                    print "w>" + word + "<" + cur + ":" + str(self.level)
                
                token = word.lower()
                
                if(token in keywords):
                    if(token == 'from'):                        
                        self.push(token)
                        self.collect("\n" + self.getSpaces() + word)
                        
                    elif(cur == 'from'):
                        self.pop()
                        self.collect("\n" + self.getSpaces() + word)
                    
                    else:
                        if(not cur):
                            self.push('query')
                            self.collect(self.getSpaces() + word)
                        else:
                            self.collect("\n" + self.getSpaces() + word)
                    
                elif(token == '('):
                    if(cur == 'from'):
                        self.push('subquery')
                        self.collect("\n" + self.getSpaces() + word)
                        self.levelUp()
                    
                elif(token == ')'):
                    if(cur == 'subquery'):
                        self.levelDown()
                        self.pop()
                        self.collect(self.getSpaces() + word)
                        
                    elif(cur == 'from'):
                        self.levelDown()
                        self.pop()
                        self.collect("\n" + self.getSpaces() + word + "\n")
                        
                    else:
                        self.collect(word)
                        
                elif(token == ';'):
                    self.collect("\n" + word + "\n\n")
                
                else:
                    self.collect(word)
        
        if(self.debug):
            print "n>"
        
        return self.phrase       

    def collect(self, word):
        self.phrase += word
    
    def getSpaces(self):
        level = self.level
        spaces = self.baseSpace * level
        return spaces
    
    def levelUp(self):
        self.level += 1
    
    def levelDown(self):
        self.level -= 1
        if(self.level < 0):
            self.level = 0   

    def pop(self):
        return self.state.pop()
    
    def push(self, word):
        self.state.append(word)
    
    def peek(self):
        return self.state[-1]


######################


parser = SQLParser()
doc = fileinput.input()
result = parser.parse(doc)
print result

