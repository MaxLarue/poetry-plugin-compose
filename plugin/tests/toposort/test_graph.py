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


@pytest.fixture
def circular_graph():
    """
        Graph structure
        A <- B <- D
        |         ^
        v         |
        C --------|
        """
    graph = Graph(lambda it: it)
    graph.add_node("A")
    graph.add_node("B")
    graph.add_node("C")
    graph.add_node("D")
    graph.add_edge("B", "A")
    graph.add_edge("D", "B")
    graph.add_edge("A", "C")
    graph.add_edge("C", "D")
    return graph


@pytest.fixture
def complex_graph():
    """
            Graph structure
            A -> B -> C -> D -> E -> F
                 |         ^    ^    |
                 V         |    |    |
                 G -> H -> I    |    |
                      |         |    |
                      V         |    V
                      J ------> K -> L
            """
    graph = Graph(lambda it: it)
    graph.add_nodes(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"])
    graph.add_edge("A", "B")
    graph.add_edge("B", "G")
    graph.add_edge("G", "H")
    graph.add_edge("B", "C")
    graph.add_edge("C", "D")
    graph.add_edge("H", "I")
    graph.add_edge("H", "J")
    graph.add_edge("J", "K")
    graph.add_edge("I", "D")
    graph.add_edge("K", "E")
    graph.add_edge("E", "F")
    graph.add_edge("K", "L")
    graph.add_edge("F", "L")
    return graph


def test_get_nodes_depending_on(simple_graph):
    depending_on_d = simple_graph.nodes_depending_on("D")
    values = [node.data for node in depending_on_d]
    assert values == ['B', 'C']


def test_get_node_dependencies(simple_graph):
    dependencies = simple_graph.node_dependencies("B")
    values = [node.data for node in dependencies]
    assert sorted(values) == ['C', 'D']


def test_get_node_dependencies_from_root(simple_graph):
    dependencies = simple_graph.node_dependencies("A")
    values = [node.data for node in dependencies]
    assert sorted(values) == ['B']


def test_leafs(simple_graph):
    leafs = simple_graph.leafs()
    values = [node.data for node in leafs]
    assert sorted(values) == ['D']


def test_roots(simple_graph):
    roots = simple_graph.roots()
    values = [node.data for node in roots]
    assert sorted(values) == ['A']


def test_detect_cycles_no_cycles(simple_graph):
    assert simple_graph.detect_cycles() == []


def test_detect_cycles_has_cycles(circular_graph):
    cycles = circular_graph.detect_cycles()
    assert len(cycles) > 0
    assert ["A", "C", "D", "B"] in [[node.data for node in cycle] for cycle in cycles]


def test_topo_sort_empty_graph():
    graph = Graph(lambda it : it)
    assert graph.toposort() == []


def test_topo_sort_simple_graph(simple_graph):
    values = [node.data for node in simple_graph.toposort()]
    assert values == ['A', 'B', 'D', 'C']


def test_topo_sort_complex_graph(complex_graph):
    values = [node.data for node in complex_graph.toposort()]
    assert values == ['A', 'B', 'G', 'C', 'H', 'D', 'I', 'J', 'K', 'E', 'L', 'F']

