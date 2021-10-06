import sys
 
 
from collections import deque
 
 
# A class to store a graph edge
class Edge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight
 
 
# A class to represent a graph object
class Graph:
    # Graph Constructor
    def __init__(self, edges, N):
 
        # resize the list to `N` elements of type `List<Edge>`
        self.adj = dict()
 
        # add edges to the undirected graph
        for e in edges:
            if e.src in self.adj:
                self.adj[e.src].append(Edge(e.src, e.dest, e.weight))
            else:
                self.adj[e.src] = []
                self.adj[e.src].append(Edge(e.src, e.dest, e.weight))
            if e.dest in self.adj:
                self.adj[e.dest].append(Edge(e.dest, e.src, e.weight))
            else:
                self.adj[e.dest] = []
                self.adj[e.dest].append(Edge(e.dest, e.src, e.weight))
            
 
# Perform BFS on graph `g` starting from vertex `v`
def modifiedBFS(g, src, k):
 
    # create a queue for doing BFS
    q = deque()
 
    # add source vertex to set and enqueue it
    vertices = [src]
 
    # (current vertex, current path cost, set of nodes visited so far in
    # the current path)
    q.append((src, 0, vertices))
 
    # stores maximum cost of a path from the source
    maxcost = -sys.maxsize
 
    # loop till queue is empty
    while q:
 
        # dequeue front node
        v, cost, vertices = q.popleft()
 
        # if the destination is reached and BFS depth is equal to `m`,
        # update the minimum cost calculated so far
        if cost > k:
            maxcost = max(maxcost, cost)
            for i in vertices:
                print(i, end=" ")
            print()
 
        # do for every adjacent edge of `v`
        for edge in g.adj[v]:
 
            # check for a cycle
            if not edge.dest in vertices:
 
                # add current node to the path
                s = []
                for i in vertices:
                    s.append(i)
                s.append(edge.dest)
 
                # push every vertex (discovered or undiscovered) into
                # the queue with a cost equal to the
                # parent's cost plus the current edge's weight
                q.append((edge.dest, cost + edge.weight, s))
 
    # return max-cost
    return maxcost
 
 
if __name__ == '__main__':
 
    # List of graph edges as per the above diagram
    edges =[  
        Edge("af", "al", 11), Edge("af", "ak", 5), Edge("ak", "al", 3), Edge("ak", "an", 5),
        Edge("ak", "ai", 7), Edge("ai", "ae", -8), Edge("ae", "ah", 10), Edge("an", "ai", -1),
        Edge("an", "ae", 9), Edge("an", "ah", 1), Edge("al", "an", 2), Edge("ar", "al", 9),
        Edge("ar", "ak", 6)
    ]
 
    # total number of nodes in the graph
    N = 9
 
    # build a graph from the given edges
    g = Graph(edges, N)
 
    src = "af"
    cost = 50
    print(g)
    # Start modified BFS traversal from source vertex `src`
    maxCost = modifiedBFS(g, src, cost)
 
    if maxCost != -sys.maxsize:
        print(maxCost)
    else:
        print("All paths from source have their costs <", cost)
