from collections import defaultdict
from typing import Any, Callable, List, Dict, TypeVar


T = TypeVar("T")


class Node:
    def __init__(self, data: T):
        self.data = data


class Edge:
    def __init__(self, from_node: Node, to_node: Node):
        self.from_node = from_node
        self.to_node = to_node


class Graph:
    def __init__(self, key_extractor: Callable[[T], str]):
        self.nodes: Dict[str, Node] = {}
        self.edges_from: Dict[str, List[Edge]] = defaultdict(list)
        self.edges_to: Dict[str, List[Edge]] = defaultdict(list)
        self.key_extractor = key_extractor

    def add_node(self, data: T):
        self.nodes[self.key_extractor(data)] = Node(data)

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
