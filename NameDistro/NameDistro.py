# NameDistro

import collections


class NameDistro(object):

    def __init__(self):
        self.GroupTuple = collections.namedtuple('Group', ['items', 'sum'])
        self.GroupingFunction = collections.namedtuple('GroupingFunction', ['name', 'func'])
        self.Result = collections.namedtuple('Result', ['groups', 'total'])
        self.GroupData = collections.namedtuple('GroupData', ['name', 'items'])

        self.group_data = [
            self.GroupData("Tens", [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]),
            self.GroupData("Geo2", [1, 2, 4, 8, 16, 32, 64, 128, 256]),
            self.GroupData("Fibo", [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]),
            self.GroupData("Mix1", [1, 55, 1, 34, 2, 21, 3, 13, 5, 8]),
            self.GroupData("Mix2", [2, 55, 1, 34, 1, 3, 21, 8, 13, 5]),
        ]

        self.group_functions = [
            self.GroupingFunction("Silly_Simple", self.silly_simple),
            self.GroupingFunction("Until_Math", self.until_math),
        ]

    def evaluate(self, result):
        min_val = result.groups[0].sum
        max_val = min_val

        for grp in result.groups:
            if grp.sum < min_val:
                min_val = grp.sum

            if grp.sum > max_val:
                max_val = grp.sum

        return max_val - min_val

## Group Algorithms:
    def generic_grouper(self, group_max, items):
        s = 0 # group index var
        g = 1 # group count so far

        print("NOT IMPLEMENTED")
        return

        total = 0
        group_total = 0
        group = []
        groups = []

        for i in range(len(items)):
            value = items[i]
            #print "item_{}: {}".format(i,value)

            if g != group_count:
                if s >= group_max:
                    gt = self.GroupTuple(group, group_total)
                    groups.append(gt)

                    s = 0
                    g += 1
                    group_total = 0
                    group = []


            group.append(i)
            group_total += value
            total += value
            s += 1

        if len(group):
            gt = self.GroupTuple(group, group_total)
            groups.append(gt)

        result = self.Result(groups, total)
        return result

    def silly_simple(self, group_count, items):
        s = 0 # group index var
        g = 1 # group count so far

        total = 0
        group_total = 0
        group = []
        groups = []
        group_max = len(items) / group_count

        for i in range(len(items)):
            value = items[i]

            if g != group_count:
                if s >= group_max:
                    gt = self.GroupTuple(group, group_total)
                    groups.append(gt)

                    s = 0
                    g += 1
                    group_total = 0
                    group = []

            group.append(i)
            group_total += value
            total += value
            s += 1

        if len(group):
            gt = self.GroupTuple(group, group_total)
            groups.append(gt)

        result = self.Result(groups, total)
        return result

    def until_math(self, group_count, items):
        g = 1 # group count so far

        total = 0
        group_total = 0
        group = []
        groups = []
        group_max = sum(items)/group_count

        for i in range(len(items)):
            value = items[i]

            if g != group_count:
                if group_total > group_max or len(items)-i == group_count-g:
                    gt = self.GroupTuple(group, group_total)
                    groups.append(gt)

                    g += 1
                    group_total = 0
                    group = []

            group.append(i)
            group_total += value
            total += value

        if len(group):
            gt = self.GroupTuple(group, group_total)
            groups.append(gt)

        result = self.Result(groups, total)
        return result
