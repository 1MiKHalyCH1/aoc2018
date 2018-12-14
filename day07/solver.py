from models.graph import Graph
import re

edge_pattern = re.compile(r'Step (\w) must be finished before step (\w) can begin.')

def get_first_star(graph):
    print("First star:", ''.join(map(str, graph.topsort())))

def get_second_star(graph):
    print("Second star:", graph.transporter(5))

def prepare_graph(data, graph):
    for edge in data:
        from_node, to_node = edge_pattern.search(edge).groups()
        graph.add_edge(from_node, to_node)


if __name__ == "__main__":
    with open('data.txt', 'r') as f:
        data = f.read().split('\n')
    
    graph = Graph()
    prepare_graph(data, graph)

    get_first_star(graph)
    get_second_star(graph)