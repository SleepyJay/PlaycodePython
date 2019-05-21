

class LayerSearchTree(object):

    def __init__(self):
        self.error = ''
        self.tree = dict()

    def add(self, keys, value):
        node = self.tree
        key_last = len(keys)-1

        for i in range(0, key_last+1):
            key = keys[i]

            if i == key_last:
                node[key] = value
            else:
                if key not in node:
                    node[key] = dict()

                node = node[key]

    def find_stackable(self, layer):
        found = []
        queue = [self.tree]
        width = layer.width
        width_set = layer.width_set

        while queue:
            node = queue.pop()

            for key in node.keys():
                if key == width:
                    found.append(node[key])
                    break
                else:
                    if key in width_set:
                        continue

                    queue.append(node[key])

        return found
