from collections import defaultdict 
import sys 
  
class Heap(): 
  
    def __init__(self): 
        self.array = [] 
        self.size = 0
        self.pos = [] 
  
    def newMinHeapNode(self, v, dist): 
        minHeapNode = [v, dist] 
        return minHeapNode 

    def swapMinHeapNode(self, a, b): 
        t = self.array[a] 
        self.array[a] = self.array[b] 
        self.array[b] = t 
 
    def minHeapify(self, idx): 
        smallest = idx 
        left = 2 * idx + 1
        right = 2 * idx + 2
  
        if left < self.size and self.array[left][1] < \ 
                                self.array[smallest][1]: 
            smallest = left 
  
        if right < self.size and self.array[right][1] < \ 
                                self.array[smallest][1]: 
            smallest = right 

        if smallest != idx: 

            self.pos[ self.array[smallest][0] ] = idx 
            self.pos[ self.array[idx][0] ] = smallest 

            self.swapMinHeapNode(smallest, idx) 
  
            self.minHeapify(smallest) 

    def extractMin(self): 
 
        if self.isEmpty() == True: 
            return
   
        root = self.array[0] 

        lastNode = self.array[self.size - 1] 
        self.array[0] = lastNode 

        self.pos[lastNode[0]] = 0
        self.pos[root[0]] = self.size - 1

        self.size -= 1
        self.minHeapify(0) 
  
        return root 
  
    def isEmpty(self): 
        return True if self.size == 0 else False
  
    def decreaseKey(self, v, dist): 
        i = self.pos[v] 

        self.array[i][1] = dist 

        while i > 0 and self.array[i][1] < \ 
                    self.array[(i - 1) / 2][1]: 
 
            self.pos[ self.array[i][0] ] = (i-1)/2
            self.pos[ self.array[(i-1)/2][0] ] = i 
            self.swapMinHeapNode(i, (i - 1)/2 ) 

            i = (i - 1) / 2; 

    def isInMinHeap(self, v): 
  
        if self.pos[v] < self.size: 
            return True
        return False
  
  
def printArr(parent, n): 
    for i in range(1, n): 
        print "% d - % d" % (parent[i], i) 
  
  
class Graph(): 
  
    def __init__(self, V): 
        self.V = V 
        self.graph = defaultdict(list) 

    def addEdge(self, src, dest, weight): 

        newNode = [dest, weight] 
        self.graph[src].insert(0, newNode) 

        newNode = [src, weight] 
        self.graph[dest].insert(0, newNode) 

    def PrimMST(self): 
        V = self.V   

        key = []    
          
        parent = []  

        minHeap = Heap() 

        for v in range(V): 
            parent.append(-1) 
            key.append(sys.maxint) 
            minHeap.array.append( minHeap.newMinHeapNode(v, key[v]) ) 
            minHeap.pos.append(v) 

        minHeap.pos[0] = 0
        key[0] = 0
        minHeap.decreaseKey(0, key[0]) 

        minHeap.size = V; 
  
        while minHeap.isEmpty() == False: 

            newHeapNode = minHeap.extractMin() 
            u = newHeapNode[0] 

            for pCrawl in self.graph[u]: 
  
                v = pCrawl[0] 

                if minHeap.isInMinHeap(v) and pCrawl[1] < key[v]: 
                    key[v] = pCrawl[1] 
                    parent[v] = u 

                    minHeap.decreaseKey(v, key[v]) 
  
        printArr(parent, V) 

graph = Graph(9) 
graph.addEdge(0, 1, 4) 
graph.addEdge(0, 7, 8) 
graph.addEdge(1, 2, 8) 
graph.addEdge(1, 7, 11) 
graph.addEdge(2, 3, 7) 
graph.addEdge(2, 8, 2) 
graph.addEdge(2, 5, 4) 
graph.addEdge(3, 4, 9) 
graph.addEdge(3, 5, 14) 
graph.addEdge(4, 5, 10) 
graph.addEdge(5, 6, 2) 
graph.addEdge(6, 7, 1) 
graph.addEdge(6, 8, 6) 
graph.addEdge(7, 8, 7) 
graph.PrimMST() 
