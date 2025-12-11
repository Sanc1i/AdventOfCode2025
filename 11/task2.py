class DirectedGraph:
    def __init__(self):
        self.graph = {}
        self._path_cache = {}  # Cache for memoization
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = set() 
    
    def add_edge(self, source, destination):
        self.add_vertex(source)
        self.add_vertex(destination)
        self.graph[source].add(destination)
    
    def get_neighbors(self, vertex):
        return self.graph.get(vertex, set()) 
    
    def display(self):
        print("Directed Graph (Adjacency List):")
        for vertex, neighbors in self.graph.items():
            print(f"{vertex} -> {list(neighbors)}")
    
    def count_simple_paths_dp(self, source, target):
        in_degree = {v: 0 for v in self.graph}
        for v in self.graph:
            for neighbor in self.graph[v]:
                in_degree[neighbor] = in_degree.get(neighbor, 0) + 1
        
        queue = [v for v in self.graph if in_degree[v] == 0]
        topo_order = []
        temp_in_degree = in_degree.copy()
        
        while queue:
            node = queue.pop(0)
            topo_order.append(node)
            for neighbor in self.get_neighbors(node):
                temp_in_degree[neighbor] -= 1
                if temp_in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        dp = {v: 0 for v in self.graph}
        dp[source] = 1
        
        for node in topo_order:
            if dp[node] > 0:
                for neighbor in self.get_neighbors(node):
                    dp[neighbor] += dp[node]
        
        return dp.get(target, 0)


graph = DirectedGraph()
with open("puzzle.txt", 'r') as file:
    for line in file:
        parts = line.split()
        if len(parts) >= 2:
            source = parts[0].rstrip(':')
            for edge in parts[1:]:
                graph.add_edge(source, edge.strip())

svr_to_dac = graph.count_simple_paths_dp("svr", "dac")
svr_to_fft = graph.count_simple_paths_dp("svr", "fft")
dac_to_fft = graph.count_simple_paths_dp("dac", "fft")
fft_to_dac = graph.count_simple_paths_dp("fft", "dac")
dac_to_out = graph.count_simple_paths_dp("dac", "out")
fft_to_out = graph.count_simple_paths_dp("fft", "out")

print(f"svr -> dac: {svr_to_dac}")
print(f"svr -> fft: {svr_to_fft}")
print(f"dac -> fft: {dac_to_fft}")
print(f"fft -> dac: {fft_to_dac}")
print(f"dac -> out: {dac_to_out}")
print(f"fft -> out: {fft_to_out}")

total = svr_to_dac * dac_to_fft * fft_to_out + svr_to_fft * fft_to_dac * dac_to_out
print(f"\nTotal: {total}")
