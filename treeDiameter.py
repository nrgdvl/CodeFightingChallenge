def treeDiameter(n, tree):
    graph = Graph()
    for path in tree:
        graph.add(path)
    vec = graph.find_diam()

    return max(0, vec-1)
    

class Graph:
    def __init__(self):
        self.graph = {}
    def add(self, path):
        self.graph[path[0]] = self.graph.get(path[0], []) + [path[1]]
        self.graph[path[1]] = self.graph.get(path[1], []) + [path[0]]
    def find_diam(self):
        if not self.graph:
            return 0
        start = [k for k in self.graph if len(self.graph[k]) < 3][0]
        best = [0]
        h = self.height(start, None, best)
        return best[0]
    def height(self, start, parent, best):
        if start is None:
            return 0
        children = [self.height(x, start, best) for x in self.graph[start] + [None] if x != parent]
        best[0] = max(1+sum(sorted(children, reverse=True)[:2]), best[0])
        #print(parent, start, best, 1+max(children))
        return 1+max(children)
        
    def __str__(self):
        return str(self.graph) + ' ' + str(self.diam.items())
