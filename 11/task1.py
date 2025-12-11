
class DirectedGraph:
    def __init__(self):
        self.graph = {}

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

    def find_all_paths(self, source, target):
        paths = []
        self.dfs_paths(source, target, [source], paths)
        return paths
    
    def dfs(self, startVertex):
        if startVertex not in self.graph:
            print("Error")
            return []
        visited = set()
        stack = [startVertex]
        traversalOrder = []

        while stack:
            current = stack.pop()
            if current not in visited:
                traversalOrder.append(current)
                visited.add(current)
                neighbors = sorted(list(self.get_neighbors(current)), reverse=True)
                for neighbor in neighbors:
                    if neighbor not in visited:
                        stack.append(neighbor)
        return traversalOrder

    def dfs_paths(self, current, target, current_path, all_paths):
        if current == target:
            all_paths.append(list(current_path)) 
            return

        for neighbor in self.get_neighbors(current):
            if neighbor not in current_path:
                current_path.append(neighbor)
                self.dfs_paths(neighbor, target, current_path, all_paths)
                current_path.pop()

graph = DirectedGraph()

with open("puzzle.txt", 'r') as file:
    lines = file.readlines()
    for line in lines:
        input_data = line.split(" ")
        for edge in input_data[1:]:
            graph.add_edge(input_data[0][:-1], edge.strip())
    graph.display()
    print(len(graph.find_all_paths("you", "out")))
