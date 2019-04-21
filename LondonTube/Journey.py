
# Data class representing the journey from one node to another and the list of lines


class Journey(object):
    
    def __init__(self, start=None):
        self.lines = []
        self.nodes = []

        if start:
            self.move([None, start])
        
    def move(self, move):
        line = move[0]
        node = move[1]
        if node in self.nodes:
            return
        
        if line:
            if line not in self.lines:
                self.lines.append(line)
        
        self.nodes.append(node)
        
        return 1
    
    def cloned(self):
        journey = Journey()
        for node in self.nodes:
            journey.nodes.append(node)
        
        for line in self.lines:
            journey.lines.append(line)
            
        return journey

    def can_move(self, move):
        node = move[1]
        if node in self.nodes:
            return 0
        else:
            return 1
    
    def furthest(self):
        return self.nodes[-1]
    
    def node_count(self):
        return len(self.nodes)
