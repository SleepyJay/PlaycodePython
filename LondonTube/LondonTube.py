
# London Tube data munger

import re
__package__="LondonTube"

from Journey import Journey

class LondonTube():
    
    def __init__(self, dataFile=None):
        self.edges = {}
        self.directed = 1
        self.found = {}
        self.targetDist = {}
        
        if dataFile:
            self.parseFile(dataFile)
    
    def setDirected(self, isDirected):
        self.directed = isDirected
    
    # Parses the data file, building a dict of the nodes with the edges
    # coming in and out of it. You need to walk both to find all stations
    # from the correct distance.
    def parseFile(self, fileName):
        f = open(fileName, 'r')
        ptrn = re.compile('([^,\n]+),([^,\n]+),([^,\n]+)')
        
        skip_line = 1
        for line in f:
            if skip_line:
                skip_line = 0
                continue
                
            m = ptrn.match(line)
            if(m):
                tube_line = m.group(1)
                from_node = m.group(2)
                to_node = m.group(3)
                
                if self.directed:
                    self.addForDirected(from_node, to_node, tube_line)
                else:
                    self.addForUndirected(from_node, to_node, tube_line)
        f.close()
    
    def addForDirected(self, from_node, to_node, tube_line):
        if from_node not in self.edges:
            self.edges[from_node] = { 'to_edges': [], 'from_edges': [] }
        
        if to_node not in self.edges:
            self.edges[to_node] = { 'to_edges': [], 'from_edges': [] }
        
        self.edges[from_node].get('to_edges').append( (tube_line, to_node) )
        self.edges[to_node].get('from_edges').append( (tube_line, from_node) )        


    def addForUndirected(self, from_node, to_node, tube_line):
        if from_node not in self.edges:
            self.edges[from_node] = []
        
        if to_node not in self.edges:
            self.edges[to_node] = []
        
        if from_node not in self.edges[to_node]:
            self.edges[to_node].append( (tube_line, from_node) )
            
        if to_node not in self.edges[from_node]:
            self.edges[from_node].append( (tube_line, to_node) )      
    
    
    # Find valid journeys from target that are n stops away
    def findJourneys(self, target, n_away):
        if self.directed:
            self.walkPathsTo(target, n_away)
            self.walkPathsFrom(target, n_away)
            
        else:
            self.walkPaths(None, target, n_away)
        
        for k in self.found:
            journey = self.found[k]
            if journey.nodeCount() == n_away+1:
                self.targetDist[k] = journey
        
        return self.targetDist
    
    # sugar for walkPaths(to_edges ...)
    def walkPathsTo(self, target, n_away):
        self.walkPaths('to_edges', target, n_away)
    
    # sugar for walkPaths(to_edges ...)
    def walkPathsFrom(self, target, n_away):
        self.walkPaths('from_edges', target, n_away) 
    
    # Walks the nodes along a line in a certain direction
    def walkPaths(self, direction, target, n_away):
        journeys = [ Journey(target) ]
 
        for j in journeys:
            curr = j.furthest()
            paths = self.getEdges(curr, direction)
            
            for move in paths:
                if j.canMove(move):
                    k = j.cloned()
                    k.move(move)
                    
                    furthest = k.furthest()
                    if furthest not in self.found or self.isMinDist(k):
                        self.found[furthest] = k                
                    
                    if k.nodeCount() <= n_away+1:
                        # keep going until we are at least the target dist away
                        journeys.append(k)
                        
                else:
                    # if no moves, this path falls out
                    pass
    
    def isMinDist(self, journey):
        return journey.nodeCount() < self.found[journey.furthest()].nodeCount() 
    
    def getEdges(self, nodeName, direction=None):        
        if direction:
            return self.edges[nodeName].get(direction)
        else:
            return self.edges[nodeName]

    
