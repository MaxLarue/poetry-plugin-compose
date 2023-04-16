import pytest

from poetry_plugin_compose.toposort.graph import Graph


@pytest.fixture
def simple_graph():
    """
    Graph structure
    A -> B -> D
         |    ^
         v    |
         C ---|
    """
    graph = Graph(lambda it: it)
    graph.add_node("A")
    graph.add_node("B")
    graph.add_node("C")
    graph.add_node("D")
    graph.add_edge("A", "B")
    graph.add_edge("B", "D")
    graph.add_edge("B", "C")
    graph.add_edge("C", "D")
    return graph


def test_get_nodes_depending_on(simple_graph):
    depending_on_d = simple_graph.nodes_depending_on("D")
    values = [node.data for node in depending_on_d]
    assert values == ['B', 'C']
