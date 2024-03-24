import numpy
import networkx as nx
import random
import time

class Graph:
    def __init__(self):
        self.edges = {}
    
    def addEdge(self, a, b):
        if a not in self.edges:
            self.edges[a] = []
        self.edges[a].append(b)

    def bfs(self, startNode, toPrint = 0):
        if startNode not in self.edges:
            return "No such Node"
        
        visited = [startNode]
        queue = [startNode]

        while queue:
            if queue[0] in self.edges:
                for neighbor in self.edges[queue[0]]:
                    if neighbor not in visited:
                        visited.append(neighbor)
                        queue.append(neighbor)
            queue.pop(0)
        
        if toPrint == 1:
            print(visited)

    def dfs(self, startNode, toPrint = 0):
        visited = [startNode]
        stack = [startNode]
        while stack:
            node = stack.pop(0)
            if node not in self.edges:
                continue
            for neighbor in self.edges[node]:
                if neighbor not in visited:
                    stack.insert(0, neighbor)
                    visited.append(neighbor)
        if toPrint == 1:
            print(visited)

def networkx_to_custom_graph(networkx_graph):
    custom_graph = Graph()
    for edge in networkx_graph.edges:
        custom_graph.addEdge(edge[0], edge[1])
    return custom_graph

def generate_random_graph(num_nodes, edge_prob):
    graph = nx.erdos_renyi_graph(num_nodes, edge_prob)
    return networkx_to_custom_graph(graph)

# graph = generate_random_graph(20, 0.5)
# print(graph.edges)
# graph.bfs(0)
# graph.dfs(0)

gap = 100
nr_nodes = 100

bfs_result = []
dfs_result = []
inputs = []


while nr_nodes<=2000:
    graph = generate_random_graph(nr_nodes, 0.5)
    start_node = random.randint(0, nr_nodes-1)
    start_time = time.time()
    graph.bfs(start_node)
    end_time = time.time()
    execution_time = end_time - start_time
    bfs_result.append(f"{execution_time:.4f}")

    start_time = time.time()
    graph.dfs(start_node)
    end_time = time.time()
    execution_time = end_time - start_time
    dfs_result.append(f"{execution_time:.4f}")


    print(nr_nodes)
    inputs.append(nr_nodes)
    nr_nodes+=gap

print(bfs_result)
print(dfs_result)
print(inputs)

length = len(bfs_result)

for i in range(0, length):
    print(f"{inputs[i]} - {bfs_result[i]}")

for i in range(0, length):
    print(f"{inputs[i]} - {dfs_result[i]}")

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