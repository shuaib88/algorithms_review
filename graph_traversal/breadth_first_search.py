

class Graph:

    def __init__ (self):
        self.adj_list = {}
        self.parent = {}
        self.level = {}

    def add_edge(self,v1,v2):
        if not v1 in self.adj_list:
            self.adj_list[v1] = set([])
            self.adj_list[v1].add(v2)
        else:
            self.adj_list[v1].add(v2)


    def bfs(self,source):

        self.level = {source:0}
        self.parent = {source:None}
        frontier = [source]
        i = 1
        while frontier:
            next = []
            for u in frontier:
                for v in self.adj_list[u]:
                    if v not in self.level:
                        next.append(v)
                        self.parent[v]= u
                        self.level[v] = i
            i+= 1
            frontier = next

# Driver code
# Create a graph given in the above diagram
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)


print g.adj_list

#
print "Following is BFS from (starting from vertex 0)"
g.bfs(0)
print g.parent