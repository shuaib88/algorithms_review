

class Graph:
    def __init__ (self):
        # TODO look for better adjacency list implementations
        self.adj_list = {}
        self.parent = {}

    def add_edge(self,v1,v2):
        if not v1 in self.adj_list:
            self.adj_list[v1] = set([])
            self.adj_list[v1].add(v2)
        else:
            self.adj_list[v1].add(v2)

    def dfs_visit(self, source):
        if source not in self.adj_list:
            return
        for v in self.adj_list[source]:
            if v not in self.parent:
                self.parent[v] = source
                self.dfs_visit(v)

    def dfs(self):
        for s in self.adj_list:
            if s not in self.parent:
                self.parent[s] = None
                self.dfs_visit(s)

# Driver code
# Create a graph given in the above diagram
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)


print g.adj_list

#
print "Following is DFS from (starting from vertex 2)"
g.dfs()
print g.parent


# graph = {'A': set(['B', 'C']),
#          'B': set(['A', 'D', 'E']),
#          'C': set(['A', 'F']),
#          'D': set(['B']),
#          'E': set(['B', 'F']),
#          'F': set(['C', 'E'])}

