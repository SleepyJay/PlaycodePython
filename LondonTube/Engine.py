# London Tube data munger

import re
from LondonTube.Journey import Journey


class Engine(object):

    def __init__(self, data_file=None):
        self.edges = {}
        self.directed = 1
        self.found = {}
        self.target_dist = {}

        if data_file:
            self.parse_file(data_file)

    def set_directed(self, is_directed):
        self.directed = is_directed

    # Parses the data file, building a dict of the nodes with the edges
    # coming in and out of it. You need to walk both to find all stations
    # from the correct distance.
    def parse_file(self, file_name):
        f = open(file_name, 'r')
        ptrn = re.compile('([^,\n]+),([^,\n]+),([^,\n]+)')

        skip_line = 1
        for line in f:
            if skip_line:
                skip_line = 0
                continue

            m = ptrn.match(line)
            if m:
                tube_line = m.group(1)
                from_node = m.group(2)
                to_node = m.group(3)

                if self.directed:
                    self.add_for_directed(from_node, to_node, tube_line)
                else:
                    self.add_for_undirected(from_node, to_node, tube_line)
        f.close()

    def add_for_directed(self, from_node, to_node, tube_line):
        if from_node not in self.edges:
            self.edges[from_node] = {'to_edges': [], 'from_edges': []}

        if to_node not in self.edges:
            self.edges[to_node] = {'to_edges': [], 'from_edges': []}

        self.edges[from_node].get('to_edges').append((tube_line, to_node))
        self.edges[to_node].get('from_edges').append((tube_line, from_node))

    def add_for_undirected(self, from_node, to_node, tube_line):
        if from_node not in self.edges:
            self.edges[from_node] = []

        if to_node not in self.edges:
            self.edges[to_node] = []

        if from_node not in self.edges[to_node]:
            self.edges[to_node].append((tube_line, from_node))

        if to_node not in self.edges[from_node]:
            self.edges[from_node].append((tube_line, to_node))

            # Find valid journeys from target that are n stops away

    def find_journeys(self, target, n_away):
        if self.directed:
            self.walk_paths_to(target, n_away)
            self.walk_paths_from(target, n_away)

        else:
            self.walk_paths(None, target, n_away)

        for k in self.found:
            journey = self.found[k]
            if journey.node_count() == n_away + 1:
                self.target_dist[k] = journey

        return self.target_dist

    # sugar for walk_paths(to_edges ...)
    def walk_paths_to(self, target, n_away):
        self.walk_paths('to_edges', target, n_away)

    # sugar for walk_paths(to_edges ...)
    def walk_paths_from(self, target, n_away):
        self.walk_paths('from_edges', target, n_away)

    # Walks the nodes along a line in a certain direction
    def walk_paths(self, direction, target, n_away):
        journeys = [Journey(target)]

        for j in journeys:
            curr = j.furthest()
            paths = self.get_edges(curr, direction)

            for move in paths:
                if j.can_move(move):
                    k = j.cloned()
                    k.move(move)

                    furthest = k.furthest()
                    if furthest not in self.found or self.is_min_dist(k):
                        self.found[furthest] = k

                    if k.node_count() <= n_away + 1:
                        # keep going until we are at least the target dist away
                        journeys.append(k)

                else:
                    # if no moves, this path falls out
                    pass

    def is_min_dist(self, journey):
        return journey.node_count() < self.found[journey.furthest()].node_count()

    def get_edges(self, node_name, direction=None):
        if direction:
            return self.edges[node_name].get(direction)
        else:
            return self.edges[node_name]
