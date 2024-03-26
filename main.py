import random
import time
from collections import deque
class Graph:
    def __init__(self):
        self.edges = {}
    
    def addEdge(self, a, b):
        if a not in self.edges:
            self.edges[a] = []
        self.edges[a].append(b)

    def bfs(self, startNode, toPrint=0):
        if startNode not in self.edges:
            return "No such Node"
        
        visited = set()
        queue = deque([startNode])

        while queue:
            node = queue.popleft()
            visited.add(node)
            
            for neighbor in self.edges[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
        if toPrint == 1:
            print(visited)

    def dfs(self, startNode, toPrint = 0):
        visited = set()
        stack = deque([startNode])

        while stack:
            node = stack.pop()
            if node in visited:
                continue
            if node not in self.edges:
                continue
            visited.add(node)
            for neighbor in reversed(self.edges[node]):
                if neighbor not in visited:
                    stack.append(neighbor)
        
        if toPrint == 1:
            print(node)

def generate_random_graph1(n):
    g = Graph()
    for i in range(n):
        for j in range(i+1, n):
            if random.random() < 1:
                g.addEdge(i, j)
                g.addEdge(j, i)
    # print(g.graph)
    return g

gap = 100
max_nodes = 2000
bfs_result = [0 for i in range(0, max_nodes//gap)]
dfs_result = [0 for i in range(0, max_nodes//gap)]
inputs = []

nr_of_tests = 5
k = nr_of_tests
while k>0:
    idx = 0
    nr_nodes = 100
    while nr_nodes<=max_nodes:
        graph = generate_random_graph1(nr_nodes)
        print(len(graph.edges))
        start_node = random.randint(0, nr_nodes-1)
        start_time = time.time()
        graph.bfs(start_node)
        end_time = time.time()
        execution_time = end_time - start_time
        bfs_result[idx] += execution_time

        start_time = time.time()
        graph.dfs(start_node)
        end_time = time.time()
        execution_time = end_time - start_time
        dfs_result[idx] += execution_time

        # print(nr_nodes)
        inputs.append(nr_nodes)
        nr_nodes+=gap
        idx+=1

    k-=1

bfs_result = [i/nr_of_tests for i in bfs_result]
dfs_result = [i/nr_of_tests for i in bfs_result]

print(bfs_result)
print(dfs_result)
print(inputs)

length = len(bfs_result)

for i in range(0, 10):
    print(f"{inputs[i]} - {bfs_result[i]}")

for i in range(0, 10):
    print(f"{inputs[i]} - {dfs_result[i]}")

import matplotlib.pyplot as plt
import numpy as np

x = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000] 

xpoints = np.array(x)
ypoints = np.array(bfs_result)

plt.plot(xpoints, ypoints, marker = 'o', label='BFS')
ypoints = np.array(dfs_result)
plt.plot(xpoints, ypoints, marker = 'o', label='DFS')
plt.legend()
plt.title("DFS")
plt.xlabel("N")
plt.ylabel("Time(s)")
plt.grid()
plt.show()

# graph = Graph()

# graph.addEdge(0, 1)
# graph.addEdge(0, 2)
# graph.addEdge(1, 3)
# graph.addEdge(1, 4)
# graph.addEdge(2, 4)
# print(graph.edges)
# print("BFS: ")
# graph.bfs(0, 1)
# print("DFS: ")
# graph.dfs(0, 1)

# graph.addEdge(0, 1)
# graph.addEdge(0, 2)
# graph.addEdge(1, 2)
# graph.addEdge(2, 0)
# graph.addEdge(2, 3)
# graph.addEdge(3, 3)
# print(graph.edges)
# print("BFS: ")
# graph.bfs(2, 1)
# print("DFS: ")
# graph.dfs(2, 1)

# graph.addEdge('A', 'B')
# graph.addEdge('A', 'C')
# graph.addEdge('B', 'A')
# graph.addEdge('B', 'D')
# graph.addEdge('B', 'E')
# graph.addEdge('C', 'A')
# graph.addEdge('C', 'F')
# graph.addEdge('D', 'B')
# graph.addEdge('E', 'B')
# graph.addEdge('E', 'F')
# graph.addEdge('F', 'C')
# graph.addEdge('F', 'E')
# print("BFS: ")
# graph.bfs('A', 1)
# print("DFS: ")
# graph.dfs('A', 1)