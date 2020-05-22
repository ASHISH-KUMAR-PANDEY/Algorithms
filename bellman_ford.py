class Graph:  
  
    def __init__(self, vertices):  
        self.V = vertices
        self.graph = []  
  
    def addEdge(self, u, v, w):  
        self.graph.append([u, v, w])  
          
    def printArr(self, dist):  
        print("Vertex Distance from Source")  
        for i in range(self.V):  
            print("{0}\t\t{1}".format(i, dist[i]))  
 
    def BellmanFord(self, src):   
        dist = [float("Inf")] * self.V  
        dist[src] = 0
  
  
        # Step 2: Relax all edges |V| - 1 times. A simple shortest  
        # path from src to any other vertex can have at-most |V| - 1  
        # edges  
        for _ in range(self.V - 1):  
            # Update dist value and parent index of the adjacent vertices of  
            # the picked vertex. Consider only those vertices which are still in  
            # queue  
            for u, v, w in self.graph:  
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:  
                        dist[v] = dist[u] + w  
  
        # Step 3: check for negative-weight cycles. The above step  
        # guarantees shortest distances if graph doesn't contain  
        # negative weight cycle. If we get a shorter path, then there  
        # is a cycle.  
  
        for u, v, w in self.graph:  
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:  
                        print("Graph contains negative weight cycle") 
                        return
                          
        # print all distance  
        self.printArr(dist)  
  
g = Graph(5)  
g.addEdge(0, 1, -1)  
g.addEdge(0, 2, 4)  
g.addEdge(1, 2, 3)  
g.addEdge(1, 3, 2)  
g.addEdge(1, 4, 2)  
g.addEdge(3, 2, 5)  
g.addEdge(3, 1, 1)  
g.addEdge(4, 3, -3)  
  
# Print the solution  
g.BellmanFord(0)
