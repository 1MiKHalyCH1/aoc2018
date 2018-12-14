from .node import Node
from .worker import Worker

class Graph:
    def __init__(self):
        self.nodes = set()
    
    def add_edge(self, from_node, to_node):
        from_node = self._create_or_get_node(from_node)
        to_node = self._create_or_get_node(to_node)

        from_node.add_to_node(to_node)
        to_node.add_from_node(from_node)

    def _create_or_get_node(self, name):
        nodes = [node for node in self.nodes if node.name == name]
        if not nodes:
            node = Node(name)
            self.nodes.add(node)
            return node
        else:
            return nodes[0]
    
    def topsort(self):
        res = []
        ready_nodes = {node for node in self.nodes if not node.from_nodes}
        
        while ready_nodes:
            res.append(min(ready_nodes))
            ready_nodes.remove(res[-1])
            ready_nodes.update({node for node in self.nodes if node not in res and not (node.from_nodes - set(res))})
        
        return res

    def transporter(self, workers):
        res = []
        workers = [Worker() for _ in range(workers)]
        ready_nodes = {node for node in self.nodes if not node.from_nodes}
        taken_works = set()
        i = 0
        
        for worker in workers:
            if ready_nodes:
                node = min(ready_nodes)
                ready_nodes.remove(node)
                worker.add_work(node)
                taken_works.add(node)
        
        while True:
            for worker in workers:
                worker.make_work_second()
                ready_work = worker.get_ready_work()
                if ready_work:
                    res.append(ready_work)
                    ready_nodes.update({node for node in self.nodes if node not in res and not (node.from_nodes - set(res))})

            for worker in workers:
                if not worker.work and ready_nodes - taken_works:
                    node = min(ready_nodes - taken_works)
                    ready_nodes.remove(node)
                    worker.add_work(node)
                    taken_works.add(node)
            
            i += 1
            if len(res) == len(self.nodes):
                return i