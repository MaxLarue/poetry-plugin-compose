from collections import defaultdict
from typing import Callable, List, Dict, TypeVar


T = TypeVar("T")


class Node:
    def __init__(self, data: T):
        self.data = data

    def __str__(self):
        return f"Node({str(self.data)})"

    def __repr__(self):
        return str(self)


class Edge:
    def __init__(self, from_node: Node, to_node: Node):
        self.from_node = from_node
        self.to_node = to_node


class CircularGraphException(Exception):
    def __init__(self, cycles):
        msg = "Cycles detected in graph: " + ",".join([str(cycle) for cycle in cycles])
        super(CircularGraphException, self).__init__(msg)
        self.cycles = cycles


class Graph:
    def __init__(self, key_extractor: Callable[[T], str]):
        self.nodes: Dict[str, Node] = {}
        self.edges_from: Dict[str, List[Edge]] = defaultdict(list)
        self.edges_to: Dict[str, List[Edge]] = defaultdict(list)
        self.key_extractor = key_extractor

    def add_node(self, data: T):
        self.nodes[self.key_extractor(data)] = Node(data)

    def add_nodes(self, datas: List[T]):
        for data in datas:
            self.add_node(data)

    def add_edge(self, from_data: T, to_data: T):
        edge = Edge(
            self.nodes[self.key_extractor(from_data)],
            self.nodes[self.key_extractor(to_data)],
        )
        self.edges_from[self.key_extractor(from_data)].append(edge)
        self.edges_to[self.key_extractor(to_data)].append(edge)

    def nodes_depending_on(self, data: T):
        return [edge.from_node for edge in self.edges_to[self.key_extractor(data)]]

    def node_dependencies(self, data: T):
        return [edge.to_node for edge in self.edges_from[self.key_extractor(data)]]

    def leafs(self):
        result = []
        for node in self.nodes.values():
            if not self.edges_from[self.key_extractor(node.data)]:
                result.append(node)
        return result

    def roots(self):
        result = []
        for node in self.nodes.values():
            if not self.edges_to[self.key_extractor(node.data)]:
                result.append(node)
        return result

    def detect_cycles(self):
        stack = [([], node) for node in self.nodes.values()]
        cycles = []
        while stack:
            path, node = stack.pop()
            if node in path:
                cycles.append(path)
                continue
            for dependencies in self.node_dependencies(node.data):
                stack.append(([*path, node], dependencies))
        return cycles

    def toposort(self):
        cycles = self.detect_cycles()
        if cycles:
            raise CircularGraphException(cycles)
        dependencies = self.roots()
        queue = [*dependencies]
        while queue:
            current = queue.pop(0)
            if current not in dependencies:
                dependencies.append(current)
            for node in self.node_dependencies(current.data):
                if node not in dependencies:
                    queue.append(node)
        return dependencies
